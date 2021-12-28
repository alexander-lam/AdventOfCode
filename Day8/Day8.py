# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 22:52:58 2021

@author: alexa
"""

# Timer
import time
start = time.time()

# Instantiate vars
patterns = []
outputs = []
unique = 0
decoderSeed = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '',}
decoders = []
total = 0

# Read input file
input = open('input1.txt', 'r').read().splitlines()

for element in input:
	vals = element.split(' ')
	pattern = []
	output = []
	for i in range(10):
		pattern.append(''.join(sorted(vals[i])))
	for i in range(11, 15):
		output.append(''.join(sorted(vals[i])))
		if len(vals[i]) in {2, 3, 4, 7}:
			unique += 1
	patterns.append(sorted(pattern, key=len))
	outputs.append(output)

for pattern in patterns:
	solved = ''
	# Load in decoder seed copy
	curDecoder = decoderSeed.copy()
	
	# Solve for top segment by finding complement of numbers 1 and 7 and add to decoder
	diff = list(set(pattern[1]) - set(pattern[0]))[0]
	for i in [0, 2, 3, 5, 6, 7, 8, 9]:
		curDecoder[i] += diff
	solved += diff
	
	i = 6
	# Find the number 6, because 0 and 9 are subsets of 1
	while set(pattern[0]).issubset(set(pattern[i])):
		i += 1
	six = pattern[i]
		
	# Solve for top right having exactly one segment from 1 missing in 6
	# This also inherently solves for bottom right
	if pattern[0][0] in six:
		segment1 = pattern[0][1]
		segment2 = pattern[0][0]
	else:
		segment1 = pattern[0][0]
		segment2 = pattern[0][1]
	solved += segment1 + segment2
	
	# Add top right to decoder
	for i in [0, 1, 2, 3, 4, 7, 8, 9]:
		curDecoder[i] += segment1
		
	# Add bottom right to decoder
	for i in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
		curDecoder[i] += segment2
	
	# Solve for bottom left because 5 has exactly one segment different from 6
	for i in range(3, 6):
		diff = list(set(six) - set(pattern[i]))
		if len(diff) == 1:
			break
	for i in [0, 2, 6, 8]:
		curDecoder[i] += diff[0]
	solved += diff[0]
	
	# Solve for middle segment because 0 is missing a single unsolved segment from 8
	for i in range(6, 9):
		diff = list(set(pattern[9]) - set(pattern[i]))[0]
		if not diff in solved:
			break
	for i in [2, 3, 4, 5, 6, 8, 9]:
		curDecoder[i] += diff
	solved += diff
	
	# Solve for top left because it is the only unsolved segment in 4
	diff = list(set(pattern[2]) - set(solved))[0]
	for i in [0, 4, 5, 6, 8, 9]:
		curDecoder[i] += diff
	solved += diff
	
	# Final unsolved piece in 8 is bottom segment
	diff = list(set(pattern[9]) - set(solved))[0]
	for i in [0, 2, 3, 5, 6, 8, 9]:
		curDecoder[i] += diff
	solved += diff
	
	# Swap dictionary value to make for easy lookup from sorted code to val
	decoders.append({''.join(sorted(value)):key for key, value in curDecoder.items()})

# Decode each message and sum it up
for i in range(len(outputs)):
	value = ''
	decoder = decoders[i]
	for num in outputs[i]:
		value += str(decoder[num])
	total += int(value)
	
print(unique)
print(total)
		
# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')