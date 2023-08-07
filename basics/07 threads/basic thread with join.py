import threading
import time


def print_time(thread_name, sleep_time):
    num = 0
    max = 6

    while num < max:
        local_time = time.localtime()

        print(thread_name, time.strftime(" %H %M %S", local_time))
        time.sleep(sleep_time)

        num += 1
    print(thread_name, " ended")


t1 = threading.Thread(target=print_time, args=("thread 1", 0.5))
t2 = threading.Thread(target=print_time, args=("thread 2", 0.2))
t3 = threading.Thread(target=print_time, args=("thread 3", 0.4))

t1.start()
t2.start()
t3.start()

# makes the main thread wiat for ending of t1, t2, t3 threads
t1.join()
print("T1 ended for main thread")
t2.join()
print("T2 ended for main thread")
t3.join()
print("T3 ended for main thread")

print("Threads ended")

