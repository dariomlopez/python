# Ejercicio 4 - GestorContactos
# Crea un programa en Python que gestione una lista de contactos.
# Los usuarios deben poder agregar nuevos contactos, buscar contactos existentes y eliminar contactos.
# Se quiere almacenar strings dentro de un array
# El enunciado no sugiere que siempre tenga que haber un número fijo de canciones así que la estructura de datos podría ser un array dinamico
#Especio por usuario: 2KB
# Programa:

class AgendaContactos:
  def __init__(self):
    self.lista_contactos = []

  def agregar_contacto(self, nombre, apellido, telefono):
    contacto = {"nombre": nombre, "apellido": apellido, "telefono": telefono}
    self.lista_contactos.append(contacto)

  def buscar_contacto(self, nombre=None, apellido=None, telefono=None):
    
    coincidencia = []
    for contacto in self.lista_contactos:
      if (nombre is not None and contacto["nombre"] == nombre) or \
         (apellido is not None and contacto["apellido"] == apellido) or \
         (telefono is not None and contacto["telefono"] == telefono):
        coincidencia.append(contacto)
    return coincidencia
  
  def eliminar_contacto(self, nombre=None, apellido=None, telefono=None):

    for contacto in self.lista_contactos:
      if (nombre != contacto["nombre"] == nombre) or \
         (apellido != None and contacto["apellido"] == apellido) or \
         (telefono != None and contacto["telefono"] == telefono):
        self.lista_contactos.remove(contacto)

  def mostrar_todos_conts(self):
    return self.lista_contactos
  

mi_agenda = AgendaContactos()

# Agregar contactos
mi_agenda.agregar_contacto("Juan", "Perez", "123456789")
mi_agenda.agregar_contacto("Maria", "Gomez", "987654321")
mi_agenda.agregar_contacto("Carlos", "Lopez", "555555555")
mi_agenda.agregar_contacto("Laura", "Fernandez", "999999999")
mi_agenda.agregar_contacto("Laura", "Fernandez", "999999999")
mi_agenda.agregar_contacto("Ana", "Rodriguez", "888888888")
mi_agenda.agregar_contacto("Pedro", "Martinez", "777777777")
mi_agenda.agregar_contacto("Luis", "Perez", "666666666")
mi_agenda.agregar_contacto("Elena", "Sanchez", "555555555")
mi_agenda.agregar_contacto("Marta", "Diaz", "444444444")
mi_agenda.agregar_contacto("Javier", "Lopez", "333333333")

# print(mi_agenda.mostrar_todos_conts())

# Buscar contacto
  # Por nombre
buscar_nombre = mi_agenda.buscar_contacto(apellido="Lopez")
print("Mi codigo:")
print(buscar_nombre)

# Eliminar contacto
eliminar_cont = mi_agenda.eliminar_contacto(apellido="Diaz")
print("eliminado apellido Diaz")
print(mi_agenda.mostrar_todos_conts())

resultados_nombre = mi_agenda.buscar_contacto("Perez")
print("Resultados de la búsqueda por nombre 'Juan':")
print(resultados_nombre)

# Intentemos buscar un contacto por apellido
resultados_apellido = mi_agenda.buscar_contacto(apellido="Perez")
print("\nResultados de la búsqueda por apellido 'Perez':")
print(resultados_apellido)

# Intentemos buscar un contacto por teléfono
resultados_telefono = mi_agenda.buscar_contacto(telefono="555555555")
print("\nResultados de la búsqueda por teléfono '555555555':")
print(resultados_telefono)

# Intentemos eliminar un contacto
mi_agenda.eliminar_contacto("Carlos", "Lopez", "555555555")

# Mostramos todos los contactos restantes
print("\nContactos restantes:")
print(mi_agenda.mostrar_todos_conts())