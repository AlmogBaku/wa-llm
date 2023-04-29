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

1. Go
2. Python
3. Buf (https://docs.buf.build/installation)

## Building

1. Create a virtual environment for python and install the requirements

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Build the chat-manager

```shell
make build-chat-manager
```

3. Running the project
```shell
make run
```