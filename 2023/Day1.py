import re
import time

# Timer
start = time.time()

# Read input from file
input = open('input1.txt', 'r').read().splitlines()

# Initialize
sum = 0

# Process line by line
for line in input:
    # Read first number in line
    for char in line:
        if char.isnumeric():
            sum += int(char)*10
            break
    
    # Read last number in line
    for char in reversed(line):
        if char.isnumeric():
            sum += int(char)
            break

print(sum)

# Reinitialize
sum = 0

# Define dict for word nums
mapping = {'one': 1,
           'two': 2,
           'three': 3,
           'four': 4,
           'five': 5,
           'six': 6,
           'seven': 7,
           'eight': 8,
           'nine': 9}

# Process line by line
for line in input:
    # Match first and last number
    matches = re.findall("one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9", line)
    firstMatch = matches[0]
    lastMatch = matches[-1]

    # Parse first number
    if firstMatch.isnumeric():
        sum += int(firstMatch)*10
    else:
        sum += mapping[firstMatch]*10

    # Parse last number
    if lastMatch.isnumeric():
        sum += int(lastMatch)
    else:
        sum += mapping[lastMatch]    
    
print(sum)

# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')   