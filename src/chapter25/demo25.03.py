# 查看数据集中的行
import pandas
df = pandas.read_csv('gapminder.tsv',sep='\t')
print(df.loc[4])
print('---------------')
print(df.loc[[2,4,5]])
print('---------------')
print(df.iloc[-1])


