#!/usr/bin/env python
# coding: utf-8

# In[2]:


def maximun(a,b,c):
    if a>b:
        if a>c:
            return('a is greater')
        else:
            return('c is greater')
    elif b>c:
        return('b is greater')
    else:
        return('c is greater')
print(maximun(55,100,150))    


# In[8]:


def vijay():
    a=[1,2,3,4,5]
    sum=0
    for i in range(0,len(a)):
        sum=sum+a[i]
    return sum
print(vijay())    


# In[9]:


a='vijay'
b=a[::-1]
b


# In[ ]:





# In[15]:


def vijay(a):
    temp=a
    b=a[::-1]
    if b==temp:
        print('palindrome')
    else:
        print('not palindrome')
x=str(input('a='))        
print(vijay(x))


# In[17]:


def fact(a):
    fac=1
    if a<1:
        return 1
    else:
        return a*fact(a-1)
print(fact(5))    


# In[27]:


def vijay(a):
    upper=0
    lower=0
    for char in a:
        if char.isupper():
            upper+=1
        if char.islower():
            lower+=1
    return('upper case is:',upper,'lower case is:',lower)
x=str(input('a='))
print(vijay(x))


# In[ ]:




