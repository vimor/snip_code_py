#encoding=utf-8
'''
Created on 2012-4-3

@author: zack
'''
class Foo:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.callbacks = []
        
    def hook(self, callback):
        self.callbacks.append(callback)
        
    def doCalculation(self):
        for c in self.callbacks:
            c(self.p1, self.p2)
            
            
def plus(num1, num2):
    print u'加法=%d' %(num1 + num2,)
    
def minus(num1, num2):
    print u'减法=%d' %(num1 - num2, )
    
def multiply(num1, num2):
    print num1 * num2
    
f = Foo(2,3)

f.hook(plus)
f.hook(minus)
f.hook(multiply)

f.doCalculation()