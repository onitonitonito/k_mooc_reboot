"""
# 판다스 DF 소팅하기
#
\n\n\n"""
print(__doc__)

import numpy as np
import pandas as pd
from pprint import pprint

x = [['a', 'b'], ['b', 'a'], ['a', 'c'], ['c', 'a']]
df = pd.DataFrame({'a': pd.Series(x)})

_ = df.a.sort_values()


print(df)
print(_)


"""
# pd.DataFrame({'a': pd.Series(x)})
        a
0  [a, b]
1  [b, a]
2  [a, c]
3  [c, a]


# df.a.sort_values()

0    [a, b]
2    [a, c]
1    [b, a]
3    [c, a]
Name: a, dtype: object
"""
