import random

def jugar_piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]

    print("                                      ")
    eleccion_usuario = input("Elige piedra, papel o tijeras: ").lower()
    print("-------------------------------------------------------------------------------------------")

    if eleccion_usuario not in opciones:
        print("Por favor, elige una opción válida.")
        return(jugar_piedra_papel_tijeras())

    eleccion_maquina = random.choice(opciones)

    print(f"Tú elegiste: {eleccion_usuario}")
    print(f"La máquina eligió: {eleccion_maquina}")

    if eleccion_usuario == eleccion_maquina:
        print("¡Es un empate!")
    elif (
        (eleccion_usuario == "piedra" and eleccion_maquina == "tijeras") or
        (eleccion_usuario == "papel" and eleccion_maquina == "piedra") or
        (eleccion_usuario == "tijeras" and eleccion_maquina == "papel")
    ):
        print("¡Ganaste!")
    else:
        print("¡La máquina gana!")

def main():
    while True:
        jugar_piedra_papel_tijeras()

        print("                                      ")
        jugar_nuevamente = input("¿Quieres jugar nuevamente? (si/no): ").lower()
        if jugar_nuevamente != 'si':
            break

if __name__ == "__main__":
    main()