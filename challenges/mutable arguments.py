employee = {
    "name": "Adam",
    "email": "adam@gmail.com",
    "rank": "programmer",
    "salary": 8000
}

def promoteToManager(user):
    if user["rank"] == "manager":
        return print("Pracownik jest już menadżerem")
    else:
        employee["salary"] *= 1.5
        employee["rank"] = "manager"

promoteToManager(employee)
print(employee)
