# thread = a flow of execution. Like a separate order of instructions.
#          However each thread takes a turn running to achieve concurrency.
#          GIL = (global interpreter lock),
#          allows only one thread to hold the control of the Python interpreter, at any one time
#
# CPU bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing (parallelism)
#
# IO bond = program/task spends most of it's time waiting for external events (user input, web scraping)
#           use multithreading (concurrent)

import threading
import time

start = time.perf_counter()

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drink coffee")


def study():
    time.sleep(5)
    print("You study")


x = threading.Thread(target=eat_breakfast, args=())  # If you have parameters you can specify them in args
x.start()

y = threading.Thread(target=drink_coffee, args=())  # If you have parameters you can specify them in args
y.start()

z = threading.Thread(target=study, args=())  # If you have parameters you can specify them in args
z.start()

x.join()  # Main thread now has to wait for thread 'x' to finish
y.join()
z.join()

# eat_breakfast()
# drink_coffee()
# study()

print(threading.active_count())
print(threading.enumerate())
total_time = time.perf_counter() - start
print("%.5f" % total_time)

