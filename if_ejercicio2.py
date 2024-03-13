def Main():
    def calcular(costo_casa,sueldo):
        if sueldo < 80000:
            pie = 0.3*costo_casa
            años = 7
            cuotas_mes = (costo_casa-pie)/(12*años)
        if sueldo >= 80000:
            pie = 0.15*costo_casa
            años= 10
            cuotas_mes = (costo_casa - pie)/(12*años)
        return pie, cuotas_mes, años
    sueldo = int(input("Ingrese sueldo del comprador: "))
    if sueldo <= 0:
        print("El sueldo no puede ser 0 o menos")
    costo_casa = int(input("Ingrese el costo de la casa: "))
    if costo_casa <=0:
        print("el valor de la casa no puede ser nada o negativo")
    
    print("\n")
    resultado = calcular(costo_casa, sueldo)
    pie = resultado[0]
    cuotas_mes = resultado[1]
    años = resultado[2]

    print(f"El comprador debe pagar ${pie:,.0f} de pie inicial ")
    print(f"El valor de cuotas mensuales de este es de ${cuotas_mes:,.0f} por {años} años ")
Main()