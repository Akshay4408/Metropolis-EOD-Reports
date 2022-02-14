#!/usr/bin/env python
# coding: utf-8

# In[52]:



import pandas as pd
import numpy as np


# In[53]:


rw = pd.read_excel(r"C:\Users\3363\Desktop\Metropolicy\Database\Dec.xlsx")
rw.head()


# In[54]:


rw['Date'] = pd.to_datetime(rw['call_date']).dt.date
rw['Time'] = pd.to_datetime(rw['call_date']).dt.time


# In[55]:


rw.head()


# In[56]:


rw['Date'] = pd.to_datetime(rw['Date'], errors='coerce')

rw['Date'] = rw['Date'].dt.strftime('%d-%b')


# In[57]:


rw.head()


# In[58]:


def test(x):
    if x == "METRO":
        return "West"
    else:
        return "South"


# In[59]:


rw['Zone'] = rw['campaign_id'].apply(lambda x: test(x))


# In[60]:


#rw['Date'] = pd.to_datetime(rw['Date'], errors='coerce')
#rw['Date'] = rw['Date'].dt.strftime('%m/%d/%Y')


# In[61]:


rw.head()


# In[62]:


Result =pd.pivot_table(data= rw, index = ['Dispositions'], columns = ['Date', 'Zone'],values = 'status_name', aggfunc = np.size, fill_value=0, margins = True, margins_name= 'Total')


# In[63]:


Result


# In[64]:


Result1 =pd.pivot_table(data= rw, index = ['Dispositions'], columns = ['full_name'],values = 'status_name', aggfunc = np.size, fill_value=0, margins = True, margins_name= 'Total')


# In[65]:


Result2 =pd.pivot_table(data= rw, index = ['Dispositions'], columns = ['Date', 'Zone'],values = 'status_name', aggfunc = np.size, fill_value=0, margins = True, margins_name= 'Total')
Result2.head()


# In[66]:


Result3 =pd.pivot_table(data= rw, index = ['Dispositions'], columns = ['Zone'],values = 'status_name', aggfunc = np.size, fill_value=0, margins = True, margins_name= 'Total')
Result3['South %'] = Result3['South'] / 21553
Result3['West %'] = Result3['West'] /12444
Result3 = Result3.rename(columns={'Total' : 'Region'})


Result3['Region %'] = Result3['Region'] / 33997

Result3['South %'] = pd.Series(["{0:.2f}%".format(val * 100) for val in Result3['South %']], index = Result3.index)
Result3['West %'] = pd.Series(["{0:.2f}%".format(val * 100) for val in Result3['West %']], index = Result3.index)
Result3['Region %'] = pd.Series(["{0:.2f}%".format(val * 100) for val in Result3['Region %']], index = Result3.index)

Result3 = Result3[['South', 'West', 'South %', 'West %', 'Region', 'Region %']]
Result3


# In[67]:




writer = pd.ExcelWriter(r"C:\Users\3363\Desktop\Akshay\Database Report.xlsx", engine='xlsxwriter')


# In[68]:




Result.to_excel(writer, sheet_name='Datewise Dispositions')
Result1.to_excel(writer, sheet_name='Agent wise')
Result3.to_excel(writer, sheet_name='Zone wise')



writer.save()


# In[ ]:




