class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def work(self):
        print(f"{self.name} is working...")

class Software(Employee):
    def __init__(self,name,age, salary,level,lang):
        super().__init__(name,age,salary)
        self.level=level
        self.lang=lang

    def work(self):
        print(f"{self.name} is coding...")


    def debug(self):
        print(f"{self.name} is debugging....")

class Design(Employee):
    def __init__(self, name, age, salary,level):
        super().__init__(name, age,salary)
        self.level = level
    def work(self):
        print(f"{self.name} is designing...")

    def draw(self):
        print(f"{self.name} is drawing....")


def mot_employee(employees):
    for employee in employees:
        employee.work()


se1=Software("Bill",25,7000,"Junior","Python")
print(se1.name,se1.age)
d1=Design("Max",37,9500,"Senior")
print(d1.name,d1.age)
se1.work()
d1.work()
se1.debug()
d1.draw()

employees=[Software("Bill",25,7000,"Junior","Python"),
           Software("Dave",32,9000,"denior","C#"),
           Design("Mike",22,8000,"Intermediate")
           ]


mot_employee(employees)