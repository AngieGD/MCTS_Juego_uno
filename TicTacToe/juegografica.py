import pygame, random, os, sys

pygame.init() #Inicializar pygame motor

size = 700 , 700
color = (28 , 170 , 156) #color
red = (255 , 0 , 0 )
screen = pygame.display.set_mode(size)  #crear ventanda
pygame.display.set_caption("TIC TAC TOE +")
screen.fill(color)
pygame.draw.line(screen , red , (10 , 10) , (300 , 300 ) , 10) #desde , hasta y grosor
run = True

while run:

    #Capturamos los enevtos que se han producido
    for event in pygame.event.get():
        #si el evento es salir de la ventana, terminamos
        if event.type == pygame.QUIT:
            run = False
#SALGO DE pygam

    pygame.display.update() # actualizo la pantalla

pygame.QUIT()