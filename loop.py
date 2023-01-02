#!/usr/bin/env python
# coding: utf-8

# In[12]:


n=int(input('n='))
a=n
rev=0
while n>0:
    rev=rev*10+(n%10)
    n=n//10
if a==rev:
    print('palindrome')
else:
    print('not palindrome')
    


# In[10]:


125//10


# In[16]:


n=int(input('n='))
temp=n
cnt=0
while n>0:
    cnt=cnt+1
    n=n//10
sum=0
n=temp
while n>0:
    rem=n%10
    sum=sum+pow(rem,cnt)
    n=n//10
if temp==sum:
    print('armstrong number')
else:
    print('not armstrong number')


# In[29]:


list=[]
for i in range(1,51):
    list.append(i)
    desc=sorted(list,reverse=True)
print(desc)


# In[30]:


list=[]
for i in range(1,51):
    list.append(i)
    desc=sorted(list)
print(desc)


# In[31]:


for i in range(1,51,2):
    print(i)


# In[4]:


n=int(input('n='))
temp=n
fact=1
while n!=1:
    fact=fact*n
    n=n-1
    
print(temp,'factorial is',fact)    


# In[6]:


n=int(input('n='))
for i in range(1,11):
    print(i,'*',n,'=',i*n)


# In[9]:


1545555574%10


# In[4]:


n=int(input('n='))
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print(sum)    
    


# In[8]:


n=int(input('n='))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)    
    


# In[11]:


n=int(input('n='))
a=0
b=1
print(a)
print(b)
for i in range(0,n):
    c=a+b
    print(c)
    a=b
    b=c


# In[8]:


num=int(input('num='))
for i in range(2,num):
    if num%i==0:
        print('not prime')
        break
else:
    print('prime number')


# In[12]:


n=int(input('n='))
temp=n
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if temp==sum:
    print('perfect number')
else:
    print('not perfect number')


# In[ ]:




