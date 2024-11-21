class Calculadora:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def suma(self):
        resultado = self._num1 + self._num2
        print(f"💖 La suma del amor es: {self._num1} + {self._num2} = {resultado}")

    def resta(self):
        resultado = self._num1 - self._num2
        print(f"💔 La resta del amor es: {self._num1} - {self._num2} = {resultado}")

    def division(self):
        resultado = self._num1 / self._num2
        print(f"💌 La división del amor es: {self._num1} / {self._num2} = {resultado}")

    def multiplicacion(self):
        resultado = self._num1 * self._num2
        print(f"🌹 La multiplicación del amor es: {self._num1} * {self._num2} = {resultado}")


operacion = Calculadora(10, 5)
operacion.suma()

operacion = Calculadora(20, 5)
operacion.resta()

operacion = Calculadora(15, 3)
operacion.division()

operacion = Calculadora(8, 4)
operacion.multiplicacion()
