""" PYCON 2019 - session room-103-01
# immutable vs. mutable
# class vs. instance
# global vs. local/nonlocal
#
# http://bit.ly/2L6VgGf
"""
# print(__doc__)


class Programmer(object):
    languages = []                          # Class 변수선언

    def __init__(self, name):
        self.name = name                    # Instance 변수선언 및 초기화
        print(f"New instance '{self.name}' assigned!")

    def add_lang(self, lang_name):
        self.languages.append(lang_name)    # Class 변수값 변경
        return self.languages


class ProgrammerCorrect(object):
    def __init__(self, name):
        self.name = name                    # Instance 변수선언 및 초기화
        self.instance_langs = []
        print(f"New instance '{self.name}' assigned!")

    def add_lang(self, lang_name):
        self.instance_langs.append(lang_name)
        return self.instance_langs


def debious_class_variation():
    """ 클래스 변수를 잘못 사용 """
    chris = Programmer('KIM')               # New instance 'KIM'

    print(chris.add_lang('python'))         # ['python']
    print(chris.add_lang('PHP'))            # ['python', 'PHP']

    yujin = Programmer('LEE')               # New instance 'LEE'

    print(yujin.languages)                # ['python', 'PHP'] ... ?!?


def correct_instance_variation():
    """ 인스턴스 변수를 바르게 사용"""
    chris = ProgrammerCorrect('KIM')        # New instance 'KIM'

    print(chris.add_lang('python'))         # ['python']
    print(chris.add_lang('PHP'))            # ['python', 'PHP']

    yujin = ProgrammerCorrect('LEE')        # New instance 'LEE'

    print(yujin.instance_langs)             # [] ... O.K!


if __name__ == '__main__':
    # debious_class_variation()
    correct_instance_variation()
    pass
