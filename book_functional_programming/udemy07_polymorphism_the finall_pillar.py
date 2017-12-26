"""
#
"""
class Employee(object):
    def set_number_of_working_hours(self):
        self.number_of_working_hours = 40

    def show_number_of_working_hours(self):
        print(self.number_of_working_hours)


class Trainee(Employee):
    def set_number_of_working_hours(self):
        self.number_of_working_hours = 45

    def reset_number_or_working_hours(self):
        super().set_number_of_working_hours()   # parent function call


employee = Employee()
employee.set_number_of_working_hours()  # set 40 hours
print("Number of working hours of employee : ", end="")
employee.show_number_of_working_hours()

trainee = Trainee()
trainee.set_number_of_working_hours()   # set 45 number_of_working_hours
print("Number of working hours of Tainee : ", end="")
trainee.show_number_of_working_hours()

trainee.reset_number_or_working_hours() # call parents function
print("Number of working hours of Tainee after reset : ", end="")
trainee.show_number_of_working_hours()
