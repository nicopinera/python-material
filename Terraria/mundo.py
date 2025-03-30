import pygame # -> pip install pygame
import random
from perlin_noise import PerlinNoise  # Para Perlin Noise -> pip install Perlin-noise
import constantes as ct

# 🌍 Clase Mundo
class Mundo:
    def __init__(self):
        self.noise = PerlinNoise(octaves=3, seed=random.randint(0, 1000))  # Más octavas = más detalle
        self.mapa = self.generar_mundo()

    def generar_mundo(self):
        mundo = [[0 for _ in range(ct.COLUMNAS)] for _ in range(ct.FILAS)]
        altura_media = ct.FILAS // 2
        escala = 15  # Aumentamos la escala para un terreno más suave

        for col in range(ct.COLUMNAS):
            altura = int(altura_media + self.noise(col / escala) * 10)  # Perlin Noise suavizado
            
            for fila in range(ct.FILAS):
                if fila > altura:
                    if fila == altura + 1:
                        mundo[fila][col] = 3  # Primera capa de pasto 🌿
                    elif fila > altura + 3:
                        mundo[fila][col] = 2  # Piedra en capas más profundas
                    else:
                        mundo[fila][col] = 1  # Tierra en la capa superior
                else:
                    mundo[fila][col] = 0  # Aire
        return mundo

    def dibujar(self, pantalla):
        for fila in range(ct.FILAS):
            for col in range(ct.COLUMNAS):
                color = ct.COLORES[self.mapa[fila][col]]
                pygame.draw.rect(pantalla, color, (col * ct.TILE_SIZE, fila * ct.TILE_SIZE, ct.TILE_SIZE, ct.TILE_SIZE))

    def colisiona(self, x, y):
        """Verifica si un punto (x, y) está tocando un bloque sólido"""
        col = int(x // ct.TILE_SIZE)
        fila = int(y // ct.TILE_SIZE)
        if 0 <= col < ct.COLUMNAS and 0 <= fila < ct.FILAS:
            return self.mapa[fila][col] in [1, 2, 3]  # Tierra, piedra o pasto
        return False