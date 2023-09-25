# Ejercicio 1 - ListaTareas
# Crea un programa en Python que almacene una lista de tareas pendientes y permita al usuario agregar nuevas tareas, eliminar tareas existentes y ver la lista de tareas pendientes.
# Se quiere almacenar strings dentro de un array
# El enunciado no sugiere que siempre tenga que haber un número fijo de tareas así que la estructura de datos podría ser un array dinamico
#Espacio por usuario: 2KB
# Programa:
class lista_tareas:
  def __init__(self):
    self.tareas = []
  
  def agregar_tarea(self, nombre_tarea):
    self.tareas.append(nombre_tarea)
  
  def eliminar_tarea(self, index = None, tarea = ""):
    # Se puede eliminar una tarea por indice o por coincidencia total del nombre
    # Control de tipo de datos
    if isinstance(tarea, str):
      if tarea in self.tareas:
        self.tareas.remove(tarea)
      elif index is not None and index < len(self.tareas) and index >= 0:
        del self.tareas[index]
      else:
        print("Indice fuera de rango o la tarea no se encuentra")
    else:
      return "Tipo de dato incorrecto"
  
  def ver_lista(self):
    return self.tareas

mi_lista = lista_tareas()
mi_lista.agregar_tarea("Hacer la compra")
mi_lista.agregar_tarea("Estudiar para el examen")
mi_lista.agregar_tarea("Comprar tomates")
mi_lista.agregar_tarea("Comprar ajos")
mi_lista.eliminar_tarea(tarea = "Comprar ajos")
print(mi_lista.ver_lista())