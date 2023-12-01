# Timer
import time
import re
start = time.time()

# Read input from file
input = open('input1.txt', 'r').read().splitlines()

# Initialization
numStacks = 9
stacks = []
for i in range(numStacks):
    stacks.append([])
lineNum = 0

# Parse lines and add containers to corresponding stack
line = input[0]
while line[1] != '1':
    for i in range(numStacks):
        if line[4*i+1] != ' ':
            stacks[i].append(line[4*i+1])
    lineNum += 1
    line = input[lineNum]

# Reverse each stack so that it is bottom up
for stack in stacks:
    stack.reverse()

# Use regex to find all the numbers for moving
for i in range(lineNum+2, len(input)):
    line = input[i]
    nums = re.findall("\d+", line)
    moveNum = int(nums[0])
    fromNum = int(nums[1])-1
    toNum = int(nums[2])-1

    # Move containers one by one
    for j in range(moveNum):
        container = stacks[fromNum].pop()
        stacks[toNum].append(container)

# Print out top of each stack
for i in range(numStacks):
    print(stacks[i].pop(), end="")
print('')

# Reinitialize for part 2
stacks = []
for i in range(numStacks):
    stacks.append([])
lineNum = 0

# Read containers as above
line = input[0]
while line[1] != '1':
    for i in range(numStacks):
        if line[4*i+1] != ' ':
            stacks[i].append(line[4*i+1])
    lineNum += 1
    line = input[lineNum]

# Reverse stack as above
for stack in stacks:
    stack.reverse()

# Parse moving info with regex, same as above
for i in range(lineNum+2, len(input)):
    line = input[i]
    nums = re.findall("\d+", line)
    moveNum = int(nums[0])
    fromNum = int(nums[1])-1
    toNum = int(nums[2])-1

    # Pop from the container stack onto the crane
    crane = []
    for j in range(moveNum):
        crane.append(stacks[fromNum].pop())
    
    # Bulk drop from the crane onto the new container stack
    for j in range(len(crane)):
        stacks[toNum].append(crane.pop())

# Pop off top of each stack and print
for i in range(numStacks):
    print(stacks[i].pop(), end="")
print('')

# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')   