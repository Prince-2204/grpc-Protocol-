package main

import (
    "context"
    "log"
    "net"

    "google.golang.org/grpc"
    pb "example.com/grpc/go/go_servicepb"
)

type server struct {
    pb.UnimplementedMultiplyServer
}

func (s *server) SendValues(ctx context.Context, req *pb.RequestValues) (*pb.ResponseAnswer, error) {
    log.Printf("Received: %v and %v", req.Value1, req.Value2)
    result := req.Value1 * req.Value2
    return &pb.ResponseAnswer{Ans: result}, nil
}

func main() {
    lis, err := net.Listen("tcp", ":50051")
    if err != nil {
        log.Fatalf("Failed to listen: %v", err)
    }

    grpcServer := grpc.NewServer()
    pb.RegisterMultiplyServer(grpcServer, &server{})

    log.Println("gRPC server listening on :50051")
    if err := grpcServer.Serve(lis); err != nil {
        log.Fatalf("Failed to serve: %v", err)
    }
}
