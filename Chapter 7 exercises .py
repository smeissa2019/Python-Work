#!/usr/bin/env python
# coding: utf-8

# In[1]:


to_f(27)


# In[2]:


def to_f(c):
 return ((9/5) * c) + 32


# In[3]:


to_f(27)


# In[4]:


def to_c(f):
    return ((5/9)* (f- 32))


# In[5]:


# In[6]:


to_c(80)


# In[7]:


to_f(to_c(25))


# In[8]:

# In[9]:


def to_f(c):
    if c < -273.15:
    raise ValueError("Temperature value is below absolute zero.")
    return ((9/5) * c) + 32


# In[10]:


def to_f(c):
    if c < -273.15:
        raise ValueError("Temperature value is below absolute zero.")
    return ((9/5) * c) + 32


# In[11]:
def to_f(c):
    if c < -273.15:
        raise ValueError("Temperature value is below absolute zero.")
    return ((9/5) * c) + 32

to_f(-3)


# In[12]:


to_f(-303)


# In[13]:


def sign(num):
    answer='?'
    if num > 0:
        answer='+'
        if num <0:
            answer='-'
            if num == 0:
                answer= ''
            return answer


# In[15]:


sign(5)


# In[16]:


sign(1)


# In[18]:


def sign(num):
    answer='?'
    if num >0:
        answer ='+'
         elif num <0:
            answer ='-'
            else:
                answer=''
                return answer
            


# In[19]:


def sign(num):
    answer='?'
    if num >0:
        answer ='+'
        elif num <0:
            answer ='-'
            else:
                answer=''
                return answer


# In[20]:


def sign(num):
    answer='?'
    if num >0:
        answer ='+'
        elif num <0:
            answer ='-'
            else:
                answer=''
                return answer


# In[21]:


def sign(num):
    answer='?'
    if num >0:
        answer ='+'
    elif num <0:
        answer ='-'
    else:
        answer=''
        return answer


# In[22]:


sign(6)


# In[29]:


def gender(name):
    if name[-1]=="o":
        return "female"
    if name[-1]== "a":
        return "male"


# In[30]:


gender("Mailo")


# In[ ]:




