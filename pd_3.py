import numpy as np
import pandas as pd

data=np.array([['','Col1','Col2'],
                ['Row1',1,2,],
                ['Row2',3,4]])
df=pd.DataFrame(data=data[1:,1:],
                index=data[1:,0],
                columns=data[0,1:])
print(df)

#Taking 2D array as input to your data frame
print("-"*20)
arr=np.array([[1,2,3],[4,5,6]])
print(pd.DataFrame(arr))
print("-"*20)
print("Taking Dictionary to your data frame")
di={'Col1':['1','3'],'Col2':['1','2'],'Col3':['2','4']}
df1=pd.DataFrame(di)
print(df1)

#Take DataFrame as input to your data frame
my_df=pd.DataFrame(data=[4,5,6,7],index=range(0,4),columns=['A'])
print(pd.DataFrame(my_df))

# Take a Series as input to your DataFrame
s=pd.Series({'United Kingdom':'London',"India":"New Delhi","US":"Washington"})

print(pd.DataFrame(s))
