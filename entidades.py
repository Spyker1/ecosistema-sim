import random

class Especie:
    def __init__(self, nombre, poblacion_inicial, tasa_de_reproduccion):
        self.nombre = nombre
        self.poblacion = max(0, poblacion_inicial)
        self.tasa_de_reproduccion = tasa_de_reproduccion
        self.edades = {"juvenil": max(0, poblacion_inicial // 3), "adulto": max(0, poblacion_inicial // 3 * 2), "anciano": 0}
        self.tasa_supervivencia = {"juvenil": 0.9, "adulto": 0.95, "anciano": 0.7}
        self.tasa_reproduccion = {"juvenil": 0, "adulto": tasa_de_reproduccion, "anciano": 0}

    def envejecer(self):
        # Mover edades
        self.edades["anciano"] += self.edades["adulto"]
        self.edades["adulto"] = self.edades["juvenil"]
        self.edades["juvenil"] = 0
        
        # Mortalidad en ancianos
        muertes = int(self.edades["anciano"] * (1 - self.tasa_supervivencia["anciano"]))
        self.edades["anciano"] -= muertes
        self.poblacion -= muertes
        self.poblacion = max(0, self.poblacion)  # Evitar población negativa
        print(f"{self.nombre} perdió {muertes} ancianos.")

    def reproducir(self):
        # Aumentar la tasa de reproducción para reflejar un crecimiento más rápido
        nuevos_juveniles = int(self.edades["adulto"] * self.tasa_reproduccion["adulto"] * 1.5)  # Incrementar la reproducción
        self.edades["juvenil"] += nuevos_juveniles
        self.poblacion += nuevos_juveniles
        print(f"{self.nombre} tiene {nuevos_juveniles} nuevos juveniles. Población total: {self.poblacion}")


class Animal(Especie):
    def __init__(self, nombre, poblacion_inicial, tasa_de_reproduccion, tasa_de_depredacion, presas_validas):
        super().__init__(nombre, poblacion_inicial, tasa_de_reproduccion)
        self.tasa_de_depredacion = tasa_de_depredacion
        self.presas_validas = presas_validas

    def tomar_decision(self, ambiente, ecosistema):
        if self.poblacion < 5:  # Decisión basada en población baja
            self.reproducir()
        elif ambiente.recursos["agua"] < 20:  # Decisión basada en falta de recursos
            self.migrar()
        else:
            # Sólo caza si hay presas disponibles
            presas_disponibles = any(presa.nombre in self.presas_validas and presa.poblacion > 0 for presa in ecosistema.especies)
            if presas_disponibles:
                self.cazar()
            else:
                print(f"{self.nombre} no encontró presas disponibles para cazar.")
                
    def cazar(self):
        if self.poblacion > 0:
            print(f"{self.nombre} está cazando.")
            # Implementar lógica de caza aquí
        else:
            print(f"{self.nombre} no tiene suficiente población para cazar.")


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

class Omnivoro(Animal):
    def __init__(self, nombre, poblacion_inicial, tasa_de_reproduccion, tasa_de_depredacion, presas_validas):
        super().__init__(nombre, poblacion_inicial, tasa_de_reproduccion, tasa_de_depredacion, presas_validas)

    def depredar(self, presa):
        # Omnívoros pueden cazar tanto plantas como animales
        if isinstance(presa, Planta) or isinstance(presa, Animal):
            super().depredar(presa)


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

    def ajustar_recursos(self, recurso, cantidad):
        if recurso in self.recursos:
            self.recursos[recurso] = cantidad
            print(f"El recurso '{recurso}' ha sido ajustado a {cantidad}.")
        else:
            print(f"El recurso '{recurso}' no existe en el ambiente.")

    def cambiar_estacion(self):
        estaciones = ["Primavera", "Verano", "Otoño", "Invierno"]
        nuevo_clima = random.choice(estaciones)
        self.modificar_clima(nuevo_clima)