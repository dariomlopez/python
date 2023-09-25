# Ejercicio 10 - GestorTareasProyecto
# Crea un programa en Python que gestione una lista de tareas de proyecto.
# Los usuarios pueden agregar nuevas tareas, marcar tareas como completadas y ver el progreso del proyecto.
# Se quiere almacenar strings dentro de un array
# El enunciado no sugiere que siempre tenga que haber un número fijo de tareas así que la estructura de datos podría ser un array dinamico
#Espacio por usuario: 2KB
# Programa:
class GestorTareasProyecto:
  def __init__(self):
    self.tareas = []
  
  def agregar_tarea(self, tarea, completada = False):
    self.tareas.append({"tarea": tarea, "completada": completada})
  
  def marcar_completada(self, index = None):
    # Se puede eliminar una tarea por indice o por coincidencia total del nombre
    if index != None and index < len(self.tareas) and index >= 0:
        self.tareas[index]["completada"] = True
    else:
      print("Indice fuera de rango o la tarea no se encuentra")

  # Método de la clase para ver 
  def ver_progreso(self):
    total_tareas = len(self.tareas)
    tareas_completadas = sum(tarea["completada"] for tarea in self.tareas)
    progreso = (tareas_completadas / total_tareas) * 100
    if total_tareas > 0:
      return f"Progreso del proyecto: {progreso:.2f}%", self.tareas
    else:
      return "No hay tareas pendientes"
    
  #  Método de la clase para eliminar tarea si completada es True
  def eliminar_tarea(self):
    self.tareas=[tarea for tarea in self.tareas if tarea["completada"] != False]
  
  # ver el éstado actual de la lista
  def ver_lista_tareas(self):
    return self.tareas
    
gestor = GestorTareasProyecto()
gestor.agregar_tarea("Hacer la presentación")
gestor.agregar_tarea("Revisar informe")
gestor.agregar_tarea("Hacer pythons")
gestor.agregar_tarea("Revisar la revisión")
# gestor.marcar_completada()

print(gestor.ver_progreso())
print(gestor.ver_lista_tareas())