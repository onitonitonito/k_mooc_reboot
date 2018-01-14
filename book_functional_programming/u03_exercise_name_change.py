""" EXERCISE 03-6 - CLASSES AND OBJECTS
Write and object oriented program that performs the following
tasks:

1. Define a class called "Employee" and create an instance
of that class

2. Create an attribute called name and assign it with a
value

3. Change the name you previously defined within a
method and call this method by making use of the object you created
"""

class Employee(object):
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name
        print("The employee\'s name is now changed to '{}'!".format(self.name))

    def show_information(self):
        print('The employee\'s name : {}'.format(self.name))

kay = Employee('Mark Mcgorven')
kay.show_information()
print()

kay.change_name('Kay Onito3')
kay.show_information()
