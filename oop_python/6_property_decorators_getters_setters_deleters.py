class Employee:
    def __int__(self, first, last):
        self.first = first
        self.last = last
    #   self.email = first + '.' + last + '@email.com' #remove email attribute

    #breaks the email attribute and have to change to method
    #property decorators define methods that we can access it like an attribute
    @property #do not need ()
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    #setter is name of property
    @fullname.setter
    def fullname(self):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')
emp_1.fullname = 'Corey Schnafer' #overruns above line
print(emp_1.email) #graps from property

#print(emp_1.fullname()) #regular

del emp_1.fullname
