import pygame
from sys import exit

pygame.init()
menuscreen = pygame.display.set_mode((800,400))
gameScreen = pygame.display.set_mode((800,400))

#Setting Icon and Caption
pygame.display.set_caption("GO GO Yay!")
pygame.display.set_icon(pygame.image.load("pitiful.png"))
clock = pygame.time.Clock()

#Setting Display Variables
currentDisplay = "menuscreen"
currentDisplayData = menuscreen
changecurrentDisplay = False

#All Surfaces
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
font_surface = test_font.render("This Game Is awesome",False,"Orange")
sky_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/ground.png")
snail_surface = pygame.image.load("graphics/snail/snail1.png")
start_button = pygame.image.load("graphics/Player/jump.png")
start_text_surface = test_font.render("Click Me to play!",False,"Lightblue")

#Fuction: Checks for Mouse Click on Object
def click(objectX,objectY,ObjectWidth,ObjectHeight):
    mouseIsClicked = "null"
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseIsClicked = True
    cursor_pos = pygame.mouse.get_pos()
    cursor_posX = cursor_pos[0]
    cursor_posY = cursor_pos[1]
    if (int(cursor_posX) >= int(objectX)) and (int(cursor_posX) <= (int(objectX) + ObjectWidth)) and (int(cursor_posY) >= int(objectY)) and (int(cursor_posY) < (int(objectY) + ObjectHeight)) and (mouseIsClicked == True):
        return True
    else:
        return False


# Centers Object In Y, X, or both axis
def center(ObjectWidth, ObjectHeight):
    displayHeight = currentDisplayData.get_height()
    displayWidth = currentDisplayData.get_width()
    if ObjectWidth == 0:
        NewYcenter = displayHeight/2 - ObjectHeight/2
        return NewYcenter
    if ObjectHeight == 0:
        NewXcenter = displayWidth/2 - ObjectWidth/2
        return NewXcenter
    else: 
        Newcenter = [displayWidth/2 - ObjectWidth/2, displayHeight/2 - ObjectHeight/2]
        return Newcenter
    
#Inital variables for gameScreen
snail_x_position = 600

#GameLoop
while True:
    
    #Quitting Mechanism
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    #Check is display is changed; if so, update display
    if changecurrentDisplay == True:
        if currentDisplay == "menuscreen":
            currentDisplay = "gameScreen"
            changecurrentDisplay == False
            currentDisplayData == gameScreen
    
    

    if currentDisplay == "gameScreen":

        #Draw Game Surfaces to gameScreen when loaded
        gameScreen.blit(sky_surface,(0,0))
        gameScreen.blit(ground_surface,(0,300))
        gameScreen.blit(font_surface,(center(font_surface.get_width(),0),100))
        gameScreen.blit(snail_surface,(snail_x_position,265))

        #Snail Mechanism
        snail_x_position -= 4
        if snail_x_position < -100:snail_x_position = 800


    elif currentDisplay == "menuscreen": 

        #Draw Surfaces to Start Menu
        menuscreen.blit(start_button,center(start_button.get_width(),start_button.get_height()))
        menuscreen.blit(start_text_surface,(center(start_text_surface.get_width(),0),100))

         # Check if start_button is being clicked (CLEAN UP LATER [New class called button])
        if click(center(start_button.get_width(),0),center(0,start_button.get_height()),start_button.get_width(),start_button.get_height()) == True:
            changecurrentDisplay = True

    #update Display
    pygame.display.update()

    #60 fps Capped
    clock.tick(60)
