class Contacto:
    def __init__(self,codigo,nombre,apellido,profesion):
        self.codigo=codigo
        self.nombre=nombre
        self.apellido=apellido
        self.profesion=profesion
    def __str__(self):
         return f"codigo:{self.codigo} nombre:{self.nombre} profesion:{self.profesion}"
    #Estas funciones permite solo devolver los valores sin modificarlos solo observarlos
    def getnombre(self):
        return self.nombre
    def getcodigo(self):
        return self.codigo
    def getapellido(self):
        return self.apellido
    def getprofesion(self):
        return self.profesion
    #Estas funciones nos permiten modificar los atributos de una clase
    def setcodigo(self,pcodigo):
        self.codigo=pcodigo
    def setnombre(self,pnombre):
        self.nombre=pnombre
    def setapellido(self,papellido):
        self.apellido=papellido
    def setprofesion(self,pprofesion):
        self.profesion=pprofesion
    
#crear contacto
def crear():
    codigo1=input("Ingrese el codigo de la persona")
    nombre1=input("Ingrese el nombre de la persona")
    apellido1=input("Ingrese el apellido de la persona")
    profesion1=input("Ingrese la profesion de la persona")
    contacto3=Contacto(codigo1,nombre1,apellido1,profesion1)
    listacontactos.append(contacto3)
    #print(contacto3)
def leer():
    print("INFORME".center(100,"="))
    for contacto in listacontactos:
        print(contacto)
def eliminar_contacto():
    print("ELIMINAR".center(100,"="))
    c_nuevo=(input("Ingrese el codigo de la persona que desea eliminar"))
    for x in listacontactos:
        if(c_nuevo==contacto1.getcodigo() or c_nuevo==contacto2.getcodigo() ):
            listacontactos.remove(x)
            print("Contacto eliminado")
def actualizar():
    print("ACTUALIZAR".center(100,"="))
    c_nuevo=(input("Ingrese el codigo de la persona que desea elimianr"))
    for x in listacontactos:
        if(c_nuevo==contacto1.getcodigo()  ):
            codigo=input("Ingrese el codigo nuevo")
            nombre=input("Ingrese el nombre nuevo")
            apellido=input("Ingrese el apellido")
            profesion=input("Ingrese la profesion")
            contacto1.setcodigo(codigo)
            contacto1.setnombre(nombre)
            contacto1.setapellido(apellido)
            contacto1.setprofesion(profesion)
        elif( c_nuevo==contacto2.getcodigo()):
            codigo=input("Ingrese el codigo nuevo")
            nombre=input("Ingrese el nombre nuevo")
            apellido=input("Ingrese el apellido")
            profesion=input("Ingrese la profesion")
            contacto2.setcodigo(codigo)
            contacto2.setnombre(nombre)
            contacto2.setapellido(apellido)
            contacto2.setprofesion(profesion)
        else:
            print("EL codigo no existe")
        
#Datos quemados 
contacto1=Contacto("001","jonathan","lituma","ingeniero en sistemas")
contacto2=Contacto("002","paul","galarza","ingeniero de soporte")
#lista de contactos vacia que vamos a utilizar
listacontactos=[]
#Agregar a la lista los contactos
listacontactos.append(contacto1)
listacontactos.append(contacto2)

#Opcion que desea el usuario
opcion=input("1.Crear\n2.Leer\n3.Actualizar\n4.Eliminar\n5.Salir\n")
while(opcion!="5"):
    if(opcion=="1"):
        crear()
    elif(opcion=="2"):
        leer()
    elif(opcion=="3"):
        actualizar()
    elif(opcion=="4"):
        eliminar_contacto()
    opcion=input("1.Crear\n2.Leer\n3.Actualizar\n4.Eliminar\n5.Salir\n")
    
      
        