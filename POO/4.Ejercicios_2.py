class Persona:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

    

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre,edad)
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} está en grado {self.grado}")

estudiante1 = Estudiante("Juan", 20, "10mo")
estudiante1.datos()
estudiante1.estudiar()  