def is_pesel(pesel):
    if len(str(pesel)) == 11:
        return True
    else: return False



while True:
    pesel = input("Wprowadź nr PESEL: ")
    if is_pesel(pesel):
        print(f"{pesel} jest numerem PESEL")
        break
    else:
        print("Wprowadź prawidłowy numer PESEL")
    continue

