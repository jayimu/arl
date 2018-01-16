# 可视化统计数据（依赖Matplotlib）
import pandas
import matplotlib.pyplot as plt
df = pandas.read_csv('gapminder.tsv',sep='\t')

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)


multi_group_var = df.groupby('year')['gdpPercap'].mean()
print(multi_group_var)

fig,(ax1, ax2) = plt.subplots(1,2,figsize=(8,4))
ax1.plot(global_yearly_life_expectancy)
ax2.plot(multi_group_var)
plt.show()
