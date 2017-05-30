def compose_data():
    global dict_list

    uid = ['onito','kaka','unins','funxd','haha','hehe',]

    name = ['Kay','Liam','Wilson','Smith','Brian','Carl']
    position = ['FW','MF','MF','DF','GK','DF']
    number = [18, 10, 11, 7, 5, 4,]

    dict_list = { w:[x,y,z] for w,x,y,z in zip(uid, name, position, number) }

def write_file():
    f = open('./static/data_docs/new_file.pdb', 'w', encoding='UTF-8')
    key_list = dict_list.keys()
    n = 1

    for x in key_list:
        data ="%d.\t%s (%d), \t%s\n"%(n, dict_list[x][0],dict_list[x][2],dict_list[x][1],)
        f.write(data)
        n+=1
    f.close()

def read_file():
    f = open('./static/data_docs/new_file.pdb', 'r', encoding='UTF-8')
    for x in range(6):
        line = f.readline()
        print(line)
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


compose_data()
write_file()
add_file('uid', 'name', 'position', 'number')
mod_file('uid', postion=None, number=None)
read_file()
#print(dict_list)
