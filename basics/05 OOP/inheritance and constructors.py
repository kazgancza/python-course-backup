
class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city
        print("Person constructor")

    def print_Person_data(self):
        print(f"Imię: {self.name}\nNazwisko: {self.surname}\nMiasto: {self.city}")

        
person1 = Person("Ola", "Kowalska", "Warszawa")
person1.print_Person_data()

class Employee(Person):
    def __init__(self, name, surname, city, company_name, salary):
        Person.__init__(self, name, surname, city)
        self.company_name = company_name
        self.salary = salary
        print("Employee constructor")

    def print_Employee_data(self):
        print("Employee.print_Employee_data")

print()
employee1 = Employee("Kasia", "Kot", "Kraków", "Amazon", 10000)
employee1.print_Person_data()
employee1.print_Employee_data()

class Manager(Employee):
    def __init__(self, name, surname, city, company_name, salary, department):
        Employee.__init__(self, name, surname, city, company_name, salary)
        self.department = department

    def hire_employee(self):
        print("Hire employee")
    
    def print_Manager_data(self):
        print("print_Manager_data")

manager1 = Manager("Adam", "Kowalski", "Toruń", "DHL", 50000, "IT")
print()
manager1.print_Person_data()
manager1.print_Employee_data()
manager1.print_Manager_data()
manager1.hire_employee()