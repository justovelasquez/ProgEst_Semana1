
for number in range (1,11):
    nombre = str(input("Ingrese el nombre del producto"))
    cantidad = int(input("Ingrese la cantidad:"))
    if cantidad == 0:
        continue
    else:
        print("su producto es:" + str(nombre))
        print("la cantidad es:"  + str(cantidad))
