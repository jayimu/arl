import pandas as pd
s1 = pd.Series([43,56,65,32])
print(s1)
s2 = pd.Series([43,12.4])
print(s2)
s3 = pd.Series([False,True])
print(s3)

s4 = pd.Series([44,23.1,True,'Hello World'])
print(s4)

# 改变第1列的索引（默认是数字）
ss = pd.Series(['Bill Gates','微软创始人'],index=['Person','Who'])
print(ss)


