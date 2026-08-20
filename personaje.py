from inventario import inventario

# clase Personaje

class Personaje:
    
    def __init__(self, nombre, nivel, vida):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
        self.inventario = inventario()

    def atacar(self):
        print(f"{self.nombre} realiza un ataque.")
        
        
    def recibir_danio(self, danio):
        
        self.vida -= danio 
        
        if self.vida < 0:
            self.vida = 0
            
        print(f"{self.nombre} recibio {danio} puntos de daño")
        
    
    def mostrar_informacion(self):
        
        print("\n ---INFO DEL PJ---")
        print(F"Nombre: {self.nombre}")
        print(F"Nivel: {self.nivel}")
        print(F"Vida: {self.vida}")
        
        
    def usar_habilidad(self):
        print(f"{self.nombre} utiliza la habilidad")
     