import csv
import pandas as pd
def find_row_by_id():
   df = pd.read_excel('Incidents.xls')
   print(df._slice(slice(0, 1)))
   print(df.columns)
   values=df['Incident'].values
   
   #id=Index(df).get_loc('IN379976')
   return print(df.iloc[[0]],values)

import pandas as pd
def find_rows_by_timestamp():
   df = pd.read_excel('Incidents.xls')
   x=df[(df['Creation Date'] > '5/1/2016 0:02:50')]
   
   return print(x)
print(find_rows_by_timestamp())
df['date'] = pd.date_range('2000-1-1', periods=200, freq='D')
mask = (df['date'] > '2000-6-1') & (df['date'] <= '2000-6-10')
print(df.loc[mask])
