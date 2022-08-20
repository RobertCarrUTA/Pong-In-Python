import pygame, sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Game Rectangle
# The ball is 30 pixels high, and 30 pixels wide
# To place the ball in the center of the window we need to find the center, # we do this, for example,
# by dividing screen_width and screen_height by 2. This isn't enough, because we would be off by a little
# bit. So we have to account for the area occupied by the ball. We do this by finding the center of the ball,
# this is why we subtract 15 each time, because the ball is 30x30 pixels wide.
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)

# Player 1:
# Player 1 is the rectangle on the left side of the window, 10 pixels wide, and 140 pixels high
player1 = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Player 2:
# Player 2 is the rectangle on the right side of the window, 10 pixels wide, and 140 pixels high
player2 = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

while True:
    # Handle input
    for event in pygame.event.get():
        # In the case that the user closes the game by pressing X
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Drawing the objects and the background
    # Keep in mind the order in which things are drawn. They are drawn in order, so the first first thing to be
    # drawn will be the bottom layer, in this case, our background, then the last thing to be drawn will be the top
    # layer, in this case, our dividing line
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player1)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.ellipse(screen, light_grey, ball)

    # Drawing the line that divides the two sides
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
