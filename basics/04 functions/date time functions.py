import time
import datetime

ticks = time.time() # Ilość sekund od 01.01.1970
print(ticks)

timeData = time.localtime()
# time.struct_time(tm_year=2023, tm_mon=3, tm_mday=15,
#  tm_hour=20, tm_min=49, tm_sec=33, tm_wday=2, tm_yday=74, tm_isdst=0)
print(timeData)
print(timeData.tm_year)

timeData = time.localtime(10) # 10 sekund od 01.01.1970
print(timeData)
print(timeData.tm_year)

# Pokazanie aktualnego czasu
result = time.asctime(time.localtime()) # Wed Mar 15 20:52:51 2023
print(result)

# Pokazanie aktualnego czasu w sposób jaki chcemy
timeData = time.localtime()
print(time.strftime("%d/%m/%Y %H:%M:%S", timeData)) # 15/03/2023 20:54:32

# W drugą stronę
timeStr = "17:23:45 08.12.2021"
timeData = time.strptime(timeStr, "%H:%M:%S %d.%m.%Y")
print(timeData)

# Funkcja sleep
i = 0
while i < 6:
    time.sleep(0.5)
    print(time.asctime(time.localtime()))
    i += 1

tStart = time.perf_counter()
time.sleep(1.2)
tEnd = time.perf_counter()
print("Code took:", (tEnd - tStart), "seconds")

# datetime z mikrosekundami
dateTimeObj = datetime.datetime.now()
print(dateTimeObj) # 2023-03-15 21:02:30.906576
#print(dir(dateTimeObj))

datetimeObj = datetime.date(2025, 12, 30)
datetimeObj = datetime.datetime(2025, 12, 30, 22, 59, 59)
print(datetimeObj.date()) # 2025-12-30
print(datetimeObj.time()) # 22:59:59
print(datetimeObj.timestamp()) # Ilość sekund od 01.01.1970
# Konkretne wartości
print(datetimeObj.year)
print(datetimeObj.month)
print(datetimeObj.day)
print(datetimeObj.hour)
print(datetimeObj.minute)
print(datetimeObj.second)

# Ładne pokazanie daty
print("format:", datetimeObj.strftime("%H:%M:%S %d/%m/%Y"))

datetimeObj = datetimeObj.now()
print("format:", datetimeObj.strftime("%H:%M:%S %d/%m/%Y"))

# Porównanie dat
datetime1 = datetime.datetime(2025,1,1, 23,59,59)
datetime2 = datetime.datetime(2030,1,1, 23,59,59)
print(datetime2 > datetime1) # True

datetime1 = datetime.date(2025,1,1)
datetime2 = datetime.date(2030,1,1)
print(datetime2 > datetime1) # True
