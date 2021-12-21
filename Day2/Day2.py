# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:07:18 2021

@author: alam
"""

input = open('input1.txt', 'r').read().splitlines()

forward1 = 0
depth1 = 0
forward2 = 0
depth2 = 0
aim2 = 0

for line in input:
    distance = int(line[-1])
    if line[0] == 'f':
        forward1 += distance
    elif line[0] == 'd':
        depth1 += distance
    elif line[0] == 'u':
        depth1 -= distance
        
for line in input:
    distance = int(line[-1])
    if line[0] == 'f':
        forward2 += distance
        depth2 += aim2 * distance
    elif line[0] == 'd':
        aim2 += distance
    elif line[0] == 'u':
        aim2 -= distance

print(forward1*depth1)
print(forward2*depth2)
        