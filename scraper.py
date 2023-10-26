import requests
import re
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def is_valid(url, seed_domain):
    """
    Comprueba si la URL es válida y pertenece al mismo dominio que la semilla.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and parsed.netloc == seed_domain

def get_all_links(url, seed_domain):
    """
    Extrae todos los enlaces de una página web y devuelve aquellos que pertenecen al mismo dominio que la semilla.
    """
    try:
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        for a in soup.find_all("a", href=True):
            link = a.attrs["href"]
            joined_url = urljoin(url, link)
            if is_valid(joined_url, seed_domain) and not joined_url.endswith('.pdf') and not joined_url.endswith('.docx') and not joined_url.endswith('.vcf') and not joined_url.endswith('.jpg'):
                yield joined_url
    except Exception as e:
        print(f"Error al procesar {url}: {e}")

def remove_html_tags(content):
    """
    Elimina todos los tags HTML del contenido.
    """
    soup = BeautifulSoup(content, "html.parser")
    return soup.get_text()

def strip_tags(content):
    return re.sub(r'<[^>]*?>', ' ', content)

def main(seed_url):
    seed_domain = urlparse(seed_url).netloc
    visited = set()  # Conjunto para almacenar las URL visitadas
    to_visit = {seed_url}  # Conjunto para almacenar las URL por visitar

    while to_visit:
        current_url = to_visit.pop()
        if current_url not in visited:
            print(f"Procesando: {current_url}")
            visited.add(current_url)

            # Guardar el contenido en un archivo
            time.sleep(1)
            try:
              response = requests.get(current_url)
            except requests.exceptions.Timeout:
                # No carga la pagina, puede deberse a que esta offline, sin inet, baneado, etc.
                print("Timeout...")
            except requests.exceptions.TooManyRedirects:
                # URL con muchos saltos no permite cargar contenido.
                print("Redirection loop...")
            except requests.exceptions.RequestException as e:
                # Casi cualquier otro error
                raise SystemExit(e)

            content_without_tags = remove_html_tags(response.text).replace('\n', ' ')
            with open(f"data/pages.txt", "a", encoding="utf-8") as f:
                f.write(re.sub("\s+"," ", content_without_tags)+'\n')

            with open(f"data/urls.txt", "a", encoding="utf-8") as f:
                f.write(current_url + '\n')

            # Extraer y agregar nuevos enlaces al conjunto to_visit
            for link in get_all_links(current_url, seed_domain):
                if link not in visited:
                    to_visit.add(link)

if __name__ == "__main__":
    seed = "https://www.claro.cl/"  # Cambia esto por tu URL semilla
    main(seed)
