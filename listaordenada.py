def listaordenada():
    # Entrada
    lista = ((input ("Ingrese su lista de nombres: ")).replace(" y ",",")).split(",")
    listalimp = []
    listadef = []
    # Proceso
    for i in range(len(lista)):
        listalimp.append(lista[i].strip())
    listalimp.sort()
    for i in range((len(listalimp)-1)):
        listadef.append(listalimp[i]+", ")
    listadef.append("y "+listalimp[(len(listalimp)-1)])
    res = "".join(listadef)
    # Salida
    print(f"Tulista ordenada alfabéticamente es: {res}")
