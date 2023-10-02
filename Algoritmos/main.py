class PromedioCalificaciones:
  def __init__(self):
    self.calificaciones = []

  def agregar_calificacion(self, calificacion):
    self.calificaciones.append(calificacion)

  def Promedio(self):
    promedioTotal = 0
    for calificacion in self.calificaciones:
      promedioTotal = (promedioTotal + calificacion)/len(self.calificaciones)
    return promedioTotal

misCalificaciones = PromedioCalificaciones()
misCalificaciones.agregar_calificacion(8.6)
misCalificaciones.agregar_calificacion(4.6)
misCalificaciones.agregar_calificacion(6.6)
misCalificaciones.agregar_calificacion(7.6)
misCalificaciones.agregar_calificacion(9.6)
misCalificaciones.Promedio()