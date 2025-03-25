#Librerias Importadas
import pygame
import constantes

#Clase Personaje
class Personajes:

    #Constructor, le pasamos la posicion (x,y) y la lista de animaciones
    def __init__(self, x, y,animaciones):

        #Propiedades para dar vuelta la imagen
        self.voltearX = False

        #Seteamos la lista de animaciones para caminar
        self.animaciones = animaciones
        self.frame_index = 0 #imagen que se muestra actualmente
        self.update_time = pygame.time.get_ticks() #guarda el tiempo en milis
        self.imagen = animaciones[self.frame_index]
        self.tiempo_actualizacion_imagen = 150

        #Creando el rectangulo de personaje, cuadrado de 20x20 en las coordenadas (0,0)
        self.forma = self.imagen.get_rect()

        #En que coordenadas colocamos la figura
        self.forma.center = (x, y)

    #Dibuja a nuestro personaje
    def dibujar(self, ventana):
        
        #nos dice si tenemos que mostrar la imagen volteada segun estemos avanzando haca delante o hacia atras
        imagen_volteada = pygame.transform.flip(self.imagen,self.voltearX, False)
        #pygame.draw.rect(ventana, constantes.COLOR_AMARILLO, self.forma,1)  # lo dibujo en la ventana y de color amarillo
        #Imprimir la figura y la imagen en la ventana
        ventana.blit(imagen_volteada, self.forma) #la imagen y donde lo quiero crear

    def movimiento(self, delta_x, delta_y):
        #movimiento a izquierda
        if delta_x < 0:
            self.voltearX = True
            self.tiempo_actualizacion_imagen = 30
        #movimiento a derecha
        elif delta_x > 0:
            self.voltearX = False
            self.tiempo_actualizacion_imagen = 30
        #No movimiento
        if delta_x == 0:
            self.tiempo_actualizacion_imagen = 150
        #desplazamientos a izquierda y derecha variando la posicion en X e Y
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