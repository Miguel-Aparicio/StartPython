def anagrama():
    a = input("Escriba una palabra: ")
    b = input("Escriba otra palabra: ")
    if a.isdigit() or b.isdigit():
        print("El valor insertado no es un numero.")
    else:
        if sorted(a) == sorted(b):
            print("Son anagramas!")
        else:
            print("No son anagramas!")