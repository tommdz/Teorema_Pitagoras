
#La función input() siempre devuelve una cadena (string)
#por lo que no necesitas convertir explícitamente el 
#esultado a string como en el caso de int(input()) para los números enteros. 
import math
def calcHipotenusa(a, b):
    hipotenusa = math.sqrt(a**2 + b**2)
    return hipotenusa


def calcCA(b, h):
    catetoadyacente = math.sqrt(h**2 - b**2)
    return catetoadyacente

def calcCO(a, h):
    catetoopuesto = math.sqrt(h**2 - a**2)
    return catetoopuesto

print("¿Posee el valor del cateto adyacente?")
ca = (input())

if ca == "si":  
    print("Ingrese valor del cateto adyacente: ")
    a = float(input())

    print("¿Posee el valor del cateto opuesto?")
    co1 = (input())
    if co1 == "si":
        print("Ingrese valor del cateto opuesto: ")
        b = float(input())
        print("El valor de la hipotenusa es:",calcHipotenusa(a, b))


elif ca == "no":
    print("¿Posee el valor del cateto opuesto: ")
    co = (input())
    if co == "si":    
        print("Ingrese valor del cateto opuesto: ")
        b = float(input())
        print("Ingrese el valor de la hipotenusa: ")
        h = float(input())
        print("El valor del cateto adyacente es:", calcCA(b, h))
    
    elif co == "no":
        print("Ingrese el valor de la hipotenusa: ")
        h = float(input())
        print("Ingrese el valor del cateto adyacente: ")
        a = float(input())
        print("El valor del cateto opuesto es:",calcCO(a, h))


 

  