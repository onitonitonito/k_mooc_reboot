#!/usr/bin/python
SEPARATOR = "__"*30+ "\n"
TEST_STR = "this is test_string example....wow!!!";
NOTICE = """
 ## Test.02 - Start Swicn Function
  - startswitch(TEST_STR, start, end+1) = True/False
  - print("( 'this' ) = ", TEST_STR.startswith( 'this' ))
  - print("( 'is', 2, 4 ) = ", TEST_STR.startswith( 'is', 2, 4 ))
  - print("( 'this', 2, 4 ) = ", TEST_STR.startswith( 'this', 2, 4 ))
  """

def playAgain():
    """ If Y/y = True, NOT=False """
    return input("Do you want to play again? (yes or no)").lower().startswith('y')

def main():
    while True:
        print(SEPARATOR + NOTICE + SEPARATOR)
        print('TEST_STRING  :\n\n', TEST_STR, '\n\n')
        print("( 'this' ) = ", TEST_STR.startswith('this'))
        print("( 'is', 2, 4 ) = ", TEST_STR.startswith('is', 2, 4))
        print("( 'this', 2, 4 ) = ", TEST_STR.startswith('this', 2, 4))

        if not playAgain():
            break

if __name__ == '__main__':
    main()
