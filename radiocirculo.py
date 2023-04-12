# Entrada
def radiocirculo():
    while True:
        radio = input ("ingrese el radio del círculo: ")
        pi = 3.14159264
        # Proceso
        try:
            area = (float(radio)) * (float(radio)) * pi
            perimetro = (float(radio)) * pi * 2
            res = (f"El área del círculo es: {round(area,2)}\nEl perímetro del círculo es:{round(perimetro,2)}")
            break
        except:
            print("El número introducido no es correcto. Intente de nuevo.")
        # Salida
    print(res)