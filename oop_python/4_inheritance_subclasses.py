class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = play

    def apply_raise(self):
        self.pay = int (self.pay * self.raise_amt)

class Developer(Employee): #instantiate our developer class
    raise_amt = 1.10

    def __int__ (self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #pass to emplyee's init method
        #another way
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang  #only handles this

class Manager(Employee):
    def __init__ (self, first, last, pay, employees=None): #shouldn't pass an empty list (mutable datatypes) as default arg
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = [] #empty list
        else:
            self.employees = employees

    #Add method
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.emplyees.remove(emp)

    def print_emps(self):
        for emp in self.emplyees:
            print('-->', emp.firstname())


print(help(Developer))
#shows method resolution order (search attributes and methods here)
#method resolution order: chain of inheritance

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')    #raises from subclass
dev_2 = Employee('Test', 'User', 60000, 'Java')         #raises from mainclass

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

#########################
print(dev_1.pay)
dev_1.apply_raise() #as dev_1 is from Developer subclass, it runs 1.10 instead of 1.04
print(dev_1.pay)
#########################

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()

###############################
#built-in: isinstance() issubclass()

print(isinstance(mgr_1, Employee)) #True
print(isinstance(mgr_1, Developer)) #False
print(issubclass(Manager, Employee)) #True
