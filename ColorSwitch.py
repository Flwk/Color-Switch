import pygame, math, random

pygame.init() # initialisation du module "pygame"

fenetre = pygame.display.set_mode( (600,800) ) # Création d'une fenêtre graphique de taille 600x600 pixels
pygame.display.set_caption("Color Switch") # Définit le titre de la fenêtre

# On définit les variables qui contiendront les positions des différents éléments (vaisseau, alien, projectile)
# Chaque position est un couple de valeur '(x,y)'
positionDepart = (300,525)
projectile = (300,600)
CoordonneArc=(300,350)
vitesse=1

#On va créé les coordonné pour le rectangle
CoorC1=(-200,-400)
CoorC2=(-400,-400)
CoorC3=(-400,-200)
CoorC4=(-200,-200)
r=100 * math.sqrt(5)
a=300
bC = -100
bT = -1200

imagescore = pygame.image.load("Roue.png").convert()
imagescore = pygame.transform.scale(imagescore,(25,25))

#On va créé les coordonné pour le triangle
zz=-100*(math.sqrt(3)-4)
CoorT1=(200,400)
CoorT2=(400,400)
CoorT3=(300,zz)
r=(800/3) - (200*math.sqrt(3)/3)
a=300
bT=-400 - (100*math.sqrt(3))/3
tour=1

#les variables pour le cercle
angle0 = 0
angle=math.pi
angle2=math.pi/2
angle3=math.pi*3/2
angle4=math.pi*2
angle5=math.pi/4560
rect=pygame.Rect(150,-1100,300,300)

#Les variables pour les twin circles
angle01 = 0
angle1=math.pi
angle21=math.pi/2
angle31=math.pi*3/2
angle41=math.pi*2

angle02 = 0
angle221=math.pi
angle22=math.pi/2
angle32=math.pi*3/2
angle42=math.pi*2

recttw1 =pygame.Rect(150,-1250,150,150)
recttw2 = pygame.Rect(300,-1250,150,150)


# On crée les variables pour les positions de segment
x1 = 1
x11 = 150
x2 = 150
x22 = 300
x3 = 300
x33 = 450
x4 = 450
x44 = 600
Yline = -1300 #ici l'ordonnée variable de l'obstacle pour le défilement de l'écran

#on créé des variables pour les couleurs

red=(255,0,0)
jaune=(255, 228, 54)
bleu=(43, 250, 250)
violet=(121, 28, 248)

#On créé une liste où on ajoutera les couleurs
seq=[]
seq.append(red)
seq.append(jaune)
seq.append(red)
seq.append(bleu)


#On assigne au hasard une couleur au projectile
couleurProjectile = random.choice(seq)
##couleurProjecilte = Couleur1
t=math.pi/4
def rectangle():
    global fenetre,red,bleu,jaune,violet,CoorC1,CoorC2,CoorC3,CoorC4,r,a,b,t,x
    x=1
    for x in range(1,1000):
         pygame.draw.line(fenetre,red,CoorC1,CoorC2,5)
         pygame.draw.line(fenetre,jaune,CoorC1,CoorC4,5)
         pygame.draw.line(fenetre,bleu,CoorC2,CoorC3,5)
         pygame.draw.line(fenetre,violet,CoorC3,CoorC4,5)
         CoorC4 = [a + r*(math.cos(t)),bC + r*(math.sin(t))]
         CoorC3 = [a - r*(math.sin(t)),bC + r*(math.cos(t))]
         CoorC2 = [a - r*(math.cos(t)),bC - r*(math.sin(t))]
         CoorC1 = [a + r*(math.sin(t)),bC - r*(math.cos(t))]
         t = t - math.pi/60000


def  triangle():
    global fenetre,red,bleu,jaune,violet,CoorT1,CoorT2,CoorT3,r,a,b,t,x,line1,line2,line3
    x=1

    for x in range(1,10):

         line1=pygame.draw.line(fenetre,red,CoorT1,CoorT2,5)
         line2=pygame.draw.line(fenetre,jaune,CoorT1,CoorT3,5)
         line3=pygame.draw.line(fenetre,bleu,CoorT3,CoorT2,5)
         CoorT3 = [a + r*(math.cos(t)),bT + r*(math.sin(t))]
         CoorT2 = [a + r*(math.cos(2*math.pi/3 + t )),bT + r*(math.sin(2*math.pi/3 + t))]
         CoorT1 = [a + r*(math.cos(-2*math.pi/3 + t)),bT + r*(math.sin(-2*math.pi/3 + t))]
         t = t - math.pi/400000

