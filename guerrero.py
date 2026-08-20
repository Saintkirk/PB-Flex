
from personaje import Personaje

class Guerrero(Personaje):
    
    def __init__(self, nombre, nivel, vida, fuerza):
        super().__init__(nombre, nivel, vida)
        self.fuerza = fuerza
        
    def atacar(self):
        print(f"{self.nombre} ataca con su espada" 
              f"con {self.fuerza} de fuerza")
        
        
    def usar_habilidad(self):
        print(f"{self.nombre} utiliza doble espada")
     