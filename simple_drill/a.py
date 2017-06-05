def func():
    print("*** Func() : This is a function in A.py")

def main():
    print("CASE.0a(main) - This is TOP LEVEL of A.py")


if __name__ == '__main__':
    print("CASE.1a(direct) - A.py를 직접실행하고 있습니다.\n")
else:
    print("CASE.2a(Import) - A.py가 임포트되어 실행하고 있습니다.\n")
