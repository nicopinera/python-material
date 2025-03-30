import pygame
import random
import constantes as ct
from mundo import Mundo
from personaje import Personaje


# Inicializar Pygame
pygame.init()
pantalla = pygame.display.set_mode((ct.ANCHO, ct.ALTO))
clock = pygame.time.Clock()

# Crear mundo y personaje
mundo = Mundo()
jugador = Personaje(ct.ANCHO // 2, 100) 

# Bucle del juego
ejecutando = True
while ejecutando:
    pantalla.fill((135, 206, 250))  # Fondo azul cielo

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Obtener teclas presionadas
    teclas = pygame.key.get_pressed()

    # Mover personaje
    jugador.mover(teclas, mundo)

    # Dibujar todo
    mundo.dibujar(pantalla)
    jugador.dibujar(pantalla)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
