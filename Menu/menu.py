# Créé par el_malla, le 31/03/2017 en Python 3.2
import pygame
from pygame.locals import*

#___________________________________
pygame.init()
fenetre = pygame.display.set_mode( (600,600) )
pygame.display.set_caption(" EL MALLEM ADAM TS02")
##position_image_menu= (300,300)

continuer=0

#______________image___________________________
image1 = pygame.image.load("MENU.png").convert()
image2 = pygame.image.load("MENU 1.png").convert()
image3 = pygame.image.load("MENU 2.png").convert()
image4 = pygame.image.load("MENU 3.png").convert()
#________________variables_______________
FOND=0

#_________________________________________
def Menu():
    global image1,image2,image3,image4,FOND
    if FOND ==0:
        fenetre.blit(image1,(0,0))
    elif FOND==1:
        fenetre.blit(image2,(0,0))
    elif FOND==2:
        fenetre.blit(image3,(0,0))
    elif FOND==3:
        fenetre.blit(image4,(0,0))
    pygame.display.flip()

def CLICK():
    global continuer
    touchesPressees=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer=0
        elif event.type== MOUSEBUTTONDOWN:
            continuer=1

def souris():
    global continuer,image1,FOND
    coord=pygame.mouse.get_pos()

    if 34<coord[0]<244 and 492<coord[1]<524:
        FOND=1
    elif 337<coord[0]<578 and 492<coord[1]<524:
        FOND=2
    elif 244<coord[0]<336 and 258<coord[1]<338:
        FOND=3
    else:
        FOND=0

continuer = 1
while continuer==1:
    souris()
    Menu()
    CLICK()



pygame.quit()
