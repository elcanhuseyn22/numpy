#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


np.ones(5)


# In[3]:


np.zeros(5)


# In[4]:


arr = np.arange(1,100)


# In[9]:


arr[arr%2==0]


# In[13]:


np.ones(5)*10


# In[14]:


np.zeros(5)+10


# In[15]:


arr = np.arange(1,17)


# In[18]:


arr


# In[22]:


arr.reshape(4,4)


# In[25]:


newArr = np.eye(4,4)


# In[26]:


newArr


# In[48]:


np.random.rand()


# In[49]:


np.random.randn()


# In[54]:


np.random.randn()


# In[59]:


np.random.randn(25).reshape(5,5)


# In[60]:


np.linspace(1,5,20)


# In[61]:


arr = np.arange(1,101).reshape(10,10)


# In[62]:


arr


# In[65]:


arr = np.arange(41,101).reshape(6,10)


# In[66]:


arr


# In[71]:


arr[4:]


# In[72]:


arr


# In[73]:


arr = np.arange(1,101).reshape(10,10)


# In[75]:


arr


# In[74]:


arr[4:]


# In[76]:


arr[6:,4:]


# In[77]:


arr


# In[78]:


arr[:3,2:4]


# In[79]:


arr[:4,3:6]


# In[80]:


arr[:3,1]


# In[88]:


arr[:,9]


# In[82]:


arr


# In[89]:


arr1 = ((np.random.rand(9) * 5).astype(int)).reshape(3,3)
arr2 = ((np.random.rand(9) * 5).astype(int)).reshape(3,3)


# In[90]:


arr1+arr2


# In[91]:


arr1


# In[93]:


arr2


# In[94]:


arr1.mean()


# In[95]:


arr1.sum()

