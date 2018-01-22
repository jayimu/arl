# 哪个罩杯的女性对黑色胸罩的需求量最大
from pandas import *
from matplotlib.pyplot import *
import sqlite3
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///bra.sqlite')
rcParams['font.sans-serif'] = ['SimHei']
options.display.float_format = '{:,.2f}%'.format
sales = read_sql('select source,size1,color1 from t_sales',engine)
braBlack = []
bra = ['A','B','C']
for zb in bra:
    size1color1Count = sales[sales['size1'] == zb].groupby(['size1','color1'])['size1'].count()
    size1color1Total = size1color1Count.sum()
    size1color1 = size1color1Count.to_frame(name='销量')
    size1color1 = size1color1.sort_values(['销量'],ascending=[0])
    size1color1.insert(0,'比例',100*size1color1Count / size1color1Total)
    size1color1Count = size1color1.iloc[0,0]
    braBlack.append(size1color1Count)
print(braBlack)
bar([1,2,3],braBlack)
xlabel(bra)
show()
