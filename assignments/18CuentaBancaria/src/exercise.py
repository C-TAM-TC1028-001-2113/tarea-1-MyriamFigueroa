def main():
    # escribe tu código abajo de esta línea
    saldo = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))
    saldo_final = (saldo + ingresos) - (egresos + (cheques * 13))
    interes = saldo_final * 0.075
    saldo_interes = (saldo_final - interes)
    print("El saldo final de la cuenta es:", saldo_interes)
    # este print muestra el resultado
if __name__ == '__main__':
    main()
