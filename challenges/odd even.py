data = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

for v in data:
    if v == 0:
        print("Zero jest parzyste")
    elif v % 2 == 0:
        print(v, "jest parzysta")
    else:
        print(v, "jest nieparzysta")
