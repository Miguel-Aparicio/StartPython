def elimduplicados():
    lista = []
    n = int(input("Ingrese la cantidad de numeros en la lista: "))
    if n.isdigit():
        for i in range(0, n):
            ele = int(input())
            lista.append(ele)
        print (list(set(lista)))
    else:
        print("El valor insertado no es un numero.")