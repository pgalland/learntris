#!/usr/bin/env python3.3
import sys



############## Creation of the matrix ####################



# matrix[i] is line number i (i goes from 0 to 21)
# matrix[_][j] is the column number j (j goes from 0 to 9)
# line 0 is the bottom line and line 21 the top one
# column 0 is the leftmost column, column 9 the rightmost one

matrix = [ ['.' for j in range(10)] for i in range(22)]




################# Functions ##########################


# prints the matrix state
def printState() :
    
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
    
    line = 21 # the first line read corresponds to the top line i.e. line number 21
    
    # read the lines
    for textLine in sys.stdin :
        
        for column in range(0,20, 2) : # hop of 2 because of the whitespace between letters
            matrix[line][int(column/2)] = textLine[column] 
        line = line-1
        
        if (line<0) : #stop after line 0
            break



############# Scanning of the commands ######################


for line in sys.stdin :
    
    if (line == 'p\n'):
        printState()
    elif (line == 'g\n'):
        setMatrix()
    else :
        quit()
    

