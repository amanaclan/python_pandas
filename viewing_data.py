import pandas as pd 
import numpy as np 

csv_path = "export.csv"
df = pd.read_csv(csv_path)
print(df)
df = df.drop([ "Unnamed: 0", "Unnamed: 2", "Unnamed: 3", "Unnamed: 4",
               "Unnamed: 5", "Unnamed: 6", "Unnamed: 7", "Unnamed: 8",
               "Unnamed: 9", "Unnamed: 10","Unnamed: 11", "Unnamed: 12",
               "Unnamed: 13", "Unnamed: 17", "Unnamed: 18"], axis=1) 

select = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
df = df.drop(select,axis=0)
#print(df)



# print(df["Kode Item"])
# print(type(df["Kode Item"]))

# names = df["Kode Item"]
# print(names[0:10])

# <--Label-->

# print(df.at[0,"Kode Item"])
# print(df.at[0,"Harga Pokok"])
# df2= pd.read_csv(csv_path,index_col="Nama Item")
#print(df.head(14))
print(df.loc["ABBOCATH 18":"ABBOCATH 24","Stok":"Harga Pokok"])