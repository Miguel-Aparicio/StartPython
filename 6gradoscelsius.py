def gradoscelsius():
    # Entrada
    gradoscelsius = (input ("Ingrese sus grados Celsius: ").replace(",","."))
    # Proceso
    try:
        gradosfahrenheit = (float(gradoscelsius)) * 1.8 + 32
    # Salida
        print(f"El equivalente de {round(gradoscelsius,2)} en grados celsius es {round(gradosfahrenheit,2)} en grados grados fahrenheit.")
    except:
        print("El número introducido no es correcto.")