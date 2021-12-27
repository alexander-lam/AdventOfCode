# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 23:21:29 2021

@author: alexa
"""

# Timer
import time
start = time.time()

# Read input file
input = open('input1.txt', 'r').read().split(',')

cycle = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
days = 256

for element in input:
	cycle[int(element)] += 1

for i in range(days):
	newCycle = {}
	for j in range(8):
		newCycle[j] = cycle[j+1]
	newCycle[6] += cycle[0]
	newCycle[8] = cycle[0]
	cycle = newCycle

print(sum(cycle.values()))

# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')