# Pandas   Matplotlib

from pandas import *
from matplotlib.pyplot import *
import sqlite3
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///bra.sqlite')
rcParams['font.sans-serif'] = ['SimHei']
sales = read_sql('select source,size1 from t_sales',engine)
#print(sales)
size1Count = sales.groupby('size1')['size1'].count()
print(size1Count)
size1Total = size1Count.sum()
print(size1Total)
print(type(size1Count))
size1 = size1Count.to_frame(name='销量')
print(size1)
options.display.float_format = '{:,.2f}%'.format
size1.insert(0,'比例', 100 * size1Count / size1Total)
print(size1)
size1.index.names=['罩杯']
print(size1)

# 数据可视化
# 一个DataFrame由一个或多个Series组成
print(size1['销量'])
labels = ['A罩杯','B罩杯','C罩杯','D罩杯']
size1['销量'].plot(kind='pie',labels = labels, autopct='%.2f%%')
axis('equal')
legend()
show()