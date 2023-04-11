def numeropar():
    #Algoritmo numeropar
    # Entrada
    while True:
        numero = input ("Inserte un número entero: ")
    # Proceso
        try:
            if (int(numero)) %2 == 0:
                resultadopar = True
            else:
                resultadopar = False
            if resultadopar == True:
                res = (f"Tu número {numero} es par.")
            else:
                res = (f"Tu número {numero} es impar.")
            break
        except:
            print("No has introducido un valor correcto.")
    # Salida
    print(res)