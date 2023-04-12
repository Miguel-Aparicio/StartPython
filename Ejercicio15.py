def posneg():
    n = int(input("Escriba un numero: "))   
    if n.isdigit(): 
        if n < 0:
            print("Es negativo")
        elif n > 0:
            print("Es positivo")
        else:
            print("Es 0")
    else:
        print("El valor introducido no es numerico")