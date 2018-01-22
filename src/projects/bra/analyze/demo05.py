# 天猫和京东各种的上胸围胸罩销售比例
from pandas import *
from matplotlib.pyplot import *
import sqlite3
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///bra.sqlite')
rcParams['font.sans-serif'] = ['SimHei']
options.display.float_format = '{:,.2f}%'.format

sales = read_sql('select source,size2 from t_sales',engine)
# DataFrame = table  view
# sales['source'] = Series
tmallSize2GroupCount = sales[sales['source'] == '天猫'].groupby('size2')['size2'].count()
tmallSize2Total = tmallSize2GroupCount.sum()
print(tmallSize2Total)
# 将Series转换为DataFrame
tmallSize2 = tmallSize2GroupCount.to_frame(name='销量')

tmallSize2.insert(0,'比例',100 * tmallSize2GroupCount / tmallSize2Total)
tmallSize2.index.names=['罩杯']
print(tmallSize2)

# 京东
jdSize2GroupCount = sales[sales['source'] == '京东'].groupby('size2')['size2'].count()
jdSize2Total = jdSize2GroupCount.sum()
print(jdSize2GroupCount)
# 将Series转换为DataFrame
jdSize2 = jdSize2GroupCount.to_frame(name='销量')

jdSize2.insert(0,'比例',100 * jdSize2GroupCount / jdSize2Total)
jdSize2.index.names=['罩杯']
print(jdSize2)

#labels1 = ['A罩杯','B罩杯','C罩杯']
#labels2 = ['A罩杯','B罩杯','C罩杯','D罩杯']
labels1 = []
labels2 = []
labels1 = tmallSize2.index.tolist()
labels2= jdSize2.index.tolist()

    
fig,(ax1,ax2) = subplots(1,2,figsize=(12,6))
'''
ax1.pie(tmallSize2['销量'],labels = labels1, autopct='%.2f%%')
ax2.pie(jdSize2['销量'],labels = labels2, autopct='%.2f%%')
ax1.legend()
ax2.legend()
ax1.set_title('天猫上胸围比例')
ax2.set_title('京东上胸围比例')
ax1.axis('equal')
ax2.axis('equal')
'''
intLabels = []
for label in labels1:
    intLabels.append(int(label))
ax1.bar(intLabels, tmallSize2['销量'])
ax2.pie(jdSize2['销量'],labels = labels2, autopct='%.2f%%')

ax2.legend()
ax1.set_title('天猫上胸围比例')
ax2.set_title('京东上胸围比例')

ax2.axis('equal')
show()
