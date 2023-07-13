import os
import pickle

script_dir = os.path.dirname(__file__)

number = 12345
list_data = ["Ania", "Ola", "Kasia", 9876]
str_data = "Tekst"

fh = open(f"{script_dir}/data.dat", "wb")
pickle.dump(number, fh)
pickle.dump(list_data, fh)
pickle.dump(str_data, fh)
fh.close()


fh = open(f"{script_dir}/data.dat", "rb")
number_info = pickle.load(fh)
list_info = pickle.load(fh)
str_info = pickle.load(fh)
fh.close()

print(number_info)
print(list_info)
print(str_info)
