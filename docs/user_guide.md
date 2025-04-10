# Guia de Usuario: Proyecto Bibliometria Uniquindio

## Requerimiento 1 : Unificacion de los Datos en Formato RIS o Bibtex

1 . flujo del programa
```mermaid
graph TD
    A[Extraer Datos] --> B[Normalizar Campos]
    B --> C[Eliminar Duplicados]
    C --> D[Generar BibTeX]
    D --> E[Visualizar Datos]
    E --> F[Generar Reporte]
    F --> G[Generar Grafico]
    G --> H[Generar CSV]
    H --> I[Generar PDF]
'
```
2. Instalar paquetes 
```bash
pip install requests pandas pybtex matplotlib
```
3. Definir la estructura de directorios
```mermaid  
proyecto_bibliometria/
├── config/
│   └── database_apis.json  # Claves API
├── src/
│   ├── data_fetcher.py     # Extraer datos
│   ├── data_unifier.py     # Unificar y limpiar
│   └── visualizer.py       # Visualización
└── main.py                 # Ejecución principal
```
