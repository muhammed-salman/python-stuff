import pandas as pd

#s = pd.Series([3, -5, 7, 4], index=['a', 'name', 'c', 'd'])

data = {'Country': ['Belgium', 'India', 'Brazil'],
        'Capital': ['Brussels', 'New Delhi', 'Brasília'],
        'Population': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data,columns=['Country','Population','Capital'])

#print(df)

#getting subset of dataframe
#print(df[1:2])

print(df)
#selecting single val by row & col
#print(df.iloc[[1],[1]])
#df.iat([0], [0])


#select by col label
df.loc[[0], ['Country']]
#df.at([0], ['Country'])

#select of single row
df.ix[2]

#selecting single col
print(df.ix[:,'Capital'])
""""
#selecting rows & cols
df.ix[1,'Capital']

"""