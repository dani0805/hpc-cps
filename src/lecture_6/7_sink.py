import requests
from bs4 import BeautifulSoup
from queue import Queue
import threading

class Worker(threading.Thread):
    def __init__(self, tasks, results):
        threading.Thread.__init__(self)
        self.tasks = tasks
        self.results = results
        self.daemon = True
        self.start()

    def run(self):
        while True:
            url = self.tasks.get()
            if url is None:
                break
            # Simulate a "task" by fetching data from the url
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.find('title').get_text()
                self.results.put((url, title))
            except Exception as e:
                self.results.put((url, e))
            finally:
                self.tasks.task_done()

class ThreadPool:
    def __init__(self, num_workers):
        self.tasks = Queue(num_workers)
        self.results = Queue()
        for _ in range(num_workers):
            Worker(self.tasks, self.results)

    def add_task(self, task):
        self.tasks.put(task)

    def wait_completion(self):
        self.tasks.join()
        while not self.results.empty():
            print(self.results.get())

# List of urls to fetch
urls = [
    'https://www.python.org/',
    'https://docs.python.org/3/',
    'http://www.crummy.com/software/BeautifulSoup/bs4/doc/',
    # Add more URLs as needed
]

# Create a thread pool and give it some work to do
pool = ThreadPool(2)

for url in urls:
    pool.add_task(url)

# Wait for the work to be done
pool.wait_completion()
