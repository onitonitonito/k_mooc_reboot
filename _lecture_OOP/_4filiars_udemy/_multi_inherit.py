"""
* 다중상속의 순서 (정한대로 참조)
"""


class OperatingSystem(object):
    multitasking = True
    name = "Mac IOS"


class Apple(object):
    website = 'http://www.apple.com'
    name = "Apple IOS"


class MacBook(OperatingSystem, Apple):
    def __init__(self):
        """ 상속 순서에 따라 앞에 name ('MacIOS')을 참조 함 """
        if self.multitasking:
            comment = "This is a multitasking system. Visit '{}' for more."
            print(comment.format(self.website))
            print("Name :", self.name, "\n\n")


mac_book = MacBook()


""" 클래스 dict 를 활성화 """
for _key, _val in MacBook.__dict__.items():
    # print("%-17s %s" %(_key, _val))
    pass

""" 글로벌 namespace """
for _key, _val in globals().items():
    print("%-17s %s" % (_key, _val))
