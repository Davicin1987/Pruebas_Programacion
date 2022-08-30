
print("")

def info_persona():
    datos_persona = {}
    saco = ""
    while True:
        tipo_dato = input("Introduce un nuevo tipo de dato: ")
        nombre_dato = input("Introduce un nuevo nombre de dato: ")
        datos_persona [tipo_dato] = nombre_dato
        print(datos_persona)
        print("")
        seguir = input("¿Quieres introducir un nuevo dato?: ")
        print("")
        if seguir == "No":
            break
    print("Datos personales introducidos: ")
    print("")
    for clave, valor in datos_persona.items():
        saco += " - " + str(clave) + ": " + str(valor) + "\n"
    print(saco)

info_persona()

