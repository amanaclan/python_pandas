import numpy as np 
import pandas as pd 
#import matplotlib.pyplot as plt

csv_path = "export1.csv"
obat_tambahan="obat_tambahan.csv"

df2=pd.read_csv(obat_tambahan)
df = pd.read_csv(csv_path)
df = df.drop([ "Unnamed: 2", 
                "Satuan" ], axis=1)
df = df.drop([21,0,2],axis=0)
df = df.append(df2,ignore_index=True)
print(df)

#<--MATPLOTLIB-->

#df['Harga Pokok'].plot(kind='hist', rot= 70, x=True, y=True)
#df.boxplot(column='Stok',by='Harga Pokok', rot=90)
#plt.show()

#<--EKPLORASI DATA & SUMMARIZE DATA-->

#print(df.shape)
#print(df["Nama Item"].value_counts(dropna=False))
#print(df.describe())
#print(df[df["Harga Pokok"]==175000])