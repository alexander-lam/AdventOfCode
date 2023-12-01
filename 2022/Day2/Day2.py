# Timer
import time
start = time.time()

# Read input from file
input = open('input1.txt', 'r').read().splitlines()

score = 0

for i in input:
    if i[0] == 'A':
        if i[2] == 'X':
            score += 4
        elif i[2] == 'Y':
            score += 8
        elif i[2] == 'Z':
            score += 3
    elif i[0] == 'B':
        if i[2] == 'X':
            score += 1
        elif i[2] == 'Y':
            score += 5
        elif i[2] == 'Z':
            score += 9
    elif i[0] == 'C':
        if i[2] == 'X':
            score += 7
        elif i[2] == 'Y':
            score += 2
        elif i[2] == 'Z':
            score += 6
print(score)

score = 0
for i in input:
    if i[0] == 'A':
        if i[2] == 'X':
            score += 3
        elif i[2] == 'Y':
            score += 4
        elif i[2] == 'Z':
            score += 8
    if i[0] == 'B':
        if i[2] == 'X':
            score += 1
        elif i[2] == 'Y':
            score += 5
        elif i[2] == 'Z':
            score += 9
    if i[0] == 'C':
        if i[2] == 'X':
            score += 2
        elif i[2] == 'Y':
            score += 6
        elif i[2] == 'Z':
            score += 7
print(score)

# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')   