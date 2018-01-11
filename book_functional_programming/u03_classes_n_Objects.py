"""
 - 3.5 Understanding Classes & Objects
 - 3.6 Implementation of Classes & Objects
  * Class = noun form.
  * Attribute = adjective form.
  * Method = verb form.
"""
SEPARATOR = '\n--------------------- %s ---'

class Employee(object):
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.sales_made_this_week = 6

    def has_achieved_target(self):
        if self.sales_made_this_week >= 5:
            print('Target has been achieved', end='\n\n')
        else:
            print('Target has not been achieved', end='\n\n')

kay = Employee('Kay Suparx', 'Sales Executive')
print(SEPARATOR% 'Employee Information')
print(' NAME : %s'% kay.name)
print(' WORK : %s hours'% kay.sales_made_this_week, end='\n\n')
kay.has_achieved_target()

print()
mark = Employee('Mark Markus', 'Senior Manager')
mark.sales_made_this_week = 4
print(SEPARATOR% 'Employee Information')
print(' NAME : %s'% mark.name)
print(' WORK : %s hours'% mark.sales_made_this_week, end='\n\n')
mark.has_achieved_target()
