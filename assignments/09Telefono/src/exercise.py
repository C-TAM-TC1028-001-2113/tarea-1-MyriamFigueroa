def main():
    # escribe tu código abajo de esta línea
    mensajes = int(input("Dame el número de mensajes: "))*(0.80)
    megas = float(input("Dame el número de megas: "))*(0.80)
    minutos = int(input("Dame el número de minutos: "))*(0.80)
    costo_mensual = mensajes + megas + minutos
    print("El costo mensual es de:", costo_mensual)



if __name__ == '__main__':
    main()
