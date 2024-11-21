# Angel Alejandro Sepulveda Gonzalez, 3W, 1215

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"🌹 Nombre: {self.nombre} \n💌 Nota de amor: {self.nota}")

    def resultados(self):
        if self.nota >= 7:
            print("💖 ¡Tu amor ha sido correspondido! 💖")
        else:
            print("💔 Parece que el amor no floreció esta vez. 💔")


estudiante1 = Estudiante("Pedro", 5)
estudiante1.imprimir()  
estudiante1.resultados()  

estudiante2 = Estudiante("Elizabeth", 7)
estudiante2.imprimir() 
estudiante2.resultados()  
