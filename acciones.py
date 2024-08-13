from entidades import *


def depredacion(depredador, presa):
    # Verificamos si el depredador tiene a la presa en su lista de presas válidas
    if presa.nombre in depredador.presas_validas:
        if isinstance(presa, Planta) and isinstance(depredador, Herbivoro):
            depredador.comer_planta(presa)
        elif isinstance(presa, Animal):
            depredador.depredar(presa)
    # No mostramos ningún mensaje si no es relevante (si no es una presa válida)

def reproduccion(especie):
    nuevos_individuos = int(especie.poblacion * especie.tasa_de_reproduccion)
    especie.poblacion += nuevos_individuos
    print(f"{especie.nombre}: +{nuevos_individuos} nuevos individuos, población total: {especie.poblacion}")

def competencia(especie1, especie2):
    # Asegurarse de que la competencia solo ocurra entre animales
    if isinstance(especie1, Animal) and isinstance(especie2, Animal):
        if especie1.poblacion > especie2.poblacion:
            especie2.poblacion -= int(especie1.poblacion * 0.05)
            print(f"{especie1.nombre} ha superado en número a {especie2.nombre}. Población de {especie2.nombre} reducida a {especie2.poblacion}")
        elif especie2.poblacion > especie1.poblacion:
            especie1.poblacion -= int(especie2.poblacion * 0.05)
            print(f"{especie2.nombre} ha superado en número a {especie1.nombre}. Población de {especie1.nombre} reducida a {especie1.poblacion}")
        else:
            print(f"{especie1.nombre} y {especie2.nombre} están equilibrados, no hay reducción en la población.")
