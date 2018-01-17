# Series的条件过滤
import pandas
scientists = pandas.read_csv('scientists.csv')
ages = scientists['Age']
print(ages[ages > ages.mean()].head(3))
print('---------')
print((ages > ages.mean()).head(3))
print('---------')
print(type(ages > ages.mean()))
print('---------')
print(ages[[True,True,False,True,False,True,True,False]])