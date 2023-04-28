package main

import (
	"context"
	"fmt"
	_ "github.com/mattn/go-sqlite3"
	"github.com/mdp/qrterminal/v3"
	"go.mau.fi/whatsmeow"
	"go.mau.fi/whatsmeow/store/sqlstore"
	waLog "go.mau.fi/whatsmeow/util/log"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/local"
	"os"
	"os/signal"
	"syscall"
	"wa-group-admin/bot"
	"wa-group-admin/proto"
)

const socket = "/tmp/wa-python-handler.sock"

func main() {
	// check if the socket exists
	if _, err := os.Stat(socket); os.IsNotExist(err) {
		panic(fmt.Errorf("socket %s does not exist", socket))
	}

	cc, err := grpc.Dial(
		fmt.Sprintf("unix://%s", socket),
		grpc.WithTransportCredentials(local.NewCredentials()),
	)
	if err != nil {
		panic(fmt.Errorf("failed to connect to socket: %w", err))
	}

	handlerRt := proto.NewHandlerClient(cc)

	dbLog := waLog.Stdout("Database", "DEBUG", true)
	// Make sure you add appropriate DB connector imports, e.g. github.com/mattn/go-sqlite3 for SQLite
	store, err := sqlstore.New("sqlite3", "file:examplestore.db?_foreign_keys=on", dbLog)
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

	bot := bot.New(handlerRt, client, waLog.Stdout("bot", "DEBUG", true))
	client.AddEventHandler(bot.EventHandler)

	// Listen to Ctrl+C (you can also do something else that prevents the program from exiting)
	c := make(chan os.Signal)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	<-c
}
