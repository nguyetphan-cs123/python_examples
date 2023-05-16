import time
import multiprocessing


def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


if __name__ == "__main__":
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()
    deposit_process = multiprocessing.Process(target=deposit, args=(balance, lock))
    withraw_process = multiprocessing.Process(target=withdraw, args=(balance, lock))
    deposit_process.start()
    withraw_process.start()
    deposit_process.join()
    withraw_process.join()
    print(balance.value)