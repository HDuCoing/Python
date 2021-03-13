import pygame
import mazeclass

# Initialize pygame
pygame.init()

# Set the height and width of the screen
size=[1000,500]
screen=pygame.display.set_mode(size)
visited = []
revisited = []
global exit
exit = (1,8)
# Set title of screen
pygame.display.set_caption("Maze Project")

# Get a new maze
mazegrid =  [[2,2,2,2,2,2,2,2,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
             [2,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,2],
             [2,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,2],
             [2,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,2],
             [2,0,1,1,1,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,2],
             [2,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,2],
             [2,0,1,1,1,1,1,0,0,0,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,2],
             [2,0,1,0,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,2],
             [2,0,1,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,2],
             [2,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
             [2,0,1,0,1,0,0,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,2],
             [2,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,2],
             [2,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,2],
             [2,0,1,1,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,1,0,1,0,0,0,2],
             [2,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,2],
             [2,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,1,1,0,1,0,2],
             [2,0,1,0,0,0,0,0,1,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,2],
             [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

the_maze = mazeclass.Maze(mazegrid)


##########################################################

# Some (silly) sample code for moving one step forward and backward

def forwardbackward(curpos):
    # Warm up at the current position
    moveto(curpos, 3)
    moveto(curpos, 3)
    # Look for positions that can be visited
    neighbourlist = unvisitedneighbours(curpos)
    if neighbourlist != []:
        # Select the first position that can be visited
        newpos = neighbourlist[0]
        # Go to that position
        moveto(newpos, 3)
        # Warm up at the new position
        moveto(newpos, 4)
        # Move back
        moveto(curpos, 4)

def unvisitedneighbours(curpos):
    # Return list of unvisited positions that can be reached from current position
    x = curpos[0]
    y = curpos[1]
    free = []
    for newpos in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0 <= newpos[0] < the_maze.rows and 0 <= newpos[1] < the_maze.columns:
                if the_maze.grid[newpos[0]][newpos[1]].status == 0:
                    free.append(newpos)
    return free

def moveto(newpos, status, movebot=True):
    # Mark the new position as being visited
    the_maze.grid[newpos[0]][newpos[1]].status = status
    # If required, move to the new position
    if movebot:
        the_maze.bot_xcoord = newpos[0]
        the_maze.bot_ycoord = newpos[1]
    # Wait a bit and then display the current state of the maze
    pygame.time.delay(10)
    the_maze.display_maze(screen)
    pygame.display.flip()
    pygame.event.pump()
def exitFound(curpos):
    #identifies exit square
    x = curpos[0]
    y = curpos[1]
    for newpos in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= newpos[0] < the_maze.rows and 0 <= newpos[1] < the_maze.columns:
            if the_maze.grid[newpos[0]][newpos[1]].status == 5:
                return True

def depthfirsttraversal(curpos):
    #press d
    # Do a depth-first traversal of all unvisited neighbours
    visited.append(curpos)
    for neighbour in unvisitedneighbours(curpos):
        moveto(curpos, 3)
        if neighbour not in visited:
            depthfirsttraversal(neighbour)
        if neighbour in visited:
            revisited.append(neighbour)
    moveto(curpos,4)

def depthfirstsearch(curpos):
    #press s
    # Perform a depth-first search to find the exit
    exit_found = exitFound(curpos)
    visited.append(curpos)

    if exit in visited:
        moveto(exit, 4)
        return True
    else:
        for neighbour in unvisitedneighbours(curpos):
            if neighbour not in visited:
                moveto(neighbour, 3)
                depthfirstsearch(curpos)
                exit_found= depthfirstsearch(neighbour)

            if exit_found:
                moveto(exit, 4)
                return True
            else:
                moveto(neighbour, 4)




def breadthfirstsearch(curpos):
    # Perform a breadth-first search to find the exit
    queue = [curpos]
    visited.append(curpos)
    queue.append(curpos)

    while queue != []:
        # dequeue next vertex
        curpath = queue.pop(0)
        curpos = curpath[-1]

        for neighbour in unvisitedneighbours(curpath):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                moveto(neighbour, 3, movebot=False)
            if exit in visited:
                visited.append(curpos)
                queue.copy()
                moveto(exit, 4)
                return True
            else:
                queue.append(neighbour)
                visited.append(neighbour)

def tokencollection(curpos):
    #nonfunctional
    #press t
    # Collect all tokens in topological order
    tokenList = mazeclass.Maze().tokens
    stack = []
    visited = []
    def recursive_helper(curpos):
        for neighbour in unvisitedneighbours[curpos]:
            if neighbour not in visited:
                visited.append(neighbour)
                recursive_helper(neighbour)
        stack.insert(0, curpos)
    for curpos in unvisitedneighbours:
        if curpos not in visited:
           recursive_helper(curpos)
    return stack



# Loop until the user clicks the close button.
done=False

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

######################################
# -------- Main Program Loop -----------
while done==False:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN: # If user wants to perform an action
                if event.key == pygame.K_f:
                    the_maze.reset(mazegrid)
                    forwardbackward((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_d:
                    the_maze.reset(mazegrid)
                    depthfirsttraversal((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_s:
                    the_maze.reset(mazegrid)
                    depthfirstsearch((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_b:
                    the_maze.reset(mazegrid)
                    breadthfirstsearch((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_t:
                    the_maze.reset(mazegrid)
                    the_maze.display_tokens()
                    tokencollection((the_maze.bot_xcoord, the_maze.bot_ycoord))

        the_maze.display_maze(screen)
        # Limit to 50 frames per second
        clock.tick(50)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

# If you forget this line, the program will 'hang' on exit.
pygame.quit ()