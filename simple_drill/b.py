# coding: utf-8

import a

def main():
    print("CASE.0b(main) - This is TOP LEVEL of B.py")

a.func()
a.main()
main()


if __name__ == '__main__':
    print("CASE.1b(direct) - B.py를 직접실행하고 있습니다.\n")
else:
    print("CASE.2b(Import) - B.py가 임포트되어 실행하고 있습니다.\n")
