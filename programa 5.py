precio = 0

print(" === hola bienvenidos ===")
print("¿que juego desea llevar?")
nom = input("ingrese nombre del juego:")
cantd = int(input("ingrese cantidad de juegos:"))
precio = float(input("ingrese el precio del juego:"))
print("nombre del juego:",nom)
print("precio del juego:",precio)
print("cantidad de juegos:",cantd)
print("el total a pagar mas el itbms seria:",(precio * cantd)* 1.07)