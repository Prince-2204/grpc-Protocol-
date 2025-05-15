from __future__ import print_function

import service_pb2
import service_pb2_grpc
import grpc
import logging
import time

def run():
    with grpc.insecure_channel('localhost:8000') as channel:
        stub = service_pb2_grpc.ChatStub(channel)
        start_time = time.time()
        response = stub.SayHi(service_pb2.HiRequest(user = "101", request = "Hi"))
        end_time = time.time()
        print(f"Response from server is:\n {response.message}")
        print(f"\nExecution time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    logging.basicConfig()
    run()
