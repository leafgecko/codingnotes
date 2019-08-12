#magic methods - implement operator overloading
#special methods - dunder  e.g. __init__ , when creating class objects

#BROKEN CODE
def __repr__ (self):
#unambigous representation of object
#debugging and logging for developers

def __str__ (self):
#readable representation to end User

############################################
Example
############################################

def__repr__(self):      #{} are placeholders
    return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)
    #sring that prints object

def __str__ (self):        #when using method, have ()
    return '{}-{}'.format(self.fullname(),self.last)

######################################################
print (repr(emp_1)) === print(emp_1.__repr__())

print (str(emp_1)) === print(emp_1.__str__())
######################################################

###################
######__add__######         Emulating Numeric Types
###################
print(1+2)   ===   print(int.__add__(1,2))

def __add__(self.other):
    return self.pay + other.play

print(emp_1 + emp_2)

###################
######__len__######         Emulating Numeric Types
###################
print(len('test'))   ===   print('test'.__len__())

def __len__(self):
    return len (self.fullname())

print(len(emp_1))

######################################################

return NotImplemented   #in def

#Not an error, falls back on other objects
#becasue other objects may how know to handle this, else error
