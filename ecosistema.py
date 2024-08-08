from entidades import Animal, Planta, Ambiente
from acciones import depredacion, reproduccion, competencia

class Ecosistema:
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.especies = []

    def agregar_especie(self, especie):
        self.especies.append(especie)
        print(f"Se ha añadido {especie.nombre} al ecosistema.")

    def ciclo(self):
        print("\n--- Nuevo Ciclo ---")
        for especie in self.especies:
            # Cada especie se reproduce
            reproduccion(especie)
        
        # Interacciones de depredación
        for depredador in self.especies:
            for presa in self.especies:
                if isinstance(depredador, Animal) and depredador != presa:
                    depredacion(depredador, presa)

        # Competencia entre especies
        if len(self.especies) > 1:
            for i in range(len(self.especies)):
                for j in range(i+1, len(self.especies)):
                    competencia(self.especies[i], self.especies[j])

        print("--- Fin del Ciclo ---\n")
