class Personaje:
    def __init__(self, id, nombre, genero, altura, peso, color_cabello, color_ojos, color_piel, nacimiento, mundo_natal):
        self.id=id
        self.nombre=nombre
        self.genero=genero
        self.altura=altura
        self.peso=peso
        self.color_cabello=color_cabello
        self.color_ojos=color_ojos
        self.color_piel=color_piel
        self.nacimiento=nacimiento
        self.mundo_natal=mundo_natal

    def mostrar_nombre_personajes(self):
        print(f'\tNombre: {self.nombre}')

    def mostrar_personajes_opcion_cuatro(self):
        None