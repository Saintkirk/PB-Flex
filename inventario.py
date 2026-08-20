
class inventario: 
    
    def __init__(self):
        
        self.objetos = []
        
   #Metodo para agregar objeto     
    def agregar_objeto(self, objeto):
        
        self.objetos.append(objeto)
        print(f"{objeto.nombre} ha sido agregado al inventario.")
        
    def mostrar_inventario(self):
        
        print("\n ----INVENTARIO---")
        
        if len(self.objetos) == 0:
            print("El inventario esta vacio")
        else:
            
            for objeto in self.objetos:
                print(f" - {objeto.nombre} ({objeto.tipo})")