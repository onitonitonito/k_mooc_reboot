import csv, os, sys

#FIND_KEY = '서울특별시'
#FIND_KEY = '서울특별시 동대문구'
#FIND_KEY = '서울특별시 동대문구 전농'
#FIND_KEY = '서울특별시 동대문구 전농1동'

#FIND_KEY = '강원도'
#FIND_KEY = '강원도 원주시'
#FIND_KEY = '강원도 원주시 명륜동'

#FIND_KEY = '전라북도'
#FIND_KEY = '전라북도 전주시'
FIND_KEY = '전라북도 전주시 중앙동'


CHOSEN_DATA = []
DESTIN_DIR = '../static/data_doc/log/'

with open(DESTIN_DIR +'00_data_population_floating.pdbv', 'r', encoding='utf8') as pop_file:
    header = []
    row_num = 0                     # when row[0] = header

    csv_data = csv.reader(pop_file) # Data reading using CSV object

    for row_list in csv_data:       # csv_dara = <class 'csv.reader'> = object type
        if row_num == 0:
            header = row_list
            row_num +=1

        if row_list[7].find(FIND_KEY) != -1:   # find()= position call
            CHOSEN_DATA.append(row_list)
            row_num +=1

# [TEST PRINTING by 2 in CHOSEN_DATA] -------------------------------------
os.system('cls')
print ('--'*40,end="")
print (header)
print ('=='*40,end="")

for n in range(2):
    print(CHOSEN_DATA[n])
    print ('__'*40,end="")

print('TOTAL_CHOSEN_NUM(%s)='%FIND_KEY,len(CHOSEN_DATA),"\n")


# [ MAKE DIR] ------------------------------------------------------------
CHOSEN_FILE = '01_data_FIND_KEY(%s)_%s.pdbv' %(FIND_KEY, str(len(CHOSEN_DATA)))

print(CHOSEN_FILE)

if os.path.exists(DESTIN_DIR + CHOSEN_FILE) == True:
    print('*** ERROR : FILE ALREADY EXISTS! REQUEST IS TERMINATED! ***')


# [ WRITE CHOSEN DATA BY FIND_KEY] ----------------------------------------
else:
    print('.......WRITING......\n\n')

    with open(DESTIN_DIR + CHOSEN_FILE, 'w', encoding='utf8') as wr_file:
        writer = csv.writer(
            wr_file,
            delimiter='\t',
            quotechar='"',
            lineterminator='\n',
            quoting=csv.QUOTE_NONNUMERIC,
            )                           # making CSV file, with parameters

        writer.writerow(header)

        for row in CHOSEN_DATA:
            writer.writerow(row)

    print('DONE!')
