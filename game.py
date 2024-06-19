# import libraries
import pygame   
import sys
import random

# initialize pygame 
pygame.init()

# set screen dimensions
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Word.io")

# load wheel 
wheel_img = pygame.image.load("./assets/wheel.jpg")

# spin wheel func
def spinWheel():
    # prizes array
    prizes = ["$500 in debt", "Skipped, Loser", "Your broke", "Grandmas secret Mac&Cheese recipe", "A free application into the military", "A date with your highschool principal"]

    # pick random prize
    prize_selected = random.choice(prizes)

    # return prize
    return prize_selected

# game loop
# while loop
active = True
while active:

    # choice 
    for event in pygame.event.get():

        # exit game 
        if event.type == pygame.QUIT:

            # end loop
            active = False

        # spin again
        if event.type == pygame.KEYDOWN:

            # spin the wheel 
            if event.key == pygame.K_SPACE:

                # spin and get result
                res = spinWheel()

                # debug
                print("Result:", res)  

    # display results
    screen.fill((255, 255, 255))  
    screen.blit(wheel_img, (50, 50)) 

    pygame.display.flip()

# end game
pygame.quit()