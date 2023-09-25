# Ejercicio 8 - CalculadoraSimple
# Escribe un programa en Python que implemente una calculadora simple. 
# Los usuarios pueden realizar operaciones de suma, resta, multiplicación y división. Debes considerar cómo gestionar los resultados anteriores.
# Se van a usar tipos númericos
# El enunciado no sugiere que siempre tenga que haber un número fijo de tareas así que la estructura de datos podría ser un array dinamico
#Espacio por usuario: 2KB
# Programa:
class Calculadora:

  def sumar(self, numero, numero2):
    if isinstance(numero, (int, float)) and isinstance(numero2, (int, float)):
      return "{:.2f}".format(numero + numero2)
    else:
      return "Tipo de dato no admitido"
  
  def restar(self, numero, numero2):
    if isinstance(numero, (int, float)) and isinstance(numero2, (int, float)):
      return "{:.2f}".format(numero - numero2)
  
  def multiplicar(self, numero, numero2):
    if isinstance(numero, (int, float)) and isinstance(numero2, (int, float)):
      return "{:.2f}".format(numero * numero2)
  
  def dividir(self, numero, numero2):
    if isinstance(numero, (int, float)) and isinstance(numero2, (int, float)):
      return "{:.2f}".format(numero / numero2)
  
mi_calculadora = Calculadora()
print(mi_calculadora.sumar(7, 9.99))