CoordInf=(400,400)
teta=math.pi/1000
def infini():
        global CoordInf,teta
        for x in range(1,100):
           pygame.draw.circle(fenetre, red , CoordInf, 7)
           CoordInf= ((pow(math.cos(teta),2)  * math.cos(math.pi/4)),(pow(math.cos(teta),2)  * math.sin(math.pi/4)))
           teta = teta + math.pi/6000



def cercle():
    global angle0, angle, angle1, angle2,angle3,angle4,angle5,rect
    for x in range(0,100):
        arc1 = pygame.draw.arc(fenetre, red , rect, angle0 , angle2,5)
        arc2 = pygame.draw.arc(fenetre, jaune, rect, angle2 , angle,5)
        arc3 = pygame.draw.arc(fenetre, bleu, rect, angle , angle3,5)
        arc4 = pygame.draw.arc(fenetre, violet, rect, angle3,angle4,5)
        angle0 = angle0 - angle5
        angle = angle - angle5
        angle2 = angle2 - angle5
        angle3 = angle3 - angle5
        angle4 = angle4 - angle5


def twincircles():
    global angle5,angle01,angle1,angle21,angle31,angle41,angle02,angle221,angle22,angle32,angle42,recttw1,recttw2
    for x in range (0,100) :
        arc11 = pygame.draw.arc(fenetre, red , recttw1, angle01 , angle21,10)
        arc21 = pygame.draw.arc(fenetre, jaune, recttw1, angle21 , angle1,10)
        arc31 = pygame.draw.arc(fenetre, bleu, recttw1, angle1 , angle31,10)
        arc41 = pygame.draw.arc(fenetre, violet, recttw1, angle31,angle41,10)

        arc12 = pygame.draw.arc(fenetre, jaune , recttw2, angle02 , angle22,10)
        arc22 = pygame.draw.arc(fenetre, red, recttw2, angle22 , angle221,10)
        arc32 = pygame.draw.arc(fenetre, violet , recttw2, angle221 , angle32,10)
        arc42 = pygame.draw.arc(fenetre, bleu , recttw2, angle32,angle42,10)

        angle01 = angle01 - angle5
        angle1 = angle1 - angle5
        angle21 = angle21 - angle5
        angle31 = angle31 - angle5
        angle41 = angle41 - angle5

        angle02 = angle02 + angle5
        angle221 = angle221 + angle5
        angle22 = angle22 + angle5
        angle32 = angle32 + angle5
        angle42 = angle42 + angle5


def trait():
    global x1,x2,x3,x4,x11,x22,x33,x44,Yline
    for x in range(0,100):
        seg1 = pygame.draw.line(fenetre, red, (x1, Yline), (x11, Yline), 5)
        seg2 = pygame.draw.line(fenetre, bleu, (x2, Yline), (x22, Yline), 5)
        seg3 = pygame.draw.line(fenetre, jaune, (x3, Yline), (x33, Yline), 5)
        seg4 = pygame.draw.line(fenetre, violet, (x4, Yline), (x44, Yline), 5)
        #mouvement du trait
        x1 = x1 + 0.02
        x11 = x11 + 0.02
        x2 = x2 + 0.02
        x22 = x22 + 0.02
        x3 = x3 + 0.02
        x33 = x33 + 0.02
        x4 = x4 + 0.02
        x44 = x44 + 0.02

# LE TRAIT VIOLET
        if x44 > 600 and x4 < 600 :
            seg4 = pygame.draw.line(fenetre, violet, (x4, Yline), (600, Yline), 5)
            segU4 = pygame.draw.line(fenetre, violet, (1, Yline), (x44-600, Yline), 5)
        if x44 > 600 and x4 > 600 :
            x4 = 1
            x44 = 150
            seg4 = pygame.draw.line(fenetre, violet, (x4, Yline), (x44, Yline), 5)
# LE TRAIT JAUNE
        if x33 > 600 and x3 < 600 :
                    seg3 = pygame.draw.line(fenetre, jaune, (x3, Yline), (600, Yline), 5)
                    segU3 = pygame.draw.line(fenetre, jaune, (1, Yline), (x33-600, Yline), 5)
        if x33 > 600 and x3 > 600 :
                    x3 = 1
                    x33 = 150
                    seg3 = pygame.draw.line(fenetre, jaune, (x3, Yline), (x33, Yline), 5)
# LE TRAIT BLEU
        if x22 > 600 and x2 < 600 :
                    seg2 = pygame.draw.line(fenetre, bleu, (x2, Yline), (600, Yline), 5)
                    segU2 = pygame.draw.line(fenetre, bleu, (1, Yline), (x22-600, Yline), 5)
        if x22 > 600 and x2 > 600 :
                    x2 = 1
                    x22 = 150
                    seg2 = pygame.draw.line(fenetre, bleu, (x2, Yline), (x22, Yline), 5)
