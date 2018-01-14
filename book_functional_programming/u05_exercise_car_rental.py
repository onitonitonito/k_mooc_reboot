""" EXERCISE 05-12 - ABSTRACTION AND ENCAPSULATION
 Similar to a library management system, write a program to
 provide layers of abstraction for a car rental system.
 Your program should perform the following:

 1. Hatchback, Sedan, SUV should be type of cars that are
 being provided for rent

 2. Cost per day:
 - Hatchback - $30
 - Sedan - $50
 - SUV - $100

 3. Give a prompt to the customer asking him the type of car
 and the number of days he would like to borrow and provide the
 fare details to the user.
 """
import os

SEPARATOR = '-'*22 +'%s--'
KIND_OF_CAR = ['Hatchback', 'Sedan', 'Suv', 'Sports']
COST_PER_DAY = [30, 50, 100, 170]
AVAILABLE_CAR_LIST = {kind : cost
    for kind, cost in zip(
        KIND_OF_CAR,
        COST_PER_DAY)}
# {'Hatchback': 30, 'Sedan': 50, 'Suv': 100, 'Sports': 170}


class CarRentalShop(object):
    def __init__(self, available_car_list):
        self.available_car_list = available_car_list

    def show_get_menu(self):
        print(SEPARATOR% 'RENTAL SERVICE')
        print('Enter 1 to show car price list')
        print('Enter 2 to rent a car')
        print('Enter 3 to return a car')
        print('Enter 4 to quit menu')
        print(SEPARATOR% '-------------')
        return input('Enter menu : ')

    def show_available_car_list(self):
        print(SEPARATOR% 'CAR LIST')
        for i, key in enumerate(self.available_car_list.keys(), 1):
            # print(i, key, self.available_car_list[key])
            print('{:}. {:<10} {:.>5} {:3,} $'.format(
                i, key, '.', int(self.available_car_list[key])))

    def get_rent_a_car(self, rented_car):
        self.available_car_list.pop(rented_car)
        print('The car has rented successfully..!')

    def add_to_car_list(self, returned_car):
        self.available_car_list[returned_car] = AVAILABLE_CAR_LIST[returned_car]
        print('The car has returned successfully..!')


class Customer(object):
    def get_borrow_car(self):
        return input('Enter name of car you want to borrow : ')

    def get_return_car(self):
        return input('Enter the name of car you would return : ')


shop = CarRentalShop(AVAILABLE_CAR_LIST.copy())
customer = Customer()

while True:
    menu_selection = shop.show_get_menu()
    print('\n'*3)

    if menu_selection.startswith('1'):
        shop.show_available_car_list()
        print()
    elif menu_selection.startswith('2'):
        borrowed_car = customer.get_borrow_car()
        result = shop.get_rent_a_car(borrowed_car)
        print()
    elif menu_selection.startswith('3'):
        returned_car = customer.get_return_car()
        shop.add_to_car_list(returned_car)
        print()
    elif menu_selection.startswith('4'):
        print('\n'*5, 'Thanks for using our service, bye~!')
        quit()
    else:
        os.system('cls')
        continue
