class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"el estudiante {self.nombre} está estudiando en el grado {self.grado}")


input_nombre = input("Ingrese el nombre del estudiante: ")
input_edad = int(input("Ingrese la edad del estudiante: "))
input_grado = input("Ingrese el grado del estudiante: ")

estudiante1 = Estudiante(input_nombre, input_edad, input_grado)

estudiante1.estudiar  () 