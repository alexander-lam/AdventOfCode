# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 09:29:23 2021

@author: alam
"""

# Read input from file
input = open('input1.txt', 'r').read().splitlines()

# Instantiate vars
counter1 = 0
counter2 = 0

# Increment counter if next input line is larger than current
for i in range(len(input) - 1):
    if int(input[i]) < int(input[i+1]):
        counter1 += 1
        
# Calculate rolling average over 3 input lines and increment counter if increased
for i in range(len(input) - 3):
    if int(input[i])+int(input[i+1])+int(input[i+2]) < int(input[i+1])+int(input[i+2])+int(input[i+3]):
        counter2 += 1
        
print(counter1)
print(counter2)