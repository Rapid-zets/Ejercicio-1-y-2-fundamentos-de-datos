def Main():
    def Calculo():
        monto_dejado_de_percibir = Precio*descuento
        monto_descuento = Precio - monto_dejado_de_percibir
        print(f"Categoría: {cat} (Descuento de un {(descuento*100):.0f}%)")
        print(f"Monto con descuento: ${monto_descuento:,.0f}")
        print(f"Dinero dejado de percibir: ${monto_dejado_de_percibir:,.0f}")
    Precio = int(input("Ingrese el precio del asiento:\n"))
    print(""*10)
    Edad = int(input("Ingrese la edad del cliente:\n"))
    if 5 <= Edad <= 14:
        descuento = 0.35
        cat = 1
        Calculo()
    if 15 <= Edad <= 19:
        descuento = 0.25
        cat = 2
        Calculo()
    if 20 <= Edad <= 45:
        descuento= 0.10
        cat = 3
        Calculo()
    if 46 <= Edad <= 65:
        descuento = 0.25
        cat = 4
        Calculo()
    if Edad >= 66:
        descuento = 0.35
        cat = 5
        Calculo()
    
Main()