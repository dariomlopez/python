# Ejercicio 7 - ListaReproduccionVideos
# Crea un programa en Python que administre una lista de reproducción de videos.
# Los usuarios pueden agregar nuevos videos, eliminar videos existentes y reproducir videos en orden.
# Se quiere almacenar strings dentro de un array
# El enunciado no sugiere que siempre tenga que haber un número fijo de vídeos así que la estructura de datos podría ser un array dinamico
#Espacio por usuario: 2KB
# Programa:

class ListaReproduccionVideo:
  def __init__(self):
    self.ListaVideos = []

  def agregar_video(self, video = ""):
    # la canción se añade al principio de la lista con el método insert que acepta dos parametros (index de array, cosa a añadir)
    # Argumentos que toma la función: esperamos sea tipo string, de momento no se controla
    self.ListaVideos.insert(0, video)

  def eliminar_video(self, video = "", index = None):
    # Se puede eliminar una cación por nombre o por index de lista
    # Argumento necesario: cancion(string)
    # Argumento no obligatorio: index (int) 
    if video in self.ListaVideos:
      self.ListaVideos.remove(video)
    elif index is not None and index < len(self.ListaVideos) and index >= 0:
      del self.ListaVideos[index]
    else:
      print("Indice fuera de rango o el vídeo no se encuentra")
  
  def siguiente_video(self):
    # Manda el primer vídeo de la lista al último lugar, pero no módifica la lista
    return self.ListaVideos.append(self.ListaVideos.pop(self.ListaVideos.index(0)))
  
  def video_anterior(self):
    # Manda el último vídeo de la lista al primer lugar, pero no módifica la lista
    return self.ListaVideos.insert(0, self.ListaVideos.pop())

  def reproducir_lista_video(self):
    # return el array actual de canciones
    return self.ListaVideos
  
lista_reproduccion = ListaReproduccionVideo()