import threading
from queue import Queue
import requests

urls = [
    "https://httpbin.org/",
    "https://jsonplaceholder.typicode.com/",
    "https://apilist.fun/",
    "https://reqres.in/",
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://www.yahoo.com/",
    "https://www.wikipedia.org/",
    "https://www.reddit.com/",
    "https://www.youtube.com/",
    "https://www.facebook.com/",
    "https://www.instagram.com/",
    "https://www.linkedin.com/",
    "https://twitter.com/",
    "https://www.netflix.com/",
    "https://www.amazon.com/",
    "https://www.microsoft.com/",
    "https://www.apple.com/",
    "https://www.adobe.com/",
    "https://www.oracle.com/"
]

with open("urls.txt", "w") as file:
    for url in urls:
        file.write(url + "\n")


class ReaderThread(threading.Thread):
    def __init__(self, start_line, lines_per_thread, queue):
        threading.Thread.__init__(self)
        self.start_line = start_line
        self.lines_per_thread = lines_per_thread
        self.queue = queue

    def run(self):
        with open('urls.txt', 'r') as f:
            # Seek to starting line
            for _ in range(self.start_line):
                next(f)

            for _ in range(self.lines_per_thread):
                # Attempt to read a line
                line = next(f, None)
                if line is None:
                    # End of file reached
                    break

                # Put line into queue and wait if queue is full
                self.queue.put(line.strip())

class WorkerThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get a url from the queue
            url = self.queue.get()
            try:
                # Send a request to the url and print the status code with a 5 second timeout
                response = requests.get(url, timeout=5)
                print(f'URL: {url} Status: {response.status_code}')
            except Exception as e:
                print(f'URL: {url} Status: {e}')

            # Indicate that this task is done or else join() will block forever
            self.queue.task_done()

def main():
    # Number of threads
    num_threads = 10

    # Maximum number of items in queue
    max_queue_size = 1

    # Total number of lines in the file (precalculated)
    total_lines = sum(1 for _ in open('urls.txt'))

    # Create a queue
    queue = Queue(maxsize=max_queue_size)

    # Calculate lines per thread
    lines_per_thread = total_lines // num_threads

    # Create reader threads
    for i in range(num_threads):
        start_line = i * lines_per_thread
        reader = ReaderThread(start_line, lines_per_thread, queue)
        reader.start()

    # Create worker threads
    for _ in range(num_threads):
        worker = WorkerThread(queue)
        worker.daemon = True
        worker.start()

    # Wait for all tasks to complete
    queue.join()

if __name__ == "__main__":
    main()
