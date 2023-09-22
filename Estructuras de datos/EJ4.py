# Ejercicio 4 - GestorContactos
# Crea un programa en Python que gestione una lista de contactos.
# Los usuarios deben poder agregar nuevos contactos, buscar contactos existentes y eliminar contactos.
# Se quiere almacenar strings y el teléfono podría ser un número entero. En mi caso todo es un string
# El enunciado sugiere que al menos tengamos nombre, apellido o teléfono. Por tanto creo lo ideal es usar un objeto de pares de llave: valor
# Espacio por usuario: 5KB
# Programa:

class AgendaContactos:
  def __init__(self):
    self.lista_contactos = []

  def agregar_contacto(self, nombre, apellido, telefono):
    # Creamos un objeto o diccionario. Cuando se usa el método agregar_contacto se crea su llave con su valor.
    # Para futuro: aviso de error para el usuario si falta algún dato
    contacto = {"nombre": nombre, "apellido": apellido, "telefono": telefono}
    # Se agrega cada contacto a self.lista_contactos
    self.lista_contactos.append(contacto)

  #  Función para buscar un contacto de la lista por nombre/apellido/telefono
  def buscar_contacto(self, nombre=None, apellido=None, telefono=None):
    
    coincidencia = []
    # Si nos han indicado el nombre/apellido/telefono y el nombre/apellido/telefono coincide con los existentes en la lista actual se muestran en pantalla
    for contacto in self.lista_contactos:
      if (nombre is not None and contacto["nombre"] == nombre) or \
         (apellido is not None and contacto["apellido"] == apellido) or \
         (telefono is not None and contacto["telefono"] == telefono):
        coincidencia.append(contacto)
      # else: throw Error "Debe especificar nombre/apellido/teléfono"
    return coincidencia
  
  # Función para eliminar contacto por nombre, apellido o teléfono
  def eliminar_contacto(self, nombre=None, apellido=None, telefono=None):
    # Si nos han indicado el nombre/apellido/telefono y el nombre/apellido/telefono coincide con los existentes se elimina
    for contacto in self.lista_contactos:
      if (nombre is not None and contacto["nombre"] == nombre) or \
         (apellido is not None and contacto["apellido"] == apellido) or \
         (telefono is not None and contacto["telefono"] == telefono):
        self.lista_contactos.remove(contacto)
      # else: throw Error "Debe especificar nombre/apellido/teléfono"
  
  # Función que muestra la lista actualizada de contactos 
  def mostrar_lista_contactos(self):
    return self.lista_contactos
  

mi_agenda = AgendaContactos()

# Agregar contactos
mi_agenda.agregar_contacto("Juan", "Perez", "123456789")
mi_agenda.agregar_contacto("Maria", "Gomez", "987654321")
mi_agenda.agregar_contacto("Carlos", "Lopez", "555555555")
mi_agenda.agregar_contacto("Laura", "Hernandez", "5565654999")
mi_agenda.agregar_contacto("Laura", "Fernandez", "999999999")
mi_agenda.agregar_contacto("Ana", "Rodriguez", "888888888")
mi_agenda.agregar_contacto("Pedro", "Martinez", "777777777")
mi_agenda.agregar_contacto("Luis", "Perez", "666666666")
mi_agenda.agregar_contacto("Elena", "Sanchez", "555555555")
mi_agenda.agregar_contacto("Marta", "Diaz", "444444444")
mi_agenda.agregar_contacto("Javier", "Lopez", "333333333")

# print(mi_agenda.mostrar_lista_contactos())

# Sí se busca por algo distinto al nombre hay que indicarlo en el parametro de la función
print("Busqueda con todos los parametros")
buscar_nombre = mi_agenda.buscar_contacto("Ana", "Rodriguez", "888888888")
print(buscar_nombre)
  # Por nombre
print("Busqueda por nombre")
buscar_nombre = mi_agenda.buscar_contacto("Juan")
print(buscar_nombre)
buscar_nombre = mi_agenda.buscar_contacto("Laura")
print(buscar_nombre)
buscar_nombre = mi_agenda.buscar_contacto("Elena")
print(buscar_nombre)

# buscar contacto por apellido
print("Busqueda por apellido")
resultados_apellido = mi_agenda.buscar_contacto(apellido="Perez")
print(resultados_apellido)
resultados_apellido = mi_agenda.buscar_contacto(apellido="Sanchez")
print(resultados_apellido)
resultados_apellido = mi_agenda.buscar_contacto(apellido="Lopez")
print(resultados_apellido)

# buscar contacto por teléfono
print("Busqueda por teléfono")
resultados_telefono = mi_agenda.buscar_contacto(telefono="555555555")
print(resultados_telefono)
resultados_telefono = mi_agenda.buscar_contacto(telefono="777777777")
print(resultados_telefono)

# Eliminar contacto
# Por nombre
mi_agenda.eliminar_contacto("Ana")
# por apellido
mi_agenda.eliminar_contacto(apellido="Diaz")
#  por teléfono
mi_agenda.eliminar_contacto(telefono="5565654999")
# Con todos los parámetros
mi_agenda.eliminar_contacto("Carlos", "Lopez", "555555555")

# Mostramos todos los contactos restantes
print("\nContactos restantes:")
print(mi_agenda.mostrar_lista_contactos())