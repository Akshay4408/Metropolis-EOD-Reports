#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np


# In[32]:


Report = pd.read_csv(r'C:\Users\3363\Desktop\Metropolicy\Daily Revenue Tracker\Dec.csv')

Report.head()


# In[33]:


Report.info()


# In[34]:


Report['Date'] = pd.to_datetime(Report['CREATED DATE'], errors='coerce')

Report['Date'] = Report['Date'].dt.strftime('%d-%b')

Report.head()


# In[35]:


#Report.to_excel(r"C:\Users\3363\Desktop\Akshay\ddatae.xlsx", index = False)


# In[36]:


Result =pd.pivot_table(data= Report, index = ['AGENTS NAME'],columns= ['Date'],values = 'Gross Revenue', aggfunc = np.sum, fill_value=0, margins = True, margins_name= 'Total')
Result.head()


# In[37]:


Result1 =pd.pivot_table(data= Report, index = [ 'Date'],columns= ['Timings'],values = 'Gross Revenue', aggfunc = np.size, fill_value=0, margins = True, margins_name= 'Total')
Result1['Shift 1%'] = Result1['Total']/ Result1['Shift 1']
Result1['Shift 2%'] = Result1['Total']/ Result1['Shift 2']
Result1['Shift 1%'] = pd.Series(["{0:.2f}%".format(val * 100) for val in Result1['Shift 1%']], index = Result1.index)
Result1['Shift 2%'] = pd.Series(["{0:.2f}%".format(val * 100) for val in Result1['Shift 2%']], index = Result1.index)

Result1


# In[38]:


Result2 =pd.pivot_table(data= Report, index = [ 'Date'],columns= ['Timings', 'Location'],values = 'Gross Revenue', aggfunc = np.sum, fill_value=0, margins = True, margins_name= 'Total')
Result2


# In[39]:


sample1 = Report.loc[(Report['Location']) == "South"]
sample1.head()


Result3 =pd.pivot_table(data= sample1, index = [ 'Date'],columns= ['Location', 'Timings'],values = 'Gross Revenue', aggfunc = np.sum, fill_value=0, margins = True, margins_name= 'Total')


Result3['South1 %'] = Result3[( 'South', 'Shift 1')] / Result3[('Total',        '')]
Result3['South2 %'] = Result3[( 'South', 'Shift 2')] / Result3[('Total',        '')]

Result3['South1 %'] = pd.Series(["{0:.2f}%".format(val * 100) for val in Result3['South1 %']], index = Result3.index)
Result3['South2 %']  = pd.Series(["{0:.2f}%".format(val * 100) for val in Result3['South2 %']] , index = Result3.index)

Result3


# In[40]:


Result3.columns


# In[41]:


sample2 = Report.loc[(Report['Location']) == "West"]
sample2.head()


Result4 =pd.pivot_table(data= sample2, index = [ 'Date'],columns= ['Location', 'Timings'],values = 'Gross Revenue', aggfunc = np.sum, fill_value=0, margins = True, margins_name= 'Total')

Result4['West1 %'] = Result4[( 'West', 'Shift 1')] / Result4[('Total',        '')]
Result4['West2 %'] = Result4[( 'West', 'Shift 2')] / Result4[('Total',        '')]

Result4['West1 %'] = pd.Series(["{0:.2f}%".format(val * 100) for val in Result4['West1 %']], index = Result4.index)
Result4['West2 %']  = pd.Series(["{0:.2f}%".format(val * 100) for val in Result4['West2 %']] , index = Result4.index)

Result4


# In[42]:


Result4.columns


# In[43]:


part1 = pd.merge(Result3, Result4, how = 'outer', on = 'Date')
part1 = part1.rename(columns={'Total_x' : 'South Total', 'Total_y' : 'West Total'})
part1['Total'] = part1['South Total'] + part1['West Total']
#part1['South%'] = (part1[( 'South', 'Shift 1')] / ('South Total',        '')) 

part1.head()


# In[44]:


part1 = part1.iloc[:, [0,1,2,5,6,7,10,3,8,4,9]]
part1


# In[45]:


part1.columns


# In[46]:


#Result4['West %'] = Result4[( 'West', 'Shift 1')] / Result4[('Total',        '')]
#Result4['West %'] = Result4[( 'West', 'Shift 2')] / Result4[('Total',        '')]

#Result4


# In[47]:


Report.columns


# In[48]:


Region =pd.pivot_table(data= Report, index = ['Timings', 'Location'],columns= ['Date'],values = 'Gross Revenue', aggfunc = np.size, fill_value=0, margins = True, margins_name= 'Total')
Region.head()


# In[49]:


Region1 =pd.pivot_table(data= Report, index = ['Timings', 'Location'],columns= ['Date'],values = 'Gross Revenue', aggfunc = np.sum, fill_value=0, margins = True, margins_name= 'Total')
Region1.head()


# In[50]:


Result.head()


# In[51]:


Target = pd.read_excel(r'C:\Users\3363\Desktop\Metropolicy\Daily Revenue Tracker\Target.xlsx')

Target.head()


# In[52]:


Result = pd.merge(Result, Target, how = 'left', on = 'AGENTS NAME')
Result['Achievement'] = Result['Total'] / Result['Target']
Result['Achievement'] = pd.Series(["{0:.2f}%".format(val * 100) for val in Result['Achievement']], index = Result.index)

Result.head()


# In[53]:




writer = pd.ExcelWriter(r"C:\Users\3363\Desktop\Akshay\Daily Revenue Report.xlsx", engine='xlsxwriter')


# In[54]:




Result.to_excel(writer, sheet_name='Agent wise', index=False)
Result1.to_excel(writer, sheet_name='Shift Wise')
part1.to_excel(writer, sheet_name='Shift VS Region')
Region.to_excel(writer, sheet_name='Region Count')
Region1.to_excel(writer, sheet_name='Region Sum')



writer.save()


# In[ ]:





# In[ ]:





# In[ ]:




