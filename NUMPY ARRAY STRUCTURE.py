#!/usr/bin/env python
# coding: utf-8

# In[2]:


data_list = [1,2,3]


# In[3]:


data_list


# In[4]:


import numpy as np


# In[5]:


arr = np.array(data_list)


# In[6]:


arr


# In[7]:


data__list = [[10,20,30],[40,50,60],[70,80,90]]


# In[8]:


arrr = np.array(data__list)


# In[9]:


arr


# In[10]:


arrr


# In[11]:


arrr[2][2]


# In[12]:


arrr[2,2]


# In[13]:


np.arange(10,21)


# In[14]:


np.zeros(10)


# In[15]:


np.zeros((3,4))


# In[16]:


np.ones((2,2))


# In[17]:


np.linspace(0,100,5)


# In[18]:


np.linspace(0,0,5)


# In[19]:


np.linspace(1,0,3)


# In[20]:


np.linspace(0,1,3)


# In[21]:


np.eye(5)


# In[22]:


np.eye(5,3)


# In[23]:


np.eye(5,5,3)


# In[24]:


np.eye(5,1)


# In[27]:


np.random.randint(0,100)


# In[28]:


np.random.randint(1,11,5)


# In[29]:


np.random.rand(3)


# In[30]:


np.random.randn(3)


# In[33]:


arr = np.arange(25)


# In[34]:


arr


# In[35]:


arr.reshape(5,5)


# In[36]:


newArray = np.random.randint(1,100,10)


# In[38]:


newArray


# In[39]:


newArray.max()


# In[40]:


newArray.sum()


# In[41]:


newArray.mean()


# In[42]:


newArray.argmax()


# In[43]:


newArray.argmin()


# In[45]:


detArray = np.random.randint(1,100,25)


# In[46]:


detArray


# In[47]:


detArray = detArray.reshape(5,5)


# In[48]:


detArray


# In[49]:


np.linalg.det(detArray)


# In[50]:


detArray2 = np.array([[1,2],[3,4]])


# In[51]:


np.linalg.det(detArray2)


# In[52]:


round(np.linalg.det(detArray2))

