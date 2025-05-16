import pygame,sys

#Inicializar esta libreria
pygame.init()

#Definir Colores
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

#Crear ventana
size= (800,500) #Tamaño
sreen = pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #Color de fondo
    sreen.fill(WHITE)

    ### ---- Zona de Dibujo
    #pygame.draw.line(sreen,GREEN,[0,100],[100,100],5)
    

    ### ---- Zona de Dibujo
    #Actualizar pantalla
    pygame.display.flip()

