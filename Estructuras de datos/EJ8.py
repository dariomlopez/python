# Ejercicio 8 - CalculadoraSimple
# Escribe un programa en Python que implemente una calculadora simple. 
# Los usuarios pueden realizar operaciones de suma, resta, multiplicación y división. Debes considerar cómo gestionar los resultados anteriores.
# Se van a usar tipos númericos
# Estructura de datos: ?
#Espacio por usuario: 2KB
# Programa:
class Calculadora:

  #  Métodos de la clase que realizan una operación con los números pasados. Incluye un control de entrada de tipo básico
  def sumar(self, numero, numero2):
    if isinstance(numero, (int, float)) and isinstance(numero2, (int, float)):
      return f"Resultado de dividir {numero} + {numero2} = ""{:.2f}".format(numero + numero2)
    else:
      return "Tipo de dato no admitido"
  
  def restar(self, numero, numero2):
    if isinstance(numero, (int, float)) and isinstance(numero2, (int, float)):
      return f"Resultado de restar {numero} - {numero2} = ""{:.2f}".format(numero - numero2)
    else:
      return "Tipo de dato no admitido"
  
  def multiplicar(self, numero, numero2):
    if isinstance(numero, (int, float)) and isinstance(numero2, (int, float)):
      return f"Resultado de multiplicar {numero} * {numero2} = ""{:.2f}".format(numero * numero2)
    else:
      return "Tipo de dato no admitido"
  
  def dividir(self, numero, numero2):
    if isinstance(numero, (int, float)) and isinstance(numero2, (int, float)):
      return f"Resultado de dividir {numero} / {numero2} = ""{:.2f}".format(numero / numero2)
    else:
      return "Tipo de dato no admitido"
  
mi_calculadora = Calculadora()
print(mi_calculadora.dividir(7, 9.99))