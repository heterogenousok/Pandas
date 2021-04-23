#%%
import pandas as pd
ser_obj = pd.Series(range(10, 20))
print(ser_obj)
# 获取数据
print(ser_obj.values)
print('* '* 50)
# 获取索引
print(ser_obj.index)
print('* '* 50)
#%%
print(ser_obj * 2)
print('* '* 50)
print(ser_obj > 15)
print('* '* 50)
#%%
year_data = {2001: 17.8, 2005: 20.1, 2003: 16.5}
ser_obj2 = pd.Series(year_data)
print(ser_obj2)
print('* '* 50)
print(ser_obj2.index)
print('* '* 50)
print(ser_obj2[2001])
print('* '* 50)

#%%
print(ser_obj2.name)
print('* '* 50)
ser_obj2.name = 'temp'
print(ser_obj2.index.name)
print('* '* 50)
ser_obj2.index.name = 'year1'
print(ser_obj2.head())
print('* '* 50)

#%% md
# DataFrame
#%%
d2 =[{"name" : "xiaohong" ,"age" :32,"tel" :10010},{ "name": "xiaogang" ,"tel": 10000} ,{"name":"xiaowang" ,"age":22}]
df6=pd.DataFrame(d2)

print(df6)
print('* '* 50)
#%%
import pandas as pd
import numpy as np
dict_data = {'A': 1,
             'B': pd.Timestamp('20190926'),
             'C': pd.Series(1, index=list(range(4)),dtype='float32'),
             'D': np.array([3] * 4,dtype='int32'),
             'E': ["Python","Java","C++","C"],
             'F': 'wangdao' }
df_obj2 = pd.DataFrame(dict_data)
print(df_obj2)
print('* '* 50)

print(df_obj2.index)
print('* '* 50)
# df_obj2.index[0] = 2
#%%
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

print(df)
print('* '* 50)
#%%
print(df_obj2['A'])
print('* '* 50)
#把df的某一列取出来是series
print(type(df_obj2['A']))
print('* '* 50)
#%%
#增加列数据
df_obj2['G'] = df_obj2['D'] + 4
print(df_obj2.head())
print('* '* 50)
#%%
# 删除列
del(df_obj2['G'] )
print(df_obj2.head())
print('* '* 50)
#%% md
# 4 Pandas的索引操作
#%%
print(df_obj2.index)
print('* '* 50)
#%%
# 索引对象不可变（上面代码增加）
# df_obj2.index[0] = 2
#%% md
# 3 常见的Index种类
# •Index，索引
# •Int64Index，整数索引
# •MultiIndex，层级索引
# •DatetimeIndex，时间戳类型
#%%
ser_obj = pd.Series(range(5), index = list("abcde"))
print(ser_obj)
print('* '* 50)
ser_obj.index
#%%
# 行索引
print(ser_obj['b'])
print('* '* 50)
print(ser_obj[2])
print('* '* 50)
#%%
# 切片索引
print(ser_obj[1:3])
print('* '* 50)
print(ser_obj['b':'d'])
print('* '* 50)
#%%
# 不连续索引
print(ser_obj[[0, 2, 4]])
print('* '* 50)
print(ser_obj[['a', 'e']])
print('* '* 50)
#%%
# 布尔索引
ser_bool = ser_obj > 2
print(ser_bool)
print('* '* 50)
print(ser_obj[ser_bool])
print('* '* 50)

print(ser_obj[ser_obj > 2])
print('* '* 50)
#%% md
# 4 DataFrame索引
#%%
import numpy as np
df_obj = pd.DataFrame(np.random.randn(5,4), columns = ['a', 'b', 'c', 'd'])
print(df_obj.head())
print('* '* 50)
#%%
# 列索引
print(df_obj['a']) # 返回Series类型
print('* '* 50)
print(df_obj[['a']]) # 返回DataFrame类型
print('* '* 50)
print(type(df_obj[['a']])) # 返回DataFrame类型
print('* '* 50)
#%% md
# 1. loc 标签索引
#%%
# 标签索引 loc
# Series
print(ser_obj)
print(ser_obj['b':'d'])
print(ser_obj.loc['b':'d'])

# DataFrame
df_obj = pd.DataFrame(np.random.randn(5,4), columns = ['a', 'b', 'c', 'd'],index=list('abcde'))
print(df_obj['a'])
print('-'*50)
print(df_obj.loc['a'])
print('-'*50)
# 第一个参数索引行，第二个参数是列,loc或者iloc效率高于直接用取下标的方式
print(df_obj.loc['a':'c', 'a':'c'])
#%% md
# iloc 位置索引
#%%
# Series
print(ser_obj[1:3])
print(ser_obj.iloc[1:3])

# DataFrame
print(df_obj.iloc[0:2, 0:2]) # 注意和df_obj.loc[0:2, 'a']的区别
#%% md