from collections.abc import Callable, Iterable, Mapping
import threading
import time
from typing import Any


class some_thread(threading.Thread):
    def __init__(self, thread_name, sleep_time):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.sleep_time = sleep_time

    def run(self):
        num = 0
        max = 6

        while num < max:
            local_time = time.localtime()

            print(self.thread_name, time.strftime(" %H %M %S", local_time))
            time.sleep(self.sleep_time)

            num += 1
        print(self.thread_name, " ended")


t1 = some_thread("T1", 0.1)
t2 = some_thread("T2", 0.3)
t3 = some_thread("T3", 0.4)

t1.start()
t2.start()
t3.start()

time.sleep(1)
print(" -- Thread 2 status: ", t2.is_alive())

t1.join()
t2.join()
t3.join()



print("Threads ended")