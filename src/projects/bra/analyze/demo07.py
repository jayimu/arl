# 哪一种颜色的胸罩卖的最好
from pandas import *
from matplotlib.pyplot import *
import sqlite3
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///bra.sqlite')
rcParams['font.sans-serif'] = ['SimHei']
options.display.float_format = '{:,.2f}%'.format
sales = read_sql('select source,color1 from t_sales',engine)
#print(sales)
color1Count = sales.groupby('color1')['color1'].count()

color1Total = color1Count.sum()
print(color1Total)
color1 = color1Count.to_frame(name='销量')
print(color1)

color1.insert(0,'比例', 100 * color1Count / color1Total)

color1.index.names=['颜色']
color1 = color1.sort_values(['销量'], ascending=[0])
print(color1)
n = 1200
others = DataFrame([color1[color1['销量'] <= n].sum()],index=MultiIndex(levels=[['其他']],labels=[[0]]))


color1 = color1[color1['销量']>n].append(others)
print(color1)


labels = color1.index.tolist()
pie(color1['销量'],labels=labels,autopct='%.2f%%')
legend()
axis('equal')
title('按胸罩颜色统计的比例')
show()
'''


# 数据可视化
# 一个DataFrame由一个或多个Series组成
print(size1['销量'])
labels = ['A罩杯','B罩杯','C罩杯','D罩杯']
size1['销量'].plot(kind='pie',labels = labels, autopct='%.2f%%')
axis('equal')
legend()
show()
'''