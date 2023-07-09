import random


class Student:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.schoolname = None
        self.fieldOfStudy = None


    def printInfo(self):
        print(self.name, self.surname, self.age, self.city, self.schoolname, self.fieldOfStudy)
    

class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.studentsList = []
        self.fieldsOfStudy = ["IT", "Math", "Robotics"]


    def addStudent(self, student):
        if isinstance(student, Student):
            self.studentsList.append(student)
        student.schoolname = self.name
        student.fieldOfStudy = random.choice(self.fieldsOfStudy)

    def printSchoolInfo(self):
        print("School name:", self.name, "\nCity:", self.city,)
        print("Students:")
        for el in self.studentsList:
            el.printInfo()



student1 = Student("Katarzyna", "Lis", 20, "Kraków")
student1.schoolname = "Tech School"
student1.country = "Poland"
student1.printInfo()
print(student1.country)
        
student2 = Student("Adam", "Kowalski", 21, "Kraków")

school = School("Technical School", "Warszawa")
school.addStudent(student1)
school.printSchoolInfo()
print()
school.addStudent(student2)
school.printSchoolInfo()