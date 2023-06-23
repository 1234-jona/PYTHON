print("Deteccion de errores con try except".center(100,"="))
#error de sintaxis
if True:
    print("Hola mundo")
#2.Excepciones
try:
    a=1/0
except Exception as e :
    print(e)
print("fin")