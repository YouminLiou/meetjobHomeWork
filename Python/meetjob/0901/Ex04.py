# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 21:39:51 2022

@author: user
"""

# jQuery => for(i=1 ; i<= 10 ; i++)

# python 是使用 range 的方式 範圍
# range(10)  => 0,1,2,3,4,5,6,7,8,9
# range(2,10)  => 2,3,4,5,6,7,8,9
# range(3,10,2) => 3,5,7,9

# range(初始值,終止值,間隔值)

for i in range(10): # 依序把值 指派給 i
    print(i)

print()

for i in range(1,10,2):
    print(i)

print()

for i in range(10,1,-2): # 當初始值 大於 終止值 ，間隔值一定要寫，並要是減的 
    print(i)
    
print()


for i in range(1,20,4):
    print(i)

print()    

print("-" * 30)

# 巢狀迴圈

for i in range(5):
    print("i=",i)
    for x in range(3):
        print("x=",x)
        
print()





