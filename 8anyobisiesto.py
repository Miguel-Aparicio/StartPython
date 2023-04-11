def anyobisiesto():
    # Entrada
    anyo = int(input("Introduzca un año para saber si es bisiesto: "))
    # Proceso
    if anyo %4 == 0 or (anyo %400 == 0 and anyo %100 == 0):
        resultado = (f"El año {anyo} es bisiesto")
    else:
        resultado = (f"El año {anyo} no es bisiesto")
    # Salida
    print(resultado)