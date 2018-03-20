import os
import time
""" What's the -- 'os.path.dirname'..?
 DESTIN_DIR ='../_static/_pickle/'  --- ONLY!!! kick in 'console' screen..
 os.path.dirhame(__file__) = D:\My Documents\GitHub\k_mooc_reboot\simple_drill
 os.path.dirhame(__file__)*2 = D:\My Documents\GitHub\k_mooc_reboot
 DESTIN_DIR = D:\My Documents\GitHub\k_mooc_reboot\_static\_pickle\
 """

MY_FILE ='i_have_a_dream.pdb'    # Address of minister, Martin Luter King
LOGFILE ='count_file_log.pdb'

DESTIN_DIR =os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            '_static', '_pickle', '')

def test1_read_splitlines_wo_LF():
    """ WAY 2-1 ... read().splitlines 'list' w/o 'LF-line feed'
     simple 'list' data without LF- '\n', you can use it simply
     """
    f = open(DESTIN_DIR + MY_FILE, 'r')

    # contents = f.read().strip()       #1-1 <class 'str'> - a whole text as 1string.
    # contents = f.readline().strip()   #1-2 <class 'str'> - read line 1 by 1
    # contents = f.readlines()          #2-1 <class 'list'>- a whole line as list
    contents = f.read().splitlines()  #2-2 <class 'list'> - a whole lines as list

    # remove all '' - LF on 'list' contents
    for n in range(contents.count('')):
        contents.remove('')

    # show line by line in 'list' contents
    for index, line in enumerate(contents, 1):
        print('%s) %s'% (index, line))
    f.close()
# test1_read_splitlines_wo_LF()

def test1_readlines_w_LF():
    """ WAY 2-2 ... readlines 'list' /w 'LF-line feed'
     you have to deal with '\n' in each lines, remove it in various way.
     """
    with open(DESTIN_DIR + MY_FILE, 'r') as f:
        # contents = f.read().strip()       #1-1 <class 'str'> - a whole text as 1string.
        # contents = f.readline().strip()   #1-2 <class 'str'> - read line 1 by 1
        contents = f.readlines()          #2-1 <class 'list'>- a whole line as list
        # contents = f.read().splitlines()  #2-2 <class 'list'> - a whole lines as list

        # remove all '' - LF on 'list' contents
        for n in range(contents.count('\n')):
            contents.remove('\n')

        # show line by line in 'list' contents
        for index, line in enumerate(contents, 1):
            print('%s) %s'% (index, line), end='')
# test1_readlines_w_LF()

def test2_for_readlines_w_LF():
    """ 'list' - readlines() doesn't contain LF = without '\n' """
    with open(DESTIN_DIR+MY_FILE,'r') as f:
        lines = f.readlines()        # 'list'

        i=1
        for line in lines:
            if line.replace('\n','').strip() != "":
                print('%2s) --> %s'% (i, line.replace('\n','')))
                i+=1
# test2_for_readlines_w_LF()

def test2_while_readline_w_LF():
    """ 'str' - readline() contains LF = '\n' """
    with open(DESTIN_DIR + MY_FILE,'r') as f:
        i = 1
        while True:
            line = f.readline().replace('\n','') # remove all LF-'\n'

            #1. if '' then 'GO BACK' to 1-line
            if line.strip() == "":          # strip blanks both end
                continue
            #2. if line == None then 'STOP'
            if not line:
                break
            #3. or 'ELSE' print result
            print('%2s) --> %s'% (i, line))  # print line x line

            i += 1
# test2_while_readline_w_LF()

def drill_data_logger():
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
# drill_data_logger()
