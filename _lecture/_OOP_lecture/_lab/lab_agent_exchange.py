class InterAgent(object):
    group, location = "국제첩보", "모름"
    secret = "알수없음"
    inven_dict = {
        1: ['권총', 1],
        }

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_intruduction(self):
        print("{} ({})\n----------".format(self.group, self.location))
        print("*** {} ({}세)".format(self.name, self.age))
        print(self.secret)

        print("--- 인벤토리:무장 ---")
        for key in self.inven_dict:
            print("  {}. {} = {}".format(
                key,
                self.inven_dict[key][0],
                self.inven_dict[key][1]))
        print('\n\n')

    def say_hello(self, other_object):
        print("'{}({})'가 '{}({})'에게....\n"
            "'안녕하세요' 라고 인사하다\n\n".format(
                self.name,
                self.group,
                other_object.name,
                other_object.group,
                ))

    def reveal_secret(self, other_object):
        print("'{}({})': 하하하~!!...\n"
            "{}, {}! 너의 비밀은 바로...\n"
            "'{}'였어....\n\n".format(
                self.name,
                self.group,
                other_object.group,
                other_object.name,
                other_object.secret,
                ))


class KingsMan(InterAgent):
    group, location = "킹스맨", "런던/영국"
    secret = "살쪘다 - 양복 바지가 작다"
    inven_dict = {
        1: ['칼ㅡ', 3],
        2: ['권총', 2],
        }


class StatesMan(KingsMan):
    group, location = "스테이츠맨", "텍사스/미국."
    secret = '초급 카우보이 - 채찍을 잘 쓰지 못한다'
    inven_dict = {
        1: ['칼ㅡ', 5],
        2: ['권총', 2],
        3: ['채찍', 1],
        }



if __name__ == '__main__':
    ai = InterAgent('IU', 26)
    jay = KingsMan('Mickey', 15)
    kay = StatesMan('SuParX', 25)

    jay.say_hello(kay)
    kay.reveal_secret(jay)

    kay.say_hello(jay)
    jay.reveal_secret(kay)

    # print(ai.__class__.mro())

    el = KingsMan('Lala', 10)
    el.secret = "발냄새가 많이 난다"
    # el.inven_dict[len(el.inven_dict)+1] = ['인형', 1]

    for agent in [ai, jay, kay, el]:
        agent.show_intruduction()

    el.say_hello(jay)
    jay.reveal_secret(el)
