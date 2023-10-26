import re # expresiones regulares

def check_word(palabra):
    if re.search("^[a-z0-9]+$", palabra):
        return palabra
    else:
        return ""

def main():
    with open(f"data/pages.txt", "r", encoding="utf-8") as archivo:
        for num_linea, linea in enumerate(archivo, start=1):
            palabras = linea.lower().split()
            for palabra in palabras:
                if len(check_word(palabra)) > 0:
                    print(f"{palabra} {num_linea}")

if __name__ == "__main__":
    main()
