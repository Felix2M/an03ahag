#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from distutils.core import setup
from setuptools import find_packages
setup(name='an03ahag',
      version='0.1',
      author='DSSS',
      author_email='felix.mutter@fau.de',
      packages=find_packages(),
      install_requires=['numpy', 'Pillow', 'ipywidgets'])

