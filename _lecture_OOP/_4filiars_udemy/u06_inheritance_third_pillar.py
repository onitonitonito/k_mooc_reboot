""" udemy06-11 Inheritance
 -
 -
"""
class Apple(object):
    menufacturer = 'Apple Inc.'
    contact_website = 'http://www.apple.com/contact'

    def contact_details(self):
        print('To contact us, log on to', self.contact_website)

class MacBook(Apple):
    def __init__(self):
        self.year_of_manufacture = 2017

    def manufacture_details(self):
        print('This MacBook was manufactured in the year {} bu {}'.format(
            self.year_of_manufacture, self.menufacturer))

macbook = MacBook()
macbook.manufacture_details()
macbook.contact_details()
