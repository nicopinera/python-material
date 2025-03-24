import pygame
import constantes
from personaje import Personajes
from weapon import Weapon

pygame.init()  # inicializando la libreria
# creando ventana
ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))
pygame.display.set_caption("Mi primer juego")  # nombre ventana

#FUNCION PARA ESCALAR IMAGENES
def escalar_imagen(imagen, escala):
    ancho = imagen.get_width()
    alto = imagen.get_height()
    nueva_imagen = pygame.transform.scale(imagen, (ancho*escala,alto*escala))
    return nueva_imagen

#importar imagenes del personaje
animaciones = []
for i in range(7):
    img = pygame.image.load(f"aset//Player0{i+1}.png")
    img = escalar_imagen(img,constantes.ESCALA_PERSONAJE)
    animaciones.append(img)

#importar imagen del arma
imagen_pistola = pygame.image.load("aset//armas//gun.png")
imagen_pistola = escalar_imagen(imagen_pistola, constantes.ESCALA_ARMA)

#crear un jugador de la clase personaje
jugador = Personajes(50, 50,animaciones)

#crear un arma de la clase weapon
arma = Weapon(imagen_pistola)

#definiendo variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

reloj = pygame.time.Clock() # permite controlar los frames por segundo

# Para que se cierre cuando cerramos la ventana
run = True

while run:
    
    #DEFINIR LOS FPS: MAX 60 
    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_BG) #color de fondo, para actualizarlo
    
    #caclular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD

    #mover y dibujar jugador
    jugador.movimiento(delta_x,delta_y)

    #Actualiza el estado del jugador
    jugador.actualizar()

    #Actualiza el estado del arma
    arma.actualizar_arma(jugador)

    #Dibuja al jugador
    jugador.dibujar(ventana)

    #Dibujar Arma
    arma.dibujar(ventana)

    for eventos in pygame.event.get():
          # lista de eventos que pueden o van a ocurrir dentro del juego

        if eventos.type == pygame.QUIT:  # evento de cerrar la ventana
            run = False

        #mover al jugador cuando toco las teclas
        if eventos.type == pygame.KEYDOWN: # tipo de evento es tocar una tecla
            if eventos.key == pygame.K_a:
                mover_izquierda = True
            if eventos.key == pygame.K_d:
                mover_derecha = True
            if eventos.key == pygame.K_w:
                mover_arriba = True
            if eventos.key == pygame.K_s:
                mover_abajo = True

        #frenar al jugador cuando se levanta la tecla
        if eventos.type == pygame.KEYUP:
            if eventos.key == pygame.K_a:
                mover_izquierda = False
            if eventos.key == pygame.K_d:
                mover_derecha = False
            if eventos.key == pygame.K_w:
                mover_arriba = False
            if eventos.key == pygame.K_s:
                mover_abajo = False

    pygame.display.update() #actualizar la pantalla para ver los cambios

pygame.quit()  # saliendo de la libreria
