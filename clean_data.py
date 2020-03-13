import pandas as pd 

spreadsheet_file_path ='data_keuangan_2019.xlsx'
df = pd.read_excel(spreadsheet_file_path)

print(df.head(20))

#df[Name] = df[].str.replace(r'r\W',"")

#df.to_excel("summary.xlsx")