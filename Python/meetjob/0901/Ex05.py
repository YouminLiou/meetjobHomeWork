# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 21:52:35 2022

@author: user
"""

# while(判斷式)  有成立才進來執行


i = 1

while(i <10):
    print(i)
    print("------------")
    i += 1 # 若沒有讓 i 變大 ，這個迴圈會無止盡的執行
    
print("程式執行完畢")

# 迴圈可以使用：break  立即跳脫「此」迴圈

x = 2

while (x < 20):
    if(x % 6 == 0):
        break
    print(x)
    x += 1
    
print("程式執行完畢2")
    
a = 1

while(a < 10):
    print("a=",a)
    x = 1
    while(x < 100):
        if(x == 5):
            break
        print("x=",x)
        x+=1
    print()
    a+=1
    
print("程式執行完畢3")


for i in range(1,10):
    for x in range(1,10,3):
        print(i,"/",x,sep='',end='\t') # \t => tab
    print()



