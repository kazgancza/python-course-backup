import user
from manager import Manager

print(f"main:: {user.user1}")

employee1 = user.Employee("Jacek")
print(f"main: {employee1}")

manager1 = Manager("Kasia")
print(f"main: {manager1}")
