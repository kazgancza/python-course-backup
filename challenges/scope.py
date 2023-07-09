employees = []

def addEmployee(email, salary):
    someDict = {
        "email": email,
        "salary": salary
    }
    employees.append(someDict)

def increaseSalary(emloyees, pctIncrease):
    for i in emloyees:
        i["salary"] = i["salary"] + ( i["salary"] * pctIncrease / 100 )


addEmployee("adam@gmail.com", 6000)
addEmployee("bartek@gmail.com", 8000)
addEmployee("zosia@gmail.com", 10000)

increaseSalary(employees, 20)

print(employees)