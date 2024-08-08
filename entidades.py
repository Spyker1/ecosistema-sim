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
    def __init__(self, nombre, poblacion_inicial, tasa_de_reproduccion, tasa_de_depredacion):
        super().__init__(nombre, poblacion_inicial, tasa_de_reproduccion)
        self.tasa_de_depredacion = tasa_de_depredacion

    def depredar(self, presa):
        if presa.poblacion > 0:
            presas_cazadas = int(presa.poblacion * self.tasa_de_depredacion)
            presa.poblacion -= presas_cazadas
            print(f"{self.nombre} cazó {presas_cazadas} de {presa.nombre}. Población de {presa.nombre}: {presa.poblacion}")
        else:
            print(f"{self.nombre} no encuentra presas de {presa.nombre}.")

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
