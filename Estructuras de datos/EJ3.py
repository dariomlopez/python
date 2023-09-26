# Ejercicio 3 - ListaReproduccion
# Diseña un programa en Python que administre una lista de reproducción de canciones. 
# Debería permitir al usuario agregar nuevas canciones, eliminar canciones existentes y reproducir la lista en orden.
# Se quiere almacenar strings dentro de un array
# El enunciado no sugiere que siempre tenga que haber un número fijo de tareas así que la estructura de datos podría ser un array dinamico
#Espacio por usuario: 2KB
# Programa:

class ListaReproduccion:
  def __init__(self):
    self.ListaCanciones = []

  def agregar_cancion(self, cancion = ""):
    # la canción se añade al principio de la lista con el método insert que acepta dos parametros (index de array, cosa a añadir)
    # Argumentos que toma la función: esperamos sea tipo string, de momento no se controla
    self.ListaCanciones.insert(0, cancion)

  def eliminar_cancion(self, cancion = "", index = None):
    # Se puede eliminar una cación por nombre o por index de lista
    # Argumento necesario: cancion(string)
    # Argumento no obligatorio: index (int) 
    if cancion in self.ListaCanciones:
      self.ListaCanciones.remove(cancion)
    elif index is not None and index < len(self.ListaCanciones) and index >= 0:
      del self.ListaCanciones[index]
    else:
      print("Indice fuera de rango o la canción no se encuentra")
  
  def siguiente_cancion(self):
    # Manda la primera canción de la lista al último lugar, pero no módifica la lista
    return self.ListaCanciones.append(self.ListaCanciones.pop(self.ListaCanciones.index(0)))
  
  def anterior_cancion(self):
    # Manda la última canción de la lista al primer lugar, pero no módifica la lista
    return self.ListaCanciones.insert(0, self.ListaCanciones.pop())

  def reproducir_lista(self):
    # return el array actual de canciones
    return self.ListaCanciones
  
lista_reproduccion = ListaReproduccion()