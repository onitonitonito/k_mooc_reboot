# from stackoverflow.com
# /questions/51716578/
# code-takes-too-long-to-run-when-looping-through-a-dataframe
# https://goo.gl/awxeqH

import pandas as pd

signal = pd.DataFrame(
        [
            [0, 0, 0],
            [-1, -1, -1],
            [1, 0, 0],
            [0, 0, 0],
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [0, -1, 1],
            [-1, 0, 0],
            [0, 0, 0],
        ],
        columns=['TKV','SWP','BWN'],
        )
# index=date_index

def remove_duplicate(df, lookahead_days):
    df = df.copy()
    df.index = pd.to_datetime(df.index)

    for i in range(0, signal.shape[0], lookahead_days-1):
        date_range = df.index[i:i+lookahead_days]
        for col in df.columns:
            duplicates = df[col][date_range].duplicated(keep="first")
            duplicates_index = df[col][date_range][duplicates].index
            df.loc[duplicates_index, col] = 0
    df.index = df.index.date
    return df

# Error occures
# remove_duplicate(signal, '2018-06-11')

# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-5-a77d27fa8df4> in <module>()
# ----> 1 remove_duplicate(signal, '2018-06-11')

# <ipython-input-4-249614fab771> in remove_duplicate(df, lookahead_days)
#       3     df.index = pd.to_datetime(df.index)
#       4
# ----> 5     for i in range(0, signal.shape[0], lookahead_days-1):
#       6         date_range = df.index[i:i+lookahead_days]
#       7         for col in df.columns:

# TypeError: unsupported operand type(s) for -: 'str' and 'int'



# Answer
# SET UP¶
# You can use drop_duplicates here, the tricky thing is that you need to create a column that will never result in duplicates outside of each n-day period (Or whatever time grouping you decide on). Let's say that you want to drop duplicates if they appear within a 5 day period, we need to create a column that is duplicated for each of these periods, that we can use as a key to drop_duplicates:

from pandas import Timestamp

signal = pd.DataFrame(
    {'TKV': {
        Timestamp('2018-01-01 00:00:00'): 0,
        Timestamp('2018-01-02 00:00:00'): -1,
        Timestamp('2018-01-03 00:00:00'): 1,
        Timestamp('2018-01-04 00:00:00'): 0,
        Timestamp('2018-01-05 00:00:00'): 1,
        Timestamp('2018-01-06 00:00:00'): 0,
        Timestamp('2018-01-07 00:00:00'): 0,
        Timestamp('2018-01-08 00:00:00'): 0,
        Timestamp('2018-01-09 00:00:00'): -1,
        Timestamp('2018-01-10 00:00:00'): 0},
     'SWP': {
         Timestamp('2018-01-01 00:00:00'): 0,
         Timestamp('2018-01-02 00:00:00'): -1,
         Timestamp('2018-01-03 00:00:00'): 0,
         Timestamp('2018-01-04 00:00:00'): 0,
         Timestamp('2018-01-05 00:00:00'): 0,
         Timestamp('2018-01-06 00:00:00'): 1,
         Timestamp('2018-01-07 00:00:00'): 0,
         Timestamp('2018-01-08 00:00:00'): -1,
         Timestamp('2018-01-09 00:00:00'): 0,
         Timestamp('2018-01-10 00:00:00'): 0},
     'BWN': {
         Timestamp('2018-01-01 00:00:00'): 0,
         Timestamp('2018-01-02 00:00:00'): -1,
         Timestamp('2018-01-03 00:00:00'): 0,
         Timestamp('2018-01-04 00:00:00'): 0,
         Timestamp('2018-01-05 00:00:00'): 0,
         Timestamp('2018-01-06 00:00:00'): 0,
         Timestamp('2018-01-07 00:00:00'): 1,
         Timestamp('2018-01-08 00:00:00'): 1,
         Timestamp('2018-01-09 00:00:00'): 0,
         Timestamp('2018-01-10 00:00:00'): 0,
     }
    })

print(signal)

'''            TKV  SWP  BWN
2018-01-01    0    0    0
2018-01-02   -1   -1   -1
2018-01-03    1    0    0
2018-01-04    0    0    0
2018-01-05    1    0    0
2018-01-06    0    1    0
2018-01-07    0    0    1
2018-01-08    0   -1    1
2018-01-09   -1    0    0
2018-01-10    0    0    0

Process returned 0 (0x0)        execution time : 0.686 s
계속하려면 아무 키나 누르십시오 . . .
'''



'''
You can use drop_duplicates here, the tricky thing is that you need to create a column that will never result in duplicates outside of each n-day period (Or whatever time grouping you decide on). Let's say that you want to drop duplicates if they appear within a 5 day period, we need to create a column that is duplicated for each of these periods, that we can use as a key to drop_duplicates:
'''

s = (signal.reset_index()
        .groupby(pd.Grouper(freq='5d', key='index'))
        ['index'].transform('first')
    )

signal.assign(flag=s.values).drop_duplicates(['flag', 'TKV', 'SWP', 'BWN']).drop('flag', 1)


'''	TKV	SWP	BWN
2018-01-01	0	0	0
2018-01-02	-1	-1	-1
2018-01-03	1	0	0
2018-01-06	0	1	0
2018-01-07	0	0	1
2018-01-08	0	-1	1
2018-01-09	-1	0	0
2018-01-10	0	0	0
'''


'''
If instead of dropping duplicates, you'd like to simply replace them with 0, you can make use of duplicated here.
'''

tmp = signal.assign(flag=s.values)
tmp[tmp.duplicated()] = 0
tmp = tmp.drop('flag', 1)

signal = pd.concat([signal]*2000)
signal = signal.reset_index(drop=True).set_index(pd.date_range(start='1995-01-01', periods=20000))

s1 = (signal.reset_index().groupby(pd.Grouper(freq='5d', key='index'))['index'].transform('first'))
signal.assign(flag=s1.values).drop_duplicates(['flag', 'TKV', 'SWP', 'BWN']).drop('flag', 1)
