class Software:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self._salary=None
        self._num_bugs_solved=0

    def code(self):
        self._num_bugs_solved+=1

    def get_salary(self):
        return self._salary

    def set_salary(self,base_value):
        if base_value<1000:
            self._salary=1000
        if base_value>20000:
            self._salary=20000
        self._salary=self.calculate_salary(base_value)

    def calculate_salary(self,base_value):
        if self._num_bugs_solved<10:
            return base_value
        if self._num_bugs_solved<100:
            return base_value*2
        return base_value*3


se=Software("Michael",33)
se.set_salary(6000)
print(se.get_salary())
se2=Software("Bill",52)
for i in range(70):
    se2.code()
se2.set_salary(10000)
print(se2.get_salary())
