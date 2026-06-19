import os
os.system('cls')

pokedex = []
opcion = ""

def agregar_pokemon(): #Create (Esta funcion permite agregar el nombre del pokémon(y se asegura que no este vacío/que ya exista) el tipo, nivel, y poder, luego crea un diccionario con los datos y los añade a la lista "pokedex" y luego muestra un mensaje para asegurarse de que funcionó)
    nombre = input("Ingrese nombre del Pokémon: ")
    if nombre == "":
        print ("El nombre no puede estar vacío")
        return
    
    for pokemon in pokedex:
        if pokemon["nombre"].lower() == nombre.lower():
            print ("Ese Pokémon ya existe...")
            return
    
    tipo = input("Ingrese el tipo de su Pokémon: ")
    if tipo == "":
        print("El tipo no puede estar vacío...")
        return
    
    while True:
        try:
            nivel = int(input("Ingrese el nivel de su Pokémon: "))
            break
        except ValueError:
            print("Debe ingresar un número...")

    while True:
        try:
            poder = int(input("Ingrese el poder: "))
            break
        except ValueError:
            print("Debe ingresar un número...")

    pokemon = {
        "nombre": nombre,
        "tipo": tipo,
        "nivel": nivel,
        "poder": poder
    }
    
    pokedex.append(pokemon)

    input("¡Pokémon agregado exitosamente!")

def buscar_pokemon(nombre): #READ (Esta funcion permite buscar un pokémon por su nombre y no devuelve nada si no existe en la lista)
    for pokemon in pokedex:
        if pokemon["nombre"].lower() == nombre.lower():
            return pokemon
    return None

def mostrar_pokedex(): #READ (Esta funcion muestra a todos los pokémon guardados, como la Pokédex...)
    if len(pokedex) == 0:
        input ("La Pokédex esta vacía... ¡Ve a capturar algunos Pokémones!")
        return
    print("-------POKÉDEX-------")
    for pokemon in pokedex:
        print("--------------")
        print(f"Nombre: {pokemon['nombre']}")
        print(f"Tipo: {pokemon['tipo']}")
        print(f"Nivel: {pokemon['nivel']}")
        print(f"Poder: {pokemon['poder']}")
    input("Pulse ENTER para continuar...")

def actualizar_pokemon(): #UPDATE (Esta fución cambia el nombre, tipo, nivel y poder del pokémon seleccionado)

    nombre = input("Ingrese el nombre del Pokémon a modificar: ")
    pokemon = buscar_pokemon(nombre)
    if pokemon == None:
        print("Pokémon no encontrado")
        return
    print("Ingrese los nuevos datos")

    pokemon["nombre"] = input("Nuevo nombre: ")
    pokemon["tipo"] = input("Nuevo tipo: ")

    while True:
        try:
            pokemon["nivel"] = int(input("Nuevo nivel: "))
            break
        except ValueError:
            print("Debe ingresar un número...")

    while True:
        try:
            pokemon["poder"] = int(input("Nuevo poder: "))
            break
        except ValueError:
            print("Debe ingresar un número...")

    input("Pokémon actualizado exitosamente")

def eliminar_pokemon(): #DELETE (Esta función elimina/""Libera"" a un Pokémon)
    nombre = input("INgrese el nombre del Pokémon a liberar: ")
    pokemon= buscar_pokemon(nombre)

    if pokemon == None:
        print("Pokémon no encontrado")
        return
    
    pokedex.remove(pokemon)
    input("Pokémon liberado exitosamente ¡Te hecharemos de menos!")

while opcion != "5":
    os.system('cls')
    print("-------POKÉDEX-------")
    print("1. Capturar un Pokémon")
    print("2. Mostrar la Pokédex")
    print("3. Editar un Pokémon")
    print("4. Liberar un pokémon")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_pokemon()
    
    elif opcion == "2":
        mostrar_pokedex()

    elif opcion == "3":
        actualizar_pokemon()

    elif opcion == "4":
        eliminar_pokemon()
    
    elif opcion == "5":
        input ("Apagando Pokédex, ¡Adiós!")
    
    else:
        input("Debe ingresar una opción valida... Pulse ENTER para continuar")