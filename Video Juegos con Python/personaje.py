import pygame
import constantes


class Personajes:
    def __init__(self, x, y,animaciones):  # coordenadas donde va a aparecer
        self.voltear = False
        self.forma = pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)  # cuadrado de 20x20 en las coordenadas 0,0
        self.forma.center = (x, y)  # lo movemos en las coordenadas x e y
        self.animaciones = animaciones
        self.frame_index = 0 #imagen que se muestra actualmente
        self.update_time = pygame.time.get_ticks() #guarda el tiempo en milis
        self.imagen = animaciones[self.frame_index]
        self.tiempo_actualizacion_imagen = 150

    def dibujar(self, ventana):
        imagen_volteada = pygame.transform.flip(self.imagen,self.voltear, False)
        #pygame.draw.rect(ventana, constantes.COLOR_AMARILLO, self.forma,1)  # lo dibujo en la ventana y de color amarillo
        ventana.blit(imagen_volteada, self.forma) #la imagen y donde lo quiero crear

    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:
            self.voltear = True
            self.tiempo_actualizacion_imagen = 30
        elif delta_x > 0:
            self.voltear = False
            self.tiempo_actualizacion_imagen = 30
        elif delta_y > 0 or delta_y < 0:
            self.tiempo_actualizacion_imagen = 30
        if delta_x == 0:
            self.tiempo_actualizacion_imagen = 150
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y

    def actualizar(self):
        #cooldown_animacion = 50
        self.imagen = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > self.tiempo_actualizacion_imagen:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0