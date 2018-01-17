# Series的基本操作
import pandas as pd

scientists = pd.DataFrame({
    'Name':['Rosaline Franklin', 'William Gosset'],
    'Occupation':['Chemist', 'Statistician'],
    'Born':['1920-07-25', '1876-06-13'],
    'Died':['1958-04-16','1937-10-16'],
    'Age':[37,61]},columns=['Occupation','Born','Died','Age'],
            index=['Rosaline Franklin', 'William Gosset'])
print(scientists)
print('--------------------')
first_row = scientists.loc['Rosaline Franklin']
print(type(first_row))
print('--------------------')
print(first_row)
print('--------------------')
print(first_row.index)
print('--------------------')
print(first_row.keys())
print('--------------------')
print(first_row.values)

print(first_row.index[0])

