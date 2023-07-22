import os
import shutil


script_dir = os.path.dirname(__file__)

fh = open(script_dir + "/test.txt", "w", encoding="utf-8")
fh.write("abcdefg")
fh.close()

if not os.path.exists(script_dir + "/newTest.txt"):
    os.rename(script_dir + "/test.txt", script_dir + "/newTest.txt")

print(os.path.getsize(script_dir + "/newTest.txt"))

print(os.path.isfile(script_dir + "/newTest.txt"))

print(os.path.isdir(script_dir + "/newTest.txt"))

print(os.path.isdir("./public"))

if os.path.exists(script_dir + "/subDir"):
    os.rmdir(script_dir + "/subDir")

if not os.path.exists(script_dir + "/subDir"):
    os.mkdir(script_dir + "/subDir")

if os.path.exists(script_dir + "/newTest.txt"):
    os.remove(script_dir + "/newTest.txt")

print(f"Current working dir: {os.getcwd()}")
os.chdir(script_dir)
print(f"Current working dir: {os.getcwd()}")

if not os.path.exists("data-copy.dat"):
    shutil.copyfile("data.dat","data-copy.dat")

