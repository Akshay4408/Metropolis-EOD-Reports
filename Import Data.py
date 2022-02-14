#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np


# In[22]:


rw = pd.read_excel(r"C:\Users\3363\Desktop\Reports\Book2.xlsx")


# In[23]:


rw.head()


# In[24]:


rw.columns


# In[25]:


rw['Company Name'] = "PADDLEPOINT"


# In[26]:


rw = rw[['APPOINTMENT DATE', 'Company Name','CAMPAIGN', 'PATIENT NAME', 'CONTACT NUMBER', 'CREATED DATE', 'ADVISOR NAME']]

rw = rw.rename(columns={'APPOINTMENT DATE' : 'Application Date', 'CAMPAIGN': 'Campaign', 'PATIENT NAME': 'Name', 'CONTACT NUMBER': 'Contact no', 'CREATED DATE': 'Created On', 'ADVISOR NAME': 'Agent Name'})


# In[27]:


rw['Created On'] = pd.to_datetime(rw['Created On'], errors='coerce')
rw['Created On'] = rw['Created On'].dt.strftime('%m/%d/%Y')

rw['Application Date'] = pd.to_datetime(rw['Application Date'], errors='coerce')
rw['Application Date'] = rw['Application Date'].dt.strftime('%m/%d/%Y')
#rw['Application Date'] = rw['Application Date'].dt.strftime('%m/%d/%Y')


# In[28]:


rw.head()


# In[29]:


#rw['Contact no Length'] = rw['Contact no'].astype(str).str.len()


# In[30]:


rw.to_excel(r"C:\Users\3363\Desktop\Akshay\Import Data.xlsx", index = False)


# In[ ]:




