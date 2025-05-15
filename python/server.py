from concurrent import futures
import service_pb2
import service_pb2_grpc
import grpc
import logging

class Chat(service_pb2_grpc.ChatServicer):
    
    def SayHi(self, request, context):
        data = "hi mate how are you"
        return service_pb2.HiResponse(message = f"Request coming from user {request.user} and request is {request.request}\n Response is {data}")
    

def serve():
    port = "8000"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ChatServicer_to_server(Chat(),server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server Started, listening on "+ port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()