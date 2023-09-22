# Ejercicio 6 - InventarioProductos
# Diseña un programa en Python que administre un inventario de productos. 
# Los usuarios pueden agregar nuevos productos, actualizar cantidades y buscar productos existentes.

class InventarioProductos:
  def __init__(self):
    self.inventario = []

  def agregar_producto(self, nombre, cantidad):
    self.inventario.append((nombre, cantidad))
    