p="vamos a utilizar varios controladores de excepciones"
print(p.upper().center(100,"="))
#Vamos a crear un archivo y vamos a leer linea por linea hasta encontrar la clave de un diccionario7
try:
    f=open("registro.txt","r")
    d={"nombre":"jonathan","apellido":"lituma"}
    for l in f:
        print(l,d[l])
#las excepciones son errores que podria teenr al momento de interactuar con la applicacion
except FileNotFoundError as e:
    print("el archivo no existe")
except KeyError as e:
    print("la clave no existe")
except Exception as e:
    print("el error es el siguiente",e)
#utilizamos else cuando no tenemos ningun error
else:
    print("No hemos tenido ningun error al momento de interactuar con la aplicacion")
    f.close()
#la sentencia finally va correr si o si no importa en cualquier caso va ser valida
finally:
    print("En cualquier caso va ser ejecutada no importa")