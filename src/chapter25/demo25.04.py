# 查看数据集中的单元格
import pandas
df = pandas.read_csv('gapminder.tsv',sep='\t')
subset = df.loc[:,['year', 'pop']]
print(subset.head(2))
print('--------------------')
subset = df.iloc[:,[2,4,-1]]
print(subset.head(2))
print('--------------------')
subset = df.iloc[:,3:6]
print(subset.head(2))
print('--------------------')
subset = df.iloc[0:3,3:6]
print(subset)
print('--------------------')
subset = df.loc[1,'lifeExp']
print(subset)







