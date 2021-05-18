import cake
import pygame, math

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
red      = ( 255,   0,   0)

class CakeRenderer:
    """renderer for displaying a cake on screen
    """

    def __init__(self, cake, center, radius):
        self.cake = cake
        self.center = center
        self.radius = radius

    def _unit_angle(self):
        """angle in radians per unit of piece thickness
        """
        return 2*math.pi / sum(self.cake.pieces)

    def display_cake(self, screen):
        # Set the screen background
        screen.fill(black)
        # init values
        x0, y0 = self.center[0], self.center[1]
        cake_area = (x0 - self.radius, y0 - self.radius, 2*self.radius, 2*self.radius)
        myfont = pygame.font.SysFont("Comic Sans MS", 24)
        unit_angle = self._unit_angle()
        angle = 0
        # draw each piece that's not taken
        for cake_piece in range(0, len(self.cake.pieces)):
            piece_angle = self.cake.pieces[cake_piece] * unit_angle
            next_angle = angle + piece_angle
            if not self.cake.is_taken(cake_piece):
                pygame.draw.arc(screen, white, cake_area, angle, next_angle, 2)
                # pygame has no proper arc drawing functions, so we must draw our legs manually
                pygame.draw.line(screen, white, (x0, y0), (x0 + self.radius * math.cos(angle), y0 - self.radius * math.sin(angle)), 2)
                pygame.draw.line(screen, white, (x0, y0), (x0 + self.radius * math.cos(next_angle), y0 - self.radius * math.sin(next_angle)), 2)
                # write thickness as number
                label = myfont.render(str(self.cake.pieces[cake_piece]), 1, red)
                label_x = x0 + self.radius * 0.9 * math.cos((angle + next_angle)/2) - 8
                label_y = y0 - self.radius * 0.9 * math.sin((angle + next_angle)/2) - 8
                screen.blit(label, (label_x, label_y))
            angle = next_angle

    def get_piece(self, pos):
        """return index of piece of cake displayed at coordinates pos=(x,y)
        """
        # check if pos is somwhere on cake
        dx = pos[0] - self.center[0]
        dy = -(pos[1] - self.center[1])
        if dx * dx + dy * dy > self.radius * self.radius: 
            return None
        # clicks right on center can't be resolved either
        if (dx == dy == 0):
            return None
        # get the angle of the pos relative to center
        angle = math.atan2(dy,dx)
        if (angle < 0):
            angle += 2*math.pi
        # translate into number of piece thickness units required
        angle_units = angle / self._unit_angle()
        cake_piece = 0
        size_sum = self.cake.pieces[0]
        while size_sum < angle_units:
            cake_piece += 1
            size_sum += self.cake.pieces[cake_piece]
        return cake_piece
