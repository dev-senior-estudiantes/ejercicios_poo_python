""" Ejercicio 1: Clase Persona 

Planteamiento 

Crear una clase Persona, con atributos Nombre y Edad. Crear un método que muestre un saludo. 


Pseudocódigo

Clase Persona:
    
    Atributos: nombre, edad
    
    Metodo saludar():
        
        Imprimir "Hola, soy {nombre} y tengo {edad} años." """
        
        
class Persona:
    
    def __init__ (self, nombre, edad):
        
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
        


# la forma en que estaba instanciado el metodo generaba un error
'''persona1 = Persona("Carlos", 30)
persona2 = Persona("Ruben", 25)
persona3 = Persona("Juan", 20)



saludar = persona1.saludar()
print(saludar)'''

# Aporte de instanciamiento instaciamos el objeto persona y el metodo saludar para cada objeto
persona1 = Persona("Carlos", 30)
persona1.saludar()
persona2 = Persona("Ruben", 25)
persona2.saludar()
persona3 = Persona("Juan", 20)
persona3.saludar()
persona4 = Persona("Luis", 29)
persona4.saludar()