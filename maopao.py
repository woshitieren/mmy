#!/usr/bin/env python
#coding:utf-8


li = [13,22,6,99,11]
print li
for m in range(4):
    num1 = li[m]
    num2 = li[m+1]
if num1 > num2:
        temp = li[m]
        li[m] = num2
        li[m+1] = temp
print li
for m in range(3):
    num1 = li[m]
    num2 = li[m+1]
if num1 > num2:
        temp = li[m]
        li[m] = num2
        li[m+1] = temp
print li
for m in range(2):
    num1 = li[m]
    num2 = li[m+1]
if num1 > num2:
        temp = li[m]
        li[m] = num2
        li[m+1] = temp
print li




简化通过for循环#  鎴戦樋閬撳か涓変唤  

#!/usr/bin/env python
#coding:utf-8


li = [13,22,6,99,11]

for n in range(1,len(li)):
#1,2,3,4
for m in range(len(li)-n):  #4,3,2,1
num1 = li[m]
        num2 = li[m+1]
if num1 > num2:
            temp = li[m]
            li[m] = num2
            li[m+1] = temp
print li
