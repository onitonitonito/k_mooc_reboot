import os, time

os.system('cls')

DESTIN_DIR ='../static/data_doc/log/'
MYFILE ='i_have_a_dream.pdb'

# [A.01]----------------------------------------------------------------
# f = open(DESTIN_DIR+ MYFILE, 'r')
#
# # contents = f.read().strip()   # <class 'str'>
# # contents = f.readline().strip()   # <class 'str'> - 1 line
# contents = f.readlines()  # <class 'list'> - list of lines
#
# for n in range(len(contents)):
#     if contents[n].strip() != '':
#         print(contents[n],end="\n")
#         time.sleep(0.1)
#
# print(type(contents))
#
# #contents =  my_file.read().strip()      # <class 'str'> a whole txt as 1
# #contents = my_file.readline().strip()  # <class 'str'> read line 1x1
# #contents = my_file.readlines() # <class 'list'>
#
# # contents = my_file.read().splitlines()  # <class 'list'>
# # for n in range(contents.count('')):     # count NUM of '' = 38
# #     contents.remove('')
# #
# # my_file.close()
#
#
# [A.02]----------------------------------------------------------------
# with open(TOTAL_FILE,'r') as my_file:
#     #contents =  my_file.read().strip()     # <class 'str'> a whole txt as 1
#     #contents = my_file.readline().strip()  # <class 'str'> read line 1x1
#     #contents = my_file.readlines()         # <class 'list'>
#
#     contents = my_file.read().splitlines()  # <class 'list'>
#     for n in range(contents.count('')):     # count NUM of '' = 38
#         contents.remove('')

# [A.03 : follows to A or B] = The same Result--------------------------
# print(contents)
# print(type(contents))
# print(len(contents))
# print("count ''=",contents.count(''))
#
# [B.01]----------------------------------------------------------------
# with open(DESTIN_DIR+MYFILE,'r') as f:
#     i=1
#     while True:
#         line = f.readline().replace('\n','') # read line 1x1
#         if line.strip() == "":          # strip blanks both end
#             continue
#         if not line:    break
#
#         print(str(i) + ' --> ' + line)  # print line x line
#         # 37 --> And when this happens, and when we allow freedom ring,
#         i+=1                           # i=i+1

# [B.02] The same as [B.01]---------------------------------------------
# with open(DESTIN_DIR+MYFILE,'r') as f:
#     i=1
#     my_file_list = f.readlines()  # <class 'list'>
#
#     for n in range(len(my_file_list)):
#         if my_file_list[n].replace('\n','').strip() == "":
#             pass
#         else:
#             print(str(i)+' --> ' + my_file_list[n].replace('\n',''))
#         # 37 --> And when this happens, and when we allow freedom ring,
#             i+=1
#
# [C.01] DATA LOGGER -------------------------------------------------
LOGFILE ='count_file_log.pdb'

if not os.path.isdir(DESTIN_DIR):
    os.mkdir(DESTIN_DIR)

if not os.path.exists(DESTIN_DIR+LOGFILE):
    f = open(DESTIN_DIR+LOGFILE, 'w', encoding='utf8')
    f.write('*** START TO WRITE A LOG ***\n')
    f.close()

with open(DESTIN_DIR+LOGFILE, 'r') as f:
    LINE_NUMBER = len(f.readlines()) - 1        # len(<class 'list'>), excl'd HEADER
    print('\n'+'--'*25+'\nSTART NUMBER: %d'%(LINE_NUMBER+1))

with open(DESTIN_DIR+LOGFILE, 'a', encoding='utf8') as f:
    import random, datetime

    for i in range(1,6):
        stamp = str(datetime.datetime.now())
        value = random.random()*100000

        LINE_NUMBER +=1

        log_line = '(%s) --> %s'%(LINE_NUMBER,stamp) + '\t' + str(value) + ' IS GENERATED...' + '\n'
        f.write(log_line)
        print('%s Is Added...'%LINE_NUMBER)
        time.sleep(1)

    print ('*** NEW LOG FILE WAS CREATED!!! ***')
    print ('END NUMBER: ', LINE_NUMBER )  # f.readlines() = <class 'list'>
    time.sleep(3)

# --------------------------------------------------
# START NUMBER: 954
# *** NEW LOG FILE WAS CREATED!!! ***
# END NUMBER:  989
# [Finished in 0.645s]
