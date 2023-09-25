# Ejercicio 6 - InventarioProductos
# Diseña un programa en Python que administre un inventario de productos. 
# Los usuarios pueden agregar nuevos productos, actualizar cantidades y buscar productos existentes.

class InventarioProductos:
  def __init__(self):
    self.inventario = []

  def agregar_producto(self, nombre, cantidad):
    self.inventario.append({"nombre": nombre, "cantidad": cantidad})
    
  def actualizar_cantidad(self, nombre, nueva_cantidad):
    for producto in self.inventario:
      if producto["nombre"] == nombre:
        producto["cantidad"] = nueva_cantidad
        return True
    return False
  
  def buscar_producto(self, nombre):
    for producto in self.inventario:
      if producto["nombre"] == nombre:
        return producto
      
inventario = InventarioProductos()

# Función agregar producto:
inventario.agregar_producto("Manzanas", 10)
inventario.agregar_producto("Plátanos", 15)
inventario.agregar_producto("Aguacates", 12)
inventario.agregar_producto("Camisetas", 25)
inventario.agregar_producto("Peras", 22)
inventario.agregar_producto("Cucharas", 19)
inventario.agregar_producto("Papel", 4)
inventario.agregar_producto("Garbanzos", 5)


# Función buscar producto:
print(inventario.buscar_producto("Aguacates"))
print(inventario.buscar_producto("Papel"))
print(inventario.buscar_producto("Manzanas"))

# Función actualizar: 
inventario.actualizar_cantidad("Cucharas", 33)
inventario.actualizar_cantidad("Garbanzos", 21)
inventario.actualizar_cantidad("Peras", 13)

#Productos actualizados:
print(inventario.buscar_producto("Cucharas"))
print(inventario.buscar_producto("Garbanzos"))
print(inventario.buscar_producto("Peras"))
