print("Cadenas como objeto".center(100,"="))
#lower nos permite devolver de una cadena de texto las minuscualas
s="Estoy aprendiendo a programar en pYthon"
print(s.lower().count("python"))
#find nos regresa el indice de donde esta ubicado una palabra
p="Python es el mejor para comenzar"
print(p.find("es"))
print(p.rfind("es"))
#el uso de join para unir una lista con un caracter
l_1=["Matematicas","Alumno 001",15]
l_2=["Biologia","Alumno 001",13]
l_3=["Historia","Alumno 002",17]
r=";".join([str(e) for e in l_1])
print(r)
#funcion replace nos ayuda a reeemplazar en una cadena un caracter
u="Vamos bien creo que si estoy aprendiendo Python"
u_p=u.replace("Python","javascrip")
print(u_p)
#nos ayuda a dividir de una cadena de texto 
f="factura #1,nombre jonathan,no debes nada"
l=f.split(",")
print(l[0])