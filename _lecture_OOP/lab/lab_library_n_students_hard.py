""" '도서관' 객채와 '학생'객체(들)의 호출() 상호작용
 예1) 학생: 빌려줘(책장 += 1) -- dict_key --> 도서관: 빌려줌(서가 -= 1)
 예2) 학생: 반납함(책장 -= 1) -- dict_key --> 도서관: 받음 (서가 += 1)
"""
import os
import time

DECORATOR = "=+" * 10
FORMAT_LIST_3 = DECORATOR +\
        "\n %s" +\
        "\n--------------------" +\
        "\n%s" +\
        "--------------------" +\
        "\n * %s \n\n\n"

""" 포맷리스트 표시형식 :
 =+=+=+=+=+=+=+=+=+=+
  목록의 제목
 --------------------
  appended - 시퀸스 목록
 --------------------
 * 기타 안내문자
 """


class Libraray(object):
    def __init__(self, name):
        self.name = name
        self.BOOK_LIST_DICT = {            # 0: ['바코드', '책제목'],
            1: ['k-01', '세인트영맨'],
            2: ['k-02', '흑집사'],
            3: ['k-03', '세븐고스트'],
            4: ['k-04', '이웃집토토로'],
            5: ['k-05', '배반의를루슈']}
        print("'%s' 시스템 접속을 환영 합니다..." % self.name)

    def __repr__(self):
        return 'Libraray'

    def show_system_menu(self):
        title = "번호를 선택해 주십시요"
        appended_squence_string = ""+\
              "\n1. 북 리스트 보기" +\
              "\n2. 책 대출하기" +\
              "\n3. 책 반납하기" +\
              "\n4. 종료하기"
        notice= "메뉴번호:"
        show_list_format_with(title, appended_squence_string, notice)


    def xxx_show_system_menu(self):
        """ 도서관 시스템 매뉴를 보여준다
          - 메뉴선택을 보여준다.
          - 메뉴선택값을 검증하고, 선택(int)을 반환한다.
         """
        while True:
            print(DECORATOR,
                  "\n번호를 선택해 주십시요"
                  "\n--------------------"
                  "\n1. 북 리스트 보기"
                  "\n2. 책 대출하기"
                  "\n3. 책 반납하기"
                  "\n4. 종료하기"
                  "\n--------------------"
                  "\n메뉴번호:\n\n", flush=True)

            int_choice = int(input())

            if not 1 <= int_choice <= 4:
                print("*** Error ***", flush=True)
                time.sleep(0.5)
                os.system('cls')
                continue
            else:
                return int_choice

    def give_book_change_list(self, other_obj, dict_key):
        print("'{}'님에게 [{}]'{:6}'을 대출하였습니다.".format(
            other_obj.name,
            self.BOOK_LIST_DICT[dict_key][0],
            self.BOOK_LIST_DICT[dict_key][1],
        ))

        # HOME_LIST_DICT 에 빌린 책을 { key : ['uid', '책제목'] }
        del self.BOOK_LIST_DICT[dict_key]


class Student(object):

    def __init__(self, name):
        self.name = name
        self.HOME_LIST_DICT = {}
        print("'%s' 객체가 생성 되었습니다.." % self.name)

    def __repr__(self):             # same as __str__(self)
        return 'Student'

    def show_others_book_list(self, other_obj):
        print("'%s'님이 도서목록을 요청하였습니다....\n" % self.name)
        print(DECORATOR + '\n'
              "현재, 대출 가능한 도서목록\n"
              "-------------------")
        for i, key in enumerate(other_obj.BOOK_LIST_DICT, 1):
            print("{:2}. [{:}] {:}".format(
                i,
                other_obj.BOOK_LIST_DICT[key][0],
                other_obj.BOOK_LIST_DICT[key][1],
            ))
        print('-' * 20, '\n\n\n')

    def get_borrow_book_dict_key(self, other_obj, dict_key):
        print("'{}'님이 [{}]'{:6}'을 대출요청 하였습니다.".format(
            self.name,
            other_obj.BOOK_LIST_DICT[dict_key][0],
            other_obj.BOOK_LIST_DICT[dict_key][1],
        ))

        # HOME_LIST_DICT 에 빌린 책을 { key : ['uid', '책제목'] }
        self.HOME_LIST_DICT[len(self.HOME_LIST_DICT) + 1] = [
            other_obj.BOOK_LIST_DICT[dict_key][0],      # uid
            other_obj.BOOK_LIST_DICT[dict_key][1],      # 책제목
        ]
        return dict_key


lib = Libraray('인천 도서관')
st1 = Student('박성하')
st2 = Student('박준하')


def show_list_format_with(title, list_dict, notice):  # 헬퍼()
    if repr(list_dict) == '':
    appended_squence_string = ""

    for key, values in zip(list_dict.keys(), list_dict.values()):
        appended_squence_string += "%2s. [%s] .. %s \n" % (
            key, values[0], values[1])

    print(FORMAT_LIST_3 % (
        title, appended_squence_string, notice))

def show_status_of(obj):
    if obj.__repr__() == 'Student':    # '학생'일 경우
        dict_list = obj.HOME_LIST_DICT
        title = "'%s'의 책장" % obj.name
    else:                              # '도서관'일 경우
        dict_list = obj.BOOK_LIST_DICT
        title = "'%s'의 장서" % obj.name

    print("\n** Class = '%s'" % obj.__repr__())
    notice = "총 보유수량 : '%s 건'" % len(dict_list)
    show_list_format_with(title, dict_list, notice)



menu_select = lib.show_system_menu()
# print("%d번을 선택하셨습니다. " % menu_select)

# if menu_select == 1:
#     st1.show_others_book_list(lib)

dict_key = st1.get_borrow_book_dict_key(lib, 2)
lib.give_book_change_list(st1, dict_key)


#
# elif  menu_select == 3:
#     pass
#
# else:
#     pass
#
#
#
# print(st1.HOME_LIST_DICT)
#
# print()
#
#
# st1.show_others_book_list(lib)
