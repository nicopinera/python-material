import pygame
import constantes as ct

class Personaje:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.ancho = ct.TILE_SIZE // 2
        self.alto = ct.TILE_SIZE
        self.en_el_suelo = False

    def mover(self, teclas, mundo):
        # Movimiento izquierda/derecha con detección de colisión
        nueva_x = self.x
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            nueva_x -= 4
            if mundo.colisiona(nueva_x, self.y) or mundo.colisiona(nueva_x, self.y + self.alto - 1):
                nueva_x = self.x  # Cancelar movimiento si está bloqueado
        elif teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            nueva_x += 4
            if mundo.colisiona(nueva_x + self.ancho, self.y) or mundo.colisiona(nueva_x + self.ancho, self.y + self.alto - 1):
                nueva_x = self.x  

        # Aplicar nueva posición en X
        self.x = nueva_x

        # Aplicar gravedad
        if not self.en_el_suelo:
            self.vel_y += 0.5 # Gravedad
        
        if not self.en_el_suelo and (teclas[pygame.K_s] or teclas[pygame.K_DOWN]):
            self.vel_y += 1.2 # Gravedad

        # Movimiento en Y
        nueva_y = self.y + self.vel_y
        if not mundo.colisiona(self.x, nueva_y + self.alto) and not mundo.colisiona(self.x + self.ancho, nueva_y + self.alto):
            self.y = nueva_y
            self.en_el_suelo = False
        else:
            self.vel_y = 0
            self.en_el_suelo = True

        # Salto con `ESPACIO`
        if (teclas[pygame.K_w] or teclas[pygame.K_SPACE] or teclas[pygame.K_UP]) and self.en_el_suelo:
            self.vel_y = -10  # Salto

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, (255, 0, 0), (self.x, self.y, self.ancho, self.alto))