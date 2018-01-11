""" Abstraction & Encapsulation (Library <-> Students)
  - Library & Costomer Interaction
"""

class Library(object):
    def __init__(self, list_of_books):
        self.available_book = list_of_books

    def display_available_book(self):
        print()
        print('Available Books: ')
        for i, book in enumerate(self.available_book, 1):
            print(' %s. %s' %(i,book))
        print('\n')


    def lend_book(self, requested_book):
        if requested_book in self.available_book:
            print('You have now borrowed the book!')
            self.available_book.remove(requested_book)
        else:
            print('Sorry, The book is not available, Thank yoou!')

    def add_book(self, returned_book):
        self.available_book.append(returned_book)
        print('You have returned the book, Thank you!')


class Customer(object):
    def request_book(self):
        print('Enter the book title you would like to borrow: ')
        self.book = input()
        return self.book
        print('??')

    def return_book(self):
        print('Enter the book title which you are returning :')
        self.book = input()
        return self.book
        print('??')

BOOK_SHIELF = [
    'Think and Grow Rich',
    'Who Will Cry When You Died',
    'For One More Day',
    'Witches\' Loaves',]

library = Library(BOOK_SHIELF)
customer = Customer()

while True:
    print('Enter 1 to display the available books')
    print('Enter 2 to request for a book')
    print('Enter 3 to return book')
    print('Enter 4 to exit')

    user_choice = int(input())

    if user_choice is 1:
        library.display_available_book()

    if user_choice is 2:
        requested_book = customer.request_book()
        library.lend_book(requested_book)

    if user_choice is 3:
        returned_book = customer.return_book()
        library.add_book(returned_book)

    if user_choice is 4:
        quit()
