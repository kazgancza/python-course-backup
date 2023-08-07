import _thread
import time


def print_time(thread_name, sleep_time):
    num = 0
    max = 100

    while num < max:
        local_time = time.localtime()

        print(thread_name, time.strftime(" %H %M %S", local_time))
        time.sleep(sleep_time)

        num += 1
    print(thread_name, " ended")


_thread.start_new_thread(print_time, ("thread 1", 0.3))
_thread.start_new_thread(print_time, ("thread 2", 0.5))

# infinite loop - for testing purposes only
while True:
    pass

