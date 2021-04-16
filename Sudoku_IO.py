# Utility to read sudoku puzzles from text files, and display sudoku puzzles to a screen.

import Snapshot, Cell
import pygame


# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)

# This sets the width and height of each grid location
width=60
height=60
 
# This sets the margin between each cell
margin=10

def loadPuzzle(puzzlefile):
    file = open(puzzlefile)
    newsnapshot = Snapshot.snapshot()
    rownumber = 0
    
    for line in file: # read lines
        newline = [int(x) for x in line.split()] 
        for columnnumber in range(9):
            newsnapshot.setCellVal(rownumber, columnnumber, newline[columnnumber])  
        rownumber +=1
    return newsnapshot


def displayPuzzle(snapshot, screen):
    # Set the screen background
    screen.fill(black)
 
    # Draw the grid squares
    color = white
    for row in range(9):
        for column in range(9):       
           pygame.draw.rect(screen,color,[(margin+width)*column+margin+(margin*(column//3)),(margin+height)*row+margin+(margin*(row//3)),width,height])
           myfont = pygame.font.SysFont("Comic Sans MS", 30)
           printVal = snapshot.getCellVal(row, column)
           if printVal == 0:
               label = myfont.render(".", 1, black)
           else:
               label = myfont.render(str(printVal), 1, black)
           screen.blit(label, ((margin+width)*column+margin+(margin*(column//3))+25,(margin+height)*row+margin+(margin*(row//3))+10))