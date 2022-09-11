"""
Demon Threads:
    They are running in the BackGround.
    But after the script terminates they stop immediately when the program exits.

    Demon used for:
    1. Web API
    2. Reading from the file

"""

import time
import logging
import threading
# import Queue
# que = Queue.Queue()
# event = threading.Event()


logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
logging.info('Starting')


class SomeIOTask:
    file_name = "text.txt"
    data = ""

    def read_from_file(self):
        while True:
            with open(self.file_name, "r") as f:
                self.data = f.read()

            print(self.data)
            time.sleep(3)  # not reading the file for 3 sec


obj = SomeIOTask()
t1 = threading.Thread(target=obj.read_from_file, daemon=False)  # now a demon thread with `False`
print(t1.isDaemon())
t1.start()



"""
Explanation:
    `t1` is a demon thread now that keeps on running in the background
    and the main thread was waiting for the input.
"""
