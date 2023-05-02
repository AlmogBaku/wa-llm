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

# Building the project

## Prerequisites

1. Docker

## Running the project

```console
docker compose up
```

# Development
When running locally, you need to install `whispercpp` package for python.
This is not included in the `requirements.txt` file because you might need to install it from source.

```console
pip install git+https://github.com/aarnphm/whispercpp.git -vv
```
