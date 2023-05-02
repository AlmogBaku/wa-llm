package main

import (
	"chat-manager/manager"
	"chat-manager/proto"
	"context"
	"fmt"
	"github.com/joho/godotenv"
	_ "github.com/lib/pq"
	"github.com/mdp/qrterminal/v3"
	"go.mau.fi/whatsmeow"
	"go.mau.fi/whatsmeow/store/sqlstore"
	waLog "go.mau.fi/whatsmeow/util/log"
	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"
	"net"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	err := godotenv.Load()
	if err != nil {
		fmt.Println("Warning: error loading .env file", err)
	}

	dbUri := "postgresql://postgres:almog1is2the3best4@localhost:5432/bot"
	if os.Getenv("DB_URI") != "" {
		dbUri = os.Getenv("DB_URI")
	}

	dbLog := waLog.Stdout("Database", "DEBUG", true)
	// Make sure you add appropriate DB connector imports, e.g. github.com/mattn/go-sqlite3 for SQLite
	store, err := sqlstore.New("postgres", dbUri, dbLog)
	if err != nil {
		panic(err)
	}
	// If you want multiple sessions, remember their JIDs and use .GetDevice(jid) or .GetAllDevices() instead.
	deviceStore, err := store.GetFirstDevice()
	if err != nil {
		panic(err)
	}
	clientLog := waLog.Stdout("client", "INFO", true)
	client := whatsmeow.NewClient(deviceStore, clientLog)

	if client.Store.ID == nil {
		// No ID stored, new login
		qrChan, _ := client.GetQRChannel(context.Background())
		err = client.Connect()
		if err != nil {
			panic(err)
		}
		for evt := range qrChan {
			if evt.Event == "code" {
				// Render the QR code here
				qrterminal.GenerateHalfBlock(evt.Code, qrterminal.L, os.Stdout)
			} else {
				fmt.Println("Login event:", evt.Event)
			}
		}
	} else {
		// Already logged in, just connect
		err = client.Connect()
		if err != nil {
			panic(err)
		}
	}

	defer client.Disconnect()

	bot := manager.New(client, waLog.Stdout("bot", "DEBUG", true))
	client.AddEventHandler(bot.EventHandler)
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	go func() {
		err := serve(ctx, bot)
		if err != nil {
			fmt.Println("got error", err)
		}
	}()

	// Listen to Ctrl+C (you can also do something else that prevents the program from exiting)
	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	<-c
}

func serve(ctx context.Context, bot manager.ChatManager) error {
	uds := "/tmp/chat-mgr.sock"
	if os.Getenv("UDS_PATH") != "" {
		uds = os.Getenv("UDS_PATH")
	}

	if _, err := os.Stat(uds); err == nil {
		if err := os.RemoveAll(uds); err != nil {
			return fmt.Errorf("failed to remove uds file: %w", err)
		}
	}

	l, err := net.Listen("unix", uds)
	if err != nil {
		return fmt.Errorf("failed to listen on socket: %w", err)
	}

	server := grpc.NewServer()
	proto.RegisterChatManagerServer(server, bot)
	reflection.Register(server)

	go func() {
		<-ctx.Done()
		server.Stop()
	}()

	fmt.Println("starting server at", uds)
	return server.Serve(l)
}
