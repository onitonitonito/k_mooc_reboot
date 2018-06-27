
class OperatingSystem(object):
    multitasking = True
    name = "Mac IOS"


class Apple(object):
    website = 'www.apple.com'


class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking:
            comment = "This is a multitasking system. Visit {} for more"
            print(comment.format(self.website))
            print("Name :", self.name)


MAC_BOOK = MacBook()
