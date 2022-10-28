# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 21:12:34 2022

@author: user
"""

# 在 python 中，是利用縮排的方式來決定程式區段
# 空白  跟 tab 出來的空白是不一樣的。
# 建議用 tab 來做空白
# spyder 的 IDE  它會將 空白和 tab 視為一樣內容

money = 20000

if( money >= 20000):
    print("零用錢好多喔")
    print("是否要存起來一些？")

print("程式執行完畢")

print()

age = 16

if(age >= 18): # 條件成立時
    print("限制級")
else: # 條件不成立時
    print("輔導級、保護級、普遍級")

print("程式執行完畢2")
print()

#甜度
sweetness = 4

if(sweetness >= 10 ):
    print("全糖，非常甜")
elif(sweetness >= 7):
    print("七分甜")
elif(sweetness >= 5):
    print("五分甜")
elif(sweetness >= 3):
    print("微微")
elif(sweetness >= 1):
    print("少少少少甜")
else:
    print("無糖!!!!")

print("程式執行完畢3")

print()

result = "Y"
price = 200

if(result == "Y"):
    print("歡迎光臨!!  聯成餐廳")
    
    if(price >= 300):
        print("可以點豪華套餐")
    elif(price >= 200):
        print("可以點主廚套餐")
    elif(price >= 100):
        print("可以點商業套餐")
    else:
        print("可以考慮小麵包")

else:
    print("請換下一家!!")

print("程式執行完畢4")



