import pandas as pd 

df = pd.read_excel(r"/home/nick/Desktop/Developing/Projects/SAEBot/Assets/SpreadSheet/CONTROLE ANAC SAE. RVB 2021 .xlsx")  # r = reads path

print(df ['ANAC'] [616])

df.info()  # lista as colunas
df.groupby(['DATA PRATICO','ANAC']).sum()
print(df)