# Timer
import time
import re
start = time.time()

# Read input from file
input = open('input1.txt', 'r').read().splitlines()

sum = 0
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
for line in input:
    # Match first and last number
    matches = re.findall("one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9", line)
    firstMatch = matches[0]
    lastMatch = matches[-1]

    # Parse first number
    if firstMatch.isnumeric():
        sum += int(firstMatch)*10
    elif firstMatch == 'one':
        sum += 10
    elif firstMatch == 'two':
        sum += 20  
    elif firstMatch == 'three':
        sum += 30 
    elif firstMatch == 'four':
        sum += 40 
    elif firstMatch == 'five':
        sum += 50
    elif firstMatch == 'six':
        sum += 60
    elif firstMatch == 'seven':
        sum += 70
    elif firstMatch == 'eight':
        sum += 80
    elif firstMatch == 'nine':
        sum += 90  

    # Parse last number
    if lastMatch.isnumeric():
        sum += int(lastMatch)
    elif lastMatch == 'one':
        sum += 1
    elif lastMatch == 'two':
        sum += 2  
    elif lastMatch == 'three':
        sum += 3 
    elif lastMatch == 'four':
        sum += 4 
    elif lastMatch == 'five':
        sum += 5
    elif lastMatch == 'six':
        sum += 6
    elif lastMatch == 'seven':
        sum += 7
    elif lastMatch == 'eight':
        sum += 8
    elif lastMatch == 'nine':
        sum += 9     
    
print(sum)

# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')   