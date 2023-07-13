import os

script_dir = os.path.dirname(__file__)
print(script_dir)

fh = open(f"{script_dir}/ogonki.txt", "w", encoding="utf-8")
fh.write("ĄąĆćĘęŁłŻżŹź\n")
fh.write("ĄąĆćĘęŁłŻżŹź\n")
fh.write("ĄąĆćĘęŁłŻżŹź")
fh.close()
