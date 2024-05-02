import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
from threading import Thread

import requests


def get_id():
    pid = os.getpid()
    name = threading.current_thread().name
    print(f"PID: {pid}, PName: {name}")


i = 0
lock = threading.Lock()
queue = Queue()
queue.put(0)


def counter():
    lock.acquire()
    global i
    j = i
    time.sleep(0.1)
    i = j + 1
    lock.release()


# Использование очередей - аналог блокинга. Очереди потокобезопасны и решают вопрос гонки
def counter_queue():
    j = queue.get()
    time.sleep(0.1)
    queue.put(j + 1)


def request_to_yandex():
    response = requests.get('https://yandex.ru')
    print(response.status_code)


def request_to_google():
    response = requests.get('https://google.com')
    print(response.status_code)


def request_to_youtube():
    response = requests.get('https://youtube.com')
    print(response.status_code)


def main():
    tasks = (request_to_yandex, request_to_google, request_to_youtube)

    with ThreadPoolExecutor() as executor:
        for task in tasks:
            executor.submit(task)

    # executor = ThreadPoolExecutor()
    # for _ in range(10):
    #     executor.submit(request_to_yandex)
    # executor.shutdown(wait=True)

    threads = [Thread(target=counter_queue, daemon=True) for _ in range(25)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # print(i)
    print(queue.qsize())
    print(queue.get_nowait())


if __name__ == '__main__':
    main()
