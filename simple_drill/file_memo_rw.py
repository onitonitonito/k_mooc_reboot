# memo.py -- file read and write --> ../static/data_docs/memo.pdb
import sys, os

os.system('cls')

# [TEST argv] --------------------------------------------------------------
# <class 'list'> command='1', arg1='2' arg2='3'

# print('sys.argv=',sys.argv)         #['memo.py', 'dd','dd']
# print('len=',len(sys.argv))         #['memo.py', 'dd','dd']
#
# for n in range(len(sys.argv)):
#     print('sys.argv[%s]='%n, sys.argv[n])         #['memo.py', 'dd','dd']
#
# print(type(sys.argv))           #['D:\..\.memo.py', 'dd','dd'] .. include {PATH}
# print(len(sys.argv))            #f
#
DESTIN_DIR='../static/data_doc/'
MY_MEMO = 'memo.pdb'

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

HEADER='''\n
====================================================
        %s
----------------------------------------------------'''

# [ BODY ] --------------------------------------------------------------

if len(sys.argv) < 2:
    print('\n**** ERR: YOU NEED MORE THAN 1 Argv(option)! ****')
    print(HELP_MESSAGE)
    raise SystemExit(1)         # Exception and forced shutdown.
else:
    option = sys.argv[1]        # [ argv_list, args1, args2...]
    MESSAGE = "MEMO OPTION: "+option
    print(HEADER % MESSAGE)


if option == '-h' or option == '--help':
    print(HELP_MESSAGE)

elif option == '-a' or option =='--append':            # append mode = -a/
    if len(sys.argv) < 3:
        print("*** MISSING ARGV[2] ***")
    else:
        memo = sys.argv[2]
        f = open(DESTIN_DIR+MY_MEMO, 'a')    # append mode open
        f.write(memo+"\n")
        # f.write("\n")
        f.close()

elif option == '-v' or option=='--verbose':            # verbose mode /
    f = open(DESTIN_DIR+MY_MEMO, 'r')    # read mode open
    memo = f.read()
    f.close()
    print(memo)

else:
    print('**** ERR: OPTION is not available! ****')
