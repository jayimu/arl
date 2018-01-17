import pandas
df = pandas.read_csv('gapminder.tsv',sep='\t')

print(df.head(10))
print(df.tail(10))



