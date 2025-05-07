#!/bin/bash

# Configurar entorno
echo "1. Configurando directorios..."
mkdir -p ./data/{raw,processed}/SAGE_RIS

echo "2. Creando/activando entorno virtual..."
python3 -m venv .venv
source .venv/bin/activate

echo "3. Instalando dependencias Python..."
pip install --upgrade pip
pip install selenium webdriver-manager
pip install selenium-stealth

echo "4. Verificando instalación de Brave..."
if ! command -v brave-browser &> /dev/null
then
    echo "Brave no encontrado, instalando..."
    sudo dnf install brave-browser
fi

echo "✅ Configuración completada!"
echo "Para activar el entorno: source .venv/bin/activate"
echo "Para ejecutar el script: python descarga_sage_brave.py"