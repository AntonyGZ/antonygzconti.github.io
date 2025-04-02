import random

# Listas de elementos narrativos
personajes = ["Un joven valiente", "Una sabia anciana", "Un guerrero", "Una hechicera", "Un dragón", "Un villano oscuro"]
lugares = ["un pequeño pueblo", "un misterioso bosque", "una ciudad en ruinas", "un castillo encantado", "un reino lejano"]
objetos = ["una espada mágica", "un amuleto antiguo", "un libro de hechizos", "una poción curativa", "un mapa del tesoro"]

# Función para generar una historia
def generar_historia():
    historia = []
    
    # Generar 5 pasos en la historia
    for i in range(5):
        personaje = random.choice(personajes)
        lugar = random.choice(lugares)
        objeto = random.choice(objetos)
        
        # Estructura de un paso en la historia
        paso = f"En el paso {i+1}, {personaje} se encontró en {lugar} con {objeto}."
        
        historia.append(paso)
    
    return "\n".join(historia)

# Interfaz de usuario básica
def main():
    print("Generador de historias automáticas")
    print("Presiona Enter para generar una historia...")
    input()
    
    historia = generar_historia()
    print("\nTu historia generada:")
    print(historia)

if __name__ == "__main__":
    main()

    