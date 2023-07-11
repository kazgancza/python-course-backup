import os

# Absolute path with file name
print(f"Absolute path to script file: {__file__}")

# Absolute path without file name (OS Library)
script_dir = os.path.dirname(__file__)
print(f"Absolute path to script dir: {script_dir}")

# Opens/makes file in current dir
fh = open(f"{script_dir}\\newfile.txt", "w")
fh.write("content")
fh.close()
