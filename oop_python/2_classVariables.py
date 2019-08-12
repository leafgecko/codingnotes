#Summary
#ClassVariables affect all instances
#InstanceVariables affect only a specific initalized Object
#if arttribute is called via __init__, __init__'s dict checkes if it has that attribute,
#else checkes the class variables and calls that

#############################################################
#############################################################



class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    #__init__ always runs everytime a new class object of Employee is instanticated (created)
    #can be used to count num of instances
    def __init__(self, first, last, pay):
        self.namefirst = first
        #
        #
        self.pay = pay

        Employee.num_of_emps += 1

    def apply_raise(self):
            self.pay = int(self.pay * self.raise_amount) #taken from class variable instead of delcaring here

#class variables should be the same of each instance

#accessible via class or an instance (__init__) of the class

    #accissing via instance
    #checks if instance has attribute, else check class or inherit classes has that attribute

emp_1 = Employee('Corey', 'Shhh', '50000')

print(Employee.__dict__) #prints everything in class
print(emp_1.__dict__)  #prints everything in __init__

emp_1.raise_amount = 1.05
    #it also adds raise_amount to emp_1's instance __init__
    #only affects emp_1
print(emp_1.__dict__)


print(Employee.__dict__) #notice that raise_amount is UNCHANGED

Employee.raise_amount = 1.05
print(Employee.__dict__)
    #affects all
