import pygame
import constantes
import math

class Weapon():
    def __init__(self,imagen):
        self.imagen_original = imagen

        self.angulo = 0

        self.imagen = pygame.transform.rotate(self.imagen_original,self.angulo)

        self.forma = self.imagen.get_rect() #Me hace la imagen un rectangulo


    def actualizar_arma(self, personaje):

        self.forma.center = personaje.forma.center

        if personaje.voltearX == False: #no rotado
            self.forma.x = self.forma.x + personaje.forma.width/3
            self.rotar_arma(False)
        elif personaje.voltearX == True: # rotado
            self.forma.x = self.forma.x - personaje.forma.width/3
            self.rotar_arma(True)
        
        #mover la pistola con el mouse
        mouse_posicion = pygame.mouse.get_pos()
        diferencia_x = mouse_posicion[0] - self.forma.centerx
        diferencia_y = -(mouse_posicion[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(diferencia_y,diferencia_x))
        print(self.angulo) #10 y -15 <---> 160 y -160


    def rotar_arma(self,rotar):
        if rotar == True:
            imagen_rotada = pygame.transform.flip(self.imagen_original, True,False)
            self.imagen = pygame.transform.rotate(imagen_rotada,self.angulo)
        else:
            imagen_rotada = pygame.transform.flip(self.imagen_original, False,False)
            self.imagen = pygame.transform.rotate(imagen_rotada,self.angulo)

    def dibujar(self, ventana):
        self.imagen = pygame.transform.rotate(self.imagen,self.angulo)
        ventana.blit(self.imagen, self.forma)
        
        
        #pygame.draw.rect(ventana, constantes.COLOR_ARMA, self.forma,1)
    
    
