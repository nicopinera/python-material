import pygame
import constantes

#Funcion para escalar imagenes
def escalar_imagen(imagen, escala):
    ancho = imagen.get_width()
    alto = imagen.get_height()
    nueva_imagen = pygame.transform.scale(imagen, (ancho*escala,alto*escala))
    return nueva_imagen

def importar_imagenes_caminando():
    animaciones = []
    for i in range(7):
        img = pygame.image.load(f"aset//Player0{i+1}.png")
        img = escalar_imagen(img,constantes.ESCALA_PERSONAJE)
        animaciones.append(img)
    return animaciones

#Si falla, poner este codigo en el main
#animaciones = []
#for i in range(7):
#    img = pygame.image.load(f"aset//Player0{i+1}.png")
#    img = fx.escalar_imagen(img,constantes.ESCALA_PERSONAJE)
#    animaciones.append(img)