import random
import time

current_timestamp = time.time()


def get_random_date():
    random_timestamp = random.randint(0, int(current_timestamp))
    random_time = time.localtime(random_timestamp)
    return time.asctime(random_time)




for i in range(0,100):
    print(get_random_date())
    time.sleep(0.5)
