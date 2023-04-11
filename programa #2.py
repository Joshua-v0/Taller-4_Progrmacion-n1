precio = 0
precf = 0

print(" === BIENVENIDO A MC donalds ===")
print("¿que desea llevar?")
print("1.hamburguesas:")
print("2.helados:")
print("3.batidos:")
opc = input("introduzca un numero de su eleccion:")
if opc == "1":
 opc = int(input("¿que tipo de hamburguesa desea llevar? \n1.big mac \n2.triple bacon \n3.cuarto de libra \n(eliga un numero por favor)"))
 if opc == 1:
 big_mac = ""
 big_mac = int(input("ingrese cantidad de big mac que desea:"))
 print("cantidad de big mac:",big_mac)
 print("el total a pagar seria:",big_mac * 4.99)
 
 elif opc == 2:
 tri_b = ""
 tri_b = int(input("ingrese cantidad de triple bacon que desea:"))
 print("cantidad de big mac:",tri_b)
 print("el total a pagar seria:",tri_b * 6.99)
 
 elif opc == 3:
 c_libra = ""
 c_libra = int(input("ingrese cantidad de triple bacon que desea:"))
 print("cantidad de big mac:",c_libra)
 print("el total a pagar seria:",c_libra * 7.99) 
 
 
 
elif opc == "2":
 selecc = int(input("¿cual sabor de helados desea?\n1.chocolate. \n2.vainilla.\n(ingrese el numero de su eleccion)"))
 if selecc == 1:
 selecc = "chocolate"
 helados = int(input("ingrese la cantidad de helados de chocolate que desea:"))
 print("sabor de helados:",selecc)
 print("cantidad de helados:",helados) 
 print("el total a pagar es de:",helados * 2.75)
 
 elif selecc == 2:
 selecc = "vainilla"
 helados = int(input("ingrese la cantidad de helados de vainilla que desea:"))
 print("sabor de helados:",selecc)
 print("cantidad de helados:",helados)
 print("el total a pagar es de:", helados * 1.95)
 
elif opc == "3":
 selecc = int(input("¿cual sabor de helados desea?\n1.chocolate. \n2.vainilla. \n3.oreo \n(ingrese el numero de su eleccion)"))
 if selecc == 1:
 selecc = "chocolate"
 batidos = int(input("ingrese la cantidad de batidos de chocolate que desea:"))
 print("sabor de helados:",selecc)
 print("cantidad de batidos:",batidos) 
 print("el total a pagar es de:",batidos * 2.99)
 
 elif selecc == 2:
 selecc = "vainilla"
 batidos = int(input("ingrese la cantidad de batidos de vainilla que desea:"))
 print("sabor de helados:",selecc)
 print("cantidad de helados:",batidos)
 print("el total a pagar es de:",batidos * 2.25)
 
 elif selecc == 3:
 selecc = "oreo"
 batidos = int(input("ingrese la cantidad de batidos de vainilla que desea:"))
 print("sabor de helados:",selecc)
 print("cantidad de helados:",batidos)
 print("el total a pagar es de:",batidos * 3.25)
 
 
 
 
 
 
 
 
 
 
 
 

 
 

 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

