def capicua():
    n = input("Ingrese un numero: ")
    if n.isdigit():
        numinv = []*10
        num = [int(x) for x in str(n)]
        for i in reversed(num):
            numinv.append(i)
        if num == numinv:
            print("El numero es capicua!")
        else:
            print("El numero no es capicua")
    else:
        print("El valor insertado no es un numero.")