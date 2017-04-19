# Cree par moi, le 16/04/2017 en Python 3.2
# -*- coding: utf-8 -*-

#===============================================MENU======================================================#
continuer=1 # On lance tout d'abord le menu
while continuer!=0:  #On lane une boucle infini qui va nous permettre de relance le jeu à l'infini
        import pygame, math, random #On importe les différentes bibliotheques que nous allons utilisé
        from pygame.locals import*  #On importe certaines fonctions qui nous serons utile pour le Menu
        pygame.init() # initialisation du module "pygame"
        fenetre = pygame.display.set_mode( (600,800) ) # Creation d'une fenêtre graphique de taille 600x600 pixels
        pygame.display.set_caption("Color Switch") # Definit le titre de la fenêtre
        #______________image___________________________
        image1 = pygame.image.load("MENU.png").convert()
        image2 = pygame.image.load("MENU 1.png").convert()
        image3 = pygame.image.load("MENU 2.png").convert()
        image4 = pygame.image.load("MENU 3.png").convert()
        image5 = pygame.image.load("GO.png").convert()
        #________________variables_______________
        FOND=0

        #_________________________________________

        #Gerer l'affichage du menu
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

        #Gerer le clique de la souris en fonction de sa position
        mode=0
        time=0
        def CLICK():
            global continuer,coord
            touchesPressees=pygame.key.get_pressed()
            coord=pygame.mouse.get_pos()
            if continuer==5:
              for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN and event.button == 1 and 337<coord[0]<578 and 660<coord[1]<700:
                               continuer=1
            if continuer==1:
              for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        continuer=0
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and 34<coord[0]<244 and 650<coord[1]<700:
                        continuer=4
                        mode=1 #On affecte 1 à mode, ce qui va nous servir pour l'affichage du temps au Game Over
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and 337<coord[0]<578 and 660<coord[1]<700:
                        continuer=2


        #Gerer le changement du fond de l'image en fonction de la position de la souris

        def souris():
            global continuer,image1,FOND
            coord=pygame.mouse.get_pos()

            if 34<coord[0]<244 and 650<coord[1]<700:
                FOND=1
            elif 337<coord[0]<578 and 660<coord[1]<700:
                FOND=2
            elif 244<coord[0]<336 and 658<coord[1]<538:
                FOND=3
            else:
                FOND=0
        clock = pygame.time.Clock()
        # On lance le menu
        while continuer==1:
            # pygame permet de fixer la vitesse de notre:
            # ici on dÃ©clare 60 tours par secondes soit une animation Ã  50 images par secondes
            clock.tick(60)
            souris()
            Menu()
            CLICK()
            timeInit=pygame.time.get_ticks()/1000


        #================================================================================================#


        #Variable pour gerer le score et le temps

        font = pygame.font.SysFont("arial", 20)
        score=0
        # On definit les variables qui contiendront les positions des differents elements comme le projectile
        # Chaque position est un couple de valeur '(x,y)'
        projectile = (300,600)
        CoordonneArc=(300,350)

        #On va cree les coordonne pour le rectangle
        CoorC1=(-200,-400)
        CoorC2=(-400,-400)
        CoorC3=(-400,-200)
        CoorC4=(-200,-200)
        r=100 * math.sqrt(5)
        a=300

        #Ce sont les y du carré et du triangle
        bC = -100
        bT = -1200

        #On va cree les variable pour afficher la roue et la redimenssioner

        imagescore = pygame.image.load("Roue.png").convert()
        imagescore = pygame.transform.scale(imagescore,(25,25))

        #On va cree les coordonne pour le triangle
        zz=-100*(math.sqrt(3)-4)
        CoorT1=(200,-400)
        CoorT2=(400,-400)
        CoorT3=(300,-zz)
        r=(800/3) - (200*math.sqrt(3)/3)
        a=300
        bT=-400 - (100*math.sqrt(3))/3
        t=math.pi/4

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

        #On cree ldes deux rectangles pour les twins cercles

        recttw1 =pygame.Rect(150,-1550,150,150)
        recttw2 = pygame.Rect(300,-1550,150,150)


        # On cree les variables pour les positions de segment
        x1 = 1
        x11 = 150
        x2 = 150
        x22 = 300
        x3 = 300
        x33 = 450
        x4 = 450
        x44 = 600
        Yline = -1300 #ici l'ordonnee variable de l'obstacle pour le defilement de l'ecran

        #on cree des variables pour les couleurs

        red=(255,0,0)
        jaune=(255, 228, 54)
        bleu=(43, 250, 250)
        violet=(121, 28, 248)

        #On cree une liste où on ajoutera les couleurs
        seq=[]
        seq.append(red)
        seq.append(jaune)
        seq.append(violet)
        seq.append(bleu)


        #On assigne au hasard une couleur au projectile
        couleurProjectile = random.choice(seq)

        #On cree la fonction rectangle qui va afficher le rectangle et le faire tourenr
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

        #On cree la fonction triangle qui va afficher le triangle et le faire tourenr
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

        #On cree la fonction cercle qui va afficher le cercle et le faire tourenr
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

        #On cree la fonction twincercle qui va afficher le twincercle et le faire tourenr
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

        #On cree la fonction trait qui va afficher le trait et le faire se deplacer sur lui même
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

        #On cree les conditions pour faire reapparaître le trait de l'autre côte de l'ecran

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

        #On cree des variables qui vont nous servir à gerer l'apparition/disparition de la roue
        chgmt=0
        chgmtC=0
        chgmtT=0
        chgmtY=0
        chgmtCe=0

        #ligne du mode time
        YlineMT = 700

        #La fonction qui va gerer le mode time et qui va afficher la barre
        def modetime() :
            global YlineMT
            LineMT = pygame.draw.line(fenetre, (255,255,255), (0, YlineMT), (600, YlineMT), 10)


        # Fonction en charge de dessiner tous les elements sur notre fenêtre graphique.
        # Cette fonction sera appelee depuis notre boucle infinie
        def dessiner():
            if continuer!=5 or continuer!=0 or again==1:
                global fenetre, projectile,red,bleu,jaune,violet,couleurProjectile,couleurProjectile,Couleur1,rect,Coor1,Coor2,Coor3,r,a,b,Yline,chgmt,score,YlineMT,Time,Temps,chgmtCe,mode,time,image5,rebourT
                # On remplit complètement notre fenêtre avec la couleur noire: (0,0,0)
                fenetre.fill( (0,0,0) )
                if chgmtC==0:  #On gère la roue qui se trouve dans le rectangle
                  fenetre.blit(imagescore,(a-13,bC))
                if chgmtT==0: #On gère la roue qui se trouve dans le triangle
                  fenetre.blit(imagescore,(a-13,bT))
                if chgmtY==0: #On gère la roue qui se trouve dans au dessus de trait
                  fenetre.blit(imagescore,(projectile[0]-15,Yline-30))
                if chgmtCe==0:
                    fenetre.blit(imagescore,(projectile[0]-15,rect[1]+150))
                if continuer==2: #On gère le mode score
                        text= font.render("Score :"  + str(score), True, pygame.Color(250,250,50))
                        fenetre.blit(text,(0,0) )
                if projectile != (-1, -1):
                    pygame.draw.circle(fenetre, couleurProjectile , projectile, 7) # On dessine le projectile (un simple petit cercle)
                # On lance les fonctions qui vont afficher les obstacles
                rectangle()
                triangle()
                cercle()
                trait()
