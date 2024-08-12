class Especie:
    def __init__(self, nombre, poblacion_inicial, tasa_de_reproduccion):
        self.nombre = nombre
        self.poblacion = poblacion_inicial
        self.tasa_de_reproduccion = tasa_de_reproduccion

    def reproducir(self):
        nuevos_individuos = int(self.poblacion * self.tasa_de_reproduccion)
        self.poblacion += nuevos_individuos
        print(f"{self.nombre}: +{nuevos_individuos} nuevos individuos, población total: {self.poblacion}")

class Animal(Especie):
    def __init__(self, nombre, poblacion_inicial, tasa_de_reproduccion, tasa_de_depredacion, presas_validas):
        super().__init__(nombre, poblacion_inicial, tasa_de_reproduccion)
        self.tasa_de_depredacion = tasa_de_depredacion
        self.presas_validas = presas_validas

    def depredar(self, presa):
        if presa.nombre in self.presas_validas and presa.poblacion > 0:
            presas_cazadas = int(presa.poblacion * self.tasa_de_depredacion)
            presa.poblacion -= presas_cazadas
            print(f"{self.nombre} cazó {presas_cazadas} de {presa.nombre}. Población de {presa.nombre}: {presa.poblacion}")
        else:
            print(f"{self.nombre} no puede cazar a {presa.nombre}.")

class Herbivoro(Animal):
    def __init__(self, nombre, poblacion_inicial, tasa_de_reproduccion, tasa_de_depredacion, presas_validas):
        super().__init__(nombre, poblacion_inicial, tasa_de_reproduccion, tasa_de_depredacion, presas_validas)

    def comer_planta(self, planta):
        if planta.poblacion > 0:
            cantidad_comida = int(planta.poblacion * self.tasa_de_depredacion)
            planta.poblacion -= cantidad_comida
            print(f"{self.nombre} comió {cantidad_comida} de {planta.nombre}. Población de {planta.nombre}: {planta.poblacion}")
        else:
            print(f"{self.nombre} no encuentra {planta.nombre} para comer.")


class Planta(Especie):
    def __init__(self, nombre, poblacion_inicial, tasa_de_reproduccion):
        super().__init__(nombre, poblacion_inicial, tasa_de_reproduccion)

class Ambiente:
    def __init__(self, clima, recursos):
        self.clima = clima
        self.recursos = recursos

    def modificar_clima(self, nuevo_clima):
        self.clima = nuevo_clima
        print(f"El clima ha cambiado a {self.clima}")

    def ajustar_recursos(self, nuevo_recurso, cantidad):
        self.recursos[nuevo_recurso] = cantidad
        print(f"Recursos actualizados: {self.recursos}")
