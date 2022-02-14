#!/usr/bin/env python
# coding: utf-8

# In[17]:



import pandas as pd
import numpy as np


# In[18]:


rw = pd.read_csv(r"C:\Users\3363\Desktop\Metropolicy\Incentive Plan\Nov.csv")
rw.head()


# In[19]:


rw['CreatedOn'] = pd.to_datetime(rw['CreatedOn'], errors='coerce')

rw['CreatedOn'] = rw['CreatedOn'].dt.strftime('%d-%b')


# In[20]:


rw.head()


# In[21]:


Result =pd.pivot_table(data= rw, index = ['AGENTS NAME'], columns = ['CreatedOn'],values = 'Gross Revenue', aggfunc = np.sum, fill_value=0)
Result.head()


# In[22]:


Result = (Result.stack()[Result.stack() >= 75000]).unstack()
Result = Result.fillna(0)
#Result['Above 75000'] = 250
#Result['Above 1 Lac'] = 500
Result


# In[23]:


Result = Result.reindex(sorted(Result.columns), axis=1)
Result


# In[24]:


Result.columns


# In[25]:


Result.to_excel(r"C:\Users\3363\Desktop\Akshay\Incetive Data.xlsx")


# In[ ]:




