# 分析与可视化天猫和京东胸罩ABCD罩杯的销售比例
from pandas import *
from matplotlib.pyplot import *
import sqlite3
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///bra.sqlite')
rcParams['font.sans-serif'] = ['SimHei']
options.display.float_format = '{:,.2f}%'.format

sales = read_sql('select source,size1 from t_sales',engine)
# DataFrame = table  view
# sales['source'] = Series
tmallSize1GroupCount = sales[sales['source'] == '天猫'].groupby('size1')['size1'].count()
tmallSize1Total = tmallSize1GroupCount.sum()
print(tmallSize1Total)
# 将Series转换为DataFrame
tmallSize1 = tmallSize1GroupCount.to_frame(name='销量')

tmallSize1.insert(0,'比例',100 * tmallSize1GroupCount / tmallSize1Total)
tmallSize1.index.names=['罩杯']
print(tmallSize1)

# 京东
jdSize1GroupCount = sales[sales['source'] == '京东'].groupby('size1')['size1'].count()
jdSize1Total = jdSize1GroupCount.sum()
print(jdSize1GroupCount)
# 将Series转换为DataFrame
jdSize1 = jdSize1GroupCount.to_frame(name='销量')

jdSize1.insert(0,'比例',100 * jdSize1GroupCount / jdSize1Total)
jdSize1.index.names=['罩杯']
print(jdSize1)

#labels1 = ['A罩杯','B罩杯','C罩杯']
#labels2 = ['A罩杯','B罩杯','C罩杯','D罩杯']
labels1 = []
labels2 = []
labels1 = tmallSize1.index.tolist()
labels2= jdSize1.index.tolist()
for i in range(len(labels1)):
    labels1[i] = labels1[i] + '罩杯'
for i in range(len(labels2)):
    labels2[i] = labels2[i] + '罩杯'
    
fig,(ax1,ax2) = subplots(1,2,figsize=(12,6))
ax1.pie(tmallSize1['销量'],labels = labels1, autopct='%.2f%%')
ax2.pie(jdSize1['销量'],labels = labels2, autopct='%.2f%%')
ax1.legend()
ax2.legend()
ax1.axis('equal')
ax2.axis('equal')
show()







