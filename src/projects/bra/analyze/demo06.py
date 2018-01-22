# 罩杯和上胸围综合统计与数据可视化
# B  75   75B  80A
from pandas import *
from matplotlib.pyplot import *
import sqlite3
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///bra.sqlite')
rcParams['font.sans-serif'] = ['SimHei']
options.display.float_format = '{:,.2f}%'.format

sales = read_sql('select source,size1,size2 from t_sales',engine)
size1size2Count = sales.groupby(['size1','size2'])['size1'].count()
print(size1size2Count)
size1size2Total = size1size2Count.sum()
print(size1size2Total)
size1size2 = size1size2Count.to_frame(name='销量')

n = 500
others = DataFrame([size1size2[size1size2['销量'] <= n].sum()],index=MultiIndex(levels=[[''],['其他']],labels=[[0],[0]]))


size1size2 = size1size2[size1size2['销量']>n].append(others)
print(size1size2)

size1size2 = size1size2.sort_values(['销量'],ascending=[0])
size1size2.insert(0,'比例',100 * size1size2Count / size1size2Total)
print(size1size2)
labels = size1size2.index.tolist()
newLabels = []
for label in labels:
    newLabels.append(label[1] + label[0])
pie(size1size2['销量'],labels=newLabels,autopct='%.2f%%')
legend()
axis('equal')
title('罩杯+上胸围销售比例')
show()




