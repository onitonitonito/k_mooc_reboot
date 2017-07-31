#!/bin/user/python3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random as rd


''' add parent dir in system path
'''
import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
PARENT_DIR = sys.path[len(sys.path)-1]+"/"
# bg = PhotoImage(file=PARENT_DIR+"static/img_stickman/bground_sq060.png")
# -----------------------------------------

DESTIN_DIR= PARENT_DIR + 'static/data_doc/'

HEADER='''
==================================================
        %s
--------------------------------------------------'''

#data = pd.read_csv('blog_blogpost.csv')
#print(data.head(10))

def test_index():       # have a problem with UTF-8
    data = pd.Series( [231312,123123123,123123,123123,1231],
                index=['Seoul','Incheon','Dejeon','Degu','Busan',],)
                # index=['서울','인천','대전','대구','부산',],)
    print(HEADER %"data = pd.Series( [231] .., index=['서울',..]")
    print(data)
# test_index()

def change_pbd():
    data = pd.read_csv(DESTIN_DIR+'blog_blogpost.csv', index_col='id', encoding='UTF-8')
    # #[SMALL TEST] ---------------
    # print(data)    # Show all
    # print(data.head(3))      # head(n)... n = num of data --> Show 3 EA.
    # #[TEST END] -----------------

    print("data = pd.read_csv(DESTIN_DIR+'blog_blogpost.csv', index_col='id', encoding='UTF-8')")
    print (HEADER %'data.INFO()')
    print(data.info())
    print("\n\n")

    print(HEADER %'data.DESCRIBE()')
    print (data.describe())
    print("\n\n")

    f = open(DESTIN_DIR+'new_file.pdb', 'w', encoding='UTF-8')
    f.write(str(data))      # f.write(data) need string data,not array.
    f.close()

    # #[SMALL TEST] ---------------
    # print(data.head())
    # conv = pd.Series(data.head())     # Show all
    # print(conv)
    # #[TEST END] -----------------

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
change_pbd()

def make_series():
    global x, y

    data = pd.Series(range(10, 14))
    sep="\n"+"-"*40+"\n"
    print("1.data = pandas.Series(range(10,14,1)) = ",sep,data,sep,)
    print("2.data.index = ", data.index,sep,)
    print("3.data.values = ", data.values,sep,)
    print("3-1.data type = ", type(data.values),sep,)
    print("4.data.values[-1] = ", data.values[-1],sep,)

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

# make_series()
# plot_bars_lines(x,y,title='NEW TRENDS DATA:2017')
