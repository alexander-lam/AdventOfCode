import re
import time

# Timer
start = time.time()

# Read input from file
input = open('input1.txt', 'r').read().splitlines()

# Initialize
result = 0
power = 0
for line in input:
    # Initialize
    numRed = 0
    numGreen = 0
    numBlue = 0
    constraintViolated = False

    # Find matches for number of cubes
    redMatches = list(map(int, re.findall('\d+(?= red)', line)))
    greenMatches = list(map(int, re.findall('\d+(?= green)', line)))
    blueMatches = list(map(int, re.findall('\d+(?= blue)', line)))

    # Check if too many cubes are drawn
    for draw in redMatches:
        if draw > 12:
            constraintViolated = True
    
    for draw in greenMatches:
        if draw > 13:
            constraintViolated = True

    for draw in blueMatches:
        if draw > 14:
            constraintViolated = True

    # Valid game, so add result
    if not constraintViolated:
        result += sum(list(map(int, re.findall('(?<=Game )\d+', line))))

    # Find minimum number of cubes required and compute power
    power += max(redMatches) * max(greenMatches) * max(blueMatches)

# Print result
print(result)
print(power)

# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')   