import json
import datetime
import sys
usuario = None #guarda el usuario del login en una variable global.

# Funcion de seteo de intentos de acceso y seleccion automatica de la funcionAdmin o funcionUsuario
def login():
    intentos = 0
    max_intentos = 3

    # Lee el archivo JSON y lo cierra automáticamente al finalizar el bloque
    with open('usuarios.json') as file:
        usuarios = json.load(file)

        while intentos < max_intentos:
            # Solicita al usuario que ingrese su usuario y clave
            print (f"Bienvenido! para continuar debe ingresar su número usuario y contraseña, tiene {max_intentos-intentos} intentos:")
            global usuario
            usuario = input("Ingrese su usuario: ")
            clave = input("Ingrese su clave: ")
            

            # Verifica las credenciales
            for usuario_info in usuarios:
                if str(usuario_info["usuario"]) == usuario and usuario_info["clave"] == clave:
                    if usuario_info["info"] == "Administrador":
                        # Ejecuta el programa para el administrador
                        seg_contrasenia(clave) 
                        ejecutar_programa_administrador()
                    else:
                        # Ejecuta el programa para otros usuarios
                        seg_contrasenia(clave) 
                        ejecutar_programa_usuario()
                    return

            # Si las credenciales no coinciden
            print("Credenciales inválidas.")
            intentos += 1
        # Si supera los 3 intentos
        print("🚫🚫🚫 USUARIO o CLAVE Invalidos 🚫🚫🚫\nLa aplicación no permite ingresar más de 3 intentos, mañana podrá volver a intentarlo. Gracias.")
    
