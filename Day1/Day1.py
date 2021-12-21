# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 09:29:23 2021

@author: alam
"""

input = open('input1.txt', 'r').read().splitlines()

#input = [199,200,208,210,200,207,240,269,260,263]
counter1 = 0
counter2 = 0

for i in range(len(input) - 1):
    if int(input[i]) < int(input[i+1]):
        counter1 += 1
        
for i in range(len(input) - 3):
    if int(input[i])+int(input[i+1])+int(input[i+2]) < int(input[i+1])+int(input[i+2])+int(input[i+3]):
        counter2 += 1
        

print(counter1)
print(counter2)