# Sepulveda Gonzalez Angel Alejandro, 3W,1215
class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio


class Moto(Fabrica):
    def cantidad(self):
        print("💖 Cantidad de llantas: {}\n🌹 Color del amor: {}\n💌 Precio: {}".format(self._llantas, self._color, self._precio))


class Carro(Fabrica):
    def cantidad(self):
        print("💖 Cantidad de llantas: {}\n🌹 Color del amor: {}\n💌 Precio: {}".format(self._llantas, self._color, self._precio))


print("🌟 OBJETO = moto 🌟")
moto = Moto(2, "Gris", "$200")
moto.cantidad()

print("\n🌟 OBJETO = carro 🌟")
carro = Carro(4, "Negro", "$600")
carro.cantidad()
