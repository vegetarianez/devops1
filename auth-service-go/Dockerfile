FROM golang:1.23-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN go build -o /app/auth-service ./cmd/auth-service/main.go

FROM alpine:latest
WORKDIR /app

COPY --from=builder /app/auth-service .
COPY --from=builder /app/config.yml . 

EXPOSE 8081
CMD ["./auth-service"]