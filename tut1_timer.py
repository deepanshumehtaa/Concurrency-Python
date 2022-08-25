# Queues and Future

# What is Future ?
# A Future represents an eventual result of an asynchronous operation.
# Not thread-safe. Future is an awaitable object.
# Coroutines can await on Future objects until they either have a result
# or an exception set, or until they are cancelled.

"""
Q: What Threads exactly look like?
A: A processor has cores (called CPU), CPU has Threads (slice of Time),
At Machine level it look like:
    1.  Ram (physical memory) has some memory space allocated to the processor
    2.  Process has multiple Threads.
    3.  There is a Thread Scheduler at OS level. It Decides which thread will get the CPU first.
        The thread scheduler selects the thread that has the highest priority, & the thread begins
        the execution of the job.
    4.  Then finally CPU gets the thread from the Scheduler to execute.


User Level Thread(ULT):
     Implemented by users and the kernel is not aware of the existence of these threads.
     It handles them as if they were single-threaded processes.
     User-level threads are small and much faster than kernel level threads.

kernel level threads(KLT):
    1. Handled by OS directly
    2. slower than ULT
    3. Why Slower ?
        KLT require a context switch, which involves changing a large set of processor registers
        that define the current memory map and permissions.
        It also evicts some or all of the processor cache.



Thread Scheduling:
Two ways:
1. Scheduling of user level threads(ULT) to kernel level threads(KLT) via lightweight process(LWP) by the application developer.
2. Scheduling of kernel level threads by the system scheduler to perform different unique os functions.

Queue:

Future:
    1. use to handle concurrent programming language.
    2. They discribed as object which act as a proxy for a result that initially unknown
    2.1 Because of its value not yet completed due to some pending/ongoing computation

"""
import time
from threading import Timer  # utilized to run a code after a specified time period


def display(msg):
    # https://docs.python.org/3/library/time.html
    print(msg + ' ' + time.strftime('%H:%M:%S'))
    return "YO"


# Basic timer:
def run_once():
    ans = display('Run once:')
    print(ans)
    # a new thread start a counter of 5 sec, then display called with args
    # this is now non-blocking, the context of execution will skip this
    # then once the thread is over it, this child thread automatically join with the main/parent thread
    t = Timer(2, display, args=['Timeout:'])
    t.start()  # starting a new Thread
    print()


run_once()
print("GO!")

time.sleep(5)  # putting the main thread to sleep
print("Woke Up!")
# t.cancel()

# creating custom Threading Timer


class MyTimer(Timer):
    def run(self) -> None:
        ...



