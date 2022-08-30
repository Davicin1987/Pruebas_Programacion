
print("")

def cesta_articulos():
    dicc_articulos = {}
    suma_precios = 0
    saco = ""
    while True:
        nom_articulo = input("Introduce el nombre de un artículo: ")
        if nom_articulo != "Salir":
            precio_articulo_s = input("Introduce el precio del artículo elegido: ")
            precio_articulo = round(float(precio_articulo_s), 2)
            numero_unidades_s = input("Introduce cuántas unidades deseas del artículo introducido: ")
            numero_unidades = int(numero_unidades_s)
            importe_total_unidades = precio_articulo * numero_unidades
            dicc_articulos[nom_articulo + "(" + str(numero_unidades) + " unidades)"] = str(importe_total_unidades) + " €"
            suma_precios += importe_total_unidades
            print("")
        elif nom_articulo == "Salir":
            break
    print("")
    print(dicc_articulos)
    print("")
    for nombre, precio in dicc_articulos.items():
        saco += " - " + nombre + ": " + precio + "\n"
    print("Artículos añadidos a la cesta: ")
    print("")
    print(saco)
    print("Importe total de los artículos seleccionados: " + str(suma_precios) + " €.")

cesta_articulos()

