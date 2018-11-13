"""
# data format in pandas --> pd.options.display.float_format
#
#
#\n\n\n"""
print(__doc__)

import pandas as pd

# pd.options.display.float_format = "${:'.2f'}".format

items = [
        123.45670023,
        234.56780023,
        345.67890023,
        456.79800023,
    ]

index = [
        'foo',
        'bar',
        'baz',
        'quux',
    ]

df = pd.DataFrame(items, index=index, columns=['Cost'])

# print df.to_string in formatters
_a = df.to_string()
print(_a,"\n\n")

_a = df.to_string(formatters={'Cost':'$ {:,.1f}'.format})
print(_a,"\n\n")

_a = type(_a)
print(_a,"\n\n")



"""
          Cost
foo   123.4567
bar   234.5678
baz   345.6789
quux  456.7980


        Cost
foo  $ 123.5
bar  $ 234.6
baz  $ 345.7
quux $ 456.8


<class 'str'>
"""
