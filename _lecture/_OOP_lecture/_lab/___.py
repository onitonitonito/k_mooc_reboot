import os
import sys

import _script_run_utf8
_script_run_utf8.main()

WORK_DIR = './_pickle/'
BOOK_LIST_FILE = 'book_list_db.pdb'

FILENAME_WITH_DIR = WORK_DIR + BOOK_LIST_FILE
# ./_pickle/book_list_v00.pdb


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
            print("*** '{}'가 대출 되었습니다.***\n\n".format(book_title))
        else:
            print("... '{}'는 현재 대출 불가능 합니다.\n\n".format(book_title))

    def return_book(self, book_title):
        if book_title in self.available_book_list:
            print("... '{}'는 반납할 수 없습니다. ...\n\n".format(book_title))
        else:
            self.available_book_list.append(book_title)
            print("*** '{}'책이 반납 되었습니다.\n\n".format(book_title))

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
        while True:
            book_title = input("반납 할 책 이름을 입력해 주세요 : \n").strip()
            if len(book_title) == 0:
                print('잘못된 입력 : 공백을 입력입니다.')
            else:
                return book_title



    # def file_write(self, file_name)


def write_book_list_to_file(filename_with_dir, book_list):
    with open(filename_with_dir, 'w', encoding='utf8') as f:
        book_titles = ''
        for book_title in book_list:
            book_titles += book_title + '\n'
        f.write(book_titles)

def read_book_list_from_file(filename_with_dir):
    if not os.path.isfile(filename_with_dir):
        print('*** 불러들일 화일이 존재 하지 않습니다. ***')
    else:
        with open(filename_with_dir, 'r', encoding='utf8') as f:
            book_list = f.read().strip().split('\n')
        return book_list


BOOK_LIST = read_book_list_from_file(FILENAME_WITH_DIR)

lib = Library(BOOK_LIST)
st1 = Student('박성하')

while True:
    choice = lib.show_menu_selection()  # 선택메뉴를 보여주고 선택받음

    if choice == '1':                   # 책목록을 보여줌
        os.system('cls')
        lib.show_available_book_list()

    elif choice == '2':                 # 책대출
        lib.lend_book(st1.student_lend_book())
        lib.show_available_book_list()

    elif choice == '3':                 # 책반납
        lib.return_book(st1.student_return_book())
        lib.show_available_book_list()

    elif choice == '4':
        write_book_list_to_file(FILENAME_WITH_DIR, BOOK_LIST)
        print('*** 북리스트를 화일에 저장하였습니다. ***')
        break
