class TestObject(object):
    """ 클래스 변수(v1, v2) = self (전역변수)로 접근한다
    """
    value1 = 10
    value2 = 20

    def __init__(self, u_id, u_pw):
        """ 클래스 전역변수 선언 = self 로 선언한다
        """
        self.id = u_id
        self.pw = u_pw

    def __main__(self):
        print(type(self))

    def show_attribute(self):
        print('==============')
        print('My ID :', self.id)
        print('My PW :', '*' * len(str(self.pw)))
        print('Val_1 :', self.value1)
        print('Val_2 :', self.value2)
        print('==============\n\n')

    def change_class_value1(self, add_value):
        before = self.value1
        self.value1 += add_value
        print("{}.value1={} --> {} 으로 변경되었습니다.".format(
            self.__dict__['id'].upper(),
            before,
            self.value1))

    def change_class_value2(self, add_value):
        before = self.value2
        self.value2 += add_value
        print("{}.value2={} --> {} 으로 변경되었습니다.".format(
            self.__dict__['id'].upper(),
            before,
            self.value2))

    def chage_class_pw(self, new_pw):
        before = self.pw
        self.pw = new_pw
        print("{}.password={} --> {} 으로 변경되었습니다.".format(
            self.__dict__['id'].upper(),
            "*" * len(before),
            "*" * len(str(self.pw))))


kay = TestObject('onito', '123456')
kay.show_attribute()

# before_val = kay.value1
# kay.value1 += 100
# print("value1={} --> {} 으로 변경되었습니다.".format(before_val, kay.value1))
kay.change_class_value1(100)
kay.change_class_value2(300)
kay.show_attribute()

# kay.pw = '333'
# print("패스워드가 {}으로 변경되었습니다.".format("*"*len(kay.pw)))
kay.chage_class_pw(333)
kay.show_attribute()

# print(kay.__pw)
# print(kay._TestObject__pw)
# print(help(TestObject))


jay = TestObject('newbie', '3333')
jay.show_attribute()
print(kay.__dict__)
print(jay.__dict__)
