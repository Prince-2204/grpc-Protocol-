package hello

import (
    "context"
    "log"
    "time"

    "google.golang.org/grpc"
    pb "example.com/grpc/python-go"
)

func main() {
    conn, err := grpc.Dial("localhost:8000", grpc.WithInsecure())
    if err != nil {
        log.Fatalf("did not connect: %v", err)
    }
    defer conn.Close()

    client := pb.NewGreeterClient(conn)
    ctx, cancel := context.WithTimeout(context.Background(), time.Second)
    defer cancel()

    res, err := client.SayHello(ctx, &pb.HelloRequest{Name: "Prince"})
    if err != nil {
        log.Fatalf("could not greet: %v", err)
    }

    log.Printf("Greeting: %s", res.GetMessage())
}
