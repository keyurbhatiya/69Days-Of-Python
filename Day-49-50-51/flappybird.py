################################## Day 49: 69 Days of Python #####################################

# Day 49: 69 Days of Python

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



# Day 50: 69 Days of Python


# creating a class of the pygame's Sprite() class to display the bird  
class FlappyBird(pygame.sprite.Sprite):  
    # defining an initializing function  
    def __init__(self, x_coordinate, y_coordinate):  
        pygame.sprite.Sprite.__init__(self)  
  
        # creating an empty list  
        self.image_list = []  
        # setting the index and counter value to 0  
        self.index = 0  
        self.counter = 0  
  
        # iterating through the range of 1 to 4  
        for i in range(1, 4):  
            # loading the sprite bird images from the directory  
            # using the load() function of the pygame.image module  
            image = pygame.image.load(f'images/bird_{i}.png')  
              
            # using the append() function to add the image to the list  
            self.image_list.append(image)  
  
        # setting the current image  
        self.image = self.image_list[self.index]  
          
        # creating a rectangle to place the bird image      
        self.rect = self.image.get_rect()  
  
        # setting the position of the bird  
        self.rect.center = [x_coordinate, y_coordinate]  
      
    # defining a function to handle the animation  
    def update(self):  
  
        # updating the counter by 1  
        self.counter += 1  
        # defining a variable to display the sprite cooldown  
        flapCooldown = 5  
  
        # if the counter value is greater than the cooldown  
        # value set the counter value to 0  
        if self.counter > flapCooldown:  
            self.counter = 0  
              
            # updating the index value by 1  
            self.index += 1  
  
            # if the index value is greater than or equal to the  
            # length of the list, set the index value to 0  
            if self.index >= len(self.image_list):  
                self.index = 0  
  
        # updating the current image  
        self.image = self.image_list[self.index]  
          
# creating an object of the Group() class of the pygame.sprite module  
birdGroup = pygame.sprite.Group()  
  
# creating an object of the FlappyBird() class with  
bird = FlappyBird(200, int(SCREEN_HEIGHT / 2))  
  
# using the add() function to add the object of the FlappyBird() class to the group  
birdGroup.add(bird)  


# using the while loop  
while game_run:  
  
    # setting the fps of the game  
    game_clock.tick(game_fps)  
  
    # drawing the background  
    display_screen.blit(background, (0, 0))  
  
    # drawing the bird  
    birdGroup.draw(display_screen)  
  
    # calling the update() function  
    birdGroup.update()  
  
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



# declaring and initializing the game variables  
birdFlying = False  
gameOver = False  

# creating a class of the pygame's Sprite() class to display the bird  
class FlappyBird(pygame.sprite.Sprite):  
    # defining an initializing function  
    def __init__(self, x_coordinate, y_coordinate):  
        pygame.sprite.Sprite.__init__(self)  
          
        # code to initialize variables for sprite bird animation  
        # ...  
        # ...  
        # ...  
  
        # defining the initial velocity of the bird  
        self.velocity = 0  
        self.pressed = False  
      
    # defining a function to handle the animation  
    def update(self):  
        # if the bird is flying then run this code  
        if birdFlying == True:  
            # adding gravity to the bird  
            # incrementing the velocity of the bird  
            self.velocity += 0.5  
  
            # if the velocity of the bird is greater than 8.5  
            # then set the final value to 8.5  
            if self.velocity > 8.5:  
                self.velocity = 8.5  
            # if the rectangle's bottom is less than 576  
            # then increment its y-axis value by velocity's integer value   
            if self.rect.bottom < 576:  
                self.rect.y += int(self.velocity)  
  
        # if the game is not over then run this code  
        if gameOver == False:  
            # if the mouse button is clicked  
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:  
                # setting the pressed variable value to True  
                self.pressed = True  
                # setting the velocity to -10  
                self.velocity = -10  
  
            # if the mouse button is released  
            if pygame.mouse.get_pressed()[0] == 0:  
                # setting the pressed variable value to False  
                self.pressed = False  
  
            # ...  
            # ...  
            # ...  
            # the sprite animation's update() function code  
              
            # rotating the bird  
            self.image = pygame.transform.rotate(self.image_list[self.index], self.velocity * -2)  
        # if the game is over  
        else:  
            # rotating the bird to -90  
            self.image = pygame.transform.rotate(self.image_list[self.index], -90)  
            # using the while loop  
