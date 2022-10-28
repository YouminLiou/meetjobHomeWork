# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 21:02:25 2022

@author: user
"""

age = 33

print(age + 2)
print(age - 3)

print(age * 5)
print(age / 2) # / 會算到小數
print(age // 2)  # // 會算到整數。表示會將小數捨去，取：商數

print(age % 5) # % 取餘數 33 / 5 看餘多少  => 3

print("-" * 40)

# 值+ 1   在 python 中 沒有 ++  --

age += 1 #  age = age + 1
print(age)

age += 3 #  age = age + 3
print(age)

#程式中， = 指派 ，將右邊的值指派到左邊
#右邊一定要先計算完成後，才可以將值 指派給左邊的變數

age -= 6 #  age = age - 6
print(age)

age *= 3 #  age = age * 3
print(age)
