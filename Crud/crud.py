print("Hola vamos a realizar un crud".center(100,"="))
#Un crud es CREAR,LEER,ACTUALIZAR,ELIMINAR
#Funcion que viasulice los contactos
def visualizar():
    for x in range(len(codigo)):
        print(codigo[x],nombre[x],apellido[x],profesion[x])
#funcion para actualizar los datos 
def actualizar():
    visualizar()
    codigo_nuevo=input("Ingrese el codigo que desea actualizar")
    for x in range(len(codigo)):
        if(codigo_nuevo==codigo[x]):
            codigo[x]=codigo_nuevo
            nombre[x]=input("Ingrese el nuevo nombre de la persona")
            apellido[x]=input("Ingrese el apellido de la persona")
            profesion[x]=input("Ingrese la profesion de la persona")
            print("Persona modificada con exito ")
#funcion para elimnar un contacto
def elimnar():
    codigo_nuevo=input("Cual es el codigo que desea eliminar")
    for x in range(len(codigo)-1,-1,-1):
        if(codigo_nuevo==codigo[x]):
            codigo.pop(x)
            nombre.pop(x)
            apellido.pop(x)
            profesion.pop(x)
            print("Contacto eliminado")
#Creacion de arrays para el posterior quemado de elementos
codigo=["001","002"]
nombre=["Jonathan","Paul"]
apellido=["Lituma","Galarza"]
profesion=["Sistemas","Electricista"]
opcion=input("1.CREAR\n2.LEER\n3.ACTUALIZAR\n4.ELIMINAR\n5.SALIR\n")
while(opcion!="5"):
    if(opcion=="1"):
        print("Crear un contacto")
        visualizar()
        codigo_nuevo=input("Ingrese el codigo nuevo")
        codigo.append(codigo_nuevo)
        nombre.append(input("Ingrese el nombre de la persona"))
        apellido.append(input("Ingrese el apellido de la persona"))
        profesion.append(input("ingrese la profesion de la persona"))
        print("Contacto guardado")
    elif(opcion=="2"):
        visualizar()
    elif(opcion=="3"):
        actualizar()
    elif(opcion=="4"):
        elimnar()
    opcion=input("1.CREAR\n2.LEER\n3.ACTUALIZAR\n4.ELIMINAR\n5.SALIR\n")
print("Gracias por utilizar el progrma")
codigot=open("codigo.txt","w")
nombret=open("nombre.txt","w")
apellidot=open("apellido.txt","w")
profesiont=open("profesion.txt","w")
for x in range(len(codigo)):
    codigot.write(codigo[x]+",")
    nombret.write(nombre[x]+",")
    apellidot.write(apellido[x]+",")
    profesiont.write(profesion[x]+",")
codigot.close()
nombret.close()
apellidot.close()
profesiont.close()
