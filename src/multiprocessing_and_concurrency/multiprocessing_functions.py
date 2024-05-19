# Multiprocessing - подходит для IO-bound и CPU-bound задач.
# Ускоряет задачи, распараллеливая их на ядра процессора (есть предел, закон Амдала)
# Создаёт процессы с отдельными интерпретаторами и GIL, которые общаются через pickle.
# API принципиально похож на многопоточность.
# Использовать Pool, а для взаимодействия между процессами Queue и Pipe.

# Плюсы:
# + Реальная параллельность любых задач
# + Не умирает из-за одного процесса
# + Процессы не зависят друг от друга (у каждого своя память и GIL)
# Минусы:
# - Большое потребления ресурсов (памяти, времени, процессора)
# - Необходимость сериализации и десериализации в pickle
# - Проблемы синхронизации (взаимодействие между процессами)


import math
import time
from multiprocessing import Process, Pool

import requests as requests


def math_evaluation():
    res = 0
    for i in range(1_000_000):
        res += abs(round(i ** 2 / 122) + i * math.pi)
    print(res)


def get_yandex():
    response = requests.get('https://ya.ru')
    print(response.status_code)


def run(parallel=False):
    time_start = time.time()

    if not parallel:
        for _ in range(10):
            math_evaluation()
            get_yandex()
    else:
        process1 = [Process(target=math_evaluation, daemon=True) for _ in range(10)]
        process2 = [Process(target=get_yandex, daemon=True) for _ in range(10)]

        for task in process1:
            task.start()
        for task in process2:
            task.start()
        for task in process1:
            task.join()
        for task in process2:
            task.join()

    print(f'Время работы функции run {time.time() - time_start} секунд.')


def summ_items(arr: list) -> None:
    print(sum(arr))


def summ_items_parallel():
    time_start = time.time()
    arr = list(range(1_000_000))
    step = 100_000
    pos = 0
    processes = []

    for _ in range(10):
        processes.append(Process(target=summ_items, args=(arr[pos:pos + step],), daemon=True))
        pos += step
    for task in processes:
        task.start()
    for task in processes:
        task.join()

    print(f'Время работы функции run {time.time() - time_start} секунд.')


def summ_items_parallel_pool():
    time_start = time.time()
    arr = list(range(1_000_000))
    step = 100_000

    with Pool(10) as pool:
        # Генерирует список возвращаемых значений функцией summ_items с разными аргументами
        pool.map(summ_items, [arr[pos:pos + step] for pos in range(0, len(arr), step)])

    print(f'Время работы функции run {time.time() - time_start} секунд.')


if __name__ == '__main__':
    run()
    run(True)

    summ_items_parallel()
    summ_items_parallel_pool()
