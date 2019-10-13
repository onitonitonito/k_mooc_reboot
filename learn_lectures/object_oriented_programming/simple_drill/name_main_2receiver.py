import name_main_1giver as giver

def main():
    print("CASE.0b(main) - This is TOP LEVEL of B.py")

giver.func()    # *** Func() : This is a function in A.py ***
giver.main()    # CASE.0a(main) - This is TOP LEVEL of A.py

main()          # CASE.0b(main) - This is TOP LEVEL of B.py
                # CASE.1b(direct) - B.py is running directly!!

if __name__ == '__main__':
    print("CASE.1b(direct) - B.py is running directly!!\n")
else:
    print("CASE.2b(Import) - B.py is imported and used indirectly.\n")
