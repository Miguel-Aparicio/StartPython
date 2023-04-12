def mayormenornum():
    # Entrada
    while True:
        lista1 = (input("Ingrese una lista de números separados por espacios: ").split(" "))
        listanum = []
    # Proceso
        try:
            for i in range(len(lista1)):
                listanum.append(int(lista1[i]))
            mayornum = listanum[0]
            menornum = listanum[0]
            for i in range(len(listanum)):
                if listanum[i]>mayornum:
                    mayornum = listanum[i]
                else:
                    if listanum[i]<menornum:
                        menornum = listanum[i]
            res = f"El número mayor es: {mayornum}, y el número menor: {menornum}"
            break
        except:
            print("Error, existen números introducidos incorrectos. Intentelo nuevamente.")
    # Salida
    print(res)