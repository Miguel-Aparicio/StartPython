#Algoritmo CalculoDNI
# Entrada
def calculodni():
    while True:
        dni = input("Introduzca su número de DNI completo para calcular su letra: ")
        listaletras = ["T","R","w","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
# Proceso
        try:
            if int(dni) <= 99999999:
                x = int(dni) %23
                res = f"La letra asignada al DNI {dni} es: {listaletras[x]}."
                break
            elif dni == "":
                res = "Sin DNI"
                break
        except:
            print("Error. DNI introducido incorrecto. Intentelo de nuevo.")
# Salida
    print(res)