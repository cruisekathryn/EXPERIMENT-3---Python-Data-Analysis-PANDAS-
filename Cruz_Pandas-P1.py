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


# ## PROBLEM 1
# 
# Using knowledge obtained from the experiment and demonstrations:  
# - Load the corresponding .csv file into a data frame named cars using pandas
# - Display the first five and last five rows of the resulting cars

# In[3]:


# Reading the csv file named 'cars.csv' to be sotred in the variable 'car'
cars = pd.read_csv('cars.csv')
cars


# In[5]:


# Displaying the first five rows of the resulting cars
cars.head()


# In[7]:


# Displaying the last five rows of the resulting cars
cars.tail()

