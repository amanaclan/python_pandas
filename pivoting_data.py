##--PIVOTING DATA --##

import pandas as pd 
import numpy as np

##read csv
csvfile = pd.read_csv('export1.csv')
#print(csvfile)

##remove Unnamed: 2 column
df = csvfile.drop('Unnamed: 2',axis=1)
#print(df)

##pivoting duplicate value
df = df.pivot_table(index='Kode Item', columns='Nama Item',values='Harga Pokok', aggfunc= np.mean)
print(df)