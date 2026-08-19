#autor: Justo velasquez
#autor: Samuel martinez

nombreProducto = str(input("Ingrese el nombre del producto: "))
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad del producto: "))

subtotal = precio * cantidad

print("Resumen de la compra: ")
print("Producto: " + str(nombreProducto))
print("Precio:" + str(precio))
print("Cantidad:" +str(cantidad))
print("Subtotal:" + str(subtotal))