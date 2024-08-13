import matplotlib.pyplot as plt

from acciones import *

class Ecosistema:
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.especies = []
        self.historial_poblacion = {}
        self.historial_recursos = {"agua": []}

    def agregar_especie(self, especie):
        self.especies.append(especie)
        self.historial_poblacion[especie.nombre] = []
        print(f"Se ha añadido {especie.nombre} al ecosistema.")

    def ciclo(self):
     print("\n--- Nuevo Ciclo ---")
     for especie in self.especies:
        especie.envejecer()
        especie.reproducir()
        if isinstance(especie, Animal):
            especie.tomar_decision(self.ambiente)
        
        # Almacenar la población
        self.historial_poblacion[especie.nombre].append(especie.poblacion)
        
        print("--- Fin del Ciclo ---\n")

    
    def evento_natural(self):
     eventos = ["Incendio", "Sequía", "Inundación", "Nada"]
     evento = random.choice(eventos)
     if evento == "Incendio":
        print("Ha ocurrido un incendio forestal!")
        for especie in self.especies:
            if isinstance(especie, Planta):
                especie.poblacion = max(0, especie.poblacion - random.randint(5, 20))  # Reducir el impacto
     elif evento == "Sequía":
        print("Ha ocurrido una sequía!")
        self.ambiente.ajustar_recursos("agua", max(0, self.ambiente.recursos["agua"] - random.randint(10, 30)))
     elif evento == "Inundación":
        print("Ha ocurrido una inundación!")
        for especie in self.especies:
            especie.poblacion = max(0, especie.poblacion - random.randint(3, 10))  # Reducir el impacto
        else:
         print("No ha ocurrido ningún evento natural significativo.")


    
    def generar_graficos(self):
        # Graficar la evolución de la población
        plt.figure(figsize=(10, 5))
        for especie, poblacion in self.historial_poblacion.items():
            plt.plot(poblacion, label=especie)
        plt.title("Evolución de la Población por Especie")
        plt.xlabel("Ciclos")
        plt.ylabel("Población")
        plt.legend()
        plt.show()

        # Graficar la evolución de los recursos
        plt.figure(figsize=(10, 5))
        for recurso, cantidad in self.historial_recursos.items():
            plt.plot(cantidad, label=recurso)
        plt.title("Evolución de los Recursos")
        plt.xlabel("Ciclos")
        plt.ylabel("Cantidad")
        plt.legend()
        plt.show()
