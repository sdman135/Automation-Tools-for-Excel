#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np

# Import Dataframe
df = pd.read_csv('train.csv')
print(f"{len(df)} transactions in your raw data")

# Format Date
print("Start Processing ...")
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
df['month-year'] = df[['month', 'year']].astype(str).apply(lambda t: t['month'].zfill(2) + '-' + t['year'], axis = 1)

# month year columns
my_cols = [str(i).zfill(2) + '-' + str(j) for j in range(2013, 2018) for i in range(1, 13)]

# pivot by store item
df_store = pd.pivot_table(df, values='sales', index=['store', 'item'],
                    columns=['month-year'], aggfunc=np.sum).fillna(0)

# sort by ascending order
df_store.sort_values(['store', 'item'], ascending = [True, True], inplace = True)
print("Processing is completed.")
print("{:,} lines in your final report".format(len(df_store)))

# reorder columns
df_store = df_store[my_cols]

# Final report
print("Start saving report.")
df_store.to_excel('sales_report.xlsx')
print("Your report is saved.")


# In[ ]:


pip install pyinstaller


# In[ ]:




