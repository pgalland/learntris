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



    



############# Scanning of the commands ######################


for line in sys.stdin :
    
    if (line == 'p\n'):
        printState()
    else :
        quit()
    

