from modelos_cafeteria import Bebida, Postre

def paso_uno():
    print("--- REGISTRO DE INVENTARIO (10 OBJETOS) ---")
    
    prod1 = Bebida(1, "Americano Express", 35.0, "Bebidas", "Chico", "Caliente")
    prod2 = Bebida(2, "Capuchino Especial VIC", 55.0, "Bebidas", "Mediano", "Caliente")
    prod3 = Bebida(3, "Latte Frio", 60.0, "Bebidas", "Grande", "Fria")
    prod4 = Bebida(4, "Frappe Moka", 70.0, "Bebidas", "Grande", "Fria")
    prod5 = Bebida(5, "Te Verde", 40.0, "Bebidas", "Mediano", "Caliente")
    prod6 = Postre(6, "Brownie", 45.0, "Postres", False)
    prod7 = Postre(7, "Galleta de Avena Sin Azucar", 25.0, "Postres", True)
    prod8 = Postre(8, "Cheesecake ", 65.0, "Postres", False)
    prod9 = Postre(9, "Panque de Elote", 30.0, "Postres", False)
    prod10 = Postre(10, "Croissant Con Jamon", 35.0, "Panaderia", False)

    print(prod1.mostrar_detalle())
    print(prod2.mostrar_detalle())
    print(prod3.mostrar_detalle())
    print(prod4.mostrar_detalle())
    print(prod5.mostrar_detalle())
    print(prod6.mostrar_detalle())
    print(prod7.mostrar_detalle())
    print(prod8.mostrar_detalle())
    print(prod9.mostrar_detalle())
    print(prod10.mostrar_detalle())

    print("\n--- VALIDACIÓN DE LOS DATOS FINALIZADA ---\n")


def paso_dos():
    print(">>> INICIANDO PROCESO DE PEDIDO...")
    print("Usuario: Víctor Serrano. (Puntos Fidelidad: 150)")
    print("Atiende: Empleado Victor JR (Cafetero/Mesero)")
    
    agotados = ["P10"]
    nombre_agotado = "Croissant"
    
    precios = {"P1": 35.0, "P2": 55.0, "P3": 60.0, "P4": 70.0, "P5": 40.0,
               "P6": 45.0, "P7": 25.0, "P8": 65.0, "P9": 30.0, "P10": 35.0}
    
    while True:
        respuesta = input("Seleccione los ID(P) de sus productos (ej. P5): ")
        
        pedidos_sucios = respuesta.split(",")
        lista_pedidos = []
        for p in pedidos_sucios:
            limpio = p.strip().upper()
            lista_pedidos.append(limpio)
        
        hay_error = False
        for p in lista_pedidos:
            if p in agotados:
                print("\n[SISTEMA]: Verificando inventario...")
                print("[ERROR]: El producto " + p + " (" + nombre_agotado + ") está agotado.")
                print("[SISTEMA]: Seleccione productos disponibles.\n")
                hay_error = True
                break
                
        if hay_error == False:
            unidos = ", ".join(lista_pedidos)
            print("\n[OK]: Productos " + unidos + " Si se pudo agragar.")
            
            suma_total = 0.0
            for p in lista_pedidos:
                if p in precios:
                    suma_total = suma_total + precios[p]
                    
            print("Monto base: $" + str(suma_total))
            break

    print("\n>>> APLICANDO DE LA GESTIÓN COMERCIAL...")
    quiere_descuento = input("¿Cuenta con LOBOCODIGO de promoción?: ")
    
    total_pagar = suma_total
    dinero_ahorrado = 0.0
    
    if quiere_descuento.upper() == "SI":
        codigo_ingresado = input("Código: ")
        if codigo_ingresado.upper() == "LOBOBUAP#04":
            print("[SISTEMA]: Validando código de loboestudiante... ¡ÉXITO! (Descuento del 20% aplicado).")
            dinero_ahorrado = suma_total * 0.20
            total_pagar = suma_total - dinero_ahorrado
            
    print("\nResumen de Pedido #67:")
    print("----------------------------------------")
    print("Cliente: Víctor Serrano.")
    print("Tipo: Consumo en sucursal")
    print("IDs Productos: [" + ", ".join(lista_pedidos) + "]")
    print("Total Final: $" + str(total_pagar) + " (Te Ahorraste $" + str(dinero_ahorrado) + ")")
    print("----------------------------------------")
    print("Estado:Esta PAGADO. El Pedido esta en PREPARACION.")
    print("De parte de Cafeteria Victor, Gracias por su espera")


if __name__ == "__main__":
    paso_uno()
    paso_dos()