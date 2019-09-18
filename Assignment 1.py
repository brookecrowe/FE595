#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Assignment 1

import numpy as np
import matplotlib.pyplot as plt

#create x values
steps = 2*np.pi/360
x = np.arange(0,2*np.pi, step = steps)


# In[5]:


#create y values for cos and sin 
yc = np.cos(x)
ys = np.sin(x)


# In[15]:


#plot cos and sin
get_ipython().run_line_magic('matplotlib', 'inline')

#plot cos(x)
plt.plot(x,yc)
#plot sin(x)
plt.plot(x,ys)
#add legend
plt.legend(('Cosine','Sine'))
#display plot
plt.show()

