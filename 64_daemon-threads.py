# daemon thread =   a thread that runs in the background, not important for program to run
#                   your program will not wait for daemon threads to complete before exiting
#                   non-daemon threads cannot normally be killed, will stay alive until task is completed
#
#                   ex. background tasks, garbage collection, waiting for input, long-running processes.

import threading
import time

# Program will not exit after input if there are non-daemon threads alive!
def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for:", count, "seconds")

# Non-daemon
# x = threading.Thread(target=timer)
# x.start()

# Daemon
x = threading.Thread(target=timer, daemon=True)
x.start()

print(x.daemon)

answer = input("Do you wish to exit?\n")






