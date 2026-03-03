list_g = [("Gasolina premium", 4.25), ("Gasolina regular", 3.85), ("Diesel", 3.65), ("Gas natural", 2.95)]
while (True):
    print("\n---SISTEMA DE VENTA DE COMBUSTIBLES---")
    print("1. Realizar venta")
    print("2. Salir")

    try:
        opc = int(input("Digite la opción que desear usar: "))
        if (opc < 1 or opc > 2):
            print("Error: Opción inválida. Digite entre 1 y 2.")
        elif (opc == 1):
            for i, (name, price) in enumerate (list_g, 1):
                print(f"\n{i}. {name}: ${price}/Litro")
            op = int(input("\nDigite la opción del combustible que desea comprar: "))
            try:
                if (op < 1 or op > 4):
                    print("Error: Opción inválida. Digite entre 1 y 4.")
                else: 
                    name, price = list_g[op-1]
                    opc_sub = int(input(f"Cuantos litros va a comprar del combustible {name, price}: "))
                    match op:
                        case 1:
                            res = opc_sub * 4.25
                        case 2:
                            res = opc_sub * 3.85
                        case 3:
                            res = opc_sub * 3.65
                        case 4:
                            res = opc_sub * 2.95

                    print("\n---COMPROBANTE DE VENTA---")
                    print(f"Combustible: {name}")
                    print(f"Precio unitario: ${price}/Litro")
                    print(f"Cantidad: {opc_sub} Litros")
                    print(f"Total a pagar: {res}")
                    input("Presione enter para continuar...")

            except ValueError:
                print("Error: Opción inválida. La opción no debe contener caracteres especiales.")

        elif (opc == 2):
            print("Gracias por usar el sistema. ¡Hasta Pronto!")
            break

    except ValueError:
        print("Error: Opción inválida. La opción no debe contener caracteres especiales.")