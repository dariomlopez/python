# Ejercicio 2:

# Escribe un programa en Python que calcule 
# el promedio de una lista de calificaciones de estudiantes. 
# Deberías permitir al usuario ingresar nuevas calificaciones y actualizar el promedio en tiempo real.

# Se quiere almacenar un promedio de notas. El dato debería ser tipo númerico
# La estructura más adecuada será un array dinámico
# Espacio ocupado:
# Programa:

class PromedioCalificaciones:
  def __init__(self):
    # En el constructor declaramos un array vacio
    # donde se almacenan las calificaciones
    self.calificaciones = []

  def agregar_calificacion(self, calificacion):
    # Añadimos un método a la clase con un sencillo append. 
    # A estás alturas aún no controlamos de qué tipo son los datos 
    self.calificaciones.append(calificacion)

  def Promedio(self):
    promedioTotal = 0
    # con un bucle for leemos las calificaciones contenidas en self.calificaciones
    # y las dividimos por la longitude del array para obtener el promedio 
    for calificacion in self.calificaciones: 
      promedioTotal = promedioTotal + calificacion
    # Formateo la salida para tener dos decimales
    promedioFormat = "{:.2f}".format(promedioTotal / len(self.calificaciones))
    return promedioFormat

misCalificaciones = PromedioCalificaciones()
misCalificaciones.agregar_calificacion(5.3)
misCalificaciones.agregar_calificacion(4.2)
misCalificaciones.agregar_calificacion(6.1)
misCalificaciones.agregar_calificacion(5.2)
misCalificaciones.agregar_calificacion(5.3)
print(misCalificaciones.Promedio())