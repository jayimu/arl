# 分组统计
import pandas
df = pandas.read_csv('gapminder.tsv',sep='\t')
# 对预期寿命分组统计
print(df.groupby('year')['lifeExp'].mean().head(3))
print('-----------------')

# 多组统计
multi_group_var = df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean().head(3)
print(multi_group_var)
print('-----------------')

print(multi_group_var.reset_index())
print('-----------------')
# 统计数量
print(df.groupby('continent')['country'].nunique())