
import pygame
import random
import time


# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Screen size
height = 600
width = 600
x1 = width/2
y1 = height/2
display = pygame.display.set_mode((width, height))
# Margin between each segment
segment_margin = 3

# Set the width and height of each snake segment
segment_width = min(height, width) / 40 - segment_margin
segment_height = min(height, width) / 40 - segment_margin

# Set initial speed
x_change = segment_width + segment_margin
y_change = 0
global snakelength
snakelength = 1

class Snake():
    """ Class to represent one snake. """
    # Constructor
    def __init__(self):
        self.segments = []
        self.spriteslist = pygame.sprite.Group()
        for i in range(1):
            x = (segment_width + segment_margin) * 30 - (segment_width + segment_margin) * i
            y = (segment_height + segment_margin) * 2
            segment = Segment(x, y)
            self.segments.append(segment)
            self.spriteslist.add(segment)

    def move(self):
        # Figure out where new segment will be
        global game_over
        x = self.segments[0].rect.x + x_change
        y = self.segments[0].rect.y + y_change
        # Don't move off the screen
        if 0 <= x <= width - segment_width and 0 <= y <= height - segment_height:
        # Insert new segment into the list
            segment = Segment(x, y)
            self.segments.insert(0, segment)
            self.spriteslist.add(segment)
        # Get rid of last segment of the snake
        # .pop() command removes last item in list
            old_segment = self.segments.pop()
            self.spriteslist.remove(old_segment)
        else:
            game_over = True
    def grow(self):
        x = self.segments[0].rect.x + x_change
        y = self.segments[0].rect.y + y_change
        segment = Segment(x, y)
        self.segments.insert(0, segment)
        self.spriteslist.add(segment)

class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of a snake. """

    # Constructor
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
        self.x = x
        self.y = y
        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)

        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Food():
    def __init__(self):
        self.spriteslist = pygame.sprite.Group()
        #add food at random locations
    def replenish(self):
        global snakelength
        if not food_group:
            food = Food_item(15,15,random.randrange(10,width-10),random.randrange(10,height-10),RED)
            snakelength += 1
            food_group.add(food)
        foodHit = pygame.sprite.pygame.sprite.spritecollide(snakeHead, food_group, True)
        foodHit2 = pygame.sprite.pygame.sprite.spritecollide(aiHead, food_group, True)
        if foodHit:
            my_snake.grow()
class Food_item(pygame.sprite.Sprite):
    def __init__(self,width,height,posx,posy,color):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [posx,posy]
class Obstacles():
    def __init__(self):
        self.x = x
        self.y = y

    def spawnObstacle(self, x, y):
        self.obstacle = Obstacle(random.randint(20,65),random.randint(20,65),obx,oby,GREEN)
        self.obstacle = Obstacle(x, y)
        self.obstacles.append(obstacle)
        self.spritesList.add(obstacle)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,width,height,posx,posy,color):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [posx,posy]

######

class AI():
       # Constructor
    def __init__(self):
        self.segments = []
        self.spriteslist = pygame.sprite.Group()
        for i in range(1):
            x = (segment_width + segment_margin) * 20 - (segment_width + segment_margin) * i
            y = (segment_height + segment_margin) * 10
            segment = aiSegment(x, y)
            self.segments.append(segment)
            self.spriteslist.add(segment)

    def move(self):
        # Figure out where new segment will be
        moves = [-10,0,10]
        x = self.segments[0].rect.x + random.choice(moves)
        y = self.segments[0].rect.y + random.choice(moves)
        # Don't move off the screen
        if 0 <= x <= width - segment_width and 0 <= y <= height - segment_height:
        # Insert new segment into the list
            segment = aiSegment(x, y)
            self.segments.insert(0, segment)
            self.spriteslist.add(segment)
        # Get rid of last segment of the snake
        # .pop() command removes last item in list
            old_segment = self.segments.pop()
            self.spriteslist.remove(old_segment)

    def grow(self):
        x = self.segments[0].rect.x + x_change
        y = self.segments[0].rect.y + y_change
        segment = aiSegment(x, y)
        self.segments.insert(0, segment)
        self.spriteslist.add(segment)


class aiSegment(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
        self.x = x
        self.y = y
        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(GREEN)

        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#####



# Call this function so the Pygame library can initialize itself
pygame.init()
score_font = pygame.font.SysFont(None, 35)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, GREEN)
    display.blit(value, [0, 0])
def Death():
    value = score_font.render("Game Over",  True, WHITE)
    display.blit(value, [200, 300])
# Create a 600x600 sized screen
screen = pygame.display.set_mode([width, height])

# Set the title of the window
pygame.display.set_caption('Snake 2: Holly DuCoing Edition')

# Create an initial snake for drawing
aiSnake = AI()
my_snake = Snake()

 #groups
obstacle_group = pygame.sprite.Group()
food_group = pygame.sprite.Group()

#obstacles to avoid
food = Food_item(15,15,random.randrange(10,width),random.randrange(10,height),RED)
food_group.add(food)
obstacle = Obstacle(25,55,random.randrange(1,width),random.randrange(200,height),GREEN)
obstacle2 = Obstacle(25,85,random.randrange(1,width)-100,random.randrange(200,height)+40,GREEN)
obstacle_group.add(obstacle)
obstacle_group.add(obstacle2)

clock = pygame.time.Clock()
#game endings
done = False
global game_over
game_over = False
while not done:

    snakeHead = my_snake.segments[0]
    aiHead = aiSnake.segments[0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the direction based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change = (segment_width + segment_margin) * -1
            y_change = 0
        if event.key == pygame.K_RIGHT:
            x_change = (segment_width + segment_margin)
            y_change = 0
        if event.key == pygame.K_UP:
            x_change = 0
            y_change = (segment_height + segment_margin) * -1
        if event.key == pygame.K_DOWN:
            x_change = 0
            y_change = (segment_height + segment_margin)

    if not game_over:
        # move snake one step
        my_snake.move()
        aiSnake.move()
        #adds food when its been eaten
        Food.replenish(food_group)
        #check if snake hits himself
        obstacleHitList = pygame.sprite.spritecollide(snakeHead, obstacle_group, False)
        hitSelf = pygame.sprite.spritecollide( my_snake.segments[0], my_snake.spriteslist, False )
        enemyHit = pygame.sprite.spritecollide( my_snake.segments[0], aiSnake.spriteslist, False )
        if len(hitSelf)> 1:
            game_over = True
        if obstacleHitList or enemyHit:
            game_over = True

    # -- Draw everything
        # Clear screen
        screen.fill(BLACK)
        #Draw sprites
        aiSnake.spriteslist.draw(screen)
        my_snake.spriteslist.draw(screen)
        food_group.draw(screen)
        obstacle_group.draw(screen)
        Your_score(snakelength - 1)

        # Flip screen
        pygame.display.flip()

        # Pause
        clock.tick(5)
    else:
        Death()
    pygame.display.flip()
pygame.quit()
