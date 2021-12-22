# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 22:07:18 2021

@author: alam
"""

input = open('input1.txt', 'r').read().splitlines()

counter1 = []
gamma = ''
epsilon = ''

o2Counter2 = 0
scrubberCounter2 = 0
o2Take = 0
scrubberTake = 0
o2 = input
narrowedO2 = []
scrubber = input
narrowedScrubber = []

for digit in input[0]:
	counter1.append(int(digit))

for i in range(1, len(input)):
	for j in range(len(input[i])):
		counter1[j] += int(input[i][j])
		
for count in counter1:
	if count >= len(input) / 2:
		gamma += '1'
		epsilon += '0'
	else:
		gamma += '0'
		epsilon += '1'
	

for i in range(len(input[0])):
	o2Counter2 = 0
	scrubberCounter2 = 0
	o2Take = 0
	scrubberTake = 1
	narrowedO2 = []
	narrowedScrubber = []
	
	for j in range(len(o2)):
		o2Counter2 += int(o2[j][i])
	for j in range(len(scrubber)):
		scrubberCounter2 += int(scrubber[j][i])

	if o2Counter2 >= len(o2) / 2:
		o2Take = 1
	if scrubberCounter2 >= len(scrubber) / 2:
		scrubberTake = 0

	if len(o2) > 1:
		for j in range(len(o2)):
			if int(o2[j][i]) == o2Take:
				narrowedO2.append(o2[j])
	else:
		narrowedO2 = o2
	if len(scrubber) > 1:
		for j in range(len(scrubber)):
			if int(scrubber[j][i]) == scrubberTake:
				narrowedScrubber.append(scrubber[j])
	else: narrowedScrubber = scrubber

	o2 = narrowedO2
	scrubber = narrowedScrubber

print(int(gamma, 2) * int(epsilon, 2))
print(int(o2[0], 2) * int(scrubber[0], 2))
        