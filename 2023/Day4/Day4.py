import re
import time

# Timer
start = time.time()

# Read input from file
input = open('input1.txt', 'r').read().splitlines()

sum = 0

for line in input:
    line = line.split('|')
    winningCards = set(map(int, re.findall('(?<= )\d+(?= )', line[0])))
    elfCards = set(map(int, re.findall('\d+', line[1])))
    matchedCards = winningCards.intersection(elfCards)
    if len(matchedCards) > 0:
        sum += 2**(len(matchedCards)-1)
    
print(sum)

newSum = 0

def getNumCardsWon(cardsWon, input, curCardIndex):
    line = input[curCardIndex].split('|')
    winningCards = set(map(int, re.findall('(?<= )\d+(?= )', line[0])))
    elfCards = set(map(int, re.findall('\d+', line[1])))
    matchedCards = winningCards.intersection(elfCards)
    cardsWon = len(matchedCards)
    while len(matchedCards) > 0:
        matchedCards.pop()
        cardsWon += getNumCardsWon(cardsWon, input, curCardIndex+1)
    return cardsWon
    
print(getNumCardsWon(0, input, 0))

# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')   