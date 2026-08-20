
class Jugador:
    
    def __init__(self, nombre):
        
        self.nombre = nombre
        self.personaje = None
        
    def seleccionar_personaje(self, personaje):
        
        self.personaje = personaje
        
        print(f"{self.nombre} selecionó al personaje"
              f" {personaje.nombre}")
        
    def mostrar_personaje(self):
        
        if self.personaje is not None:
            
            print(f"El jugador {self.nombre} "
                  f"utiliza a {self.personaje.nombre} .")
            
        else:
            print("El jugador no tiene un personaje seleccionado")