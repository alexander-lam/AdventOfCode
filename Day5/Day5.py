# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 17:32:15 2021

@author: alexa
"""
# Timer
import time
start = time.time()

# Read input file
input = open('input1.txt', 'r').read().splitlines()

# Instantiate vars
vents = []
overlaps = {}

# Break input into lists of tuples representing start/stop coords for each vent
for element in input:
	coordSet = element.split(' -> ')
	vent = []
	for coords in coordSet:
		coord = coords.split(',')
		vent.append((int(coord[0]), int(coord[1])))
	vents.append(vent)

for vent in vents:
	startX = vent[0][0]
	startY = vent[0][1]
	stopX = vent[1][0]
	stopY = vent[1][1]
	if startX == stopX:
		# Handle y = a case and order coords from minY to maxY
		if startY <= stopY:
			min = startY
			max = stopY
		else:
			min = stopY
			max = startY
		for i in range(min, max + 1):
			coord = (startX, i)
			# If coord already exists as key, add one to value. Otherwise add new key.
			if coord in overlaps:
				overlaps[coord] += 1
			else:
				overlaps[coord] = 1
	elif startY == stopY:
		# Handle x = a case and order coords from minX to maxX
		if startX <= stopX:
			min = startX
			max = stopX
		else:
			min = stopX
			max = startX
		for i in range(min, max + 1):
			# If coord already exists as key, add one to value. Otherwise add new key.
			coord = (i, startY)
			if coord in overlaps:
				overlaps[coord] += 1
			else:
				overlaps[coord] = 1
	else:
		# Handle y = mx + b case by calculating linear function and order coords from minX to maxX
		m = (stopY - startY) / (stopX - startX)
		b = startY - m * startX
		if startX <= stopX:
			min = startX
			max = stopX
		else:
			min = stopX
			max = startX
		for x in range(min, max + 1):
			# Evaluate linear func and if coord already exists as a key, add one to value. Otherwise add new key.
			coord = (x, m * x + b)
			if coord in overlaps:
				overlaps[coord] += 1
			else:
				overlaps[coord] = 1

# Print number of values where overlap is greater than 1
print(sum(i > 1 for i in overlaps.values()))

# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')