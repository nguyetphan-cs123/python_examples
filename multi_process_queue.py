import multiprocessing

# share file, share memory use queue


def calc_square(numbers, q):
    for n in numbers:
        q.put(n*n)


if __name__ == "__main__":
    numbers = [2, 3, 5]
    # shared resources using queue
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=calc_square, args=(numbers, q))
    p1.start()
    p1.join()



