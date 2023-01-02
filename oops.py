#!/usr/bin/env python
# coding: utf-8

# In[11]:


class vijay:
    def fname(self):
        self.a='vijay msg'
        self.b='dhoni msg'
class dhoni(vijay):
    def sname(self):
        self.c=self.a+self.b
    def display(self):    
        print(self.c)
obj=dhoni()
obj.fname()
obj.sname()
obj.display()


# In[12]:


class vijay:
    def num(self):
        self.a=int(input('a='))
        self.b=int(input('b='))
class raaj(vijay):
    def add(self):
        self.c=self.a+self.b
    def display(self):
        print(self.c)
obj=raaj()
obj.num()
obj.add()
obj.display()


# In[13]:


class russia:
    def num(self):
        self.a=int(input('a='))
class usa:
    def qum(self):
        self.b=int(input('b='))
class ukraine(russia,usa):
    def sum(self):
        self.c=self.a-self.b
    def display(self):
        print(self.c)
obj=ukraine()
obj.num()
obj.qum()
obj.sum()
obj.display()


# In[16]:


class russia:
    def name(self):
        self.a='friend '
class usa(russia):
    def sname(self):
        self.b='of '
class ukraine(usa):
    def fname(self):
        self.c='nature'
    def display(self):
        print(self.a,self.b,self.c)
obj=ukraine()
obj.name()
obj.sname()
obj.fname()
obj.display()


# In[22]:


class vijay:
    def pi(self):
        self.pi=3.14
class raaj(vijay):
    def rrr(self):
        self.r1=int(input('r1='))
    def aoc(self):
        self.area=self.pi*(self.r1)**2
    def display(self):
        print(self.area)
class raam(vijay):
    def radius(self):
        self.r2=int(input('r2='))
    def ac(self):
        self.area=self.pi*(self.r2)**2
    def dsplay(self):
        print(self.area)
class ravi(vijay):
    def rav(self):
        self.r3=int(input('r3='))
    def ao(self):
        self.area=self.pi*(self.r3)**2
    def diplay(self):
        print(self.area)    
obj1=raaj()
obj1.pi()
obj1.rrr()
obj1.aoc()
obj1.display()
obj2=raam()
obj2.pi()
obj2.radius()
obj2.ac()
obj2.dsplay()
obj3=ravi()
obj3.pi()
obj3.rav()
obj3.ao()
obj3.diplay()


# In[32]:


import datetime
date.today().day


# In[34]:


import datetime
birth_day=int(input('birth_day:'))
birth_month=int(input('month :'))
birth_year=int(input('year :'))
curr_date=date.today().day
curr_month=date.today().month
curr_year=date.today().year
age_day=curr_date-birth_day
age_month=curr_month-birth_month
age_year=curr_year-birth_year
print('your age is',age_year)


# In[36]:


import datetime
class employee:
    def __init__(self):
        self.name=str(input('enter name'))
        self.birthyear=int(input('enter birth year'))
        self.curyear=date.today().year-self.birthyear
class age(employee):        
    def age(self):
        print(self.name,'is',self.curyear,'years old')
obj=age()
obj.age()


# In[ ]:




