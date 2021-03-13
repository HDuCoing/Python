"""
 Animating multiple objects using a list.
 based on Sample Python/Pygame Programs
 Simpson College Computer Science

"""

# Import libraries 'pygame' and 'random'
import pygame
import random

# Initialize the game engine
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
colorlist = [GREEN ,RED, BLUE, WHITE]

colour = random.choice(colorlist)


# Set the height and width of the screen
SIZE = [400, 400]


screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Winter!")
clock = pygame.time.Clock()

snow_list = []
# Loop 100 times and add a snow flake in a random x,y position
for i in range(100):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append((WHITE, [x, y]))
done = False
count = 0
snowflake = [[x,y], random.choice(colorlist)]
def recolour_snowflake(snowflake):
    colour = random.choice(colorlist)
    return (colour, snowflake[1])

def drawsnow(snowflake):
    x, y = snowflake[1]
    y += random.randrange(1,3)
    if y > 400:
        x, y = (random.randrange(0, 400), random.randrange(-50, -10))
    return (snowflake[0], [x, y])

def keep_snowflake(snowflake):
    if snowflake[0][1] < 0.30:
        return False
    else:
        return True

while not done:

    snow_list = list(filter(keep_snowflake, snow_list))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if count == 5:
        snow_list = list(map(recolour_snowflake, snow_list))
        count = 0
    count += 1
    if not snow_list:
        #a little extra something for ending the program
        screen.fill(random.choice(colorlist))
        pygame.display.update()
        done = True
    # Set the screen background
    screen.fill(BLACK)

    # Process each snow flake in the list
    snow_list = list(map(drawsnow, snow_list))

    # draw the snow flakes
    for snow in snow_list:
        pygame.draw.circle(screen, *snow, 2)


    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(20)
# If you forget this line, the program will 'hang' on exit.
pygame.quit()

