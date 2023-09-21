# Ejercicio 3 - ListaReproduccion
# Diseña un programa en Python que administre una lista de reproducción de canciones. 
# Debería permitir al usuario agregar nuevas canciones, eliminar canciones existentes y reproducir la lista en orden.
# Se quiere almacenar strings dentro de un array
# El enunciado no sugiere que siempre tiene que haber un número de tareas así que la estructura de datos podría ser un array dinamico
#Especio por usuario: 2KB
# Programa:

class ListaReproduccion:
  def __init__(self):
    self.ListaCanciones = []

  def AgregarCancion(self, cancion = ""):
    # Para variar un poco sobre el ejercicio de tareas,
    # la canción se añade al principio de la lista con el método insert que acepta dos parametros (index, cosa a añadir)
    self.ListaCanciones.insert(0, cancion)

  def EliminarCancion(self, cancion = "", index = None):
    if cancion in self.ListaCanciones:
      self.ListaCanciones.remove(cancion)
    elif index is not None and index < len(self.ListaCanciones) and index >= 0:
      del self.ListaCanciones[index]
    else:
      print("Indice fuera de rango o la canción no se encuentra")
  
  def siguiente_cancion(self):
    # Manda la primera canción de la lista al último lugar
    return self.ListaCanciones.append(self.ListaCanciones.pop(self.ListaCanciones.index(0)))

  def ReproducirLista(self):
    return self.ListaCanciones
  
lista_reproduccion = ListaReproduccion()