def main():
    from math import ceil
    # escribe tu código abajo de esta línea
    palabra = int(input("Dame el número de palabras: "))
    pagina = ceil(palabra/475)
    publicacion = (pagina*60)
    costo = (publicacion*0.90)
    print("El costo de la publicación es:", costo)


if __name__ == '__main__':
    main()