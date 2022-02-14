#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np


# In[2]:


Agent = pd.read_excel(r"C:\Users\3363\Desktop\Metropolicy\Target VS Achievement Report\Agent List.xlsx")
Agent.head()


# In[3]:


Sale = pd.read_excel(r"C:\Users\3363\Desktop\Metropolicy\Target VS Achievement Report\Sale File.xlsx")
Sale.head()


# In[4]:


agentsale = pd.DataFrame(Sale.groupby(by="ADVISOR NAME")['GROSS REVENUE'].sum())


# In[5]:


agentsale = pd.merge(Agent ,agentsale, how= 'outer',on = 'ADVISOR NAME')
agentsale['Daily Target%'] = agentsale['GROSS REVENUE'] / agentsale['Daily Target']
agentsale['Daily Target%'] = pd.Series(["{0:.2f}%".format(val * 100) for val in agentsale['Daily Target%']], index = agentsale.index)


agentsale["GROSS REVENUE"].fillna(0, inplace = True)
agentsale["Daily Target%"] = agentsale["Daily Target%"].replace("nan%", "0.0%", regex=True)


# In[6]:


agentsale


# In[7]:


agentsale.to_excel(r"C:\Users\3363\Desktop\Akshay\Target VS Achivement Report.xlsx", index = False)


# In[ ]:




