class base:
    def __init__(self):
        self.f=int(input('enter force: '))
        self.s=int(input('enter speed: '))
        self.o=int(input('enter teta: '))
        self.m=int(input('enter mass: '))
        self.v=int(input('enter velocity: '))
        self.g=9.8
        self.h=int(input('enter height: '))
        self.t=int(input('enter time: '))
    def work(self):
        import math
        self.work=self.f*self.s*math.cos(self.o)
        print('work =',self.work)
        return
    def kineticenergy(self):
        self.k=0.5*self.m*self.v**2
        print('kineticenergy =',self.k)
        return
class derived(base):
    def power(self):
        self.p=self.work/self.t
        print('power =',self.p)
        return
    def mechanicalenergy(self):
        self.u=self.m*self.g*self.h
        self.me=self.u+self.k
        print('mechanicalenergy =',self.me)
        return
