# 罩杯和上胸围分布【盒状图和直方图】
# 75B
from pandas import *
from matplotlib.pyplot import *
import sqlite3
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///bra.sqlite')
rcParams['font.sans-serif'] = ['SimHei']
options.display.float_format = '{:,.2f}%'.format
sales = read_sql('select source,size1,size2,color1 from t_sales', engine)

sales.loc[sales['size1'] == 'A','size1'] = 1
sales.loc[sales['size1'] == 'B','size1'] = 2
sales.loc[sales['size1'] == 'C','size1'] = 3
sales.loc[sales['size1'] == 'D','size1'] = 4
sales = sales.dropna()
print(sales)
sales['size3'] = sales['size1'].astype('str') + '.' + sales['size2'].astype('str')
print(sales)
# 将size3转换为float类型的列
sales['size3'] = sales['size3'].astype('float')
box = {
    'facecolor':'0.75',
    'edgecolor':'b',
    'boxstyle':'round'
    }
fig,(ax1,ax2) = subplots(1,2,figsize=(12,6))
ax1.hist(x=sales.size3) 
ax2.boxplot(sales.size3)
ax1.text(3.5,8000,'1:A\n2:B\n3:C\n4:D\n小数部分：上胸围\n1.80 = A80\n2.75 = B75',bbox = box)
ax2.text(1.2,4,'1:A\n2:B\n3:C\n4:D\n小数部分：上胸围\n1.80 = A80\n2.75 = B75',bbox = box)

show()

# A、B、C、D  =  1、2、3、4
# B.75  2.75   3.80


