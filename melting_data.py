#<<--TIDY DATA-->>

import numpy as np 
import pandas as pd 

##open & read csv file
dataframe = 'export1.csv'
df = pd.read_csv(dataframe)
print(df.head())

##remove 'Unnamded: 2 ' column
df = df.drop('Unnamed: 2',axis=1)

##melting dataframe
df=pd.melt(df, id_vars=['Nama Item', 'Satuan','Stok'])
print(df.head)
