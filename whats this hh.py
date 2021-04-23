import numpy as np
import pandas as pd
ser_obj = pd.Series(np.random.randint(0,10,10))
print(ser_obj)
print('* '* 50)
print(ser_obj.map(lambda x : x ** 2))
print('* '* 50)
df_obj = pd.DataFrame({'data1' : ['a']*5 + ['b']*5,
                       'data2': np.random.randint(0,4,10)})
print(df_obj)
print('* '* 50)

df_obj1 = pd.DataFrame(np.random.randint(0,10,(3,2)),index = ['a', 'b','c'],columns = ['A','B'])
df_obj2 = pd.DataFrame(np.random.randint(0,10,(2,2)),index = ['a', 'b'],columns = ['C','D'])
print(df_obj1)
print('* '* 50)
print(df_obj2)
print('* '* 50)
print(pd.concat([df_obj1,df_obj2]))
print('* '* 50)
print(pd.concat([df_obj1,df_obj2]), axis = 1, join = 'iner')
