def main():
    # escribe tu código abajo de esta línea
    juegos_nuevos = int(input("Dame el número de juegos nuevos: "))*(1000)
    juegos_usados = int(input("Dame el número de juegos usados: "))*(350)
    total = juegos_nuevos + juegos_usados
    print("El total de la compra es:", total)


if __name__ == '__main__':
    main()
