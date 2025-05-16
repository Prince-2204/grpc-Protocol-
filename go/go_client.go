package main

import (
    "context"
    "log"
    "time"

    "google.golang.org/grpc"
    pb "example.com/grpc/go/go_servicepb"
)

func main() {
    conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
    if err != nil {
        log.Fatalf("Failed to connect: %v", err)
    }
    defer conn.Close()

    client := pb.NewMultiplyClient(conn)

    ctx, cancel := context.WithTimeout(context.Background(), time.Second)
    defer cancel()

    req := &pb.RequestValues{
        Value1: 8,
        Value2: 5,
    }

    res, err := client.SendValues(ctx, req)
    if err != nil {
        log.Fatalf("Error calling SendValues: %v", err)
    }

    log.Printf("Multiplication Result: %v", res.Ans)
}
