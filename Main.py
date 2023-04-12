import os
import calculoDNI
import salariobase
import radiocirculo
import mayormenornum
import gradoscelsius
import numeropar
import anyobisiesto
import palindromo
import listaordenada
import Ejercicio11
import Ejercicio12
import Ejercicio13
import Ejercicio14
import Ejercicio15
import Ejercicio16
import Ejercicio17
import Ejercicio18
import Ejercicio19
import Ejercicio20

while True:
    os.system('cls') #limpia pantalla
    print('Bienvenidos')
    print('1- Determinar letra del DNI')
    print('2-Calcular salario neto de un empleado')
    print('3-NO DISPONIBLE')
    print('4-Calcular area y perimetro del circulo a partir de su radio')
    print('5-Obtener el numero mayor y menor de una lista')
    print('6-Conversor de grados Celsius a Farenheit')
    print('7-Determinar si un numero entero es par o impar')
    print('8-Determinar si un año es bisiesto o no')
    print('9-Determina si un texto es palindromo')
    print('10-Ordenar nombres por orden alfabético')
    print('11-Calcular el factorial de un número entero')
    print('12-Determinar si un número es primo o no')
    print('13-Calcular área y volumen de un cubo')
    print('14-Sumar todos los nuemros pares de una lista')
    print('15-Determinar si un numero es positivo, negativo o cero)')
    print('16-Calcular la media de una lista de números')
    print('17- Juego: adivina un número del 0 al 100')
    print('18-Determina si dos cadenas de texto son anagramas')
    print('19-Eliminar números duplicados de una lista')
    print('20- Determinar si un número es capicúa')
    print('0- Salir del programa')
    opcion = input('seleccione programa a ejecutar: ')
    if opcion == '1':
      calculoDNI.calculodni()
    elif opcion == '2':
      salariobase.salariobase()
    #elif opcion == '3':
    # Falta ejercicio 3   
    elif opcion == '4':
      radiocirculo.radiocirculo()
    elif opcion == '5':
      mayormenornum.mayormenornum()
    elif opcion == '6':
      gradoscelsius.gradoscelsius()
    elif opcion == '7':
      numeropar.numeropar()
    elif opcion == '8':
      anyobisiesto.anyobisiesto()
    elif opcion == '9':
      palindromo.palindromo()
    elif opcion == '10':
      listaordenada.listaordenada()
    elif opcion == '11':
      Ejercicio11.factorial()
    elif opcion == '12':
      Ejercicio12.numeroprimo()
    elif opcion == '13':
      Ejercicio13.cubo()
    elif opcion == '14':
      Ejercicio14.sumalista()
    elif opcion == '15':
      Ejercicio15.posneg()
    elif opcion == '16':
      Ejercicio16.medialista()
    elif opcion == '17':
      Ejercicio17.adivinarrand()
    elif opcion == '18':
       Ejercicio18.anagrama()
    elif opcion == '19':
       Ejercicio19.elimduplicados()
    elif opcion == '20':
      Ejercicio20.capicua()
    elif opcion == 0:
      print('Un placer, hasta la proxima')
      break
    continuar = input('presione enter para continuar')


  