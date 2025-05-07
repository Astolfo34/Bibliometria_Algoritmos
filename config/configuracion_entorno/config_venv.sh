#!/bin/bash

# Configuración del entorno virtual
echo "Configurando entorno virtual..."
python3 -m venv venv
source venv/bin/activate

# Instalación de dependencias
echo "Instalando dependencias..."
pip install --upgrade pip
pip install selenium webdriver-manager pandas requests beautifulsoup4
pipi install beautifulsoup4

# Descarga de ChromeDriver
echo "Configurando ChromeDriver..."
python3 -c "from webdriver_manager.chrome import ChromeDriverManager; ChromeDriverManager().install()"

echo ""
echo "¡Configuración completada!"
echo "Para activar el entorno virtual ejecuta: source venv/bin/activate"