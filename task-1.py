from queue import Queue
from time import sleep
import random


def generate_request(queue, id):
    request = f"Request №{id}"
    queue.put(request)
    print(f"New request generated: {request}")


def process_request(queue):
    if not queue.empty():
        request = queue.get()
        print(f"Processing request: {request}")
    else:
        print("Queue is empty.")


def main():
    request_queue = Queue()
    id = 0

    try:
        while True:
            sleep(1)

            if random.choice([True, False]):
                id += 1
                generate_request(request_queue, id)
            
            if random.choice([True, False]):
                process_request(request_queue)
            

    except KeyboardInterrupt:
        print("The program was terminated by the user.")

if __name__ == "__main__":
    main()