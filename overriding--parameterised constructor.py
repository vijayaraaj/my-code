#!/usr/bin/env python
# coding: utf-8

# In[3]:


class murugan:
    def fname(self):
        super().fname()
        print('murugan msg')
class sumathi:
    def fname(self):
        super().fname()
        print('sumathi msg')
class deekshanya:
    def fname(self):
        print('deek msg')
class vijay(murugan,sumathi,deekshanya):
    def fname(self):
        super().fname()
        print('vijay msg')
obj=vijay()
obj.fname()


# In[39]:


class A:
    def __init__(self,a):
        self.a=a
class B:
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b
class C(B,A):
    def __init__(self,a,b,c):
        super().__init__(b,a)
        self.c=c
    def display(self):
        self.add=self.a+self.b+self.c
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.add)
obj=C(20,10,30)
obj.display()
        


# In[20]:


class A:
    def __init__(self,a):
        self.a=a
class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b

    def display(self):
        self.c=self.a+self.b
        print(self.a)
        print(self.b)
        print(self.c)
obj=B(20,10) 
obj.display()
        


# In[40]:


class A:
    def __init__(self,a):
        self.a=a
class B:
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b
class C(B,A):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
    def display(self):
        self.add=self.a+self.b+self.c
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.add)
obj=C(10,20,30)
obj.display()
        


# In[ ]:




