"""
This program simulates the operation of a service center by generating and processing requests.

Functions:
1. generate_request(queue, id):
   Generates a new request with a unique ID and adds it to the queue.
   Parameters:
     - queue: a queue object to store requests.
     - id: a unique identifier for the request.

2. process_request(queue):
   Processes a request by removing it from the queue.
   Parameters:
     - queue: a queue object from which requests are processed.
   If the queue is empty, a message is displayed indicating that there are no requests to process.

3. main():
   The main function that continuously generates and processes requests in random order.
   The loop runs until interrupted by the user (KeyboardInterrupt), at which point a termination message is printed.
"""



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
                sleep(1)
                process_request(request_queue)
            

    except KeyboardInterrupt:
        print("The program was terminated by the user.")

if __name__ == "__main__":
    main()