while game_run:  
    # setting the fps of the game  
    game_clock.tick(game_fps)  
  
    # drawing the background  
    display_screen.blit(background, (0, 0))  
  
    # drawing the bird  
    birdGroup.draw(display_screen)  
  
    # calling the update() function  
    birdGroup.update()  
  
    # drawing the base  
    display_screen.blit(base, (baseScroll, 576))  
  
    # checking if bird has hit the ground  
    if bird.rect.bottom > 576:  
        gameOver = True  
        birdFlying = False  
  
    # checking if the game is not over  
    if gameOver == False:  
        # scrolling the base  
        baseScroll -= scrollSpeed  
        if abs(baseScroll) > 70:  
            baseScroll = 0  
  
    # using the for loop to iterate through the events of the game  
    for event in pygame.event.get():  
        # setting the variable value to False if the event's type is equivalent to pygame's QUIT constant  
        if event.type == pygame.QUIT:  
            game_run = False  
        # setting the variable value to True if the event's type is equivalent to pygame's MOUSEBUTTONDOWN constant, the bird is not flying and game is not over  
        if event.type == pygame.MOUSEBUTTONDOWN and birdFlying == False and gameOver == False:  
            birdFlying = True  
  
    # using the update() function of the pygame.display module to update the events of the game  
    pygame.display.update()  



''' Adding Scrolling Pipes to the Game -> Day 51: 69 Days of Python '''


# declaring and initializing the game variables  
pipeGap = 150  
pipeFrequency = 1450 # milliseconds  
lastPipe = pygame.time.get_ticks() - pipeFrequency  

# creating a class of the pygame's Sprite() class to display the pipes  
class Pipe(pygame.sprite.Sprite):  
    # defining an initializing function  
    def __init__(self, x_coordinate, y_coordinate, position):  
        pygame.sprite.Sprite.__init__(self)  
        # loading the sprite pipe image from the directory  
        # using the load() function of the pygame.image module  
        self.image = pygame.image.load('images/pipe.png')  
          
        # creating a rectangle to place the pipe image  
        self.rect = self.image.get_rect()  
  
        # position 1 is from the top, -1 is from the bottom  
        if position == 1:  
            self.image = pygame.transform.flip(self.image, False, True)  
            self.rect.bottomleft = [x_coordinate, y_coordinate - int(pipeGap / 2)]  
        if position == -1:  
            self.rect.topleft = [x_coordinate, y_coordinate + int(pipeGap / 2)]  
  
    # defining a function to handle pipes animation and memory  
    def update(self):  
        # setting the scroll speed of the pipes  
        self.rect.x -= scrollSpeed  
  
        # destroying the pipes once they left the screen to release the memory  
        if self.rect.right < 0:  
            self.kill()  
  
# creating an object of the Group() class of the pygame.sprite module  
pipeGroup = pygame.sprite.Group()  


# using the while loop  
while game_run:  
    # setting the fps of the game  
    game_clock.tick(game_fps)  
  
    # drawing the background  
    display_screen.blit(background, (0, 0))  
  
    # drawing the bird  
    birdGroup.draw(display_screen)  
  
    # calling the update() function  
    birdGroup.update()  
  
    # drawing the pipes  
    pipeGroup.draw(display_screen)  
  
    # drawing the base  
    display_screen.blit(base, (baseScroll, 576))  
  
    # looking for collision  
    if pygame.sprite.groupcollide(birdGroup, pipeGroup, False, False) or bird.rect.top < 0:  
        gameOver = True  
  
    # checking if bird has hit the ground  
    if bird.rect.bottom >= 576:  
        gameOver = True  
        birdFlying = False  
  
    # checking if the game is not over  
    if gameOver == False and birdFlying == True:  
  
        # generating new pipes  
        timeNow = pygame.time.get_ticks()  
        if timeNow - lastPipe > pipeFrequency:  
            pipeHeight = random.randint(-100, 100)  
            bottomPipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT / 2) + pipeHeight, -1)  
            topPipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT / 2) + pipeHeight, 1)  
            pipeGroup.add(bottomPipe)  
            pipeGroup.add(topPipe)  
            lastPipe = timeNow  
  
        # scrolling the base  
        baseScroll -= scrollSpeed  
        if abs(baseScroll) > 70:  
            baseScroll = 0  
        # calling the update() function  
        pipeGroup.update()  
  
    # using the for loop to iterate through the events of the game  
    for event in pygame.event.get():  
        # setting the variable value to False if the event's type is equivalent to pygame's QUIT constant  
        if event.type == pygame.QUIT:  
            game_run = False  
        # setting the variable value to True if the event's type is equivalent to pygame's MOUSEBUTTONDOWN constant, the bird is not flying and game is not over  
        if event.type == pygame.MOUSEBUTTONDOWN and birdFlying == False and gameOver == False:  
            birdFlying = True  
  
    # using the update() function of the pygame.display module to update the events of the game  
    pygame.display.update()  


'''NEXT TOPIC: Creating a Score Counter in the Game -> Day 52: 69 Days of Python'''