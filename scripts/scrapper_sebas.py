from selenium.webdriver.common.devtools.v133.fetch import continue_request

# ---------   { Enlace web de sitio a Scrap }  ---------
URL_BASE_TO_SCRAPER="https://link-springer-com.crai.referencistas.com/search?new-search=true&query=edge+computing"
URI_TEST = "https://example.com/"
ENCABEZADO_ANTIMUROS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
import requests
import browser_cookie3
from bs4 import BeautifulSoup



def scraper ():

    """
            Segmento de la función para el acceso a la web:
    """
    # COOKIES DE MI NAVEGADOR CON LA SESIÓN ACTIVA (solo users de cra podrán usarlo)
    cookies = browser_cookie3.brave(domain_name='referencistas.com')
    try:
        respuesta = requests.get(URL_BASE_TO_SCRAPER, cookies=cookies)
        validar_solicitud(respuesta)

        SOPA = BeautifulSoup(respuesta.text, 'html.parser')
        print(SOPA)

    except Exception as e:
        print("Error al obtener cookies de Brave:", e)

    """
            Segmento de la función para acceder a cada enlace de los resultados de la búsqueda por pagina.
            segun el analisis del contenido html de la pagina , se determina en donde se encuentran
            los elementos que contienen los enlaces a cada articulo, de alli se obtienen los titulos 
            y los enlaces al articulo
    """
    selector_resultadosBusqueda = 'li.app-card-open[data-test="search-result-item"]'
    selector_enlaceArticulo = 'h3.app-card-open__heading[data-test="title"] a.app-card-open__link'

    reultados_ayados = SOPA.select(selector_resultadosBusqueda)
    if not reultados_ayados:
        print("No se encontraron resultados en la búsqueda.")

    lista_enlaces = []
    for i,aux in enumerate(reultados_ayados):  #extraer el enlace del artículo y el title
        enlace_elemento = aux.select_one(selector_enlaceArticulo)
        if enlace_elemento:
            title = enlace_elemento.text.strip()
            hipervinculo = URL_BASE_TO_SCRAPER + enlace_elemento.get('href')
            # si el vinculo es relativo, lo hacemos absoluto
            if not hipervinculo and not hipervinculo.startswith('http'):
                hipervinculo = URL_BASE_TO_SCRAPER + hipervinculo
            print("---> titulo del articulo : "+title)
            print("---> enlace del articulo : "+hipervinculo)
            lista_enlaces.append({
                'title': title,
                'enlace': hipervinculo
            })
    # buscamos los botones de descargas de citas
    #------ (PENDIENTE...) -----------------

    print("\n--- Resultados de los articulos identificados en los resultados de busqueda ---")
    for auxItem in lista_enlaces:
        print(f"titulo : {auxItem['title']}")
        print(f"enlace : {auxItem['enlace']}")
    """
            Segmento para extraer el contenido de la pagina en html
            esto con el objetivo de analizar el contenido por pagina en el futuro
    """
    # Escribimos en un archivo el contenido de la página
    with open('pagina.html', 'w', encoding='utf-8') as f:
        f.write(str(SOPA))

    # Buscamos el título de la página
    titulo = SOPA.select_one('h1').text
    print("el titulo de la pagina es : "+titulo)



def validar_solicitud (requestHTTP):

               # Función para validar la solicitud HTTP
    if requestHTTP.status_code == 200:
        print("La solicitud no ha fallado ")
        return True


if __name__ == "__main__":
    scraper()