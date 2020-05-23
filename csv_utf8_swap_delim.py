import pandas as pd
import glob

path = "/Users/antonssl/*.csv"

for fname in glob.glob(path):
   print(fname)
   df=pd.read_csv(fname, sep=',', encoding='utf8')
   new_name =  fname + '.new'
   print(new_name)
   df.to_csv(new_name,sep='~',index=False,encoding='utf8')
