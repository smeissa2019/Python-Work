#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("This is a string")
print(25)
print(12.5)
print(True)


# In[2]:


a = 5
b = 7
try:
    if(type(b)==type(0)):
        print("Well done.")
    else:
        print("b is not assigned a value of an integer type")
except:
    print("Make sure to initialize b to a value in the session")


# In[3]:


a = 5
b = "Hi"
try:
    if(type(b)==str):
        print("Hello World")
    else:
        print("b is not assigned a value of an integer type")
except:
    print("Make sure to initialize b to a value in the session")


# In[6]:


a = 5
b = 42.0
try:
    if isinstance(b, float):
        print(b)
    else:
        print("b is not assigned a value of an integer type")
except:
    print("Make sure to initialize b to a value in the session")


# In[7]:


a = 5
b = True
try:
    if isinstance(b, bool):
        print(b)
    else:
        print("b is not assigned a value of an integer type")
except:
    print("Make sure to initialize b to a value in the session")


# In[ ]:




