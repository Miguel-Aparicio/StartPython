def medialista():
    lista = []
    total = 0
    n = int(input("Ingrese la cantidad de numeros en la lista: "))
    if n.isdigit():
        for i in range(0, n):
            ele = int(input())
            lista.append(ele) 
        for j in lista:
            total = total + j
        total = total/len(lista)
        print(total)
    else: 
        print("El valor introducido no es un numero")