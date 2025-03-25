import pygame

#Funcion para escalar imagenes
def escalar_imagen(imagen, escala):
    ancho = imagen.get_width()
    alto = imagen.get_height()
    nueva_imagen = pygame.transform.scale(imagen, (ancho*escala,alto*escala))
    return nueva_imagen