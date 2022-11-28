#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


import json


# In[3]:


response_API = requests.get('https://www.met.ie/Open_Data/json/National.json')


# In[4]:


data = response_API.text


# In[5]:


print(data)


# In[48]:


import pandas as pd


# In[79]:


left = pd.DataFrame(
        {
            "letter1": ["A", "A", "A", "A"],
            "letter2": ["B", "B", "B", "B"],
            "letter1_2": ["AB", "AB", "AB", "AB"],
        }
    )
    
right = pd.DataFrame(
       {
            "letter1": ["A", "A", "A", "A"],
            "letter2": ["B", "B", "B", "B"],
            "letter2_1": ["BA", "BA", "BA", "BA"],
        }
    )
    

result = pd.merge(left, right, on=["letter1", "letter2"])


# In[80]:


print(result)


# In[ ]:




