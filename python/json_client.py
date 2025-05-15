import requests
import time

def run():
    url = "http://localhost:5000/sayhi"
    payload = {
        "user": "101",
        "request": "Hi"
    }

    start = time.time()
    response = requests.post(url, json=payload)
    end = time.time()

    json_data = response.json()
    print(f"Response from server is:\n{json_data['message']}")
    print(f"\nClient execution time: {end - start:.6f} seconds")
    print(f"Server-side execution time (reported): {json_data['execution_time']:.6f} seconds")

if __name__ == "__main__":
    run()
