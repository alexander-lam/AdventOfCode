# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 22:07:18 2021

@author: alam
"""

# Timer
import time
start = time.time()

# Read input file
input = open('input1.txt', 'r').read().splitlines()

# Instantiate vars for pt 1
counter1 = []
gamma = ''
epsilon = ''

# Instantiate vars for pt 2
o2Counter2 = 0
scrubberCounter2 = 0
o2Take = 0
scrubberTake = 0
o2 = input
narrowedO2 = []
scrubber = input
narrowedScrubber = []

# Seed counter bitwise with first diagnostic code
for digit in input[0]:
	counter1.append(int(digit))

# Add each bit from diagnostics to the corresponding counter
for i in range(1, len(input)):
	for j in range(len(input[i])):
		counter1[j] += int(input[i][j])
	
# Figure out values by finding the most common bit value in each counter
for count in counter1:
	if count >= len(input) / 2:
		gamma += '1'
		epsilon += '0'
	else:
		gamma += '0'
		epsilon += '1'
	

for i in range(len(input[0])):
	# Reset vars
	o2Counter2 = 0
	scrubberCounter2 = 0
	o2Take = 0
	scrubberTake = 1
	narrowedO2 = []
	narrowedScrubber = []
	
	# Sum up bits in the o2 and srubber lists
	for j in range(len(o2)):
		o2Counter2 += int(o2[j][i])
	for j in range(len(scrubber)):
		scrubberCounter2 += int(scrubber[j][i])

	# Find most common bit in o2 list
	if o2Counter2 >= len(o2) / 2:
		o2Take = 1
	# Find least common bit in scrubber list
	if scrubberCounter2 >= len(scrubber) / 2:
		scrubberTake = 0
		
	# Narrow down the o2 codes that have the correct bit in position
	# If narrowed down to 1 code, skip because we are done
	if len(o2) > 1:
		for j in range(len(o2)):
			if int(o2[j][i]) == o2Take:
				narrowedO2.append(o2[j])
		o2 = narrowedO2
		
	# Narrow down the scrubber codes that have the correct bit in position
	# If narrowed down to 1 code, skip because we are done
	if len(scrubber) > 1:
		for j in range(len(scrubber)):
			if int(scrubber[j][i]) == scrubberTake:
				narrowedScrubber.append(scrubber[j])
		scrubber = narrowedScrubber

# Convert binary to int to solve
print(int(gamma, 2) * int(epsilon, 2))
print(int(o2[0], 2) * int(scrubber[0], 2))

# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')   