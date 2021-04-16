import pygame, os, random, Sudoku_IO, Solver
import Snapshot

# Initialize pygame
pygame.init()
  
# Set the height and width of the screen
size=[660,660]
screen=pygame.display.set_mode(size)
 
# Set title of screen
pygame.display.set_caption("Sudoku Solver")
 
# Loop until the user clicks the close button.
done=False
 
# Used to manage how fast the screen updates
clock=pygame.time.Clock()


# -------- Main Program Loop -----------
while done==False:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN: # If user wants to perform an action
                if event.key == pygame.K_e:
                    # Choose a random puzzle to solve
                    easypuzzle = random.choice(os.listdir("easypuzzles")) #change dir name if necessary
                    easypuzzle = "easypuzzles/" + easypuzzle
                    firstSnapshot = Sudoku_IO.loadPuzzle(easypuzzle)
                    Solver.solve(firstSnapshot, screen)
                if event.key == pygame.K_h:
                    # Choose a random puzzle to solve
                    hardpuzzle = random.choice(os.listdir("hardpuzzles")) #change dir name if necessary
                    hardpuzzle = "hardpuzzles/" + hardpuzzle
                    firstSnapshot = Sudoku_IO.loadPuzzle(hardpuzzle) 
                    Solver.solve(firstSnapshot, screen)

   
        # Limit to 20 frames per second
        clock.tick(10)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
# If you forget this line, the program will 'hang' on exit.
pygame.quit ()
