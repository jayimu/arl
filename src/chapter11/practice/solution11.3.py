import re
s = '2\d{3}-\d{1,2}-\d{1,2}'
print(re.match(s, '2001-12-12'))
ss = '日期1：2012-4-12，日期2：1994-12-12，日期3：2054-4-1，日期4：24212-4-5，日期5：2033-05-12'
print(re.findall(s, ss))