import pygame
import constantes


class Personajes:
    def __init__(self, x, y):  # coordenadas donde va a aparecer
        self.forma = pygame.Rect(
            0, 0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE
        )  # cuadrado de 20x20 en las coordenadas 0,0
        self.forma.center = (x, y)  # lo movemos en las coordenadas x e y

    def dibujar(self, ventana):
        pygame.draw.rect(
            ventana, constantes.COLOR_AMARILLO, self.forma
        )  # lo dibujo en la ventana y de color amarillo

    def movimiento(self, delta_x, delta_y):
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y