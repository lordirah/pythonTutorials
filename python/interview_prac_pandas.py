import pandas as pd

data = {'a' : [1,2,3,4],
        'b' : [1,5,3,4],
        'c' : [1,5,6,4],}
df = pd.DataFrame(data, columns = ['a','b','c'])
print(df)
df = df.drop('a', axis= 1)
print(df)
df = df.sort_index()
print(df)
df = df.sort_values(by = 'b')
print(df)
#df = df.rank()
print(df)
