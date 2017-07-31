import a

def main():
    print("CASE.0b(main) - This is TOP LEVEL of B.py")

a.func()
a.main()
main()


if __name__ == '__main__':
    print("CASE.1b(direct) - B.py is running directly!!\n")
else:
    print("CASE.2b(Import) - B.py is imported and used indirectly.\n")
