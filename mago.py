
from personaje import Personaje

class Mago(Personaje):
    
    def __init__(self, nombre, nivel, vida, poder_magico):
        super().__init__(nombre, nivel, vida)
        self.poder_magico = poder_magico
        
    def atacar(self):
        print(f"{self.nombre} lanza un hechizo "
              f"con {self.poder_magico} de poder mágico")
            
    def usar_habilidad(self):
        print(f"{self.nombre} utiliza bola de fuego")
     