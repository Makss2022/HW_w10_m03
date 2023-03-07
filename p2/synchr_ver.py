from time import time


def factorize(*numbers: int) -> dict:
    resoult_dict = {}
    for number in numbers:
        resoult_dict[number] = func_calculation(number)
    return resoult_dict


def func_calculation(number: int) -> list:
    resoult_list = []
    for el in range(1, number):
        if not number % el:
            resoult_list.append(el)
    resoult_list.append(number)
    return resoult_list


if __name__ == "__main__":
    t1 = time()
    resoult = factorize(10651060, 40651060, 10621060,
                        20651060, 10051060, 10000, 100000, 1000000)
    t2 = time()
    for key, vel in resoult.items():
        print(key, ":", vel)
    print(t2 - t1)
