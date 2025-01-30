"""
Managing Multiple Threads, when many resources try to alter single resource.


Semaphore:
    a variable or abstract data type used to control access to a common resource by multiple threads
    and avoid critical section problems in a concurrent system such as a multitasking OS.
    Semaphores are a type of synchronization primitive.


"""
import time
import threading

import logging
logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
logging.info('Starting')

# num = 1


class SimpleMultiThreadingExample:
    """
    The result of this Example is:
    the value of `num` seems never be changed
    because in the `main` we have spawned two threads which parallely try to change the value.
    hence, always print 1
    """
    num = 1

    def double_it(self):
        # global num
        while 0 < self.num < 20_000:
            self.num *= 2
            time.sleep(1)
            logging.info(self.num)

        logging.info("Exiting double_it!")

    def half_it(self):
        # global num
        while 0 < self.num < 40_000:
            self.num /= 2
            logging.info(self.num)
            time.sleep(1)

        logging.info("Exiting half_it!")


class LockMultiThreadingExample:
    """
    Note: the both the lock objects in both the methods are same and
    if you will create new object in both the methods this will not work.
    """
    num = 1
    lock = threading.Lock()

    def double_it(self):
        lock_obj = self.lock
        lock_obj.acquire()
        while 0 < self.num < 20_000:
            self.num *= 2
            time.sleep(1)
            logging.info(self.num)

        logging.info("Exiting double_it!")
        lock_obj.release()

    def half_it(self):
        lock_obj = self.lock
        lock_obj.acquire()
        while 1 < self.num < 40_000:
            self.num /= 2
            logging.info(self.num)
            time.sleep(1)

        logging.info("Exiting half_it!")
        lock_obj.release()


class SemaphoreThreadingExample:
    """
    usage of semaphore is very much same as Locking
    Let's limit the access to the variable so that not my unlimited threads try to access
    my single mf resource.
    """
    num = 1
    sem = threading.Semaphore()

    def double_it(self):
        sem_obj = self.sem
        sem_obj.acquire()
        while 0 < self.num < 20_000:
            self.num *= 2
            time.sleep(1)
            logging.info(self.num)

        logging.info("Exiting double_it!")
        sem_obj.release()

    def half_it(self):
        sem_obj = self.sem
        sem_obj.acquire()
        while 1 < self.num < 40_000:
            self.num /= 2
            logging.info(self.num)
            time.sleep(1)

        logging.info("Exiting half_it!")
        sem_obj.release()


class AttackingSemaphoreThreadingExample:
    """
    when multiple Threads try to access the single Resource
    """
    num = 1
    sem = threading.Semaphore()  # default value is 1

    def double_it(self):
        logging.info(f"Trying to Access: {threading.get_ident()}")
        sem_obj = self.sem
        sem_obj.acquire()
        while 0 < self.num < 20_000:
            logging.info(f"Updating by: {threading.get_ident()}")
            self.num *= 2
            time.sleep(1)
            logging.info(self.num)

        logging.info("Exiting double_it!")
        sem_obj.release()

    def half_it(self):
        sem_obj = self.sem
        sem_obj.acquire()
        while 1 < self.num < 40_000:
            self.num /= 2
            logging.info(self.num)
            time.sleep(1)

        logging.info("Exiting half_it!")
        sem_obj.release()


if __name__ == '__main__':
    # 1.
    obj = SimpleMultiThreadingExample()
    t1 = threading.Thread(target=obj.double_it)
    t2 = threading.Thread(target=obj.half_it)

    # t1.start()
    # t2.start()

    # 2.
    obj = LockMultiThreadingExample()
    t3 = threading.Thread(target=obj.double_it)
    t4 = threading.Thread(target=obj.half_it)

    # t3.start()
    # t4.start()

    # 3.
    obj = SemaphoreThreadingExample()
    t5 = threading.Thread(target=obj.double_it)
    t6 = threading.Thread(target=obj.half_it)

    # t5.start()
    # t6.start()

    # 4.
    obj = AttackingSemaphoreThreadingExample()
    for _ in range(5):
        t7 = threading.Thread(target=obj.double_it)
        t7.start()
        time.sleep(0.4)
