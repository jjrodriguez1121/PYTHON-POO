class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Llamando desde el {self.modelo}")

    def colgar(self):
        print(f"Colgando la llamada en el {self.modelo}")

celular1 = Celular("Samsung", "Galaxy S21", "108MP")
celular2 = Celular("Apple", "iPhone 13", "12MP")

celular1.llamar()
celular1.colgar()
celular2.llamar()
celular2.colgar()
