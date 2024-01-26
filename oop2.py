'''
se1 = ["Software Engineer", "Bill", 55, "Master", 150000]
se2 = ["Software Engineer", "Mike", 25, "Junior", 50000]
d1 = ["Designer", "Michael"]
'''

class softwareEng:
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f"{self.name} is coding...")

    def code_in_lang(self, lang):
        print(f"{self.name} is coding in {lang}...")

    def __str__(self):
        info=f"name={self.name}, age={self.age}, level={self.level}, salary={self.salary}"
        return info

    def __eq__(self, other):
        return self.name==other.name and self.age==other.age

    @staticmethod
    def entry_salary(age):
        if age<25:
            return 5000
        if age<30:
            return 7000
        return 9000


se1 = softwareEng("Bill", 55, "Master", 150000)
se2 = softwareEng("Mike", 25, "Junior", 50000)
se3 = softwareEng("Mike", 25, "Junior", 50000)
print(se1.__dict__)
print(se2.__dict__)
se1.code_in_lang("python")
print(se1)
print(se2)
print(se2==se3)
print(softwareEng.alias)
print(se1.entry_salary(24))
print(softwareEng.entry_salary(27))
#-----------------------------------------------------------

# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))
