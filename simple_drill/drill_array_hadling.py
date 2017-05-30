import keyword, random

def kw_show():
     print(keyword.kwlist)
#kw_show()
#------------------------

li_st = [1,2,3,]          # array
tu_ple = (1,2,3,)
dic_t = {'a':1, 'b':2}

for x in range(5):
    li_st.append(4+x)
print(li_st)

#for x in range(5):
#    tu_ple.append(4+x)
# print(li_st)
#

li_st = []
for x in range(10):
    li_st.append(random.randint(0,11))
print(li_st)


li_st = [ random.randint(0,11) for x in range(10)] # global Num; Num=[random.randint(0,100) for n in range(5)]
print(li_st)

print(li_st[0])
print(li_st[9])

matrix_li = [[1,2,3],[3,4,5],[4,5,6]]
print(matrix_li[0])
print(matrix_li[1][1])

# Dictionary use in - ZIP function
name = ['Park', 'Choi', 'Kim',]
position = ['FW','MD','DF',]
number = [18,15,4,]

national_team = { name: [position, number] for name, position, number in zip(name, position, number) }
print (national_team)

print( 'PARK =' , national_team['Park'] )
print( national_team['Park'][1] )
# -----------------------------------------
