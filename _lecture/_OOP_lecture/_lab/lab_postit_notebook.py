import os
import time
import random

# class PostIt(object):
#     def __init__(self, content):
#         self.content = content


class NoteBook(object):
    def __init__(self, book_title):
        self.book_title = book_title
        self.counter = 0
        self.note_dict = {}

    def add_post_it(self, page, content):
        self.counter += 1
        self.note_dict[page] = content
        self.show_status()

    def get_total_pages(self):
        return self.counter

    def show_used_pages(self):
        keys = list(self.note_dict.keys())
        keys.sort()

        for key in keys:
            print("{:2d}. {}".format(key, self.note_dict[key]), flush=True)

    def show_status(self):
        print("~~~~ %s ~~~~"% self.book_title)
        print("포스트잇 갯수 = ", self.get_total_pages(), flush=True)
        print('=='*10)
        self.show_used_pages()
        print('\n\n')
        time.sleep(0.2)
        os.system('cls')

def add_list_to_postit(obj, titles,):
    for title in titles:
        while True:
            page = random.randint(1, len(titles))

            if page not in obj.note_dict:
                obj.add_post_it(page=page, content=title)
                break



titles = [
    '돈크라이포미 알젠티나',
    '내가 제일 잘나가',
    '이세상에 하나밖에',
    '저녁노을 바라보며',
    '아침에 이슬이 맺힌다',
    '돈크라이포미 알젠티나',
    '내가 제일 잘나가',
    '이세상에 하나밖에',
    '저녁노을 바라보며',
    '아침에 이슬이 맺힌다',
    '돈크라이포미 알젠티나',
    '내가 제일 잘나가',
    '이세상에 하나밖에',
    '저녁노을 바라보며',
    '아침에 이슬이 맺힌다',
    '돈크라이포미 알젠티나',
    '내가 제일 잘나가',
    '이세상에 하나밖에',
    '저녁노을 바라보며',
    '아침에 이슬이 맺힌다',
    '돈크라이포미 알젠티나',
    '내가 제일 잘나가',
    '이세상에 하나밖에',
    '저녁노을 바라보며',
    '아침에 이슬이 맺힌다',
    '돈크라이포미 알젠티나',
    '내가 제일 잘나가',
    '이세상에 하나밖에',
    '저녁노을 바라보며',
    '아침에 이슬이 맺힌다',
    '내가 제일 잘나가',
    '이세상에 하나밖에',
    '저녁노을 바라보며',
    '아침에 이슬이 맺힌다',
    '돈크라이포미 알젠티나',
    '내가 제일 잘나가',
    '이세상에 하나밖에',
    '저녁노을 바라보며',
    '아침에 이슬이 맺힌다',
    '내가 제일 잘나가',
    '이세상에 하나밖에',
    '저녁노을 바라보며',
    '아침에 이슬이 맺힌다',
    '돈크라이포미 알젠티나',
    '내가 제일 잘나가',
    '이세상에 하나밖에',
    '저녁노을 바라보며',
    '아침에 이슬이 맺힌다',
    ]

nb1 = NoteBook(book_title='노래모음집')
add_list_to_postit(nb1, titles)

nb2 = NoteBook(book_title='가사모음집')
add_list_to_postit(nb2, titles)
