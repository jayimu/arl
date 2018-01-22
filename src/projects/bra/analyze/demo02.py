# 直接使用复杂的SQL语句和视图
from pandas import *
from matplotlib.pyplot import *
import sqlite3
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///bra.sqlite')
rcParams['font.sans-serif'] = ['SimHei']
sales = read_sql('''
select 'A' as 罩杯,  printf('%.2f%%',(100.0 * count(*) / (select count(*) from t_sales where size1 is not null))) as 比例,count(*) as 销量 from t_sales where size1='A'
union all
select 'B' , printf('%.2f%%',(100.0 * count(*) / (select count(*) from t_sales where size1 is not null))) as 比例,count(*) from t_sales where size1='B'
union all
select 'C' , printf('%.2f%%',(100.0 * count(*) / (select count(*) from t_sales where size1 is not null))) as 比例,count(*)from t_sales where size1='C'
union all
select 'D' , printf('%.2f%%',(100.0 * count(*) / (select count(*) from t_sales where size1 is not null))) as 比例,count(*) from t_sales where size1='D'
order by 销量 desc
''',engine)
print(sales)

sales1 = read_sql('select * from v_sales', engine)

labels = ['A罩杯','B罩杯','C罩杯','D罩杯']
sales1['销量'].plot(kind='pie',labels = labels, autopct='%.2f%%')
axis('equal')
legend()
show()
