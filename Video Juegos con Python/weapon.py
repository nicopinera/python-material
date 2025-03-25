#Librerias importadas
import pygame
import constantes
import math

#Clase arma
class Weapon():

    #Constructor del arma, parametros: la imagen y la imagen de las balas
    def __init__(self,imagen, imagen_bala):
        #Imagen original del arma
        self.imagen_original = imagen

        #Imagen De la bala
        self.imagen_bala = imagen_bala

        #Angulo del arma
        self.angulo = 0

        #Imagen del arma rotada segun el angulo
        self.imagen = pygame.transform.rotate(self.imagen_original,self.angulo)

        #Seteamos la forma del arma como un rectangulo
        self.forma = self.imagen.get_rect() #Me hace la imagen un rectangulo
        
        #Booleano para saber si fue disparada
        self.disparada = False

        #Tiempo en milis de la ultima vez que se disparo
        self.ultimo_disparo = pygame.time.get_ticks()

    #Funcion para actualizar el estado del arma
    def actualizar_arma(self, personaje):
        #Dilay entre disparo
        disparo_retraso = 500

        #bala del arma
        bala = None

        #Se dibuja en el centro de la forma de nuestro personaje
        self.forma.center = personaje.forma.center

        #Comprobamos si mi personaje no esta rotado, no totamos el arma
        if personaje.voltearX == False: #no rotado
            #Le subimos unos pixeles
            self.forma.x = self.forma.x + personaje.forma.width/3

            #Le mandamos false para que no rote el arma
            self.rotar_arma(False)
        
        #Si el personaje esta rotado, rota el arma
        elif personaje.voltearX == True: # rotado
            self.forma.x = self.forma.x - personaje.forma.width/3
            self.rotar_arma(True)
        
        #mover la pistola con el mouse
        #Tomamos un vector de las posiciones x e y del mouse
        mouse_posicion = pygame.mouse.get_pos()

        #Calculamos la distancia en x
        diferencia_x = mouse_posicion[0] - self.forma.centerx

        #calculamos la distancia en y
        diferencia_y = -(mouse_posicion[1] - self.forma.centery)

        #Establecemos el angulo
        self.angulo = math.degrees(math.atan2(diferencia_y,diferencia_x))

        #print(self.angulo) #10 y -15 <---> 160 y -160

        #detectar los click del mouse
        if pygame.mouse.get_pressed()[0] and self.disparada == False and (pygame.time.get_ticks()-self.ultimo_disparo >= disparo_retraso): #0 izquierdo, 1 rueda, 2 derecho
            bala = Balas(self.imagen_bala, self.forma.centerx, self.forma.centery, self.angulo)
            self.disparada = True
            self.ultimo_disparo = pygame.time.get_ticks()
        if pygame.mouse.get_pressed()[0] == False:
            self.disparada = False
        return bala

    #Para rotar el arma
    def rotar_arma(self,rotar):
        #Rotamos el arma
        if rotar == True:
            imagen_rotada = pygame.transform.flip(self.imagen_original, True,False)

            #Se establece la imagen como rotada
            self.imagen = pygame.transform.rotate(imagen_rotada,self.angulo)
        else:
            imagen_rotada = pygame.transform.flip(self.imagen_original, False,False)
            self.imagen = pygame.transform.rotate(imagen_rotada,self.angulo)

    #Dibujar el arma
    def dibujar(self, ventana):
        self.imagen = pygame.transform.rotate(self.imagen,self.angulo)
        ventana.blit(self.imagen, self.forma)
        #pygame.draw.rect(ventana, constantes.COLOR_ARMA, self.forma,1)
    
#Clase balas
class Balas(pygame.sprite.Sprite): #Hereda de Sprite y recibe todos sus metodos
    def __init__(self,imagen, x, y, angulo):
        pygame.sprite.Sprite.__init__(self) #constructor de la clase sprite
        self.imagen_original = imagen
        self.angulo = angulo
        self.imagen_bala = pygame.transform.rotate(self.imagen_original,self.angulo)
        self.rectangulo = self.imagen_bala.get_rect()
        self.rectangulo.center = (x,y)
        

    def dibujar(self, ventana):
        ventana.blit(self.imagen_bala, (self.rectangulo.centerx,
                                        self.rectangulo.centery - int(self.imagen_bala.get_height())))
    

        
