# Whatsapp LLM

This project introduce a bot that can help Whatsapp communities (using groups) to enrich their experience by using
LLM models.

# How does it work?

The project is composed by two main components:

1. A `chat-manager` that is responsible for connecting to Whatsapp, and interacting with it. This component is written
   in Go and exposes a gRPC API over a Unix Domain Socket.
2. The `bot` which is a python application that connects to the `chat-manager` and uses it to interact with Whatsapp.
   This component is written in Python and uses the `chat-manager` to interact with Whatsapp. It is using LangChain and
   OpenAI.

# Running the project

## Prerequisites

1. Docker

## Configuring the project variable

1. Copy the `.env.edit` file to `.env` and edit it to your needs.
    1. You must define the `OPENAI_API_KEY` variable with your own key
    2. If you wish to use the pre-configured postgres database, there's no need to define it's variable.

## Run the project

```console
docker compose up -d
```

## Setting up your bot

1. The first time you connect, the `chat-manager` container will show you a QR code. [Scan it with your Whatsapp
   mobile application](https://faq.whatsapp.com/1079327266110265/).
2. Add your bot to the group you wish to use it in (using the mobile app, or another Whatsapp web).
3. After the bot is running(both `chat-manager` and `bot` containers with no errors), and after the bot got a few
   messages in some groups, you'll be able to see those groups in the database under the `groups` table.
4. To allow the bot to interact with the group, you need to set the `managed` column to `true` for the group you wish to
   use the bot in.
