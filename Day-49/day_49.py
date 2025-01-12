################################## Day 49: 69 Days of Python #####################################

# Flappy Bird Game using PyGame in Python

'''
Step 1: Firstly, we will import the required modules.

Step 2: We will then create a Scrolling background.

Step 3: This step involves adding the Sprite Animation to the Game.

Step 4: We will then add some physics to the Game.

Step 5: In this step, we will add the scrolling pipes to the Game.

Step 6: We will then add a score counter.

Step 7: We will last add functions for game over and reset the game.
'''



# importing the required modules  
import pygame               # importing the pygame module  
from pygame.locals import * # importing everything from the pygame.locals module  
import random               # importing the random module  


# Scrolling background
# using the init() function to initialize the pygame window  
pygame.init()  
  
# creating an object of the Clock() class of the pygame.time module  
game_clock = pygame.time.Clock()  
  
# defining the fps for the game  
game_fps = 60  
  
# defining the width and height of the game screen  
SCREEN_WIDTH = 750  
SCREEN_HEIGHT = 900  
  
# using the set_mode() function of the pygame.display module to set the size of the screen  
display_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
  
# setting the title of the application using the set_caption() function  
pygame.display.set_caption('Flappy Bird - JAVATPOINT')  
  
# declaring and initializing the game variables  
baseScroll = 0  
scrollSpeed = 4  
  
# loading images  
background = pygame.image.load('images/background.png')  
base = pygame.image.load('images/base.png')  
  
# declaring a variable and initializing its value with True  
game_run = True  
  
# using the while loop  
while game_run:  
    # setting the fps of the game  
    game_clock.tick(game_fps)  
  
    # drawing the background  
    display_screen.blit(background, (0, 0))  
  
    # drawing and scrolling the base  
    display_screen.blit(base, (baseScroll, 768))  
    baseScroll -= scrollSpeed  
    if abs(baseScroll) > 70:  
        baseScroll = 0  
  
    # using the for loop to iterate through the events of the game  
    for event in pygame.event.get():  
        # setting the variable value to False if the event's type is equivalent to pygame's QUIT constant  
        if event.type == pygame.QUIT:  
            game_run = False  
  
    # using the update() function of the pygame.display module to update the events of the game  
    pygame.display.update()  
  
# using the quit() function to quit the game  
pygame.quit()  




