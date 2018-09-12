import numpy as np
import pandas as pd

columns=['age','gender','height',
     'weight','ap_hi','ap_lo',
     'cholesterol','gluc','smoke',
     'alco','active']

arr_2d = [
        [35,2,160,56,120,80,1,1,0,0,1],
        [35,2,160,56,120,80,1,1,0,0,1],
    ]

np_a = np.array(arr_2d)
print(len(columns))
print(np_a.shape)

df = pd.DataFrame(np_a, columns=columns)
print (df.head(n=5))
