from multiprocessing import Pool, cpu_count
from time import time


def factorize(*numbers: int):
    with Pool(cpu_count()) as p:
        p.map_async(
            func_calculation,
            list(numbers),
            callback=callback,
        )

        p.close()  # перестати виділяти процеси в пулл
        p.join()  # дочекатися закінчення всіх процесів


def func_calculation(number: int) -> list:
    resoult_list = []
    for el in range(1, number):
        if not number % el:
            resoult_list.append(el)
    resoult_list.append(number)
    return number, resoult_list


def callback(resoult):
    for el in resoult:
        print(el[0], ":", el[1])


if __name__ == "__main__":
    t1 = time()
    factorize(10651060, 40651060, 10621060, 20651060,
              10051060, 10000, 100000, 1000000)
    t2 = time()
    print(t2 - t1)