# Aqui esta la funcion de el menu Admin con sus opciones:
def ejecutar_programa_administrador():
    proveedores = list ()
    def mostrar_bienvenida_admin():
        mensaje = "********* 🔓 Bienvenido al modo Administrador 🔓 *********\nTe mostramos todo lo que podés hacer desde la app de tu consorcio, sin moverte de donde estés. Selecciona tu opción:\n"
        mensaje += "[1] Gestion de Usuarios\n"
        mensaje += "[2] Administrar Proveedores\n"
        mensaje += "[3] Obtener Reportes\n"
        mensaje += "[6] Salir del sistema\n"
        return mensaje

    def mostrar_submenu(opcion):
        submenus = {
            1: {
                "mensaje": "Has seleccionado la opción 1: Gestion de Usuarios.",
                "opciones": {
                    1: "Listar Usuarios",
                    2: "Crear Usuario",
                    3: "Eliminar Usuario",
                    0: "Volver al Menú Principal"
                }
            },
            2: {
                "mensaje": "Has seleccionado la opción 2: Datos de proveedores.",
                "opciones": {
                    1: "Listar Proveedores",
                    2: "Modificar Proveeedores",
                    3: "Eliminar Proveedores",
                    4: "Agregar Nuevo Proveedor",
                    0: "Volver al Menú Principal"
                }
            },
            3: {
                "mensaje": "Has seleccionado la opción 3: Reportes.",
                "opciones": {
                    1: "Ultimas expensas",
                    2: "Listar reclamos",
                    0: "Volver al Menú Principal"
                }
            },
            6: {
                "mensaje": "Muchas Gracias por usar nuestro sistema. Vuelva pronto! 👍",
                "opciones": {
                
                }
            }
        }

        submenu_info = submenus.get(opcion)
        if submenu_info:
            submenu_mensaje = submenu_info["mensaje"]
            submenu_opciones = submenu_info["opciones"]
            submenu = f"{submenu_mensaje}\n"
            for key, value in submenu_opciones.items():
                submenu += f"[{key}] {value}\n"
            return submenu
        elif opcion == 0:
            return mostrar_bienvenida_admin()
        else:
            return "Opción inválida. Por favor, selecciona una opción válida."

    # codigo
    opcion = None
    while opcion != 6:
        bienvenida = mostrar_bienvenida_admin()
        print(bienvenida)

        opcion = int(input("Selecciona una opción: "))
        submenu = mostrar_submenu(opcion)
        print(submenu)

        if opcion == 1:
            subopcion = None
            while subopcion != 0:
                subopcion = int(input("Selecciona una opción del submenú: "))
                if subopcion == 0:
                    break
                #aca van cada una de las subopciones del submenu 1 listar Usuarios:
                if subopcion == 1:
                    print ("los usuarios actuales son: ")
                    archivoUsuarios = open("usuarios.json", "r") #si se mueve el archivo a otro file, modificar la ruta
                    usuarios = json.loads(archivoUsuarios.read())
                    for usuario in usuarios:
                        print ("-"*30)
                        for clave, valor in usuario.items():
                            print (f"{clave}: {valor}")
                    archivoUsuarios.close
                    print("[0] Volver al Menú Principal")

                #Submenu  AGREGAR NUEVO USUARIO    
                if subopcion == 2:
                    with open("usuarios.json", "r") as archivoUsuarios:
                        usuarios = json.load(archivoUsuarios)
                    print("A continuacion agregue los datos del nuevo usuario:")

                    nuevo_usuario = input("Ingrese el nuevo usuario: ")
                    nuevo_clave = input("Ingrese la nueva clave: ")
                    nuevo_info = input("Ingrese la nueva infomracion util: ")
                    
                    # Crear el diccionario del nuevo usuario
                    nuevo_usuario = {
                        "id_usuario": (len(usuarios))+1,
                        "usuario": nuevo_usuario,
                        "clave": nuevo_clave,
                        "info": nuevo_info
                    }

                    # Abrir el archivo JSON en modo de lectura
                    with open("usuarios.json", "r") as archivoUsuarios:
                        usuarios = json.load(archivoUsuarios)

                        # Agregar el nuevo usuario a la lista de usuarios
                        usuarios.append(nuevo_usuario)

                    # Guardar los datos actualizados en el archivo JSON
                    with open("usuarios.json", "w") as archivoUsuarios:
                        json.dump(usuarios, archivoUsuarios, indent=4)

                    print(f"el siguiente usuario fue agregado exitosamente:")
                    print(f"Usuario '{nuevo_usuario}")
                    print("[0] Volver al Menú Principal")
                    
                #Submenu ELIMINAR USUARIO
                if subopcion == 3:
                    print("Los USUARIOS actuales son:")
                    with open("usuarios.json", "r") as archivoUsuarios:
                        usuarios = json.load(archivoUsuarios)
                        for usuario in usuarios:
                            print("-" * 30)
                            for clave, valor in usuario.items():
                                print(f"{clave}: {valor}")

                    opcion_usuario = int(input("Ingrese el ID del USUARIO que desea ELIMINAR (0 para volver): "))

                    if opcion_usuario == 0:
                    # Volver al menú principal
                        break

                    if opcion_usuario > 0 and opcion_usuario <= len(usuarios):
                        usuario_eliminado = usuarios.pop(opcion_usuario - 1)
                    
                        # Guardar los datos actualizados en el archivo JSON
                        with open("usuarios.json", "w") as archivoUsuarios:
                            json.dump(usuarios, archivoUsuarios, indent=4)

                        print(f"Usuario eliminado exitosamente.")
                        archivoUsuarios.close
                    else:
                        print("Opción inválida.")    
                        
                    print("[0] Volver al Menú Principal")
                    
        if opcion == 2:
            subopcion = None
            while subopcion != 0:
                subopcion = int(input("Selecciona una opción del submenú: "))
                if subopcion == 0:
                    break
                #aca van cada una de las subopciones del submenu 2:
                if subopcion == 1:
                    print ("los proveedores actuales son: ")
                    archivoProveedores = open("proveedores.json", "r") #si se mueve el archivo a otro file, modificar la ruta
                    proveedores = json.loads(archivoProveedores.read())
                    for proveedor in proveedores:
                        print ("-"*30)
                        for clave, valor in proveedor.items():
                            print (f"{clave}: {valor}")
                    archivoProveedores.close
                    print("[0] Volver al Menú Principal")

                if subopcion == 2:
                    print("Los proveedores actuales son:")
                    with open("proveedores.json", "r") as archivoProveedores:
                        proveedores = json.load(archivoProveedores)
                        for proveedor in proveedores:
                            print("-" * 30)
                            for clave, valor in proveedor.items():
                                print(f"{clave}: {valor}")

                    opcion_proveedor = int(input("Ingrese el ID del proveedor que desea modificar (0 para volver): "))

                    if opcion_proveedor == 0:
                    # Volver al menú principal
                        break

                    if opcion_proveedor > 0 and opcion_proveedor <= len(proveedores):
                        proveedor_seleccionado = proveedores[opcion_proveedor - 1]

                        # Realizar las modificaciones necesarias en el proveedor seleccionado
                        nuevo_consorcio = input("Ingrese el nuevo consorcio del proveedor: ")
                        nuevo_servicio = input("Ingrese el nuevo servicio del proveedor: ")
                        nuevo_proveedor = input("Ingrese el nuevo proveedor del proveedor: ")
                        nuevo_telefono = input("Ingrese el nuevo teléfono del proveedor: ")
                        nuevo_info = input("Ingrese la nueva info del proveedor: ")
                        proveedor_seleccionado["consorcio"] = nuevo_consorcio
                        proveedor_seleccionado["servicio"] = nuevo_servicio
                        proveedor_seleccionado["proveedor"] = nuevo_proveedor
                        proveedor_seleccionado["telefono"] = nuevo_telefono

                        # Guardar los datos modificados en el archivo JSON
                        with open("proveedores.json", "w") as archivoProveedores:
                            json.dump(proveedores, archivoProveedores, indent=4)

                        print("Proveedor modificado exitosamente.")
                        archivoProveedores.close
                    else:
                        print("Opción inválida.")

                if subopcion == 3:
                    print("Los proveedores actuales son:")
                    with open("proveedores.json", "r") as archivoProveedores:
                        proveedores = json.load(archivoProveedores)
                        for proveedor in proveedores:
                            print("-" * 30)
                            for clave, valor in proveedor.items():
                                print(f"{clave}: {valor}")

                    opcion_proveedor = int(input("Ingrese el ID del proveedor que desea ELIMINAR (0 para volver): "))

                    if opcion_proveedor == 0:
                    # Volver al menú principal
                        break

                    if opcion_proveedor > 0 and opcion_proveedor <= len(proveedores):
                        proveedor_eliminado = proveedores.pop(opcion_proveedor - 1)
                    
                        # Guardar los datos actualizados en el archivo JSON
                        with open("proveedores.json", "w") as archivoProveedores:
                            json.dump(proveedores, archivoProveedores, indent=4)

                        print(f"Proveedor eliminado exitosamente.")
                        archivoProveedores.close
                    else:
                        print("Opción inválida.")    
                        
                    print("[0] Volver al Menú Principal")

                if subopcion == 4:
                    with open("proveedores.json", "r") as archivoProveedores:
                        proveedores = json.load(archivoProveedores)
                    print("A continuacion agregue los datos del nuevo proveedor:")

                    nuevo_consorcio = input("Ingrese la direccion de consorcio: ")
                    nuevo_servicio = input("Ingrese el servicio: ")
                    nuevo_proveedor = input("Ingrese el nombre del nuevo proveedor: ")
                    nuevo_telefono = input("Ingrese teléfono: ")
                    nuevo_info = input("Ingrese la informacion util: ")
                    
                    # Crear el diccionario del nuevo proveedor
                    nuevo_proveedor = {
                        "id": (len(proveedores))+1,
                        "consorcio": nuevo_consorcio,
                        "servicio": nuevo_servicio,
                        "proveedor": nuevo_proveedor,
                        "telefono": nuevo_telefono,
                        "info": nuevo_info
                    }

                    # Abrir el archivo JSON en modo de lectura
                    with open("proveedores.json", "r") as archivoProveedores:
                        proveedores = json.load(archivoProveedores)

                        # Agregar el nuevo proveedor a la lista de proveedores
                        proveedores.append(nuevo_proveedor)

                    # Guardar los datos actualizados en el archivo JSON
                    with open("proveedores.json", "w") as archivoProveedores:
                        json.dump(proveedores, archivoProveedores, indent=4)

                    print(f"el siguiente proveedor fue agregado exitosamente:")
                    print(f"Proveedor '{nuevo_proveedor}")
                    print("[0] Volver al Menú Principal")
            

        if opcion == 3:
                subopcion = None
                while subopcion != 0:
                    subopcion = int(input("Selecciona una opción del submenú: "))
                    if subopcion == 0:
                        break
                    #aca van cada una de la subopcion para listar expensas:
                    if subopcion == 1:
                        print ("el detalle de expensas es: ")
                        archivoExpensas = open("expensas.json", "r") #si se mueve el archivo a otro file, modificar la ruta
                        expensas = json.loads(archivoExpensas.read())
                        for expensa in expensas:
                            print ("-"*30)
                            for clave, valor in expensa.items():
                                print (f"{clave}: {valor}")
                        archivoExpensas.close
                        print("[0] Volver al Menú Principal")

                    # Para listar los reclamos actuales   
                    if subopcion == 2:
                        print ("los reclamos actuales son: ")
                        archivoReclamos = open("reclamos.json", "r") #si se mueve el archivo a otro file, modificar la ruta
                        reclamos = json.loads(archivoReclamos.read())
                        for reclamo in reclamos:
                            print ("-"*30)
                            for clave, valor in reclamo.items():
                                print (f"{clave}: {valor}")
                        archivoReclamos.close
                        print("[0] Volver al Menú Principal")

