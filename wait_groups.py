"""

A wait group is a synchronization primitive used in concurrent programming to wait for a collection of threads or processes to complete their execution. 
The primary purpose of a wait group is to coordinate the termination of multiple parallel tasks and ensure that the main program doesn't proceed until all the tasks are finished.

The concept is commonly used in languages like Go, where it's part of the standard library. In Go, the sync.WaitGroup type provides this functionality.
"""

import threading

class WaitGroup:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()
        self.event = threading.Event()

    def add(self, delta=1):
        with self.lock:
            self.count += delta

    def done(self):
        with self.lock:
            self.count -= 1
            if self.count == 0:
                self.event.set()

    def wait(self):
        self.event.wait()

def worker_thread(worker_id, wait_group):
    print(f"Worker {worker_id} is starting.")
    # Simulate some work
    for _ in range(3):
        print(f"Worker {worker_id} is doing some work.")
    print(f"Worker {worker_id} is done.")
    
    wait_group.done()  # Signal that the work is done

# Create a WaitGroup
wg = WaitGroup()

# Create and start three threads
threads = []
for i in range(3):
    wg.add(1)  # Increment the counter before starting a thread
    thread = threading.Thread(target=worker_thread, args=(i, wg))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
wg.wait()

print("All threads have finished.")


