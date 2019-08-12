
#regular methods takes in the instance (i.e. self) as the first arguement

class Employee():

@classMethods #decorators allow us to use classMethods
def set_raise_amt(cls, amount): #cls == class variable name as first argument
    cls.raise_amt = amount

Employee.set_raise_amt(1.05) #uses class method
#Employee.raise_amt = 1.05 #same as above


#Classmethods as alternative constructor
@classMethods
def from_string(cls, emp_str):
    first, last, pay = emp_str.split('-')
    return cls(first, last, pay)

# Above class method same as
# first, last, pay = emp_str_1.split('-') #parsing a string by -
#new_emp_1 = Employee(first, last, pay)

emp_str_1 = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)


#StaticMethods -> no automatic arguments, logically connected
#but not depending on any specific instance or class variable

@StaticMethods
def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6:
        return False
    return True
#note that StaticMethods did not access the instance or the class

import datetime
my_date = datetime.date(2016.7.11)
print(Employee.is_workday(my_date)
