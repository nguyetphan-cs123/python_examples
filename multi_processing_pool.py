import os, sys
from multiprocessing import Pool
import time


def f(n):
    sum = 0
    for x in range(1000):
        sum += x * x
    return sum


def get_elapsed_time(start_time, end_time):
    hrs, remainders = divmod((end_time - start_time), 3600)
    mins, secs = divmod(remainders, 60)
    return f"{str(int(hrs))}:{str(int(mins))}:{str(float(secs))}"


if __name__ == "__main__":
    # arr = [1, 2, 3, 4, 5]
    # result = []
    # for n in arr:
    #     result.append(f(n))
    # print(result)
    # arr = [1, 2, 3, 4, 5]
    t1 = time.time()
    p = Pool()
    # result = p.map(f, arr)
    result = p.map(f, range(100000))
    p.close()
    # p.join() return only when all worker processes return
    p.join()
    print(f"Parallel result: {result}")
    print(f"Pool finished with Elapsed Time: {get_elapsed_time(t1, time.time())}")

    # Serial processing
    t2 = time.time()
    result = []
    for x in range(100000):
        result.append(f(x))
    print(f"Serial result: {result}")

    print(f"Serial processing took: {get_elapsed_time(t1, time.time())}")
