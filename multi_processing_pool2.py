import os, sys
from multiprocessing import Pool
import time


def f(n):
    sum = 0
    for x in range(1000):
        sum += x * x
    return sum

def d(n):
    p = Pool(processes=3)
    result = p.map(f, range(10000))

def c(n):
    d(1000)





def get_elapsed_time(start_time, end_time):
    hrs, remainders = divmod((end_time - start_time), 3600)
    mins, secs = divmod(remainders, 60)
    return f"{str(int(hrs))}:{str(int(mins))}:{str(float(secs))}"


if __name__ == "__main__":
    t1 = time.time()
    p = Pool(processes=3)
    result = p.map(c, range(100000))
    for n in result:
        print(n)
    print(f"Finish with Elapsed Time: {get_elapsed_time(t1, time.time())}")
