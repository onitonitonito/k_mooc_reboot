import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#data = pd.read_csv('blog_blogpost.csv')
#print(data.head(10))

def test_index():       # have a problem with UTF-8
    data = pd.Series( [231312,123123123,123123,123123,1231],
                #index=['Seoul','Incheon','Dejeon','Degu','Busan',],)
                index=['서울','인천','대전','대구','부산',],)
    print(data)
#test_index()

def change_pbd():
    data = pd.read_csv('./static/data_docs/blog_blogpost.csv', index_col='id', encoding='UTF-8')
    pd.read_csv
    print(data.head(3))      # head(n)... n = num of data

    print ("="*40,"\n\tdata.INFO()\n"+"_"*40,"\n",)
    print(data.info())
    print("\n\n")

    print ("\n"+"="*40,"\n\tdata.DESCRIBE()\n"+"_"*40,"\n",data.describe(),"\n"+"-"*40,)

    f = open('./static/data_docs/new_file.pdb', 'w', encoding='UTF-8')
    f.write(str(data))      # f.write(data) need string data,not array.
    f.close()
    # conv = pd.Series(data.head())
    # print(conv)

    ''' RUN RESULT of change_pdb """
        =======================================
        	data.INFO()
        ________________________________________

        <class 'pandas.core.frame.DataFrame'>
        RangeIndex: 3 entries, 0 to 2
        Data columns (total 9 columns):
        id                3 non-null int64
        title             3 non-null object
        slug              3 non-null object
        description       3 non-null object
        content           3 non-null object
        create_date       3 non-null object
        published_date    3 non-null object
        author_id         3 non-null int64
        category_id       3 non-null int64
        dtypes: int64(3), object(6)
        memory usage: 184.0+ bytes
        None



        ========================================
        	data.DESCRIBE()
        ________________________________________
                 id  author_id  category_id
        count  3.0   3.000000     3.000000
        mean   2.0   1.666667     1.666667
        std    1.0   0.577350     0.577350
        min    1.0   1.000000     1.000000
        25%    1.5   1.500000     1.500000
        50%    2.0   2.000000     2.000000
        75%    2.5   2.000000     2.000000
        max    3.0   2.000000     2.000000
        ----------------------------------------
        [Finished in 3.308s]'''
# change_pbd()

data = pd.Series(range(10, 14))
sep="\n"+"-"*40+"\n"
print("data = pandas.Series(range(10,14,1)) = ",sep,data,sep,)
print("data.index = ", data.index,sep,)
print("data.values = ", data.values,sep,)
print("data.values[-1] = ", data.values[-1],sep,)

x = np.arange(0,3,1)
y = data.values

def plot_bars_lines(x,y,title=None):
    plt.figure(figsize=(7,5))           # window size
    if title :
        plt.title(title)
    else:
        plt.title('')

    plt.plot(y, 'rs--')                         # line plot - trends
    for x,y in zip(x,y):                # Bar chart
        plt.bar(x, y, facecolor='#ffaaaa', edgecolor='grey')
        plt.text(x, y+0.05, '%.1f'%y, ha='center', va= 'bottom')

    plt.grid()
    plt.show()
plot_bars_lines(x,y,title='NEW TRENDS DATA:2017')
