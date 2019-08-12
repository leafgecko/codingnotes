
#Summary
#Created class (learnt class vs instance of a class)
#Initialize class attributes
#Created Methods

#######################################################
#######################################################


class Employee():

    #pass #lets you leave it empty, skip it

    #Class Attributes are shared variable belonging to main class
    #Defined OUTSIDE of constructor function (__init__)
    species = 'human'

    #Instance Attributes
    def __init__(self, first, last, pay):    #initialize, like a constructor
        #instance is called self
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

#creating a method in class to put functionality in one place
    #each method within a class takes the instance as the first argeuemt (i.e. self)
    #Instance Method
    def fullname (self):
        return '{} {}'.format(self.first, self.last)

#Instantiate the Employee Object
emp_1 = Employee('Corey', 'Schafer', 50000) #instance of employee class
#runs init method

print(emp_1.email)

    #    super(, self).__init__()
    #    self.arg = arg

#Class is a blueprint for creating instances

#Adding methods to class
#e.g. display full name of Employee

print('{} {}'.format(emp_1.first, emp_1.last))

#creating a method in class to put functionality in one place
#Calling Instance Method
print(emp_1.fullname()) #() are needed as it is now a method and not an attribute
#above is code reuse
#intance (emp_1) is automatically being passed into fullname, despite args seemingly empty

#another way
print(Employee.fullname(emp_1))
