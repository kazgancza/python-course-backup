import os

print(f"Current working dir: {os.getcwd()}")

files = os.listdir(".")
# print(files)


files = os.listdir("./private")
# print(files)

files = os.listdir("..")
# print(files)

files = os.listdir("../ISO Systems")
print(files)