# LE TRAIT ROUGE
        if x11 > 600 and x1 < 600 :
                    seg1 = pygame.draw.line(fenetre, red, (x1, Yline), (600, Yline), 5)
                    segU1 = pygame.draw.line(fenetre, red, (1, Yline), (x11-600, Yline), 5)
        if x11 > 600 and x1 > 600 :
            x1 = 1
            x11 = 150
            seg1 = pygame.draw.line(fenetre, red, (x1, Yline), (x11, Yline), 5)


chgmt=0



# Fonction en charge de dessiner tous les éléments sur notre fenêtre graphique.
# Cette fonction sera appelée depuis notre boucle infinie
def dessiner():
    global fenetre, projectile,red,bleu,jaune,violet,couleurProjectile,couleurProjectile,Couleur1,rect,Coor1,Coor2,Coor3,r,a,b,tour,Yline,chgmt
    # On remplit complètement notre fenêtre avec la couleur noire: (0,0,0)
    fenetre.fill( (0,0,0) )
    if chgmt==0:
      fenetre.blit(imagescore,(a-13,bC))
    if chgmt==1:
      fenetre.blit(imagescore,(a-13,bT))
    if chgmt==2:
      fenetre.blit(imagescore,(projectile[0]-15,Yline-50))
    if projectile != (-1, -1):
        pygame.draw.circle(fenetre, couleurProjectile , projectile, 7) # On dessine le projectile (un simple petit cercle)
    rectangle()
    triangle()
    cercle()
    trait()
    pygame.display.flip() # Rafraichissement complet de la fenêtre avec les dernières opérations de dessin



# Fonction en charge de gérer les évènements clavier (ou souris)
# Cette fonction sera appelée depuis notre boucle infinie
def gererClavierEtSouris():
    global continuer, positionDepart, projectile, vitesse,rect,Yline,bC,bT,recttw1,recttw2,rect
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Permet de gérer un clic sur le bouton de fermeture de la fenêtre
            continuer = 0
    # Gestion du clavier ainsi que du déplacement du projectile
    touchesPressees = pygame.key.get_pressed()
    if touchesPressees[pygame.K_SPACE] == True:
        projectile = (projectile[0], projectile[1] - 7)
        vitesse = 1
    if touchesPressees[pygame.K_SPACE] == True and projectile[1] <= 400: #Ce if gère le défilement du terrain ( des obstacles ) en fonction de la position du projectile
        projectile = (projectile[0], 400)
        bC = bC + 7
        bT = bT + 7
        rect[1] = rect[1] + 7
        Yline = Yline + 7
        recttw1[1]= recttw1[1] + 7
        recttw2[1]= recttw2[1] + 7
    if bC > 1000 :
        bC = -500
    if bT > 1000 :
        bT = -500
    if rect[1] > 1000 :
        rect[1] = -500
    if Yline > 1000 :
        Yline = -500
    if touchesPressees[pygame.K_SPACE] != True:
        projectile = (projectile[0], projectile[1] + 5)

# On crée une nouvelle horloge qui nous permettra de fixer la vitesse de rafraichissement de notre fenêtre
clock = pygame.time.Clock()

# La boucle infinie de pygame:
# On va continuellement dessiner sur la fenêtre, gérer les évènements et calculer certains déplacements
continuer = 1
while continuer==1:
    # pygame permet de fixer la vitesse de notre:
    # ici on déclare 50 tours par secondes soit une animation à 50 images par secondes
    clock.tick(60)
    dessiner()
    gererClavierEtSouris()


   # On gère la fin de la partie, la détection du passage de l'obstacle et le changement de couleur
    if projectile[1] > 800:
        continuer=0
##    if projectile[1]<800 and couleurProjectile!=fenetre.get_at(projectile):
##        continuer=0

    rectObstacle1 = pygame.Rect(a-50,bC,100,50)
    if  chgmt==0 and rectObstacle1.collidepoint(projectile):
        couleurProjectile=random.choice(seq)
        chgmt=1
    rectObstacle2 = pygame.Rect(a-50,bT,100,50)
    if  chgmt==1 and rectObstacle2.collidepoint(projectile):
        couleurProjectile=random.choice(seq)
        chgmt=2
    rectObstacle3 = pygame.Rect(300,Yline-40,100,50)
    if chgmt==2 and rectObstacle3.collidepoint(projectile):
        couleurProjectile=random.choice(seq)
        chgmt=3

# A la fin, lorsque l'on sortira de la boucle, on demandera à Pygame de quitter proprement
pygame.quit()

