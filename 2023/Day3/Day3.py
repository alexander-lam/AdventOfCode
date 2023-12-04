import re
import time

# Timer
start = time.time()

# Read input from file
input = open('input1.txt', 'r').read().splitlines()

# Initialize
sum = 0
for i in range(len(input)):
    # Find all numbers in line
    nums = re.finditer('\d+', input[i])

    # Look for symbols in all directions
    for match in nums:
        symbolFound = False
        startIndex = match.start(0)
        endIndex = match.end(0)

        for index in range(startIndex, endIndex):
            # Look left
            try:
                if not (input[i][index-1].isnumeric() or input[i][index-1] == '.'):
                    symbolFound = True
                    break
            except:
                pass
            
            # Look right
            try:
                if not (input[i][index+1].isnumeric() or input[i][index+1] == '.'):
                    symbolFound = True
                    break
            except:
                pass

            # Look up
            try:
                if not (input[i-1][index].isnumeric() or input[i-1][index] == '.'):
                    symbolFound = True
                    break
            except:
                pass

            # Look down
            try:
                if not (input[i+1][index].isnumeric() or input[i+1][index] == '.'):
                    symbolFound = True
                    break
            except:
                pass

            # Look diag left down
            try:
                if not (input[i+1][index-1].isnumeric() or input[i+1][index-1] == '.'):
                    symbolFound = True
                    break
            except:
                pass    

            # Look diag right down
            try:
                if not (input[i+1][index+1].isnumeric() or input[i+1][index+1] == '.'):
                    symbolFound = True
                    break
            except:
                pass

            # Look diag right up
            try:
                if not (input[i-1][index+1].isnumeric() or input[i-1][index+1] == '.'):
                    symbolFound = True
                    break
            except:
                pass                       

            # Look diag left up
            try:
                if not (input[i-1][index-1].isnumeric() or input[i-1][index-1] == '.'):
                    symbolFound = True
                    break
            except:
                pass 

        # Symbol found, so add the number to the output
        if symbolFound:
            sum += int(match.group(0))

print(sum)

# Reinitialize
gearSum = 0
gearIndices = {}

for i in range(len(input)):
    # Find all numbers in line
    nums = re.finditer('\d+', input[i])
    for match in nums:
        startIndex = match.start(0)
        endIndex = match.end(0)

        # Search for gear in all directions and store index of gear and adjacent number in dictionary
        # If gear has already been found, multiply number by the dictionary value and add to output
        for index in range(startIndex, endIndex):
            # Look left
            try:
                if input[i][index-1] == '*':
                    gearIndex = (i, index-1)
                    if gearIndex in gearIndices:
                        gearSum += int(match.group(0)) * gearIndices[gearIndex]
                    else:
                        gearIndices[gearIndex] = int(match.group(0))
                    break
            except:
                pass
            
            # Look right
            try:
                if input[i][index+1] == '*':
                    gearIndex = (i, index+1)
                    if gearIndex in gearIndices:
                        gearSum += int(match.group(0)) * gearIndices[gearIndex]
                    else:
                        gearIndices[gearIndex] = int(match.group(0))
                    break
            except:
                pass

            # Look up
            try:
                if input[i-1][index] == '*':
                    gearIndex = (i-1, index)
                    if gearIndex in gearIndices:
                        gearSum += int(match.group(0)) * gearIndices[gearIndex]
                    else:
                        gearIndices[gearIndex] = int(match.group(0))
                    break
            except:
                pass

            # Look down
            try:
                if input[i+1][index] == '*':
                    gearIndex = (i+1, index)
                    if gearIndex in gearIndices:
                        gearSum += int(match.group(0)) * gearIndices[gearIndex]
                    else:
                        gearIndices[gearIndex] = int(match.group(0))
                    break
            except:
                pass

            # Look diag left down
            try:
                if input[i+1][index-1] == '*':
                    gearIndex = (i+1, index-1)
                    if gearIndex in gearIndices:
                        gearSum += int(match.group(0)) * gearIndices[gearIndex]
                    else:
                        gearIndices[gearIndex] = int(match.group(0))
                    break
            except:
                pass    

            # Look diag right down
            try:
                if input[i+1][index+1] == '*':
                    gearIndex = (i+1, index+1)
                    if gearIndex in gearIndices:
                        gearSum += int(match.group(0)) * gearIndices[gearIndex]
                    else:
                        gearIndices[gearIndex] = int(match.group(0))
                    break
            except:
                pass

            # Look diag right up
            try:
                if input[i-1][index+1] == '*':
                    gearIndex = (i-1, index+1)
                    if gearIndex in gearIndices:
                        gearSum += int(match.group(0)) * gearIndices[gearIndex]
                    else:
                        gearIndices[gearIndex] = int(match.group(0))
                    break
            except:
                pass                       

            # Look diag left up
            try:
                if input[i-1][index-1] == '*':
                    gearIndex = (i-1, index-1)
                    if gearIndex in gearIndices:
                        gearSum += int(match.group(0)) * gearIndices[gearIndex]
                    else:
                        gearIndices[gearIndex] = int(match.group(0))
                    break
            except:
                pass 

print(gearSum)

# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')   