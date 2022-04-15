productos = [["Combo 2 lb", 2500], ["Combo 3 lb", 3000],["Pintura anticorrosiva negra",2000],["Pintura negro brillante", 1500], ["Foco LED embutido 18W Luz Fría",2500]]
comunas = [["Santiago",4000],["Maipú",7000],["La Reina",6000],["Lo Barnechea",7000],["San Miguel",5000]]
cantidad = 0
decision = "SI"
valid = 1
optionvalid = 0
i = 0
h = 0
total = 0
subtotal = 0
subtotalp = 0

#Saludo
print("--------------------------")
print("¡Bienvenido a la ferretería!")
print("--------------------------")
print("")
print("Lista de productos: ")

#Imprimir productos
for x in productos:        
    print("Código: " + str(i+1) +  " | " + str(x[0]) + ": " + str(x[1]) )
    i = i+1

#Ingreso de productos
while valid == 1:
    print("")
    idproducto = int(input("Ingrese el código del producto que desea comprar: "))-1
    cantidad = int(input("Ingrese cantidad: "))
    subtotalp = cantidad * productos[idproducto][1]

    #Desea agregar más productos
    print("")
    print("¿Desea agregar otro producto? (SI o NO): ")
    decision = input().upper()
    
    #Validar si o no
    if decision !="SI":
        while optionvalid == 0:
            if decision =="SI":
                optionvalid = 1
            elif decision =="NO":
                valid = 0
                optionvalid = 1
            else:
                print("Opción no válida. Ingrese SI o NO: ")
                decision = input().upper()
        optionvalid = 0

    #Calculo de subtotal productos
    subtotal = subtotalp + subtotal

#Mostrar total:
print("")
print("Total: " + str(subtotal))

#Preguntar Despacho
print("")
respuestadespacho = input("¿Desea agregar despacho?: ").upper()

while optionvalid == 0:
    #Validar si o no
    if respuestadespacho =="NO":
        #Final
        print("")
        print("El total de su compra es: " + str(subtotal))
        optionvalid = 1
    elif respuestadespacho =="SI":
        #imprimir comunas
        print("")
        for y in comunas:        
            print("Código: " + str(h+1) +  " | " + str(y[0]) + ": " + str(y[1]) )
            h = h+1
        print("")
        idcomuna = int(input("Ingrese el código su comuna: "))-1
        total = subtotal + comunas[idcomuna][1]
        #Final
        print("")
        print("El total de su compra es: " + str(total)) 
        optionvalid = 1
    else:
        print("Opción no válida. Ingrese SI o NO: ")
        respuestadespacho = input().upper()