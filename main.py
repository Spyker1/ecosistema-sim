from ecosistema import *
from entidades import *


def main():
    ambiente = Ambiente(clima="Tropical", recursos={"agua": 100, "alimento": 100})
    ecosistema = Ecosistema(ambiente)

    leon = Animal(nombre="León", poblacion_inicial=5, tasa_de_reproduccion=0.3, tasa_de_depredacion=0.05, presas_validas=["Cebra"])
    zebra = Herbivoro(nombre="Cebra", poblacion_inicial=20, tasa_de_reproduccion=0.5, tasa_de_depredacion=0.05, presas_validas=["Pasto"])
    pasto = Planta(nombre="Pasto", poblacion_inicial=100, tasa_de_reproduccion=0.5)
    aguila = Animal(nombre="Águila", poblacion_inicial=3, tasa_de_reproduccion=0.3, tasa_de_depredacion=0.02, presas_validas=["Cebra", "Peces", "Roedores"])
    oso = Omnivoro(nombre="Oso", poblacion_inicial=5, tasa_de_reproduccion=0.3, tasa_de_depredacion=0.03, presas_validas=["Pasto", "Peces", "Cebra"])

    ecosistema.agregar_especie(leon)
    ecosistema.agregar_especie(zebra)
    ecosistema.agregar_especie(pasto)
    ecosistema.agregar_especie(aguila)
    ecosistema.agregar_especie(oso)

    for _ in range(10):  # Ejecutar 10 ciclos de simulación
        ecosistema.ciclo()
        ambiente.cambiar_estacion()
        ecosistema.evento_natural()

    # Generar gráficos al final de la simulación
    ecosistema.generar_graficos()

if __name__ == "__main__":
    main()

