"""
# argv returns list of arguments along with filename '*.py' at pos[0]
# run this, with arg1 arg2 arg3 arg4
"""
# PS C:\module_PyQt> python test_sys_argv.py arg1 arg2 arg3 arg4
# argv returns list of arguments atteched along with *.py
# run this, with arg1 arg2 arg3 arg4
# arguments = ['test_sys_argv.py', 'arg1', 'arg2', 'arg3', 'arg4']

import sys

print(__doc__)

def main():
    print(f"arguments = {sys.argv}")
    pass





if __name__ == '__main__':
    main()