# Aquí va la funcion del menu para los usuarios que no son ADMIN:
def ejecutar_programa_usuario():
    print("Ejecutando programa para otros usuarios...")
    
    def mostrar_bienvenida_usuario():
        mensaje = "**** Bienvenido usuario ****\nTe mostramos todo lo que podés hacer desde la app de tu consorcio, sin moverte de donde estés. Selecciona tu opción:\n"
        mensaje += "[1] Conocé más de tu consorcio\n"
        mensaje += "[2] Últimas expensas\n"
        mensaje += "[3] Informá tu pago\n"
        mensaje += "[4] Inicia un reclamo\n"
        mensaje += "[6] Salir del sistema\n"
        return mensaje

    def mostrar_submenu(opcion):
        submenus = {
            1: {
                "mensaje": "Has seleccionado la opción 1: Conocé más de tu consorcio.",
                "opciones": {
                    1: "Dirección",
                    2: "CUIT",
                    3: "Tu encargado",
                    4: "Telefonos Utiles",
                    0: "Volver al Menú Principal"
                }
            },
            2: {
                "mensaje": "Has seleccionado la opción 2: Últimas expensas.",
                "opciones": {
                    1: "Monto de expensa actual",
                    2: "Expensas historicas",
                    0: "Volver al Menú Principal"
                }
            },
            3: {
                "mensaje": "Has seleccionado la opción 3: Informá tu pago.",
                "opciones": {
                    1: "Ingresa los datos de tu comprobante",
                    0: "Volver al Menú Principal"
                }
            },
            4: {
                "mensaje": "Has seleccionado la opción 4: Inicia un reclamo.",
                "opciones": {
                    1: "Nuevo Reclamo",
                    0: "Volver al Menú Principal"
                }
            },
            6: {
                "mensaje": "Muchas Gracias por usar nuestro sistema. Vuelva pronto!",
                "opciones": {
                
                }
            }
        }

        submenu_info = submenus.get(opcion)
        if submenu_info:
            submenu_mensaje = submenu_info["mensaje"]
            submenu_opciones = submenu_info["opciones"]
            submenu = f"{submenu_mensaje}\n"
            for key, value in submenu_opciones.items():
                submenu += f"[{key}] {value}\n"
            return submenu
        elif opcion == 0:
            return mostrar_bienvenida_usuario()
        else:
            return "Opción inválida 🚫. Por favor, selecciona una opción válida."

    # CODIGO:
    opcion = None
    while opcion != 6:
        bienvenida = mostrar_bienvenida_usuario()
        print(bienvenida)

        opcion = int(input("Selecciona una opción: "))
        submenu = mostrar_submenu(opcion)
        print(submenu)

        if opcion == 1:
            subopcion = None
            while subopcion != 0:
                subopcion = int(input("Selecciona una opción del submenú: "))
                if subopcion == 0:
                    break
                #aca van cada una de las subopciones del submenu 1:

                #Opcion para mostrar la Direccion del consorcio del usuario:
                if subopcion == 1:
                    # 1. Leer el archivo JSON y cargar su contenido en una variable
                    with open('expensas.json') as file:
                         expensas_data = json.load(file)

                    # 2. Recorrer la lista de elementos del archivo JSON y buscar el elemento que coincida con el número de documento ingresado por el usuario
                    for expensa in expensas_data:
                        if expensa["usuario_dni"] == usuario:
                            # 4. Mostrar el valor de los campos correspondientes a las ultimas expensas si se encuentra el elemento
                            print(f"La direccion de consorcio asociada a tu usuario: ´{usuario}´ es: ", expensa["Consorcio"])

                    print("[0] Volver al Menú Principal")

                #Opcion para conocer el CUIT del consorcio del usuario logueado
                if subopcion == 2:
                    with open('expensas.json') as file:
                         expensas_data = json.load(file)

                    # 2. Recorrer la lista de elementos del archivo JSON y buscar el elemento que coincida con el número de documento ingresado por el usuario
                    for expensa in expensas_data:
                        if expensa["usuario_dni"] == usuario:
                            # 4. Mostrar el valor de los campos correspondientes a las ultimas expensas si se encuentra el elemento
                            print(f"El CUIT de consorcio asociada a tu usuario: ´{usuario}´ es: ", expensa["CUIT_consorcio"])                    
                    print("[0] Volver al Menú Principal")

                #Opcion para conocer el nombre y detalle del encargado:
                if subopcion == 3:
                    with open('expensas.json') as file:
                         expensas_data = json.load(file)

                    # 2. Recorrer la lista de elementos del archivo JSON y buscar el elemento que coincida con el número de documento ingresado por el usuario
                    for expensa in expensas_data:
                        if expensa["usuario_dni"] == usuario:
                            # 4. Mostrar el valor de los campos correspondientes a las ultimas expensas si se encuentra el elemento
                            print(f"Tu Encargado se llama: ", expensa["Encargado"])     
                    print("[0] Volver al Menú Principal")
                if subopcion == 4:
                    print("Estos son algunos telefonos Utiles 📞")
                    print("Emergencias con el ascensor 🚡? llama a la empresa Testa SA al 1112-2223")
                    print("Policia 🚓: 911")
                    print("Bomberos 🚒: 100")
                    print("Defensa Civil ⛑️ : 103")
                    print("SAME 🚑: 107")
                    print("[0] Volver al Menú Principal")
        if opcion == 2:
                subopcion = None
                while subopcion != 0:
                    subopcion = int(input("Selecciona una opción del submenú: "))
                    if subopcion == 0:
                        break
                    
                    #codigo para mostrar las ultimas expensas del usuario que se loguea:
                    if subopcion == 1:
                        # 1. Leer el archivo JSON y cargar su contenido en una variable
                        with open('expensas.json') as file:
                            expensas_data = json.load(file)

                        for expensa in expensas_data:
                            if expensa["usuario_dni"] == usuario:
                                # 2_ Mostrar el valor del campo "Monto_ultimas_expensas" si se encuentra el elemento
                                print(f"El monto de las últimas expensas de tu usuario ´{usuario}´ es de: $ ", expensa["Monto_ultimas_expensas"])

                        print("[0] Volver al Menú Principal")
                        #debajo el codigo que muestra las expensas historicas del usuario que se logueo:
                    
                    #subopcion para  mostrar las expensas historicas del usuario:
                    if subopcion == 2:
                        # 1. Leer el archivo JSON y cargar su contenido en una variable
                        with open('expensas.json') as file:
                            expensas_data = json.load(file)

                        for expensa in expensas_data:
                            if expensa["usuario_dni"] == usuario:
                                # 4. Mostrar el valor de los campos correspondientes a las ultimas expensas si se encuentra el elemento
                                print(f"El monto de las expensas historicas de tu usuario ´{usuario}´ son: \n", expensa["Expensas_informadas"])
                                print("Enero 2023: $",expensa["enero_2023"])
                                print("Febrero 2023: $",expensa["febrero_2023"])
                                print("Marzo 2023: $",expensa["marzo_2023"])
                                print("Abril 2023: $",expensa["abril_2023"])
                                print("Mayo 2023: $",expensa["mayo_2023"])

                        print("[0] Volver al Menú Principal")
        if opcion == 3:
                subopcion = None
                while subopcion != 0:
                    subopcion = int(input("Selecciona una opción del submenú: "))
                    if subopcion == 0:
                        break
                    #aca van cada una de las subopciones del submenu 3:
                    #Opcion para cargar comprobante de pago de expensas:
                    if subopcion == 1:
                        with open("comprobantes.json", "r") as archivoComprobantes:
                            comprobantes = json.load(archivoComprobantes)

                        comprobante_fecha_de_comprobante = input("ingrese la fecha de pago que consta en su comprobante en formato dd/mm/yyyy: ")
                        comprobante_monto_abonado = input("Ingrese en pesos el importe abonado: ")
                        comprobante_DEPTO = input("Ingrese cual es su DEPTO/UF/Local: ")
                        # Creando el diccionario del nuevo reclamo:
                        nuevo_comprobante = {
                            "id": (len(comprobantes))+1,
                            "usuario_dni": usuario, #usa el usuario guardado en memoria
                            "fecha": datetime.date.today().strftime("%d/%m/%Y"),
                            "fecha_de_comprobante": comprobante_fecha_de_comprobante,
                            "monto_abonado": comprobante_monto_abonado,
                            "DEPTO": comprobante_DEPTO
                        }

                        # Abrir el archivo JSON en modo de lectura
                        with open("comprobantes.json", "r") as archivoComprobantes:
                            comprobantes = json.load(archivoComprobantes)

                            # Agregar el nuevo pago a la lista de comprobantes
                            comprobantes.append(nuevo_comprobante)

                        # Guardar los datos actualizados en el archivo JSON
                        with open("comprobantes.json", "w") as archivoComprobantes:
                            json.dump(comprobantes, archivoComprobantes, indent=4)

                        print(f"el pago de la expensa fue cargado para revision exitosamente por el usuario {usuario}:")
                        print("[0] Volver al Menú Principal")
        if opcion == 4:
                subopcion = None
                while subopcion != 0:
                    subopcion = int(input("Selecciona una opción del submenú: "))
                    if subopcion == 0:
                        break
                    #aca subopcion para ingresar un nuevo reclamo:
                    if subopcion == 1:
                        with open("reclamos.json", "r") as archivoReclamos:
                            reclamos = json.load(archivoReclamos)

                        nuevo_comentario = input("Ingrese su reclamo en este espacio en menos de 200 caracteres: ")
                        while len(nuevo_comentario) > 200:
                            print(f"El comentario excede por {len(nuevo_comentario)-200} los 200 caracteres. Intente nuevamente.")
                            nuevo_comentario = input("Ingrese su reclamo en este espacio en menos de 200 caracteres: ")
                        print("Comentario válido, Gracias:")

                        nuevo_contacto = input("Ingrese los datos de como quiere que lo contactemos: ")
                        
                        # Creando el diccionario del nuevo reclamo:
                        nuevo_reclamo = {
                            "id": (len(reclamos))+1,
                            "fecha": datetime.date.today().strftime("%d/%m/%Y"),
                            "comentarios": nuevo_comentario,
                            "usuario": usuario, #usa el usuario guardado en memoria
                            "contacto": nuevo_contacto
                        }

                        # Abrir el archivo JSON en modo de lectura
                        with open("reclamos.json", "r") as archivoReclamos:
                            reclamos = json.load(archivoReclamos)

                            # Agregar el nuevo reclamo a la lista de reclamos
                            reclamos.append(nuevo_reclamo)

                        # Guardar los datos actualizados en el archivo JSON
                        with open("reclamos.json", "w") as archivoReclamos:
                            json.dump(reclamos, archivoReclamos, indent=4)

                        print(f"el siguiente reclamo fue agregado exitosamente por el usuario {usuario}:")
                        print(f"Reclamo '{nuevo_reclamo}")
                        print("[0] Volver al Menú Principal")

#Funcion que evalua y muestra la seguridad de la clave
def seg_contrasenia(clave):
    num_caracteres = len(clave)

    if num_caracteres <= 3:
        print(f"Le debemos informar que su contraseña posee {num_caracteres} caracteres, lo que significa que es débil en términos de seguridad.")
    elif num_caracteres >= 4 and num_caracteres <= 7:
        print(f"Le debemos informar que su contraseña posee {num_caracteres} caracteres, lo que significa que es normal en términos de seguridad.")
    else:
        print(f"Le debemos informar que su contraseña posee {num_caracteres} caracteres, lo que significa que es fuerte en términos de seguridad.")

# Llama a la función de inicio de sesión
login()
