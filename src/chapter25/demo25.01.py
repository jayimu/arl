import pandas
df = pandas.read_csv('gapminder.tsv',sep='\t')
print(type(df))
# 获取前面的n行
print(df.head())

# 获取二维表的维度
print(df.shape)

# 获取列名
print(df.columns)
for column in df.columns:
    print(column,end = ' ')


