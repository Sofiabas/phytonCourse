
agenda = []

letras = ["a","b","c","d"]

def checkDocumento(documento):
    try:
        int(documento)
        return True
    except:
        return False


def contactoEnAgenda(documento):
    if documento in agenda:
        return True
    else:
        return False


def borrarContacto():
    try:
        documento = input("Ingrese el documento del contacto ha borrar: ")
        if checkDocumento(documento):
            if documento in agenda:
                del agenda[documento]
                print("Contacto eliminado")
            else:
                print("No se encontró el contacto con el documento" + documento)
            opcion = input(
                "a) Volver al menú principal" +
                "\nb) Borrar otro contacto" +
                "\nIngrese una opción: "
            )
            if opcion == "a":
                menu()
            elif opcion == "b":
                borrarContacto()
            else:
                errorMenu("b", "La opción ingresada no es válida")
        else:
            errorMenu(
                "b", "El n° de documento ingresado es incorrecto. Intente nuevamente ingresando el n° sin puntos")
    except:
        errorMenu("b")

def listarContacto(): 
    contador_contacto = 0
    for key, contacto in agenda.items():
        contador_contacto += 1
        print("CONTACTO" + str(contador_contacto))
        print("Apellido y nombre: " + str(contacto["apellido"]) + ", " + str(contacto["nombre"]))
        print()
    opcion = input(
                "a) Volver al menú principal" +
                "\nb) Imprimir agenda nuevamente" +
                "\nIngrese una opción: "
            )
    if opcion == "a":
        menu()
    elif opcion == "b":
        listarContacto()
    else:
        errorMenu("d", "La opción ingresada no existe.")

def extraerContacto(): 
    apellido = input("Ingresa el apellido del contacto a buscar: ")
    encontrados = 0
    for key, contacto in agenda.items():
        if apellido.lower() == contacto["apellido"].lower(): 
            encontrados += 1
            print(
                "Apellido y nombre: " + str(contacto["apellido"]) + ", " + str(contacto["nombre"]) +
                "\nN° de doc.: " + str(contacto["documento"]) +
                "\nFecha de nacimiento: " + str(contacto["fecha de nacimiento"]) +
                "\nDirección: " + str(contacto["direccion"])
            )
    if encontrados == 0:
        print("No se encontraron contactos con el apellido ingresado.")
    opcion = input(
                "a) Volver al menú principal" +
                "\nb) Agregar otro contacto" +
                "\nIngrese una opción: "
            )
    if opcion == "a":
        menu()
    elif opcion == "b":
        extraerContacto()
    else:
        errorMenu("c", "La opción ingresada no existe.")

def grabarContacto():
    try:
        contacto = input("Ingresa Apellido, Nombres, DNI(entero sin puntos), Direccion y fecha de nacimiento \nseparando cada dato con coma (,): ")
        data_del_contacto = contacto.split(",")
        dato_ok = [0, "Sin errores."] 
        if len(data_del_contacto) == 5:
            for dato in data_del_contacto:
                if len(dato) > 0:
                    if dato_ok[0] == 2:
                        if checkDocumento(data_del_contacto[2]) != True:
                            dato_ok[0] -= 1
                            dato[1] -= "Error en el n° de documento ingresado." 
                    dato_ok[0] += 1
                else:
                    if dato_ok[0] == 0:
                        dato_ok[1] = "Error en el apellido ingresado."
                    elif dato_ok[0] == 1:
                        dato_ok[1] = "Error en el/los nombre/s ingresado/s."
                    elif dato_ok[0] == 3:
                        dato_ok[1] = "Error en la dirección ingresada."
                    elif dato_ok[0] == 4:
                        dato_ok[1] = "Error en la fecha de nacimiento ingresada."
            if dato_ok[0] == 5 and dato_ok[1] == "Sin errores.":
                agenda[data_del_contacto[2]] = {
                    "apellido": data_del_contacto[0],
                    "nombre": data_del_contacto[1],
                    "documento": data_del_contacto[2],
                    "direccion": data_del_contacto[3],
                    "fecha de nacimiento": data_del_contacto[4]
                }
                print("Contacto guardado correctamente! Volviendo al menú...")
                opcion = input("" +
                            "a) Volver al menú principal" +
                            "\nb) Agregar otro contacto" +
                            "\nIngrese una opción: ")
                if opcion == "a":
                    menu()
                elif opcion == "b":
                    grabarContacto()
                else:
                    errorMenu("a", "La opción ingresada no existe.")
            else:
                print("Ocurrió un error:")
                print(dato_ok[1])

        else:
            errorMenu("a", "Faltan datos para completar el contacto. Asegurate de ingresar los 5 valores, separados por coma.")
    except:
        errorMenu("a")



def errorMenu(opcion_menu, msg="Ocurrió un error inesperado."):
    print(msg)
    try:
        menu_principal = True
        while menu_principal:
            opcion = input("" +
                        "a) Volver al menú principal" +
                        "\nb) Intentar nuevamente" +
                        "\nIngrese una opción: ")
            if opcion == "a":
                menu()
                break
            elif opcion == "b":
                if opcion == "a":
                    grabarContacto()
                    break
                elif opcion == "b":
                    borrarContacto()
                    break
                elif opcion == "c":
                    extraerContacto()
                    break
                elif opcion == "d":
                    listarContacto()
                    break
            else:
                print("Ingresa una de las opciones disponibles (a-b)")
                input("Presiona enter para continuar...")

    except Exception:
        errorMenu(opcion_menu)

def menu():
    try:
        menu_principal = True
        while menu_principal:
            opcion = input("" +
                        "a) Grabar un contacto" +
                        "\nb) Borrar un contacto" +
                        "\nc) Extraer un contacto de la agenda" +
                        "\nd) Lista de contactos" +
                        "\nIngresa una opción: ")
            print(opcion)
            if opcion == "a":
                grabarContacto()
                break
            elif opcion == "b":
                borrarContacto()
                break
            elif opcion == "c":
                extraerContacto()
                break
            elif opcion == "d":
                listarContacto()
                break
            else:
                print("Ingresa una de las opciones disponibles (a-b-c-d)")
                input("Presiona enter para continuar...")
    except:
        print("Ingresa una de las opciones disponibles (a-b-c-d)")
        input("Presiona enter para continuar...")
        menu()


menu()
