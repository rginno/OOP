class User:
    def log(self):
        print(self)


class Teacher(User):
    def log(self):
        print("Teacher!!!")


class Customer(User):
    def __init__(self,name,membership_type):
        self.name=name
        self.membership_type=membership_type
    @property
    def name(self):
        print("Getting name!!!")
        return self._name

    @name.setter
    def name(self,name):
        print("Setting name!!!")
        self._name=name

    @name.deleter
    def name(self):
        del self._name

    def update_membership(self, new_membership):
        print("membership updated!!!")
        self.membership_type=new_membership


    def read_customer(self):
        print("Customer Read!!!")

    def __str__(self):
        print("convert to string")
        return self.name+" "+self.membership_type


    def print_all_customers(customers):
        for customer in customers:
            print(customer)

            
    def  __eq__(self, other):
        if self.name==other.name and self.membership_type==other.membership_type:
            return True
        return False
    __repr__=__str__

''' 
c = Customer("Vince","Gold")
print(c.name, c.membership_type)
c2 = Customer("Steve","Platinum")
print(c2.name, c2.membership_type)
'''
customers = [Customer("Vince","Gold"), Customer("Steve","Platinum"),Teacher()]

#Customer.print_all_customers(customers)
'''
print(customers[0].name)
print(customers[1].name, customers[1].membership_type)
customers[1].upgrade_membership("Golden Platinum")
print(customers[1].membership_type)
Customer.read_customer()
print(customers[1])

Teacher=["Michael","Silver"]
print(id(customers[0]),id(customers[1]))
print(customers[0]==customers[1])
print(customers)
'''
customers[2].log()
for customer in customers:
    customer.log()






