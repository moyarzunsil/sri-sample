import sys
from collections import defaultdict

def main():
    indice_invertido = defaultdict(lambda: defaultdict(int))

    for linea in sys.stdin:
        linea = linea.strip()  # Elimina espacios adicionales y el salto de línea
        if not linea:
            continue

        palabra, numero_linea = linea.split()
        numero_linea = int(numero_linea)

        indice_invertido[palabra][numero_linea] += 1

    # Imprime el índice invertido en el formato solicitado y ordenado lexicográficamente
    for palabra in sorted(indice_invertido.keys()):
        lineas = indice_invertido[palabra]
        listado = " ".join([f"{num_linea} {conteo}" for num_linea, conteo in lineas.items()])
        print(f"{palabra} {str(len(lineas))} {listado}")


if __name__ == "__main__":
    main()

