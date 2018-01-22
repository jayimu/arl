# 按上胸围分析胸罩的销售比例
from pandas import *
from matplotlib.pyplot import *
import sqlite3
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///bra.sqlite')
rcParams['font.sans-serif'] = ['SimHei']
options.display.float_format = '{:,.2f}%'.format

sales = read_sql('select source,size2 from t_sales',engine)
size2Count = sales.groupby('size2')['size2'].count()
print(size2Count)

size2Total = size2Count.sum()
print(size2Total)
size2 = size2Count.to_frame(name='销量')

size2.insert(0,'比例',100*size2Count/size2Total)

size2.index.names=['上胸围']
size2 = size2.sort_values(['销量'], ascending=[0])
print(size2)

labels = size2.index.tolist()
size2['销量'].plot(kind='pie',labels=labels,autopct='%.2f%%')
legend()
axis('equal')
show()


