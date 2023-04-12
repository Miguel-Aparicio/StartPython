def palindromo():
    #Algoritmo palindromo
    # Entrada
    while True:
        cadenatxt = input("Introduzca su cadena de texto para saber si es un palíndormo: ").replace(" ","").lower()
        cadenainv = []
        # Proceso
        if cadenatxt == (""):
            print("Pero... ¿Quieres escribir algo? XD")
            # dar la opcion a salir
        else:
            for i in range((len(cadenatxt)-1),-1,-1):
                cadenainv.append(cadenatxt[i])
            cadenacomp = "".join(cadenainv)
            if cadenatxt == cadenacomp:
                res = ("Sí, es palíndromo.")
            else:
                res = ("No, no es palíndormo.")
            break
    # Salida
    print(res)