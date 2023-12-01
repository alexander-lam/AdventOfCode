# Timer
import time
start = time.time()

# Read input from file
input = open('input1.txt', 'r').read().splitlines()

# Instantiate vars
maxCal = 0
calSums = []
i = 0

while i < len(input):
    curCal = 0
    
    # Sum up calories for each elf
    while i < len(input) and (input[i] != ''):
        curCal += int(input[i])
        i += 1

    # Store max calorie value and append to list
    if curCal > maxCal:
        maxCal = curCal
    calSums.append(curCal)
    i += 1

# Get elf with most calories
print(maxCal)

# Get top 3 elves with calories
calSums.sort(reverse=True)
print(calSums[0] + calSums[1] + calSums[2])

# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')   