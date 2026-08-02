class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy de {self.nacionalidad}")

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f"Mi habilidad es {self.habilidad}")

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa

    def mostrar_informacion(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años, soy de {self.nacionalidad}, mi habilidad es {self.habilidad}, gano {self.salario} y trabajo en {self.empresa}")

roberto = EmpleadoArtista("Roberto", 30, "Mexicano", "Pintura", 50000, "Empresa X")
roberto.hablar()
roberto.mostrar_habilidad()
roberto.mostrar_informacion()