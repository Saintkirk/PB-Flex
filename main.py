from jugador  import Jugador
from mago import Mago
from guerrero import Guerrero
from objeto import Objeto
# from inventario import inventario

#Método principal

def main():
    
#crear jugador

    jugador = Jugador("Eric")
    
    jugador_dos = Jugador("fernando")


#CREAR PERSONAJE

    magician = Mago("Saruman", 10, 80, 150)
    
    guerrero = Guerrero("Aragon", 12, 150, 80)
    
    #ASOCIAR JUGADOR CON PERSONAJE
    jugador.seleccionar_personaje(magician)
    
    # Mostrar info del mago
    
    magician.mostrar_informacion()
    
    #ataque de mago
    
    magician.atacar()
    
    #asociamo el nuevo jugador a un nuevo pj
    jugador_dos.seleccionar_personaje(guerrero)
    
    guerrero.mostrar_informacion()
    
    guerrero.atacar()
    
    #crear objeto
    
    pocion = Objeto("Pocion de vida", "Consumible")
    
    espada = Objeto("Excalibur", "Arma")
    
    magician.inventario.agregar_objeto(pocion)
    
    magician.inventario.agregar_objeto(espada)
    
    #mostrar inventario
    
    magician.inventario.mostrar_inventario()
    
    #mago recibe daño
    
    magician.recibir_danio(30)
    
    #polimorfismo
    
    personajes = [magician, guerrero]
    
    for personajes in personajes:
        
        personajes.atacar()
        
    
    
    
if __name__ == "__main__":
    main()