#!/usr/bin/env python
# coding: utf-8

# <div style="color:white;
#            display:fill;
#            border-radius:5px;
#            background-color:yellow;
#            font-size:200%;
#            font-family:Serif;
#            letter-spacing:0.5px">
# 
# <p style="padding: 10px;
#           color:black;
#           font-size:120%;
#           text-align:center;">
# Aggregations
# </p>
# </div>

# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd
import numpy as np


# ### Step 2. Import the dataset occupation.csv from the folder or [here](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). 

# In[2]:


pd.read_csv('Occupation.csv',sep='|')


# ### Step 3. Assign it to a variable called users.

# In[3]:


users=pd.read_csv('Occupation.csv',sep='|')
users


# ### Step 4. Discover what is the mean age per occupation

# In[15]:


users.groupby(['occupation'])['age'].mean().sort_values()


# ### Step 5. Discover the Male ratio per occupation and sort it from the most to the least.
# 
# Use numpy.where() to encode gender column.

# In[16]:


a=users.groupby(['gender'])['occupation'].value_counts().sort_values()
a['M']


# In[6]:


z=users[users['gender']=='M']
z['occupation'].value_counts()


# ### Step 6. For each occupation, calculate the minimum and maximum ages

# In[7]:


users.groupby(['occupation'])['age'].agg(['min','max']).sort_values(by='min',ascending=True)


# ### Step 7. For each combination of occupation and gender, calculate the mean age

# In[8]:


users.groupby(['occupation','gender'])['age'].mean().sort_values(ascending=True)


# ### Step 8.  For each occupation present the percentage of women and men

# In[9]:


users['gender'].value_counts(normalize=True)*100


# In[10]:


users.groupby(['occupation'])['gender'].value_counts(normalize=True)*100

