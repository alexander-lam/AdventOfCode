# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 22:41:59 2021

@author: alexa
"""

from statistics import median, mean

# Timer
import time
start = time.time()

# Instantiate vars
fuel1 = 0
fuel2 = 0

# Read input file
input = open('input1.txt', 'r').read().split(',')

# Convert input list to int list
for i in range(len(input)):
	input[i] = int(input[i])

# Calculate median and find distance of each input to median
med = median(input)

for element in input:
	fuel1 += int(abs(element - med))

# Calculate mean and find sum of geometric sum of n+1 from start to mean
avg = int(mean(input))

for element in input:
	for i in range(1, int(abs(element - avg)) + 1):
		fuel2 += i

print(fuel1)
print(fuel2)

# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')