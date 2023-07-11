
fh = open("C:\\Users\\quil8\\Desktop\\Python\\test.txt", "r")
lines = fh.readlines()
fh.close()

for line in lines:
    print(line)

