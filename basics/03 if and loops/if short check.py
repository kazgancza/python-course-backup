flag = True

if flag == True: # taki zapis jest ok
    print("flag = True")

if flag is True: # taki zapis jest raczej nie ok
    print("flag = True")

if flag: # najlepszy, najkrótszy zapis
    print("flag = True")

flag = False

if flag != True:
    print("flag = False")

if flag == False:
    print("flag = False")

if flag is not True:
    print("flag = False")

if not flag: # najlepszy, najkrótszy zapis
    print("flag = False")
