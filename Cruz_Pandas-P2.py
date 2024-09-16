#!/usr/bin/env python
# coding: utf-8

# # **Python Experiment 3**

# ***  
# Name: **Cruz, Kathryn Angel S.**  
# Section: **2ECE-A**  
# ***

# In[1]:


import numpy as np
import pandas as pd


# ## PROBLEM 2  
# 
# Using the dataframe cars in Problem 1, extract the following information using subsetting, slicing, and indexing operations.  
# - Display the first five rows with odd-numbered columns (columns 1,3,5,7,...) of cars. 
# - Display the row that contains the ‘Model’ of ‘Mazda RX4’.
# - How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
# - Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 
# Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ hav02X
# 

# In[10]:


# Displaying the first five rows with odd-numbered columns of cars by using .iloc
cars.iloc[0:5,::2]


# In[12]:


# Displaying the row containing the Mazda RX4 Model by using .loc to locate 'Mazda RX4' from the 'Model'
cars.loc[cars["Model"] == "Mazda RX4"]


# In[14]:


# Displaying the number of cylinders ('cyl') of the car model ‘Camaro Z28’
cars.loc[(cars['Model'] == 'Camaro Z28'), ['Model','cyl']]


# In[16]:


# Displaying the amount of cylinders ('cyl') and gear type ('gear') of the car models 'Mazda RX4 Wag', 'Ford Pantera L’ and ‘Honda Civic’ 
cars.loc[(cars['Model'] == 'Mazda RX4 Wag') |
          (cars['Model'] == 'Ford Pantera L') | 
          (cars['Model'] == 'Honda Civic'), ['Model', 'cyl', 'gear']]

