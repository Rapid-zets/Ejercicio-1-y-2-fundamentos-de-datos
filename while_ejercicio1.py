def Main():
    On = ""
    def Calculo():
            monto_dejado_de_percibir = Precio*descuento
            monto_descuento = Precio - monto_dejado_de_percibir
            print(f"Categoría: {cat} (Descuento de un {(descuento*100):.0f}%)")
            print(f"Monto con descuento: ${monto_descuento:,.0f}")
            print(f"Dinero dejado de percibir: ${monto_dejado_de_percibir:,.0f}")
    while On != "no":
        try:
            Precio = int(input("Ingrese el precio del asiento:\n"))
            if Precio <= 0:
                print("El precio no puede ser menos de 1")
                print(""*10)
            Edad = int(input("Ingrese la edad del cliente:\n"))
        except:
            print("ERROR")
            continue
        if Edad < 5:
            print("los menores de 5 años no pueden entrar al teatro")
        elif 5 <= Edad <= 14:
            descuento = 0.35
            cat = 1
            Calculo()
        elif 15 <= Edad <= 19:
            descuento = 0.25
            cat = 2
            Calculo()
        elif 20 <= Edad <= 45:
            descuento= 0.10
            cat = 3       
            Calculo()     
        elif 46 <= Edad <= 65:
            descuento = 0.25
            cat = 4
            Calculo()
        elif Edad >= 66:
            descuento = 0.35
            cat = 5 
            Calculo()   
        On = input("desea hacerlo denuevo? (Presione Si o No): ").lower()
    
                            
                            
        

    
Main()