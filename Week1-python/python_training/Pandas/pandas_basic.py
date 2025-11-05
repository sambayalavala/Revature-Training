import pandas as pd
df=[1,2,3,4,5]
series=pd.Series(df)
print(series)

data={
'name':['siva','ram'],
'age':[21,22],
'working':['Revature','hcl']
}
d=pd.DataFrame(data)
print(d)