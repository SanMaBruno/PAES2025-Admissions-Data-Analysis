# PAES2025 Admissions Analysis

## Descripción del Proyecto

Este proyecto tiene como objetivo analizar los datos de admisión para el proceso PAES 2025, enfocado en la distribución de estudiantes por sexo, rama educacional y región. Se incluyen procesos de limpieza, transformación y visualización de los datos para obtener insights que permitan una mejor comprensión de la composición de los estudiantes inscritos.

## Estructura del Proyecto

La estructura de carpetas está organizada de acuerdo a las mejores prácticas de un flujo de trabajo de análisis de datos en Data Science:

```bash
PAES2025_ADMISSIONS_ANALYSIS/
│
├── data/                    # Almacena los datos sin procesar y procesados
│   ├── processed/            # Archivos de datos limpios y procesados
│   │   ├── clean_admissions_data_2025.csv
│   │   ├── cleaned_admissions_data_2025.csv
│   ├── raw/                  # Archivos de datos sin procesar
│       ├── admissions_codes_2025.xlsx
│       ├── admissions_data_2025.csv
│
├── notebooks/                # Notebooks de análisis y visualización
│   ├── eda.ipynb             # Análisis exploratorio de datos (EDA)
│   ├── visualizacion.ipynb   # Visualización de los resultados del análisis
│
├── scripts/                  # Scripts para la limpieza y transformación de datos
│   ├──       # Script de limpieza de datos
│
├── outputs/                  # Resultados y gráficos generados
│
├── venv/                     # Entorno virtual Python
│
├── .gitignore                # Archivos y carpetas a ignorar por Git
└──                  # Archivo que describe el proyecto
```

## Requisitos

- Python 3.8 o superior
- Entorno virtual con las dependencias necesarias

Instalar las dependencias requeridas:

```bash
pip install -r requirements.txt
```

## Uso del Proyecto

### 1. Limpieza de Datos

El archivo `data_cleaning.py` en la carpeta `scripts/` contiene el código necesario para realizar la limpieza y preprocesamiento de los datos crudos. Este script transforma los datos brutos (`admissions_data_2025.csv`) en datos listos para el análisis.

Ejecutar el script de limpieza de datos:

```bash
python [data_cleaning.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5CBS%5C%5CDocuments%5C%5CPAES2025_Admissions_Analysis%5C%5Cscripts%5C%5Cdata_cleaning.py%22%2C%22_sep%22%3A1%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FBS%2FDocuments%2FPAES2025_Admissions_Analysis%2Fscripts%2Fdata_cleaning.py%22%2C%22scheme%22%3A%22file%22%7D%7D)
```

### 2. Análisis Exploratorio de Datos (EDA)

El notebook `eda.ipynb` en la carpeta `notebooks/` realiza un análisis exploratorio de datos, donde se inspeccionan las principales características del dataset, como la distribución de los estudiantes por sexo, región y rama educacional.

Para ejecutar el análisis EDA:

1. Abrir `eda.ipynb` con Jupyter Notebook.
2. Ejecutar las celdas para ver los insights iniciales de los datos.

### 3. Visualización de Resultados

El notebook `visualizacion.ipynb` en la carpeta `notebooks/` crea visualizaciones interactivas utilizando Plotly. Los gráficos generados permiten explorar la distribución de los estudiantes según variables clave como sexo, rama educacional y región.

Para ejecutar la visualización:

1. Abrir `visualizacion.ipynb` con Jupyter Notebook.
2. Ejecutar las celdas para generar las visualizaciones interactivas.

### 4. Outputs

Los resultados del análisis, como gráficos y tablas, se almacenan en la carpeta `outputs/`. Esta carpeta contendrá los productos generados a partir de los notebooks y scripts.

## Visualizaciones

Una de las principales visualizaciones generadas es un gráfico treemap que muestra la distribución de los estudiantes por sexo, rama educacional y región. Los colores distinguen entre hombres y mujeres, y los cuadros representan la proporción de cada grupo.