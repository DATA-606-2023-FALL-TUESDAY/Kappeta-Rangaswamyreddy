#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df1 = pd.read_csv('athlete_events.csv')
df2 = pd.read_csv('noc_regions.csv')


# In[3]:


df1.head()


# In[4]:


df2.head()


# In[5]:


print(df1.shape)
print(df2.shape)


# In[7]:


df = df1.merge(df2, on = 'NOC', how = 'left')
df.head()


# In[8]:


df.info()


# In[9]:


df.describe()


# In[10]:


df.isnull().sum()


# In[15]:


df.dtypes


# In[ ]:




