# 查看数据集中的列
import pandas
df = pandas.read_csv('gapminder.tsv',sep='\t')

# 获取列
country_df = df['country']
print(country_df.head(2))
print(country_df.tail(2))


subset = df[['country', 'continent', 'year']]

print(subset.head(2))
print(subset.tail(2))