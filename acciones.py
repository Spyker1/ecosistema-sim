def depredacion(depredador, presa):
    if depredador.poblacion > 0 and presa.poblacion > 0:
        presas_cazadas = int(presa.poblacion * depredador.tasa_de_depredacion)
        presa.poblacion -= presas_cazadas
        if presa.poblacion < 0:
            presa.poblacion = 0
        print(f"{depredador.nombre} cazó {presas_cazadas} de {presa.nombre}. Población de {presa.nombre}: {presa.poblacion}")
    else:
        print(f"{depredador.nombre} no encuentra presas de {presa.nombre}.")

def reproduccion(especie):
    nuevos_individuos = int(especie.poblacion * especie.tasa_de_reproduccion)
    especie.poblacion += nuevos_individuos
    print(f"{especie.nombre}: +{nuevos_individuos} nuevos individuos, población total: {especie.poblacion}")

def competencia(especie1, especie2):
    if especie1.poblacion > especie2.poblacion:
        especie2.poblacion -= int(especie1.poblacion * 0.05)
        print(f"{especie1.nombre} ha superado en número a {especie2.nombre}. Población de {especie2.nombre} reducida a {especie2.poblacion}")
    elif especie2.poblacion > especie1.poblacion:
        especie1.poblacion -= int(especie2.poblacion * 0.05)
        print(f"{especie2.nombre} ha superado en número a {especie1.nombre}. Población de {especie1.nombre} reducida a {especie1.poblacion}")
    else:
        print(f"{especie1.nombre} y {especie2.nombre} están equilibrados, no hay reducción en la población.")
