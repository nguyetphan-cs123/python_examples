import os, sys
import time
import multiprocessing


def calc_square(numbers, result, v):
    v.value = 5.67
    for idx, n in enumerate(numbers):
        time.sleep(1)
        result[idx] = n * n


def calc_cube(numbers):
    for n in numbers:
        time.sleep(5)
        print(f"cube: {n * n * n}")


def get_elapsed_time(start_time, end_time):
    hrs, remainders = divmod((end_time - start_time), 3600)
    mins, secs = divmod(remainders, 60)
    return f"{int(hrs)}:{int(mins)}:{int(secs)}"


if __name__ == "__main__":
    start_time = time.time()
    arr = [2, 3, 8, 9, 10, 11, 12]
    result = multiprocessing.Array('i', 7)
    v = multiprocessing.Value('d', 0.0)
    p1 = multiprocessing.Process(target=calc_square, args=(arr, result, v))
    # p2 = multiprocessing.Process(target=calc_cube, args=(arr,))
    p1.start()
    # p2.start()
    p1.join()
    # p2.join()

    end_time = time.time()
    print(result)
    print(v.value)
