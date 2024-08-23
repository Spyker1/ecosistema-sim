from entidades import *


def depredacion(depredador, presa):
    if presa.nombre in depredador.presas_validas and presa.poblacion > 0:
        if isinstance(presa, Planta) and isinstance(depredador, Herbivoro):
            presas_cazadas = min(int(depredador.poblacion * depredador.tasa_de_depredacion), presa.poblacion)
            depredador.poblacion += presas_cazadas
            presa.poblacion -= presas_cazadas
            print(f"{depredador.nombre} comió {presas_cazadas} de {presa.nombre}. Población de {presa.nombre}: {presa.poblacion}")
        elif isinstance(presa, Animal):
            presas_cazadas = min(int(depredador.poblacion * depredador.tasa_de_depredacion), presa.poblacion)
            depredador.poblacion += presas_cazadas
            presa.poblacion -= presas_cazadas
            print(f"{depredador.nombre} cazó {presas_cazadas} de {presa.nombre}. Población de {presa.nombre}: {presa.poblacion}")


def reproduccion(especie):
    nuevos_individuos = max(1, int(especie.poblacion * especie.tasa_de_reproduccion))
    especie.poblacion += nuevos_individuos
    print(f"{especie.nombre}: +{nuevos_individuos} nuevos individuos, población total: {especie.poblacion}")


def competencia(especie1, especie2):
    if isinstance(especie1, Animal) and isinstance(especie2, Animal):
        if especie1.poblacion > especie2.poblacion:
            reduccion = min(int(especie1.poblacion * 0.05), especie2.poblacion)
            especie2.poblacion -= reduccion
            print(f"{especie1.nombre} ha superado en número a {especie2.nombre}. Población de {especie2.nombre} reducida a {especie2.poblacion}")
        elif especie2.poblacion > especie1.poblacion:
            reduccion = min(int(especie2.poblacion * 0.05), especie1.poblacion)
            especie1.poblacion -= reduccion
            print(f"{especie2.nombre} ha superado en número a {especie1.nombre}. Población de {especie1.nombre} reducida a {especie1.poblacion}")
        else:
            print(f"{especie1.nombre} y {especie2.nombre} están equilibrados, no hay reducción en la población.")
