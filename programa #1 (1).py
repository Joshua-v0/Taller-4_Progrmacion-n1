
precio = 0
total = 0
precf = 0
reloj = "" 

print("=== AMAZON COMPRAS ===")
print("carrito de compras de accesorios:") 
print("1.accesorios:")
print("2.playstations:")
print("3.ropas:")
print("4.comidas:")
print("5.autos o vehiculos:")
opc = input("eliga una opcion:")
 
if opc == "1":
 print("ingrese el tipo de accesorios que desea:")
 print("1.reloj")
 print("2.pulseras")
 print("3.lentes")
 opc = input("eliga una opcion:")
 if opc == "1":
 nom = input("ingrese el nombre del reloj:")
 precio = float(input("ingrese el precio del reloj:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio del reloj incluyendole el itbms seria:",precf)
 elif opc == "2":
 precio = float(input("ingrese el precio de la pulsera:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio de la pulsera mas el itbms queda en:",precf)
 elif opc == "3":
 nom = input("ingrese nombre del lente:")
 precio = float(input("ingrese precio del lente:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio del lente mas el itbms quedaria en:",precf)
 else:
 print("404 not found")

if opc == "2":
 print("ingrese el tipo de playstations que desea:")
 print("1.playstation")
 print("2.playstation2")
 print("3.playstation3")
 print("4.playstation4")
 print("5.playstation5")
 opc = input("eliga una opcion:")
 if opc == "1":
 precio = float(input("ingrese el precio del playstation1:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio del playstation1 incluyendole el impuesto queda en:",precf)
 elif opc == "2":
 precio = float(input("ingrese el precio del playstation2:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio del playstation2 incluyendole el impuesto queda en:",precf)
 elif opc == "3":
 precio = float(input("ingrese el precio del playstation3:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio del playstation3 incluyendole el impuesto queda en:",precf)
 elif opc == "4":
 precio = float(input("ingrese el precio del playstation4:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio del playstation4 incluyendole el impuesto queda en:",precf)
 elif opc == "5":
 precio = float(input("ingrese el precio del playstation5:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio del playstation5 incluyendole el impuesto queda en:",precf)
 else:
 print("404 not found")
 
 
 
if opc == "3":
 print("¿que tipo de ropa desea?")
 print("1.jeans para mujeres")
 print("2.jeans para hombres")
 print("3.sueter de mujer")
 print("4.sueter de hombre")
 print("4.abrigos para mujeres")
 print("5.abrigos para hombres")
 print("6.tangas")
 print("7.lencerias")
 opc = input("eliga una opcion:")
 if opc == "1":
 nom = input("ingrese la marca del jeans:")
 precio = float(input("ingrese el precio del jeans:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio del jeans mas el itbms seria:",precf)
 elif opc == "2":
 nom = input("ingrese la marca del jeans:")
 precio = float(input("ingrese el precio del jeans:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio del jeans mas el itbms seria:",precf)
 elif opc == "3":
 nom = input("ingrese la marca del sueter:")
 precio = float(input("ingrese el precio del sueters")) 
 precio = precio * 1.07
 precf = precio + total
 print("el precio del jeans mas el itbms seria:",precf)
 elif opc == "4":
 marca = input("ingrese el tipo de marca del abrigo:")
 precio = float(input("ingrese el precio del abrigo:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio del abrigo mas el impuesto quedaria en:",precf)
 elif opc == "5":
 marca = input("ingrese el tipo de marca del abrigo:")
 precio = float(input("ingrese el precio del abrigo:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio del abrigo mas el impuesto quedaria en:",precf)
 elif opc == "6":
 marca = input("ingrese el tipo de marca de la tanga:")
 precio = float(input("ingrese el precio de la tanga:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio de la tanga incluendole el itbms seria:",precf)
 elif opc == "7":
 marca = input("ingrese el tipo de marca de la lenceria:")
 precio = float(input("ingrese el precio de la lenceria:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio de la lenceria incluendole el itbms seria:",precf)
 else:
 print("404 not found") 
 

if opc == "4":
 print("¿Que tipo de comida desea?")
 print("1.hamburguesa")
 print("2.trago")
 print("3.cerveza")
 print("4.hot dogs")
 print("5.soda")
 opc = input("eliga una opcion:")
 if opc == "1":
 print("el precio de la hamburguesa es de 4.55")
 elif opc == "2":
 print("el precio del trago es de, 5.00")
 elif opc == "3":
 print("el precio de la cerveza es de 2.00")
 elif opc == "4":
 print("el precio del hot dogs es de 3.55")
 elif opc == "5":
 print("el precio de la soda es de 1.00")
 else:
 print("404 not found") 
 
 
if opc == "5":
 print("===ESTOS SON LOS AUTOS QUE ESTAN DISPONIBLES===")
 print("1.toyota")
 print("2.infiniti")
 print("3.range rovers")
 print("4.lexus")
 opc = input(" eliga su opcion:")
 if opc == "1":
 modelo = input("¿que tipo de modelo desea?")
 precio = float(input("ingrese el precio:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio del modelo de toyota que escogio es de:",precf)
 elif opc == "2":
 modelo = input("¿que tipo de modelo desea?")
 precio = float(input("ingrese el precio:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio del modelo del infiniti que escogio es de:",precf)
 elif opc == "3":
 modelo = input("¿que tipo de modelo desea?")
 precio = float(input("ingrese el precio:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio del modelo del ran rovers que escogio es de:",precf)
 elif opc == "4":
 modelo = input("¿que tipo de modelo desea?")
 precio = float(input("ingrese el precio:"))
 precio = precio * 1.07
 precf = precio + total
 print("el precio del modelo de lexus que escogio es de:",precf)
 else:
 print("404 not found")
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 