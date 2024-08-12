from ecosistema import *
from entidades import *


def main():
    ambiente = Ambiente(clima="Tropical", recursos={"agua": 100, "alimento": 100})
    ecosistema = Ecosistema(ambiente)

    leon = Animal(nombre="León", poblacion_inicial=5, tasa_de_reproduccion=0.1, tasa_de_depredacion=0.05, presas_validas=["Cebra"])
    zebra = Herbivoro(nombre="Cebra", poblacion_inicial=20, tasa_de_reproduccion=0.2, tasa_de_depredacion=0.05, presas_validas=["Pasto"])
    pasto = Planta(nombre="Pasto", poblacion_inicial=100, tasa_de_reproduccion=0.3)

    ecosistema.agregar_especie(leon)
    ecosistema.agregar_especie(zebra)
    ecosistema.agregar_especie(pasto)

    for _ in range(10):  # Ejecutar 10 ciclos de simulación
        ecosistema.ciclo()

if __name__ == "__main__":
    main()

