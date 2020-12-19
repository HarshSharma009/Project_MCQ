# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 13:04:54 2020

@author: abcd
"""

class login:
    def __init__(self,user,password):
        f=open('user_details.txt','r')
        self.flag=False
        for i in f.readlines():
            print(i)
            self.user1,self.password1=i.strip().split(',')
            if self.user1==user:
                if self.password1==password:
                    self.flag=True
                    self.s='Login Successful'
                    break
                else:
                    self.s='Password Invalid!'
                    break
            else:
                self.s='User doesn\'t exit'
        f.close()
    def add_user(self,user,password):
        f=open('user_details.txt','a+')
        f.write('\n'+user+','+password)
        f.close()
        
    
    def check(self):
        return self.flag
    
    def __str__(self):
        return self.s