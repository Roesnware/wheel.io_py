## Implement 
##  - new dashboard with start button (use wheel.jpg)
##  - user input (oppurtunity to add new list)
##  - actual generated wheel (turtle draw wheel with spaces for each input)
##  - wheel spin animation (spin wheel and slow to stop on result)

# import libraries
import pygame   
import sys 
import random 

# initialize pygame 
pygame.init() 
pygame.font.init() 

# set screen dimensions
screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Wheel.io")

# spin wheel func
def spinWheel():
    # prizes array
    prizes = ["Naruto", "Bleach", "One Piece", "Tokyo Ghoul", "JJK", "Akame ga kill"]

    # pick random prize
    prize_selected = random.choice(prizes)

    # return prize
    return prize_selected

# display dashboard screen func
def showDash():
# render dash text 
    welcome_text = pygame.font.SysFont('Comic Sans MS', 50)
    text_surface = welcome_text.render('Welcome to Wheel.io', False, (255, 255, 255))
    screen.blit(text_surface, (145,240))

    welcome_text = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = welcome_text.render('Press any key to continue!', False, (255, 255, 255))
    screen.blit(text_surface, (195,300))

# display wheel screen func
def showWheel():
# load wheel 
    wheel_img = pygame.image.load("wheel.JPG")
    screen.fill((0, 0, 0))  
    screen.blit(wheel_img, (5, 115)) 

def displayResult(res):
    # render dash text 
    res_text = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = res_text.render(res, False, (255, 255, 255))
    screen.blit(text_surface, (300,50))

# game loop
# while loop
showDash() 
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
            pygame.display.update()
            showWheel()

            # spin the wheel 
            if event.key == pygame.K_SPACE:

                # spin and get result
                res = spinWheel()

                # debug
                print("Result:", res)
                displayResult(res)

    pygame.display.flip()

# end game
pygame.quit()