class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy de {self.nacionalidad}")

class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,puesto,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.puesto = puesto
        self.salario = salario

roberto = Empleado("Roberto", 30, "Mexicano", "Ingeniero de Software", 50000)
roberto.hablar() 