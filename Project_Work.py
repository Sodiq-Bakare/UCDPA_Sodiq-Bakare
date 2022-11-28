#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


import pandas as pd


# In[114]:


import matplotlib.pyplot as plt


# In[115]:


import seaborn as sns


# In[ ]:





# In[ ]:


#Importing dataset


# In[6]:


housing_data = pd.read_csv('/Users/Sonic_Baker/Downloads/housing_dataset.csv')


# In[ ]:





# In[ ]:


#Getting the first 5 rows of my dataset


# In[8]:


housing_data.head()


# In[87]:




#Prepartion of Data
# In[ ]:


#Checking for Null values in my dataset


# In[9]:


pd.isnull(housing_data).sum()


# In[ ]:





# In[ ]:


#Getting information about my dataset


# In[10]:


housing_data.info()


# In[ ]:





# In[ ]:


#After getting the information on my dataset, I only needed certain columns. I sliced the dataset set down to the neccesary column i needed.


# In[11]:


df_data = housing_data[['Neighborhood', 'HouseStyle', 'YearBuilt', 'BedroomAbvGr', 'GarageCars', 'Fireplaces', 'YrSold', 'SalePrice', 'MoSold']].copy()


# In[12]:


df_data.head()


# In[ ]:





# In[ ]:


#Description of new dataset


# In[13]:


df_data.describe().transpose()


# In[ ]:





# In[ ]:


#Sorting updated dataset by the most expensive sale price


# In[14]:


sorted_most_expensive = df_data.sort_values('SalePrice', ascending = False)


# In[15]:


sorted_most_expensive.head(10)


# In[ ]:





# In[ ]:


#Sorting updated dataset by the least expensive sale price


# In[16]:


sorted_least_expensive = df_data.sort_values('SalePrice', ascending = True)


# In[17]:


sorted_least_expensive.head(10)


# In[ ]:





# In[ ]:


#Sorting updated dataset by year built


# In[18]:


df_data = df_data.sort_values('YearBuilt', ascending = True)


# In[19]:


df_data.head()


# In[ ]:





# In[ ]:


#Setting the year built as index


# In[20]:


df_data.set_index('YearBuilt', inplace=True)


# In[21]:


df_data.head()


# In[ ]:





# In[ ]:


#Renamed some columns for better understanding


# In[22]:


df_data.rename(columns={'BedroomAbvGr': 'No._of_Bedroom', 'MoSold': 'Month_Sold'}, inplace=True)


# In[23]:


df_data.head()


# In[ ]:





# In[ ]:


#Change the month numbers to month letters for better understanding


# In[26]:


df_data['Month_Sold'] = pd.to_datetime(df_data['Month_Sold'], format='%m').dt.month_name().str.slice(stop=3)


# In[27]:


df_data.head()


# In[ ]:





# #Analysis

# In[ ]:


#grouping my dataset by year sold and month sold to know how many houses were sold in what year and month


# In[30]:


df_data.groupby(["YrSold", "Month_Sold"])["SalePrice"].count()


# In[ ]:





# In[ ]:


#Checking to see if there's any duplicates in my updated data set 


# In[155]:


df_data.duplicated(subset = 'Neighborhood', keep = 'first')


# In[ ]:





# In[ ]:


#Attempting to create a custom function 


# In[64]:


def value_per_room ():
    print(df_data['SalePrice'] / df_data['No._of_Bedroom'])


# In[63]:


print(value_per_room)


# In[ ]:





# In[ ]:


#Below are some numpy functions to get the total sum of house price over the period covered in my data set, also got the mean, maximum and mimimum sale price in my updated dataset


# In[65]:


np.sum(df_data['SalePrice'])


# In[66]:


np.mean(df_data['SalePrice'])


# In[67]:


np.max(df_data['SalePrice'])


# In[68]:


np.min(df_data['SalePrice'])


# In[ ]:





# In[ ]:


#Using the 'Where' loop to get the total sale price of houses sold in 'Oldtown' neighborhood


# In[85]:


np.where(df_data['Neighborhood']=='OldTown', df_data['SalePrice'],0).sum()
    


# In[90]:


df_data_numpy = df_data.to_numpy()


# In[92]:


print(df_data_numpy)


# In[ ]:





# In[121]:


x = df_data['Neighborhood']


# In[122]:


y = df_data['SalePrice']


# In[135]:


sns.displot(df_data['SalePrice'], bins=50);


# In[137]:


sns.displot(df_data['Month_Sold'], bins=50);


# In[ ]:





# In[145]:


df_data['SalePrice'].hist(bins=100)


# In[147]:


df_data.plot.scatter(x='Month_Sold',y='SalePrice')


# In[148]:


df_data.columns


# In[149]:


df_data.plot.scatter(x='GarageCars',y='SalePrice')


# In[150]:


df_data.plot.scatter(x='No._of_Bedroom',y='SalePrice')


# In[151]:


df_data.plot.scatter(x='HouseStyle',y='SalePrice')


# In[152]:


df_data.plot.scatter(x='Fireplaces',y='SalePrice')


# In[ ]:




