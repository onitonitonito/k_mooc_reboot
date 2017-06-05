# memo.py -- file read and write --> ../static/data_docs/memo.pdb
import sys

HELP_MESSAGE='''\n\n\
====================================================
           MEMO.PY -- HELP MESSAGE
---------------------------------------------------
This is simple example of read & write file funtion

USAGE:    python memo.py {mode}, [args1]
=====
   -a --append:     ADD Memo = args1
   -v --verbose:    VIEW Memo w/o args1
----------------------------------------------------
'''
if len(sys.argv) != 2:
    print(HELP_MESSAGE)
    print('**** ERR: MALFUNTION, TRY AGAIN! ****')
    raise SystemExit(1)         # Exception and forced shutdown.
else:
    option = sys.argv[1]        # [ argv_list, args1, args2...]
    print("OPTION=",option)

if option == None or option == '-h' or option == '--help':
    print(HELP_MESSAGE)

elif option == '-a' or option =='--append':            # append mode = -a/
    memo = sys.argv[2]
    f = open('../static/data_docs/memo.pdb', 'a')    # append mode open
    f.write(memo)
    f.write("\n")
    f.close()

elif option == '-v' or option=='--verbose':            # verbose mode /
    f = open('../static/data_docs/memo.pdb', 'r')    # read mode open
    memo = f.read()
    f.close()
    print(memo)

else:
    print('**** ERR: OPTION is not available! ****')