##                twincircles() # Fais beaucoup ralentire le jeu
                if continuer==4: #On gère le mode time
                    time=pygame.time.get_ticks()/1000 - timeInit #On calcule le temps qu'il s'est écoulé entre le lancement du jeux et le lancement du mode time
                    Time=round(time,2) #On limite le nombre après la virgule à 0
                    if Time>=2:
                        modetime()
                    text2= font.render("Time :"  + str(Time), 0 , pygame.Color(250,250,250))
                    fenetre.blit( text2 ,(0,0) )
                    mode=1
            if continuer==5: #Si le joueur perd, on lance la page Game Over et on aff
                if mode==0:
                   fenetre.blit(image5,(0,0))
                   text= font.render("Score :"  + str(score), 40, pygame.Color(0,0,0))
                   fenetre.blit(text,(0,0))
                if mode==1:
                   fenetre.blit(image5,(0,0))
                   text2= font.render("Time :"  + str(Time), 40 , pygame.Color(0,0,0))
                   fenetre.blit( text2 ,(0,0) ) #On affiche le temps du joueur
            pygame.display.flip() # Rafraichissement complet de la fenêtre avec les dernières operations de dessin




        # Fonction en charge de gerer les evènements clavier (ou souris)
        # Cette fonction sera appelee depuis notre boucle infinie
        def gererClavierEtSouris():
            global continuer, projectile,rect,Yline,bC,bT,recttw1,recttw2,rect,YlineMT
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Permet de gerer un clic sur le bouton de fermeture de la fenêtre
                    continuer = 0
                    true=1
            # Gestion du clavier ainsi que du deplacement du projectile
            touchesPressees = pygame.key.get_pressed()
            if touchesPressees[pygame.K_SPACE] == True: # On fait monter le projectile
                projectile = (projectile[0], projectile[1] - 7)
                if continuer==4: # Si le mode Time est lance on fait ET que le projectile monte, la barre descend
                    YlineMT = YlineMT  + 5
            if touchesPressees[pygame.K_SPACE] == True and projectile[1] <= 400: #Ce if gère le defilement du terrain ( des obstacles ) en fonction de la position du projectile
                projectile = (projectile[0], 400) # Si le projectile a atteint la moitie de l'ecran, ALORS le projectile n'avance plus et on fait defiler les obstacles
                bC = bC + 7
                bT = bT + 7
                rect[1] = rect[1] + 7
                Yline = Yline + 7
                recttw1[1]= recttw1[1] + 7
                recttw2[1]= recttw2[1] + 7
        #Ici, on va gerer le replacement des obtsacles quand isl disparaissent de l'ecran
            if bC > 1000 : # Si le carre disparait en bas de l'ecran, alors il se remet au dessus de l'ecran pour reapparaître ensuite
                bC = -700
            if bT > 1000 :
                bT = -700
            if rect[1] > 1000 :
                rect[1] = -700
            if Yline > 1000 :
                Yline = -700
            if recttw1[1] and recttw2[1] > 1000:
                recttw1[1]=-700
                recttw2[1]=-700
            if touchesPressees[pygame.K_SPACE] != True: # On gère la chute du projectile si on n'appuie pas sur espace
                projectile = (projectile[0], projectile[1] + 5)
                if continuer==4: # So le mode time est lance ET que la barre espace n'est pas appuye, ALORS la ligne du mode temps MONTE
                    YlineMT = YlineMT - 5
                if YlineMT >= 800 : #La barre du mode temps ne peut pas descendre plus bas que le bas de l'ecran
                    YlineMT = 800



        while continuer==2 or continuer==4: # On lance le mode score si le joueur a clique sur Score
            rebourT = pygame.time.get_ticks()/1000
            clock.tick(60)
            dessiner()
            gererClavierEtSouris()
           # On gere la fin de la partie, la detection  du passage de l'obstacle et le changement de couleur
            if projectile[1] > 800:
                continuer=5
                rebour=pygame.time.get_ticks()/1000
            if projectile[1]<800 and couleurProjectile!=fenetre.get_at(projectile):
                continuer=5
                rebour=pygame.time.get_ticks()/1000
        #Detection de la collision et changement de la couleur
            rectObstacle1 = pygame.Rect(a-50,bC,100,50)
            if  chgmtC==0 and rectObstacle1.collidepoint(projectile): #Si le changement est egale à 0 et que le projectile entre en collsision avec la roue ALORS la couleur est choisi aléatoirement, et le core augmente
                couleurProjectile=random.choice((red,jaune,bleu))
                chgmtC=1
                score=score+1
            if bC > 800: #Une fois que l'obstacle a disparu de l'écran, le changement est egal 0 et la roeu peut ré apparaître
                chgmtC=0
            rectObstacle2 = pygame.Rect(a-50,bT,100,50)
            if  chgmtT==0 and rectObstacle2.collidepoint(projectile):
                couleurProjectile=random.choice((red,jaune,bleu))
                chgmtT=1
                score=score+1
            if bT > 800:
                chgmtT=0
            rectObstacle3 = pygame.Rect(300,Yline-50,100,30)
            if chgmtY==0 and rectObstacle3.collidepoint(projectile):
                couleurProjectile=random.choice(seq)
                chgmtY=1
                score=score+1
            if Yline > 800:
                chgmtY=0
            rectObstacle4 = pygame.Rect(projectile[0],rect[1]+150,20,30)
            if chgmtCe==0 and rectObstacle4.collidepoint(projectile):
                couleurProjectile=random.choice(seq)
                chgmtCe=1
            if rect[1]>800:
                chgmtCe=0

        #On gère la perte d'une partie
        while continuer==5:
            gererClavierEtSouris()
            CLICK()
            clock.tick(60)
            rebour1 = rebour - pygame.time.get_ticks()/1000
            if rebour1 < -3: #La page se ferme au bout de 03 secondes
                 continuer=1
            else :
               dessiner()
        pygame.display.quit() #Ferme l'AFFICHAGE seulement
# A la fin, lorsque l'on sortira de la boucle, on demandera Ã  Pygame de quitter proprement
pygame.quit()