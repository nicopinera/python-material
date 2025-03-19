import os
os.system('cls')

### Clases ### 

class PersonaVacia:
    pass #para finalizar cuando no hago nada

class Persona:
    def __init__(self, nombre, apellido, alias = "Sin alias"): #Constructor
        #self.nombre = nombre #self =this
        #self.apellido= apellido
        self.full_name = f"{nombre} {apellido} ({alias})" # Publica
        self.__nombre = nombre #Variables privadas
        self.__apellido = apellido #Variables privadas
        self.__alias = alias #Variables privadas

    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getAlias(self):
        return self.__alias
    
    def caminar(self):
        print(self.getNombreCompleto() ,"Esta caminando")
        
    def getNombreCompleto(self):
        return self.full_name
        

mi_persona = Persona("Nicolas", "Piñera")
print(mi_persona.full_name)
mi_persona.caminar()