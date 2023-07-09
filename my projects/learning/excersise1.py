# Napisz program, który poprosi użytkownika o wprowadzenie listy liczb całkowitych,
# a następnie wyświetli dwie listy: jedną z parzystymi liczbami wprowadzonymi przez użytkownika, a drugą z nieparzystymi.
# Na koniec program powinien również wyświetlić sumę i iloczyn każdej z list.

numbers = input("Podaj liczby oddzielone przecinkami: ")
numbers_list = numbers.split(",")
numbers_list_even = []
numbers_list_uneven = []
numbers_list_even_sum = 0
numbers_list_even_multiplied = 1
numbers_list_uneven_sum = 0
numbers_list_uneven_multiplied = 1


for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])

for i in numbers_list:
    if i % 2 == 0:
        numbers_list_even.append(i)
    else:
        numbers_list_uneven.append(i)

for i in numbers_list_even:
    numbers_list_even_sum += i
    numbers_list_even_multiplied *= i

for i in numbers_list_uneven:
    numbers_list_uneven_sum += i
    numbers_list_uneven_multiplied *= i


print("Liczby parzyste:", numbers_list_even)
print("Suma parzystych:", numbers_list_even_sum)
print("Iloraz parzystych:", numbers_list_even_multiplied)

print("Liczby nieparzyste:", numbers_list_uneven)
print("Suma nieparzystych:", numbers_list_uneven_sum)
print("Iloraz nieparzystych:", numbers_list_uneven_multiplied)
