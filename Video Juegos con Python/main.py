#Librerias importadas
import pygame
import constantes
from personaje import Personajes
from weapon import Weapon
import funciones_extra as fx

# inicializando la libreria
pygame.init()

# creando ventana
ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))

#Colocando titulo a la ventana
pygame.display.set_caption("Mi primer juego")


#importar imagenes del personaje para hacer la animacion
animaciones = []
for i in range(7):
    img = pygame.image.load(f"aset//Player0{i+1}.png")
    img = fx.escalar_imagen(img,constantes.ESCALA_PERSONAJE)
    animaciones.append(img)

#importar imagen del arma
imagen_pistola = pygame.image.load("aset//armas//gun.png")
imagen_pistola = fx.escalar_imagen(imagen_pistola, constantes.ESCALA_ARMA)

#Importar imagen de balas
imagen_balas = pygame.image.load("aset//armas//bala.png")
imagen_balas = fx.escalar_imagen(imagen_balas, constantes.ESCALA_BALA)

#crear un jugador de la clase personaje
jugador = Personajes(50, 50,animaciones)

#crear un arma de la clase weapon
arma = Weapon(imagen_pistola,imagen_balas)

#Creando un grupo de sprites
grupo_balas = pygame.sprite.Group()

#definiendo variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda = False

# permite controlar los frames por segundo
reloj = pygame.time.Clock()

# Para que se cierre cuando cerramos la ventana
run = True
while run:
    
    #DEFINIR LOS FPS: MAX 60 
    reloj.tick(constantes.FPS)

    #color de fondo, para actualizarlo
    ventana.fill(constantes.COLOR_BG) 
    
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
    bala = arma.actualizar_arma(jugador)
    if bala:
        grupo_balas.add(bala)

    #Dibuja al jugador
    jugador.dibujar(ventana)

    #Dibujar Arma
    arma.dibujar(ventana)

    #dibujando balas
    for bala in grupo_balas:
        bala.dibujar(ventana)

    # lista de eventos que pueden o van a ocurrir dentro del juego
    for eventos in pygame.event.get():

        # evento de cerrar la ventana
        if eventos.type == pygame.QUIT:  
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

    #actualizar la pantalla para ver los cambios
    pygame.display.update() 

#saliendo de la libreria
pygame.quit()  
