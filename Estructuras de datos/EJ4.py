# Ejercicio 4 - GestorContactos
# Crea un programa en Python que gestione una lista de contactos.
# Los usuarios deben poder agregar nuevos contactos, buscar contactos existentes y eliminar contactos.

class AgendaContactos:
  def __init__(self, nombre, apellido, telefono):
    self.lista_contactos = []
    self.nombre = nombre
    self.apellido = apellido
    self.telefono = telefono

  def agregar_contacto(self, nombre, apellido, telefono):
    