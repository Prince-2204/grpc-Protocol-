import grpc

from concurrent import futures
import service_pb2
import service_pb2_grpc

class Chat(service_pb2_grpc.ChatServicer):
    def SendMessage(self, request, context):
        return service_pb2.GetResponse(message=f"Hello to request {request.id}")
    

def serve():
    port = "8000"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ChatServicer_to_server(Chat(),server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print(f"Server started at port {port}")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
    