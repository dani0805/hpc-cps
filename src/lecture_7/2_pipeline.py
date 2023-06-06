from multiprocessing import Process, Queue

def fetch(q):
    for i in range(10):
        q.put(i)
    q.put(None)  # Sentinel value to signal the end

def process(fetch_q, save_q):
    while True:
        i = fetch_q.get()
        if i is None:  # If we received the sentinel value, we break the loop
            break
        result = i * i
        save_q.put(result)
    save_q.put(None)  # Signal the end for the next stage

def save(save_q):
    while True:
        result = save_q.get()
        if result is None:  # Again, we break on the sentinel value
            break
        print(f"Result saved: {result}")

if __name__ == "__main__":
    fetch_q = Queue()
    save_q = Queue()

    fetch_process = Process(target=fetch, args=(fetch_q,))
    process_process = Process(target=process, args=(fetch_q, save_q))
    save_process = Process(target=save, args=(save_q,))

    fetch_process.start()
    process_process.start()
    save_process.start()

    fetch_process.join()
    process_process.join()
    save_process.join()