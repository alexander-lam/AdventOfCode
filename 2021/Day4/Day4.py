# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 00:39:30 2021

@author: alexa
"""

# Timer
import time
start = time.time()

# Read input file
input = open('input1.txt', 'r').read().splitlines()

# Read bingo number draws and remove first newline
draws = list(map(int, input.pop(0).split(',')))
input.pop(0)

# Instantiate bingo board vars
boards = []
curBoard = []
won = False
scores = []

# Create boards and append final board in input
for element in input:
	if element == '':
		boards.append(curBoard)
		curBoard = []
	else:
		curBoard.append(list(map(int, element.split())))
boards.append(curBoard)

# Iterate through each bingo draw
for draw in draws:
	winningBoards = []
	# In each board, check to see if draw exists.
	for board in boards:
		for i in range(len(board)):
			for j in range(len(board[0])):
				if draw == board[i][j]:
					# Draw exists. Set value to -1 to mark
					board[i][j] = -1
					rowWon = True
					colWon = True
					
					# Check if row and col are marked to see if there is win
					for k in range(len(board)):
						if board[k][j] != -1:
							colWon = False
					for k in range(len(board[i])):
						if board[i][k] != -1:
							rowWon = False
					
					# Collect winning boards and calculate scores
					if colWon or rowWon:
						won = True
						winningBoards.append(board)
						total = 0
						
						# Compute sum of unmarked board spaces
						for row in board:
							for element in row:
								if element != - 1:
									total += element
					
						scores.append(total*draw)
						
	# Remove winning boards from future consideration			
	for board in winningBoards:
		boards.remove(board)
	
print(scores[0])
print(scores[-1])

# Stop timer
end = time.time()
print('Time elapsed:', round((end-start)*1000, 3), 'ms')