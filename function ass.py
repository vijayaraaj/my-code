#!/usr/bin/env python
# coding: utf-8

# In[21]:


def vijay(a):
    for i in range(2,a):
        if a%i==0:
            s='TRUE'
            return s
            break
        
        else:
            d='FALSE'
            return d
x=int(input('x='))        
p=vijay(x)
print(p)


# In[27]:


a=int(input('a='))
fac=1
while a>0:
    fac=fac*a
    a-=1
print(fac)    


# In[28]:


def vijay(a):
    fac=1
    while a>0:
        fac=fac*a
        a-=1
    return fac
x=int(input('a='))
print(vijay(x))


# In[33]:


def vijay(a):
        if a%2==0:
            s='TRUE'
            return s
            
        
        else:
            d='FALSE'
            return d
x=int(input('x='))        
p=vijay(x)
print(p)


# In[40]:


def vijay():
    a=[2,45,87,7,74,12,75,44,22]
    b=[]
    for i in a:
        if i%2==0:
            b.append(i)
 
    return (b)
print(vijay())        


# In[ ]:




