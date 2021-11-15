#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

#img = np.random.randint(0, 255, (256, 256, 3)) #enter your picture as an array

def imshow(X, resize=None):
    img = Image.fromarray(np.uint8(X))
    img = img.resize(resize)
    return img
    
#imshow(img, resize=(20,50)) #use imshow(arrayYouWannaResize, resize=(width, height))
    #"""
    #You should create a way to resize an image from an array X. 
    #The use of widgets is optional but you can take a look to interact.
    #We should be able to install this pack
pass

# In[ ]:





# In[ ]:





# In[ ]:




