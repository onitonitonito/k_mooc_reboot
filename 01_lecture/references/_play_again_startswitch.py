#!/usr/bin/python
SEPARATOR = '\n' + '__'*30 + '\n'
def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

while True:
    """
    ## Test.02 - Start Swicn Function
    > - startswitch(test_str, start, end+1) = True/False
    - print("( 'this' ) = ", test_str.startswith( 'this' ))
    - print("( 'is', 2, 4 ) = ", test_str.startswith( 'is', 2, 4 ))
    - print("( 'this', 2, 4 ) = ", test_str.startswith( 'this', 2, 4 ))
    """

    test_str = "this is test_string example....wow!!!";
    print(SEPARATOR)
    print('test_string =', test_str, '\n\n')
    print("( 'this' ) = ", test_str.startswith( 'this' ))
    print("( 'is', 2, 4 ) = ", test_str.startswith( 'is', 2, 4 ))
    print("( 'this', 2, 4 ) = ", test_str.startswith( 'this', 2, 4 ))

    if not playAgain():
        break
