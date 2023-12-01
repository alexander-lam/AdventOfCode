# Timer
import time
start = time.time()

# Read input from file
input = open('input1.txt', 'r').read().splitlines()

# Get signal and substring 14 characters
signal = input[0]
for i in range(len(signal)):
    marker = signal[i:i+14]
    
    valid = True
    for j in range(len(marker)):
        for k in range(j+1,len(marker)):
            # Compare each char with each other and if it matches, not a valid marker
            if marker[j] == marker[k]:
                valid = False
    if valid:
        # Valid marker, print the index of the last character
        print(i+14)
        break

# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')   