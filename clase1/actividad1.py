class Errnum10(Exception):
    pass
class ErrnumInt(Exception):
    pass

maxn= 10

while(True):

    try:
        num = input("Introduzca un numero")
        if (int(num)>10):
            raise Errnum10
        else:
            break
    except Errnum10:
        print("numero mayor que 10")
    except ValueError:
        print("NO es un numero entero")

print("numero valido")


        
        



