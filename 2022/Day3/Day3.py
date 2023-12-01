# Timer
import time
start = time.time()

# Read input from file
input = open('input1.txt', 'r').read().splitlines()

priority = 0
for sack in input:
    items = {}
    # Iterate through every item in the sack
    for i in range(len(sack)):
        if i < len(sack)/2:
            # If I haven't seen the item before in first half, add it to the dict
            if sack[i] not in items.keys():
                items[sack[i]] = 1
        else:
            # If I have seen the item before in second half, set to 0
            if sack[i] in items.keys():
                items[sack[i]] = 0
    
    # Do ASCII math to figure out the priority for char that is 0
    for item in items.keys():
        if items[item] == 0:
            val = ord(item)
            if val < 91:
                # Uppercase
                priority += val-38
            else:
                # Lowercase
                priority += val-96
            break
print(priority)

priority = 0
for i in range(int(len(input)/3)):
    items = {}
    # Iterate through items in sack groups of 3
    group = input[3*i:3*i+3]
    for sack in group:
        for j in range(len(sack)):
            item = sack[j]
            # If I haven't seen it before, set to 2
            if item not in items.keys():
                items[sack[j]] = 2
            # If I have seen it before and this is not a duplicate in the sack, subtract 1
            elif item not in sack[0:j]:
                items[sack[j]] -= 1

    # Do ASCII math to figure out the priority for char that is 0
    for item in items.keys():
        if items[item] == 0:
            val = ord(item)
            if val < 91:
                # Uppercase
                priority += val-38
            else:
                # Lowercase
                priority += val-96
            break
print(priority)

# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')   