class Software:

    def __init__(self):
        self._salary=None

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        self._salary=value

    @salary.deleter
    def salary(self):
        del self._salary

    def printDetails(self,salary):
        print(F"Salary: {self._salary}")


se=Software()
se.salary=6000
print(se.salary)
se2=Software()
se2.salary=10000
print(se2.salary)
se.printDetails(10000)
se2.printDetails(se2.salary)
