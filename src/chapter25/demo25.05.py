# 分组统计
import pandas
df = pandas.read_csv('gapminder.tsv',sep='\t')
# 对预期寿命分组统计
print(df.groupby('year')['lifeExp'].mean())

print(type(df.groupby('year')))
print(type(df.groupby('year')['gdpPercap']))

# 多组统计
multi_group_var = df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean()
print(multi_group_var)
print(type(multi_group_var))

print(multi_group_var.reset_index())

# 统计数量
print(df.groupby('continent')['country'].nunique())
print(df.groupby('country')['year'].nunique())