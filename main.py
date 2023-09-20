class ListaTareas:
  def __init__(self):
    self.tareas = []

  def agregar_tarea(self, nombre_tarea):
    self.tareas.append(nombre_tarea)

  def eliminar_tarea(self, index=None, tarea=""):
    # *
    # Se puede eliminar una tarea por su indice
    # o se puede eliminar por coincidencia parcial por nombre de la tarea
    # *#
    if tarea:
      tarea_eliminada = [
        #   # la primera instancia de tareas toma el valor del index del array self.tareas[...]
        #   # La segunda instancia se refiere al array en su totalidad
        tarea for tarea in self.tareas if tarea in tarea
      ]
      self.tareas = [
        tarea for tarea in self.tareas if tarea not in tarea
      ]
      return tarea_eliminada
    elif index is not None and index >= 0:
      del self.tareas[index]
    else:
      print("Indice fuera de rango o la tarea no se encuentra")

  def ver_lista(self):
    return self.tareas


mi_lista = ListaTareas()
mi_lista.agregar_tarea("Hacer la compra")
mi_lista.agregar_tarea("Estudiar para el examen")
mi_lista.agregar_tarea("Comprar tomates")
mi_lista.agregar_tarea("Comprar ajos")
mi_lista.eliminar_tarea(tarea="ajos")
print(mi_lista.ver_lista())