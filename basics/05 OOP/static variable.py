
class Employee:
    "Employee class describing company empolyee"
    # static variables for all objects based on Employee
    num_employees = 0
    employees_list = []

    def __init__(self, name):
        "Constructor for employee"
        """
            line 1
            line 2
        """
        self.name = name
        Employee.num_employees += 1
        Employee.employees_list.append(self.name)

        print(f"Employee.num_employees: {Employee.num_employees}")
        print(Employee.employees_list)

    def print_all_employees(self):
        for i in Employee.employees_list:
            print(i)

employee1 = Employee("Ola")
employee2 = Employee("Adam")
employee3 = Employee("Katarzyna")
employee4 = Employee("Karol")

employee1.print_all_employees()

# help(Employee)

print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)

print(f"name attr in Employee: {hasattr(employee1, 'name')}")
print(f"name attr in Employee: {hasattr(employee1, 'city')}")
employee1.city = "Kraków"
print(f"name attr in Employee: {hasattr(employee1, 'city')}")

setattr(employee1, "name", "Kasia")
print(f"employee1.name: {getattr(employee1, 'name')}")

