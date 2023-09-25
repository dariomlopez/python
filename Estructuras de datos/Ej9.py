# Ejercicio 9 - ColaAtencionCliente
# Diseña un programa en Python que simule una cola de atención al cliente. 
# Los usuarios pueden agregar solicitudes de atención al cliente y estas se manejan en orden FIFO.
# Se quiere almacenar strings dentro de un array
# El enunciado no sugiere que siempre tenga que haber un número fijo de tareas así que la estructura de datos podría ser un array dinamico
#Espacio por usuario: 2KB
# Programa:

class ColaAtencionClientes:
  def __init__(self):
    # En el constructor inicializamos un array vacio
    # para guardar nuestros documentos
    self.cola_clientes = []

  def agregar_solicitud(self, solicitud):
    # el documento es agregado en la posición cero del array
    self.cola_clientes.insert(0, solicitud)
  
  def atender_solicitud(self):
    if self.cola_clientes:
      return self.cola_clientes.pop(0)
    else:
      return "No hay documentos para imprimir"
    
  def ver_cola(self):
    return self.cola_clientes