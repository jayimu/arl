# DataFrame的过滤条件
import pandas as pd
scientists = pd.read_csv('scientists.csv')

print(scientists[scientists['Age'] > scientists['Age'].mean()])
print('------------------')
print(scientists.loc[[True,True,False,True]])
print('------------------')
print(scientists.iloc[[1,3,4]])
print('------------------')
print(scientists[['Name','Age','Occupation']][scientists['Age'] > scientists['Age'].mean()].head(2))
print('------------------')
print(scientists[['Name','Age','Occupation']][scientists['Age'] > scientists['Age'].mean()].loc[[True,True]])
print('------------------')
print(scientists[['Name','Age','Occupation']][scientists['Age'] > scientists['Age'].mean()].iloc[[0,2]])
