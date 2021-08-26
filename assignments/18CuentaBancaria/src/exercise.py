def main():
    # escribe tu código abajo de esta línea
    saldo = float(input("Dame el saldo del mes anterior: "))*(75/100)
    ingresos = float(input("Dame los ingresos: "))*(75/100)
    egresos = float(input("Dame los egresos: "))*(75/100)
    cheques = int(input("Dame el número de cheques: "))*(75/100)
    saldo_final = saldo + ingresos + egresos + cheques
    print("El saldo final de la cuenta es:", saldo_final)


if __name__ == '__main__':
    main()
