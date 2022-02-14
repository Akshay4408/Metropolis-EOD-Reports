#!/usr/bin/env python
# coding: utf-8

# In[80]:



import pandas as pd
import numpy as np


# In[81]:


rw = pd.read_excel(r"C:\Users\3363\Desktop\Reports\Jitesh.xlsx")
rw.head()


# In[82]:


#rw['call_date'] = pd.to_datetime(rw['call_date'], errors='coerce')
#rw['call_date'] = rw['call_date'].dt.strftime('%m/%d/%Y')

#rw['Application Date'] = pd.to_datetime(rw['Application Date'], errors='coerce')
#rw['Application Date'] = rw['Application Date'].dt.strftime('%m/%d/%Y')
#rw['Application Date'] = rw['Application Date'].dt.strftime('%m/%d/%Y')


# In[83]:


rw['Date'] = pd.to_datetime(rw['call_date']).dt.date
rw['Time'] = pd.to_datetime(rw['call_date']).dt.time

#rw.drop('call_date',
#  axis='columns', inplace=True)

rw.head()


# In[84]:


rw['datehour'] = rw['call_date'].dt.hour


# In[85]:


import datetime


# In[86]:


rw['Date'] = rw['call_date'].dt.strftime('%d %b')


# In[87]:


def test(x):
    if x == 7:
        return "7 AM - 8 AM"
    if x == 8:
        return "8 AM - 9 AM"
    if x == 9:
        return "9 AM - 10 AM"
    if x == 10:
        return "10 AM - 11 AM"
    if x == 11:
        return "11 AM - 12 PM"
    if x == 12:
        return "12 PM - 1 PM"
    if x == 13:
        return "1 PM - 2 PM"
    if x == 14:
        return "2 PM - 3 PM"
    if x == 15:
        return "3 PM - 4 PM"
    if x == 16:
        return "4 PM - 5 PM"
    if x == 17:
        return "5 PM - 6 PM"
    if x == 18:
        return "6 PM - 7 PM"
    if x == 19:
        return "7 PM - 8 PM"
    if x == 20:
        return "8 PM - 9 PM"
    else:
        return "Time exceeds"
    


# In[88]:


rw['Hours'] = rw['datehour'].apply(lambda x: test(x))


# In[89]:


rw = rw[rw.Hours != "Time exceeds"]


# In[90]:


Result =pd.pivot_table(data= rw, index = ['Hours'],columns= ['Date'],values = 'call_date', aggfunc = np.size, fill_value=0, margins = True, margins_name= 'Total')
Result.head()


# In[91]:


Time = pd.read_excel(r"C:\Users\3363\Desktop\Reports\Time table.xlsx")
Time.head()


# In[92]:


Report = pd.merge(Result, Time, how='left',
        left_on='Hours', right_on='Hours')


Report = Report.sort_values(by=['Num'])

Report.drop('Num',
  axis='columns', inplace=True)


Report


# In[93]:


Report.to_excel(r"C:\Users\3363\Desktop\Akshay\Jitesh Data.xlsx")


# In[ ]:




