# Solver 2021
# Template for the algorithm to solve a sudoku. Builds a recursive backtracking solution
# that branches on possible values that could be placed in the next empty cell. 
# Initial pruning of the recursion tree - 
#       we don't continue on any branch that has already produced an inconsistent solution
#       we stop and return a complete solution once one has been found

import Sudoku_IO
import pygame


# TODO solve the sudoku
def solve(snapshot, screen):
    # display current snapshot
    pygame.time.delay(10)
    Sudoku_IO.displayPuzzle(snapshot, screen)
    pygame.display.flip()
    # returns value of possible cells

    if isComplete(snapshot) == True:
        return True
        # if there's nowhere left, then
        # we're done because we only allowed valid input
        # if current snapshot is complete ... return a value
        # look for remaining cells
        # if current snapshot not complete ...
        # for each possible value for an empty cell
        # shot is consistent, perform recursive call
        # return a value
    else:
        # gets every empty cell to be solved
        unsolved_cells = snapshot.unsolvedCells()
        # loops over each empty cell in unsolved cells
        for cell in unsolved_cells:
            possible = possible_cells(cell, snapshot)
            # if there is no possible values return false
            if not possible:
                return False
            # if there is a possible cell, add to snapshot
            if len(possible) == 1:
                cell.setVal(possible[0])
                finished = solve(snapshot, screen)
                solve(snapshot, screen)
                if finished:
                    return True


def possible_cells(cell, snapshot):
    # This function checks and returns which possible values are valid options in a certain cell.
    options = []
    for x in range(1,10):
        test = snapshot.clone()
        test.setCellVal(cell.getRow(), cell.getCol(), x)
        if checkConsistency(test):
            options.append(x)
    return options

# Check whether a snapshot is consistent, i.e. all cell values comply
# with the sudoku rules (each number occurs only once in each block, row and column).
def checkConsistency(snapshot):
    # row
    for row in range(9):
        valuesin_Row = []
        cellsinRow = snapshot.cellsByRow(row)
        for cell in cellsinRow:
            valuesin_Row.append(cell.getVal())
        # if there is more than 1 of any value, this snapshot is invalid
        for value in range(1, 10):
            if valuesin_Row.count(value) > 1:
                return False
    # column
    for col in range(9):
        valuesin_Col = []
        cellsinCol = snapshot.cellsByCol(col)
        for cell in cellsinCol:
            valuesin_Col.append(cell.getVal())
# if there is more than 1 of any value, this snapshot is invalid
        for value in range(1, 10):
            if valuesin_Col.count(value) > 1:
                return False
    # block
    for row in range(9):  # check if any box holds duplicates
        for col in range(9):
            valuein_Block = []
            cellsinBlock = snapshot.cellsByBlock(row, col)
            for cell in cellsinBlock:
                valuein_Block.append(cell.getVal())
# if there is more than 1 of any value, this snapshot is invalid
            for value in range(1,10):
                if valuein_Block.count(value) > 1:
                    return False
    return True

# Check whether a puzzle is solved. 
# return true if the sudoku is solved, false otherwise
def isComplete(snapshot):
    if snapshot.unsolvedCells() == [] and checkConsistency(snapshot):
        return True
    else:
        return False