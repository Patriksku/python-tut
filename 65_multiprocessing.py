# *********************************
# Python multiprocessing
# *********************************
#
# multiprocessing = running tasks in parallel on different CPU cores, bypasses GIL, used for threading
#                   multiprocessing = better for cpu bound tasks (heavy CPU usage)
#                   multithreading = better for io bound tasks (waiting around)
#

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    start = time.perf_counter()

    print(cpu_count())  # Amount of cores

    # If we create more processes than the amount of cores that we have
    # There is significant overhead when beginning and destroying processes
    # Therefore you are creating additional processes, to no extra benefit,
    # So overhead results in slower execution (hindering the performance of the computer)
    a = Process(target=counter, args=(25000000,))
    b = Process(target=counter, args=(25000000,))
    c = Process(target=counter, args=(25000000,))
    d = Process(target=counter, args=(25000000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    res = time.perf_counter() - start
    print("finished in: %.5f" % res, "seconds")

# If we create a child process from main, it's going to copy the main module, and the child
# process will create its own children processes -> problem (Windows)

# We add this so when we create a child process, it will copy our module, but will not execute it
if __name__ == '__main__':
    main()





