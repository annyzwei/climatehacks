import pygame
import random
import pygame, sys
pygame.init()

#variables
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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

def makeroom():
    pygame.draw.rect(gameDisplay, WHITE,(35, 50, DISPLAY_WIDTH-70, DISPLAY_HEIGHT-100)) 
    pygame.draw.rect(gameDisplay, WHITE,(50, 35, DISPLAY_WIDTH-100, DISPLAY_HEIGHT-70)) 

def gameLoop():
     rect_x = (DISPLAY_WIDTH * 0.45)
     
def quitGame():
    pygame.quit()
    sys.exit()
    quit()
    
def textObjects(text, font, colour):
    textSurface = font.render(text, True, colour)
    #returns text + rectangle
    return textSurface, textSurface.get_rect()

#main display
def menu():
     #Declaration of variables    
    gameExit = True
    makeroom()
    while gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                gameExit = False
                quit()
       # gameDisplay.fill(BLACK)

        #Displays name
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        textSurf, textRect = textObjects("CLIMATE ESCAPE", largeText, BLACK)   
        textRect.center = (400, 300)
        gameDisplay.blit(textSurf, textRect)


       # largeText = pygame.font.Font('freesansbold.ttf', 20)
       # textSurf, textRect = textObjects("Test", largeText, BLACK)   
       # textRect.center = (200, 300)
       # gameDisplay.blit(textSurf, textRect)

 
        pygame.display.update()
        clock.tick(60)
menu()
