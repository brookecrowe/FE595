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
yt = np.tan(x) #GG: create array of tan


# In[15]:


#plot cos and sin
get_ipython().run_line_magic('matplotlib', 'inline')

#plot cos(x)
plt.plot(x,yc)
#plot sin(x)
plt.plot(x,ys)
#GG: plot tan(x)
plt.plot(x,yt)
#add legend #GG: Added Tan to legend
plt.legend(('Cosine','Sine','Tan'))
#GG: add y-axis display limits
plt.ylim((-10,10))
#display plot
plt.show()

