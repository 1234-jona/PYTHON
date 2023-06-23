#Realizar un programa con una clase tipo alumno 
#que solo tenga de atributos nombre y nota 
#Al final ver si el alumno aprobo o no aprobo 
class Alumno:
    #Atributos de la clase
    def __init__(self,nombre,apellido,nota):
        self.nombre=nombre
        self.apellido=apellido
        self.nota=nota
    def __str__(self) :
        return (f"Nombre alumno:{self.nombre}Apellido alumno:{self.apellido} Nota alumno{self.nota}")
    #Aqui los regresa los getters para visualizar los atributos 
    def getnombre(self):
        return self.nombre
    def getnota(self):
        return self.nota
nombre=input("Ingrese el nombre del estudiante")
apellido=input("Ingrese el apellido del estudiante")
nota=float(input("Ingrese la nota del estudiante"))
#Aqui se crea una intancia de la clase
estudiante1=Alumno(nombre,apellido,nota)
if(estudiante1.nota<7):
    print(f"El estudiante:{estudiante1.getnombre()} tiene una nota de:{estudiante1.getnota()}")
    print("No aprobo")
elif(estudiante1.nota>=7 and estudiante1.nota<=10):
    print(f"El estudiante:{estudiante1.getnombre()} tiene una nota de:{estudiante1.getnota()}")
    print("Aprobo")
print("Gracias por utilizar el programa")
