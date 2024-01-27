"""
Barrier objects in python are used to wait for a fixed number of thread to complete execution before any particular thread can proceed forward with the execution of the program. 
Each thread calls wait() function upon reaching the barrier. The barrier is responsible for keeping track of the number of wait() calls. 
If this number goes beyond the number of threads for which the barrier was initialized with, then the barrier gives a way to the waiting threads to proceed on with the execution. 
All the threads at this point of execution, are simultaneously released.
"""



"""
We create a Barrier object with a count of 3, meaning that it will wait for three threads to reach the barrier before allowing them to proceed.
The worker_thread function is the target for each thread. Each thread prints a message before and after waiting at the barrier.
Three threads are created and started.
The main thread waits for all worker threads to finish using the join method.
"""

import threading
import time

# Define a Barrier object with a count of 3
barrier = threading.Barrier(3)

def worker_thread(worker_id):
    print(f"Worker {worker_id} is waiting at the barrier.")
    barrier.wait()  # Wait for all threads to reach this point
    print(f"Worker {worker_id} passed the barrier.")
    # Do some work after passing the barrier

# Create and start three threads
threads = []
for i in range(3):
    thread = threading.Thread(target=worker_thread, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads have finished.")

