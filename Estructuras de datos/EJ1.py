# Se quiere almacenar strings dentro de un array
# El enunciado no sugiere que siempre tiene que haber un número de tareas así que la estructura de datos podría ser un array dinamico
#Especio por usuario:
# Programa:
class lista_tareas:
  def __init__(self):
    self.tareas = []
  
  def agregar_tarea(self, nombre_tarea):
    self.tareas.append(nombre_tarea)
  
  def eliminar_tarea(self, index = None, tarea = ""):
    if tarea in self.tareas:
      self.tareas.remove(tarea)
    elif index is not None and index < len(self.tareas):
      del self.tareas[index]
    else:
      print("Indice fuera de rango")
  
  def ver_lista(self):
    return self.tareas

mi_lista = lista_tareas()
mi_lista.agregar_tarea("Hacer la compra")
mi_lista.agregar_tarea("Estudiar para el examen")
mi_lista.agregar_tarea("Comprar tomates")
mi_lista.agregar_tarea("Comprar ajos")
mi_lista.eliminar_tarea(tarea="Comprar ajos")
print(mi_lista.ver_lista())