# Angel-Alejandro-Sepulveda-Gonzalez-3W-PY

1-

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

![image](https://github.com/user-attachments/assets/bb229562-0fb9-4ed6-89ad-7b79f55e3d7e)
![image](https://github.com/user-attachments/assets/685afde2-ff30-42a0-a5d6-c0dadd003cdb)

2-

# Sepulveda Gonzalez Angel Alejandro, 3W,1215

class Persona:

  def __init__(self, nombre, edad):
    
  self.nombre = nombre
        
  self.edad = edad

  def cumpleaños(self):
     
  self.edad += 1

nombre = input("💖 Ingrese el nombre de su ser amado: ")

edad = int(input("🎂 Ingrese su edad: "))

p = Persona(nombre, edad)

p.cumpleaños()

p.cumpleaños()

print(f"🌹 {p.nombre} cumple ahora {p.edad} años. ¡El amor sigue creciendo con los años! 🌟")

![image](https://github.com/user-attachments/assets/11ca7ca4-09e3-482c-9a80-4e7ed09aec6a)
![image](https://github.com/user-attachments/assets/7970c0b4-7966-4bdd-a8e9-223f0c1cd320)

3-

# Sepulveda Gonzalez Angel Alejandro, 3W,1215

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

![image](https://github.com/user-attachments/assets/168b60fa-7224-4ea5-9bfe-4e209809c0de)
![image](https://github.com/user-attachments/assets/9c4dc017-b832-4b12-bf42-5770e2c12627)
![image](https://github.com/user-attachments/assets/90888c15-f383-4364-854d-033467c51322)

4-

class Persona:
   
  def __init__(self, nom, ape):
  
  self.nombre = nom
  
  self.apellido = ape
  
  def nombre_completo(self):
  
  print(f"💖 {self.nombre} {self.apellido}")


class Estudiante(Persona):
    
  def __init__(self, nom, ape, carr):
  
  super().__init__(nom, ape)
  
  self.carrera = carr

  def mostrar_carrera(self):

  print(f"🌹 Carrera del amor: {self.carrera}")


![image](https://github.com/user-attachments/assets/017c3491-9405-4bfc-9576-7611e1cf5bbd)
![image](https://github.com/user-attachments/assets/685afde2-ff30-42a0-a5d6-c0dadd003cdb)

5-

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

![image](https://github.com/user-attachments/assets/d8bcf1ca-88eb-40c2-bbbb-958b9ed81668)
![image](https://github.com/user-attachments/assets/ccb778fd-755b-4a21-bcf9-1a890f65d2b6)
![image](https://github.com/user-attachments/assets/b1bc9faa-9b06-4b5d-998b-eafc1b1d5f29)

8-

class Fabrica():
    
  def __init__(self, llantas, color, precio):
  
  self._llantas=llantas
  
  self._color=color
  
  self._precio=precio

class Moto(Fabrica):
  
  def cantidad(self):
  
  print(«La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}».format(self._llantas,self._color,self._precio))

class Carro(Fabrica):
  
  def cantidad(self):
  
  print(«La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}».format(self._llantas,self._color,self._precio))

  print(«OBJETO=moto»)

moto=Moto(2, «Gris», «$200»)

moto.cantidad()

print(«OBJETO=carro»)

carro=Carro(4 ,»Negro», «$600»)

carro.cantidad()

![image](https://github.com/user-attachments/assets/1794c37d-d064-47e6-85e1-241a597f3ca6)
![image](https://github.com/user-attachments/assets/14b2a147-7a6f-4f05-b447-3321ddd29919)
![image](https://github.com/user-attachments/assets/685afde2-ff30-42a0-a5d6-c0dadd003cdb)


7-

# Sepulveda Gonzalez Angel Alejandro, 3W,1215

class Marino:

  def hablar(self):
  
  print("💖 Hola, soy un habitante del océano lleno de amor!")

class Pulpo(Marino):
  
  def hablar(self):
  
  print("🐙 Hola, soy un pulpo que abraza con amor!")

class Foca(Marino):
   
  def hablar(self, mensaje):
       
  self.mensaje = mensaje
        
  print(mensaje)

marino = Marino()

marino.hablar()

pulpo = Pulpo()

pulpo.hablar()

foca = Foca()

foca.hablar("🦭 Hola, soy una foca amante de los abrazos!")

![image](https://github.com/user-attachments/assets/4d503624-61d6-41a6-9e4f-14ac39a295cd)
![image](https://github.com/user-attachments/assets/989c3777-1fc4-4eb5-89bc-580f44634163)

