''' PENERAPAN ITERASI FILE csv_files = ['file1.csv','file2.csv','file3.csv']
    KETIGA FILE TERSEBUT AKAN DIGABUNGKAN'''

import pandas as pd 

csv_file = glob.glob('*.csv') #untuk membuka list *.csv

# membuat list
frame = [] # agar ketiga file bisa digabungkan

# iterasi
for csv in csv_file :       #untuk semua csv yang berada dalam csv_file
    df = pd.read_csv(csv)   #mengubah csv menjadi dataframe df
    frame.append(df)        #menambahkan setiap elemen df ke frame

#menggabungkan setiap frame 
uber = pd.concat(frame,ignore_index=True)

print(uber.head())

