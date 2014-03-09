#!/usr/bin/env python3.3
import sys



############## Initialization of the matrix and the score  ####################



# matrix[i] is line number i (i goes from 0 to 21)
# matrix[_][j] is the column number j (j goes from 0 to 9)
# line 0 is the bottom line and line 21 the top one
# column 0 is the leftmost column, column 9 the rightmost one

matrix = [ ['.' for j in range(10)] for i in range(22)]
score = 0
numberOfClearedLines = 0




###################### Functions ##########################


# prints the matrix state
def printMatrix() :
    
    # prints lines from the top to the bottom :
    for line in range(21,-1,-1) :
        #prints columns from left to right
        for column in range(0,10) :
            if (column<9) :
                print(matrix[line][column], end=" ")
            else :
                print(matrix[line][column], end="\n") #prints newline for the last column



# reads the represantation of the matrix (22 line of text from stdin)
# and set the matrix according to the textual representation
def setMatrix() :
    global matrix
    line = 21 # the first line read corresponds to the top line i.e. line number 21
    
    # read the lines
    for textLine in sys.stdin :
        
        for column in range(0,20, 2) : # hop of 2 because of the whitespace between letters
            matrix[line][int(column/2)] = textLine[column] 
        line = line-1
        
        if (line<0) : #stop after line 0
            break


# clear the matrix -> set all to '.'
def clearMatrix() :
    global matrix
    for line in range(0,22):
        for column in range(0,10):
            matrix[line][column] = '.'


# displays the score (initially score = 0)
def displayScore() :
    print(score)

# displays the number of cleared lines (initially 0)
def displayClearedLines() :
    print(numberOfClearedLines)


# returns True if the line is full (without '.') and False otherwise 
def fullLine(line) :
    
    for column in range(0,10):
        if (matrix[line][column] == '.'):
            return False
    
    return True

# clears the line #line in the matrix
def clearLine(line) :
    global matrix
    for column in range(0,10):
        matrix[line][column] = '.'


# step searchs to see if there is a full line in the matrix (line with no '.')
# if there is : clears the line / numberOfClearedLines+1 / score+100
def step() :
    global numberOfClearedLines, score, matrix
    for line in range(0,22):
        if fullLine(line) :
            clearLine(line)
            numberOfClearedLines = numberOfClearedLines+1
            score = score+100
        
    



############# Scanning of the commands ######################


for line in sys.stdin :
    
    if (line == 'p\n'): # print matrix
        printMatrix()

    elif (line == 'g\n'):# set matrix to given matrix
        setMatrix()

    elif (line == 'c\n'): # clear matrix
        clearMatrix()

    elif (line == '?s\n'): # query for the score
        displayScore()

    elif (line == '?n\n'): # query for the numbers of cleared lines
        displayClearedLines()

    elif (line == 's\n'): # executes one step
        step()

    else:
        quit()

