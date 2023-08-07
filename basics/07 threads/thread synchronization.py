import threading
import time
from typing import Any


data = ["Adam", "Bartek", "Czesiu", "Damian", "Edek"]
data_lock = threading.Lock()


class some_thread(threading.Thread):
    def __init__(self, thread_name, data_len, sleep_time):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.data_len = data_len
        self.sleep_time = sleep_time

    def run(self):
        num = 0

        while num < self.data_len:
            
            data_lock.acquire()
            data[num] = f"{data[num]} {str(num)}"
            print(self.thread_name, data[num])
            data_lock.release()

            time.sleep(self.sleep_time)

            num += 1
        print(self.thread_name, " ended")


t1 = some_thread("T1", len(data), 0.1)
t2 = some_thread("T2", len(data), 0.3)
t3 = some_thread("T3", len(data), 0.4)

t1.start()
t2.start()
t3.start()

time.sleep(1)
print(" -- Thread 2 status: ", t2.is_alive())

t1.join()
t2.join()
t3.join()



print("Threads ended")