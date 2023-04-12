def gradoscelsius():
    # Entrada
    while True:
        entrada = (input ("Ingrese sus grados Celsius: ").replace(",","."))
        # Proceso
        try:
            gradoscelsius = float(entrada)
            gradosfahrenheit = gradoscelsius * 1.8 + 32
        # Salida
            res = (f"El equivalente de {round(gradoscelsius,2)} en grados celsius es {round(gradosfahrenheit,2)} en grados grados fahrenheit.")
            break
        except:
            print("El número introducido no es correcto.")
    print(res)