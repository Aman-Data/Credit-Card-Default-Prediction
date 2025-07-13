import pandas as pd

df=pd.read_csv(r'C:\Users\amant\OneDrive\Desktop\Mlendtoend\data\rawdata.csv')

df.head()
df.info()

import os 

os.makedirs(r'C:\Users\amant\OneDrive\Desktop\Mlendtoend\data\cleaneddata',exist_ok=True)

df.to_csv(r'C:\Users\amant\OneDrive\Desktop\Mlendtoend\data\cleaned.csv',index=False)
