# Ejercicio 6 - InventarioProductos
# Diseña un programa en Python que administre un inventario de productos. 
# Los usuarios pueden agregar nuevos productos, actualizar cantidades y buscar productos existentes.

class InventarioProductos:
  def __init__(self):
    self.inventario = []

  def agregar_producto(self, nombre, cantidad):
    self.inventario.append({"nombre": nombre,
                            "cantidad": cantidad})
    
  def actualizar_cantidad(self, nombre, nueva_cantidad):
    for producto in self.inventario:
      if producto["nombre"] == nombre:
        producto["cantidad"] = nueva_cantidad
        return True
    return False