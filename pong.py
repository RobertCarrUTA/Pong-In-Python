# This program will have a lot of comments because it is for my learning, I want to be able to remember
# why I did something long after this program was made.

import pygame, sys, random

def ball_animation_collision():
    global ball_speed_x, ball_speed_y # Only use this approach because the program is simple
    
    # Moving the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Setting the boundaries for the ball
    # Think of a graph and how a line gets flipped. Multiplying a y or x by -1 will make the line look
    # as if it has been deflected, we use that here to give the impression that the ball is bouncing and
    # it is why we use the *= -1's.
    #
    # If the ball hits the top or the bottom of the window, bounce it off the boundary
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    # If the ball hits the left or right of the window, reset it
    if ball.left <= 0 or ball.right >= screen_width:
        ball_reset()

    # Detecting ball collisions with the paddles (or players), speed it up every time a player hits the ball
    if ball.colliderect(opponent) or ball.colliderect(player2):
        ball_speed_x *= -1
        ball_speed_x *= 1.03
        ball_speed_y *= 1.03

def ball_reset():
    global ball_speed_x, ball_speed_y # Only use this approach because the program is simple
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_x =  7 * random.choice((1, -1))
    ball_speed_y = 7 * random.choice((1, -1))

def player2_movement():
    player2.y += player2_speed

    # Player 2 border detection
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height

def opponent_ai_movement():
    # Make the opponent try to block the ball
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    
    # Opponent border detection
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Game Rectangle
# The ball is 30 pixels high, and 30 pixels wide
# To place the ball in the center of the window we need to find the center, # we do this, for example,
# by dividing screen_width and screen_height by 2. This isn't enough, because we would be off by a little
# bit. So we have to account for the area occupied by the ball. We do this by finding the center of the ball,
# this is why we subtract 15 each time, because the ball is 30x30 pixels wide.
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)

# Opponent:
# Opponent is the rectangle on the left side of the window, 10 pixels wide, and 140 pixels high
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Player 2:
# Player 2 is the rectangle on the right side of the window, 10 pixels wide, and 140 pixels high
player2 = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
opponent_speed = 7
player2_speed = 0

while True:
    # Handle input
    for event in pygame.event.get():
        # In the case that the user closes the game by pressing X
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # If player 2 presses up on the keyboard
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player2_speed += 7
            if event.key == pygame.K_UP:
                player2_speed -= 7
        # If player 2 presses down on the keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player2_speed += 7
            if event.key == pygame.K_UP:
                player2_speed -= 7

    ball_animation_collision()
    player2_movement()
    opponent_ai_movement()

    # Drawing the objects and the background
    # Keep in mind the order in which things are drawn. They are drawn in order, so the first first thing to be
    # drawn will be the bottom layer, in this case, our background, then the last thing to be drawn will be the top
    # layer, in this case, our dividing line
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.ellipse(screen, light_grey, ball)

    # Drawing the line that divides the two sides
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
