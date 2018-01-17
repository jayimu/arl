# 分组统计
import pandas
df = pandas.read_csv('gapminder.tsv',sep='\t')
# 对预期寿命分组统计
print(df.groupby(['continent','year'])['lifeExp'].mean())
