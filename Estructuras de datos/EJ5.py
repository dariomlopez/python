# Ejercicio 5 - ColaDeImpresion
# Escribe un programa en Python que simule una cola de impresión. 
# Los usuarios pueden agregar trabajos de impresión y se imprimen en orden FIFO (primero en entrar, primero en salir).
# Se quiere almacenar strings dentro de un array
# la estructura de datos podría ser un array dinamico
#Espacio por usuario: 2KB
# Programa:

class ColaImpresion:
  def __init__(self):
    # En el constructor inicializamos un array vacio
    # para guardar nuestros documentos
    self.cola_impresion = []

  def agregar_documento(self, documento):
    # el documento es agregado en la posición cero del array
    self.cola_impresion.insert(0, documento)
  
  def imprimir_documento(self):
    # Sí la cola de impresión contiene algo se imprime el "documento eliminado" en primera posicion
    if self.cola_impresion:
      return self.cola_impresion.pop(0)
    else:
      return "No hay documentos para imprimir"
  
mi_imprenta = ColaImpresion()

mi_imprenta.agregar_documento("Presentación.doc")
print(mi_imprenta.imprimir_documento())
mi_imprenta.agregar_documento("Historia del Imperio Austrohungaro.ppt")
print(mi_imprenta.imprimir_documento())
mi_imprenta.agregar_documento("Gastos 2023.xlsx")
print(mi_imprenta.imprimir_documento())

print(mi_imprenta.mostrar_cola_impresion())
