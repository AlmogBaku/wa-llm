ARG TARGETOS=linux
ARG TARGETARCH=amd64
ARG LDFLAGS

## Build protobuf files
FROM bufbuild/buf:1.14.0 as buf
WORKDIR /workspace
COPY ./proto /workspace/proto
COPY buf.yaml /workspace
COPY buf.lock /workspace
COPY buf.gen.yaml /workspace

RUN buf generate --include-imports .

### Build
FROM golang:1.20 AS build
WORKDIR /workspace
COPY chat-manager/go.mod /workspace
COPY chat-manager/go.sum /workspace
RUN go mod download
COPY chat-manager /workspace
COPY --from=buf /workspace/chat-manager/proto /workspace/proto

RUN CGO_ENABLED=0 GOOS=${TARGETOS} GOARCH=${TARGETARCH} go build -ldflags="-X google.golang.org/protobuf/reflect/protoregistry.conflictPolicy=ignore ${LDFLAGS}" -o /out/chat-manager *.go

FROM gcr.io/distroless/static:nonroot as chat-manager
LABEL org.opencontainers.image.source="https://github.com/AlmogBaku/wa-llm"

WORKDIR /
COPY --from=build /out/chat-manager .

ENTRYPOINT ["/chat-manager"]

FROM mcr.microsoft.com/playwright/python:v1.33.0-jammy as bot
LABEL org.opencontainers.image.source="https://github.com/AlmogBaku/wa-llm"

RUN apt-get update -y && apt-get install ffmpeg -y

RUN pip install --upgrade pip

WORKDIR /bot
COPY ./requirements.txt /bot/
RUN pip install -r requirements.txt

COPY ./bot /bot
COPY --from=buf /workspace/bot/src/proto /bot/src/proto

ENV PYTHONUNBUFFERED=1
CMD [ "python", "./main.py" ]