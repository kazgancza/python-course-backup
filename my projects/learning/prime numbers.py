prime_num = 3
checking_num = 2
prime_list = []
quantity_expected = int(input("Podaj ile liczb pierwszych chcesz zobaczyć:"))
quantity = 0

while quantity_expected > quantity:
    while prime_num != checking_num:
        if prime_num % checking_num != 0:
            checking_num += 1
        else:
            prime_num += 1
            checking_num = 2
            break
        if prime_num == checking_num:
            prime_list.append(prime_num)
            quantity += 1
            prime_num += 1
            checking_num = 2
            
print(prime_list)
