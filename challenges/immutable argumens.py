def increaseSalary(money, bonus):
    money += money * 0.2
    return money + bonus

salary = 5000
newSalary = increaseSalary(salary, 1000)
print(salary)
print(newSalary)
