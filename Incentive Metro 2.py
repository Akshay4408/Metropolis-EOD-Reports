#!/usr/bin/env python
# coding: utf-8

# In[12]:



import pandas as pd
import numpy as np


# In[13]:


rw = pd.read_excel(r"C:\Users\3363\Desktop\Akshay\Incetive Data.xlsx")
rw.head()


# In[14]:


def test(x):
    if x == 0:
        return 0
    
    if x <= 100000:
        return 1
    else:
        return 2


# In[15]:


rw.columns


# In[16]:


rw['04-Nov'] = rw['04-Nov'].apply(lambda x: test(x))
rw['05-Nov'] = rw['05-Nov'].apply(lambda x: test(x))
rw['06-Nov'] = rw['06-Nov'].apply(lambda x: test(x))


rw['08-Nov'] = rw['08-Nov'].apply(lambda x: test(x))
rw['14-Nov'] = rw['14-Nov'].apply(lambda x: test(x))
rw['17-Nov'] = rw['17-Nov'].apply(lambda x: test(x))
rw['19-Nov'] = rw['19-Nov'].apply(lambda x: test(x))
rw['22-Nov'] = rw['22-Nov'].apply(lambda x: test(x))
rw['24-Nov'] = rw['24-Nov'].apply(lambda x: test(x))
rw['27-Nov'] = rw['27-Nov'].apply(lambda x: test(x))

rw.head()


# In[17]:


rw['04-Nov'].replace({1: 250, 2: 500}, inplace=True)
rw['05-Nov'].replace({1: 250, 2: 500}, inplace=True)
rw['06-Nov'].replace({1: 250, 2: 500}, inplace=True)
rw['08-Nov'].replace({1: 250, 2: 500}, inplace=True)
rw['14-Nov'].replace({1: 250, 2: 500}, inplace=True)
rw['17-Nov'].replace({1: 250, 2: 500}, inplace=True)
rw['19-Nov'].replace({1: 250, 2: 500}, inplace=True)
rw['22-Nov'].replace({1: 250, 2: 500}, inplace=True)
rw['24-Nov'].replace({1: 250, 2: 500}, inplace=True)
rw['27-Nov'].replace({1: 250, 2: 500}, inplace=True)

rw.head()


# In[18]:


rw['Total'] = rw.sum(axis=1) 
rw


# In[19]:


rw.to_excel(r"C:\Users\3363\Desktop\Akshay\Incetive Data.xlsx")

