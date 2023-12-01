# Timer
import time
start = time.time()

# Read input from file
input = open('input1.txt', 'r').read().splitlines()

count1 = 0
count2 = 0
for pairing in input:
    # Split pairs
    middleIndex = pairing.index(',')
    section1 = pairing[0:middleIndex]
    section2 = pairing[middleIndex+1:]

    # Extract ranges for each section in pairing
    rangeIndex1 = section1.index('-')
    rangeIndex2 = section2.index('-')
    section1Start = int(section1[0:rangeIndex1])
    section1End = int(section1[rangeIndex1+1:])
    section2Start = int(section2[0:rangeIndex2])
    section2End = int(section2[rangeIndex2+1:])
    range1 = range(section1Start, section1End+1)
    range2 = range(section2Start, section2End+1)

    # Find if one list is subset of the other
    if all(item in range1 for item in range2) or all(item in range2 for item in range1):
        count1 += 1

    # Find if list intersection has items
    if len(list(set(range1) & set(range2))) > 0:
        count2 += 1

print(count1)
print(count2)

# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')   