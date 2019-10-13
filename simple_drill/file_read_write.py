import os

F_NAME = 'new_file.pdb'
DESTIN_DIR = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            '_statics', '_pickle', '')

def compose_data():
    global dict_list

    uid = ['onito','kaka','unins','funxd','haha','hehe','kkkk','hhhh',]
    name = ['Kay','Liam','Wilson','Smith','Brian','Carl','Michael','Louis',]
    position = ['FW','MF','MF','DF','GK','DF','MF','DF',]
    number = [18, 10, 11, 7, 5, 4, 17, 3,]

    dict_list = { w:[x,y,z] for w,x,y,z in zip(uid, name, position, number) }
    # dict_list = { 'kaka'   : ['Liam', 'MF', 18],
    #                'unins' : ['wilson', 'MF', 11],
    #           ..... }

def write_file():
    f = open(DESTIN_DIR + F_NAME, 'w', encoding='UTF-8')
    key_list = dict_list.keys()     # extract, key_list = [uids.. onito, kaka,..]
    n = 1                           # numbering start from 'n'

    # write line x line with format --> 1,	Kay (18), 	FW    (repeat)
    for x in key_list:              # key_list = [onito, kaka, ...]
        data ="%d,\t%s (%d), \t%s\n"%(n, dict_list[x][0],dict_list[x][2],dict_list[x][1],)
        f.write(data)
        n+=1
    f.close()

def read_file():
    f = open(DESTIN_DIR + F_NAME, 'r', encoding='UTF-8')
    for x in range(MEMBER):
        line = f.readline()
        print(line, end="")
    f. close()

def add_file(uid, name, position, number):
    # ADD DICT & modify file
    pass

def mod_file(uid, postion=None, number=None):
    # Modify DICT & Re-write
    position = None
    number = None
    if position == None:
        postion = None
    elif number == None:
        number = None
    pass


compose_data()          # make dict_list using zip()
#print(len(dict_list))  # length of dict_list = 8 : OK

MEMBER = len(dict_list) # when use read_file,

write_file()            # open file and wrinte line x line
add_file('uid', 'name', 'position', 'number')       # pass
mod_file('uid', postion=None, number=None)          # pass
read_file()
#print(dict_list)
