"""
# class function definition
# Library class = show available / lend book / restore book
# Customer class = borrow book / return book /
# : https://www.udemy.com/python-oops-beginners/learn/v4/t/lecture/7359328

 (1) pickle = write directly into a file as data-format
 (2) read =
 (3) write =
 (4) os.exists & os.remove
 """
import os
import sys
import pickle

BOOK_LIST_FILE = 'book_list_v00.pdb'
BOOK_LIST = [
    '진격의거인',
    '공각기동대',
    '페트레이버',
    '포켓몬스터',
    '케모노프렌즈']

WORK_DIR = os.path.dirname(__file__)
ROOT_WORD = 'k_mooc_reboot'                 # root directory

ROOT_DIR = WORK_DIR.partition(ROOT_WORD)[0] + WORK_DIR.partition(ROOT_WORD)[1]
PICKLE_WITH_DIR = ROOT_DIR + '\\_static\\_log\\' + BOOK_LIST_FILE
print(PICKLE_WITH_DIR)

"""
PICKLE_WITH_DIR = 북리스트(피클)화일을 저장 할 위치(DIR)
C:\\Users\nitt0\Documents\Github\k_mooc_reboot\_static\_log\book_list_v00.pdb

WORK_DIR = 현재 작성하고 있는 화일이 있는 위치 : 워킹디렉토리(DIR)
C:\\Users\nitt0\Documents\Github\k_mooc_reboot\01_lecture\making_things
"""

class Library(object):
    def __init__(self, available_book_list):
        self.available_book_list = available_book_list

    def show_available_book_list(self):
        print('*** 현재, 대출 가능한 책목록 : ({}권)***'.format(len(self.available_book_list)))
        for i, book_title in enumerate(self.available_book_list, 1):
            print(' {:2}. {}'.format(i, book_title))

    def lend_book(self, book_title):
        if book_title in self.available_book_list:
            self.available_book_list.remove(book_title)
            print("*** '{}'가 대출 되었습니다.***".format(book_title))
        else:
            print("... '{}'는 현재 대출 불가능 합니다.".format(book_title))

    def return_book(self, book_title):
        if book_title in self.available_book_list:
            print("... '{}'는 반납할 수 없습니다. ...".format(book_title))
        else:
            self.available_book_list.append(book_title)
            print("*** '{}'책이 반납 되었습니다.".format(book_title))

    def show_menu_selection(self):
        print("\n\n")
        print("*** 도서관 매뉴 리스트 ***")
        print(" 1. 대출가능 도서 목록 (Show)")
        print(" 2. 도서 대출하기 (Lend)")
        print(" 3. 도서 반납하기 (Return)")
        print(" 4. 나가기 (Quit)")
        return input('선택매뉴 : \n')


class Student(object):
    def __init__(self, name):
        self.name = name
        print("*** '{}'님이 도서관에 접속하였습니다. ***".format(self.name))

    def student_lend_book(self):
        return input("대출 할 책 이름을 입력해 주세요 : \n")

    def student_return_book(self):
        return input("반납 할 책 이름을 입력해 주세요 : \n")


def get_read_file_from_pickle(pickle_with_dir, data=BOOK_LIST):
    """ 피클화일 읽어오기(GET)
    - 피클화일이 있으면, loaded_data 리턴
    - 피클화일이 없으면, 초기 Dict를 읽어서 피클화일을 만들고, loaded_data 리턴
    """
    if os.path.exists(pickle_with_dir):
        with open(pickle_with_dir, mode='rb') as f:
            loaded_data = pickle.load(f)
            # 중요(!) : f = _io.BufferReader, 피클화일 자체가 아니다.
        return loaded_data

    else:
        print("주의!! ... 피클화일이 존재하지 않습니다 ...", flush=True)
        print("       ... 초기 피클화일을 만듭니다. ...", flush=True)
        write_file_to_pickle(pickle_with_dir, data)
        return data

def write_file_to_pickle(pickle_with_dir, data):
    """ 피클화일 쓰기 (WRITE PICKLE FILE)
    - 피클화일이 없으면, 초기 Dict를 읽어서 피클화일을 만들고, 성공Echo 발생.
    - 피클화일이 있으면, 있다고 존재Echo 발생.
    """
    if not os.path.exists(pickle_with_dir):
        with open(pickle_with_dir, mode='wb') as f:
            pickle.dump(data, f)
        print('*** 새로운 피클화일을 만들었습니다. ***', flush=True)
    else:
        print('... 이미 피클화일이 존재 합니다 ...', flush=True)

def remove_pickle(pickle_with_dir):
    if os.path.exists(pickle_with_dir):
        os.remove(pickle_with_dir)
        print('*** 기존 피클화일을 삭제 하였습니다. ***', flush=True)
    else:
        print('... 피클화일이 더 이상 존재하지 않습니다 ...', flush=True)

AVAILABLE_BOOK_LIST = get_read_file_from_pickle(PICKLE_WITH_DIR)

student = Student('Kay Onito')
library = Library(AVAILABLE_BOOK_LIST)

while True:
    menu = library.show_menu_selection()
    os.system('cls')

    if menu.startswith('1') or menu.lower().startswith('s'):
        library.show_available_book_list()

    elif menu.startswith('2') or menu.lower().startswith('l'):
        lend_book_title = student.student_lend_book()
        library.lend_book(lend_book_title)

    elif menu.startswith('3') or menu.lower().startswith('r'):
        return_book_title = student.student_return_book()
        library.return_book(return_book_title)

    elif menu.startswith('4') or menu.lower().startswith('q'):
        if os.path.exists(PICKLE_WITH_DIR):
            remove_pickle(PICKLE_WITH_DIR)

        write_file_to_pickle(PICKLE_WITH_DIR, library.available_book_list)
        print("*** 최근 도서목록을 저장하고, 접속을 끊습니다. ***")
        quit()
