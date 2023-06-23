#Lector app es una aplicacion que permite gestionar la biblioteca virtual de una de los gestores
#o mas lectores
#Vamos a crear una clase biblioteca
#Atributos de una biblioteca:nombre,cantidad libros,dueño,libros(lista de libros)
#acciones agregar un libro 
#eliminar un libro 
#unir dos bibliotecas
class Biblioteca:
    def __init__(self,id,nombre,lector=None,libros=None):
        self.id=id
        self.nombre=nombre
        self.lector=lector if lector is not None else "-"
        self.libros=libros if libros is not None else []
        self.cantidad_libros=len(self.libros)
    def agregar_libro(self,libro):
        if(type(libro)==Libro):
            self.libros.append(libro)
            print("Se agrego una entidad tipo libro")
        else:
            print("Ingrese un entidad tipo libro")
    def __str__(self):
        return self.nombre
    def __repr__(self):
        return"Biblioetca <{},{}>".format(self.nombre,self.id)
    def __add__(self,obj):
        libros=self.libros+obj.libros
        libros=list(set(libros))
        return Biblioteca(3,"{}-{}".format(self.nombre,obj.nombre),libros=libros)
class Libro:
    def __init__(self,id,titulo):
        self.id=id
        self.titulo=titulo
    def __repr__(self):
        return "libro <{},{}>".format(self.id,self.titulo)
class Lector:
    def __init__(self,id,titulo,biblioteca):
        self.id=id
        self.titulo=titulo
        self.biblioteca=[]
    def agregar_biblioteca(self,biblioteca):
        if(type(biblioteca)==Biblioteca):
            if(len(self.biblioteca)<=3):
                self.bibilioteca=biblioteca
                print("Se agrego correctamente la biblioteca")
            
        else:
            print("Agrgue une entidad tipo biblioteca")
#Class lector basico
class Lectorbasic(Lector):
    def __init__(self,id,nombre):
        super().__init__(id,nombre)
        self.privado_biblioteca=[]
    def agregar_biblioteca_privada(self,biblioteca):
        if(type(biblioteca)==Biblioteca):
            if(len(biblioteca)<=3):
                self.privado_biblioteca.append(biblioteca)
                print("Se aagrego con exito la biblioteca")
        else:
            print("Debe de ingresar una entidad tipo biblioteca")
class LectorPremium(Lector):
    def agregar_biblioteca(self,biblioteca):
        self.privado_biblioteca.append(biblioteca)
#Creando entidades biblioteca
biblioteca_1=Biblioteca(1,"Cuentos entre otros")
biblioteca_2=Biblioteca(2,"Libros de ciencia ficcion")
libro_1=Libro(1,"los tres chanchitos")
libro_2=Libro(2,"Libro de pokemos")
libro_3=Libro(3,"lIbro de silvestre")
libro_4=Libro(4,"Libro de lavagirl")
biblioteca_1.agregar_libro(libro_1)
biblioteca_1.agregar_libro(libro_2)
biblioteca_2.agregar_libro(libro_3)
biblioteca_2.agregar_libro(libro_4)
print(biblioteca_1.nombre)
print(biblioteca_2.nombre)
print(biblioteca_1+biblioteca_2)