try:
    fichero = open("numero.txt", "r")
    lines = fichero.readlines()
    print(lines)
except IOError as errIO:
        print("no encuentro el fichero o no puedo leerlo",errIO)
except OSError as erros:
        print("error de os", erros)
else:
    print("se leyo bien")
    fichero.close()


