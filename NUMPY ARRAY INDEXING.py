#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


arr = np.arange(1,10)


# In[4]:


arr


# In[5]:


np.arange(1,10,3)


# In[6]:


arr[1:5]


# In[7]:


arr[:4]


# In[8]:


arr[1::3]


# In[9]:


arr[::-1]


# In[10]:


arr


# In[11]:


arr[:3] = 25


# In[12]:


arr


# In[17]:


arr = np.arange(1,10)


# In[18]:


arr


# In[19]:


arr2 = arr


# In[20]:


arr2


# In[21]:


arr2[:3] = 100


# In[22]:


arr2


# In[23]:


arr


# In[25]:


arr = np.arange(1,10)


# In[26]:


arr


# In[27]:


arr2 = arr.copy()


# In[28]:


arr2


# In[29]:


arr2[:3] = 100


# In[30]:


arr2


# In[31]:


arr


# In[34]:


newArray = np.arange(1,21)


# In[35]:


newArray


# In[38]:


newArray.reshape(5,4)


# In[41]:


newArray = newArray.reshape(5,4)


# In[42]:


newArray


# In[43]:


newArray[0,0]


# In[44]:


newArray[:,:2]


# In[45]:


newArray[:3,:3]


# In[58]:


newArray[:2,:]


# In[59]:


arr = np.arange(1,10)


# In[60]:


arr


# In[61]:


arr>3


# In[64]:


booleanArray = arr>3


# In[65]:


booleanArray


# In[66]:


arr[booleanArray]


# In[67]:


arr[arr>5]

