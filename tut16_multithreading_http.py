"""
ref: https://python.plainenglish.io/send-http-requests-as-fast-as-possible-in-python-304134d46604

So if you’re making several requests to the same host,
the underlying TCP connection will be reused,
which can result in a significant performance increase — Session Objects

https://realpython.com/async-io-python/
"""

import requests
from requests.sessions import Session
import time
from threading import Thread, local
from queue import Queue

"""
Also, `local` is a class that represents thread-local data. Thread-local data is data that 
is associated with a specific thread and is not shared with other threads. 

This can be useful for storing data that is specific to a particular thread, such as:
the current request's session


user_id = local()
user_id.value = 1

def child_thread():
    print(user_id.value)

t = Thread(target=child_thread)
t.start()
t.join()


"""

url_list = ["https://www.google.com/", "https://www.bing.com"] * 50
q = Queue(maxsize=0)  # Use a queue to store all URLs

for url in url_list:
    q.put(url)

thread_local = local()  # The thread_local will hold a Session object


def get_session() -> Session:
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()  # Create a new Session if not exists
    return thread_local.session


def download_link() -> None:
    '''download link worker, get URL from queue until no url left in the queue'''
    session = get_session()
    while True:
        url = q.get()
        with session.get(url) as response:
            print(f'Read {len(response.content)} from {url}')
        q.task_done()  # tell the queue, this url downloading work is done


def download_all(urls) -> None:
    """Start 10 threads, each thread as a wrapper of downloader"""
    thread_num = 10
    for i in range(thread_num):
        t_worker = Thread(target=download_link)
        t_worker.start()
    q.join()  # main thread wait until all url finished downloading


print("start work")
start = time.time()
download_all(url_list)
end = time.time()
print(f'download {len(url_list)} links in {end - start} seconds')
