"""
# How to use apply() in pandas dataframe
# ---------
# 파이썬 판다스 데이터프레임의 apply 함수를 이용하는 방법
# https://tariat.tistory.com/622
#
\n\n"""
print(__doc__)

import pandas as pd

def make_list(x):
    if x == 0:
        return 999
    elif x == 1:
        return 300
    else:
        return x


test_func = [make_list(x) for x in range(10)]

test_compre = [999 if x == 0 else 300 if x == 1 else x for x in range(10)]

test_lambda = map(lambda x: 999 if x == 0 else 300 if x == 1 else x,
                  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


print(test_compre)          # [999, 300, 2, 3, 4, 5, 6, 7, 8, 9]
print(test_func)            # [999, 300, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(test_lambda))    # [999, 300, 2, 3, 4, 5, 6, 7, 8, 9]


# df.ix[df["order"]==0,"order"]=999
# df["order"] = df["order"].apply(make_list)
# df["order"] = df["order"].apply(lambda x: 999 if x == "" else 300 if x==1 else x)

df = pd.DataFrame(
    [i for i in range(10)],
    columns=["order", ],
    dtype=int)
print(df)

# change values individually, 1 by 1 :
df.ix[df["order"] == 0, "order"] = 999
df.ix[df["order"] == 1, "order"] = 300
print(df)

# change values using function make_list(x) :
df["order"] = df["order"].apply(make_list)
print(df)

# change values
df["order"] = df["order"].apply(
    lambda x: 999 if x == 0 else 300 if x == 1 else x)
print(df)
