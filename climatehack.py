import pygame
import random
import pygame, sys
pygame.init()

#variables
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Climate Escape!")
clock = pygame.time.Clock()

def button(text, x, y, width, height, size, icolour, acolour, action = None):
    #Detects user input from mouse
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #Checks position of mouse to be in the button area
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, acolour,(x, y, width, height))
        if click[0] == 1 and action != None:
            action() #activates action
    else:
        #Changes button colour
        pygame.draw.rect(gameDisplay, icolour,(x, y, width, height))

    #Text of button
    largeText = pygame.font.Font('freesansbold.ttf', size)
    textSurf, textRect = textObjects(text, largeText, BLACK)   
    textRect.center = (x+(width/2), y+(height/2))
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
     rect_x = (DISPLAY_WIDTH * 0.45)
     
def quitGame():
    pygame.quit()
    sys.exit()
    quit()

#main display
def menu():
     #Declaration of variables    
    gameExit = True
   
    while gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                gameExit = False
                quit()
        gameDisplay.fill(BLACK)

        #Displays name
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        textSurf, textRect = textObjects("CLIMATE ESCAPE", largeText, BRIGHT_YELLOW)   
        textRect.center = (400, 300)
        gameDisplay.blit(textSurf, textRect)


        largeText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = textObjects("WINS: "+str(wins. count('1')), largeText, BRIGHT_GREEN)   
        textRect.center = (200, 300)
        gameDisplay.blit(textSurf, textRect)


        #Buttons to quit, start, and how to play the game
        button("QUIT", 500, 350, 200, 50, 20, BRIGHT_RED, RED, quitGame)      
        button("START", 100, 350, 200, 50, 20, BRIGHT_GREEN, GREEN, gameLoop)
        button("HOW TO PLAY", 300, 350, 200, 50, 20, BRIGHT_YELLOW, YELLOW, instructions)
 
        pygame.display.update()
        clock.tick(60)
menu()
