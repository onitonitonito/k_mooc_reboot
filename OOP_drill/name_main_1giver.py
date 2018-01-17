def func():
    print("*** Func() : This is a function in A.py ***")

def main():
    print("CASE.0a(main) - This is TOP LEVEL of A.py")

# CASE.1a(direct) - A.py is running directly!!
if __name__ == '__main__':
    print("CASE.1a(direct) - A.py is running directly!!\n")
else:
    print("CASE.2a(Import) - A.py is imported and used indirectly.\n")
