# COVID-19 Epidemiological Analysis

**Análisis y Visualización de Tendencias Epidemiológicas Globales**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Descripción

Este proyecto realiza un análisis exhaustivo de datos epidemiológicos de COVID-19 utilizando los datos oficiales de Johns Hopkins University (JHU CSSE). El análisis incluye limpieza de datos, análisis exploratorio, visualizaciones avanzadas y un dashboard interactivo para la exploración de tendencias globales.

**Universidad Católica de la Santísima Concepción**  
**Curso:** Gestión de Datos 2025-II  
**Profesor:** Lorenzo Paredes Grandón

## 🎯 Objetivos

- Procesar y limpiar grandes volúmenes de datos epidemiológicos
- Realizar análisis exploratorio de tendencias globales
- Generar visualizaciones avanzadas e informativas
- Desarrollar un dashboard interactivo para exploración de datos
- Optimizar el procesamiento de datos para mejorar la eficiencia

## 📊 Fuente de Datos

Los datos provienen del repositorio oficial de Johns Hopkins University:
- **Repositorio:** [CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19)
- **Formato:** Archivos CSV con reportes diarios
- **Periodo analizado:** 2020-2022

## 🏗️ Estructura del Proyecto

```
covid19-epidemiological-analysis/
│
├── data/
│   ├── raw/                  # Datos originales de JHU
│   └── processed/            # Datos procesados y limpios
│
├── notebooks/
│   ├── 01_limpieza_datos.ipynb
│   ├── 02_analisis_exploratorio.ipynb
│   ├── 03_visualizaciones.ipynb
│   └── 04_optimizacion.ipynb
│
├── dashboard/
│   ├── app.py                # Aplicación principal del dashboard
│   ├── requirements.txt      # Dependencias específicas del dashboard
│   └── README.md            # Instrucciones de uso del dashboard
│
├── src/
│   ├── __init__.py
│   ├── data_processing.py   # Funciones de limpieza y procesamiento
│   ├── analysis.py          # Funciones de análisis
│   └── visualization.py     # Funciones de visualización
│
├── reports/
│   ├── perfilado.html       # Reporte de perfilado automático
│   └── informe_tecnico.pdf  # Informe técnico final
│
├── docs/
│   └── project_instructions.md
│
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

## 🚀 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/covid19-epidemiological-analysis.git
cd covid19-epidemiological-analysis
```

2. Crear un entorno virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## 📝 Uso

### Notebooks

Los notebooks están organizados en orden secuencial y deben ejecutarse en el siguiente orden:

1. **01_limpieza_datos.ipynb**: Limpieza y preparación inicial de datos
2. **02_analisis_exploratorio.ipynb**: Análisis exploratorio y perfilado
3. **03_visualizaciones.ipynb**: Visualizaciones avanzadas
4. **04_optimizacion.ipynb**: Optimización del procesamiento

Para ejecutar los notebooks:
```bash
jupyter notebook notebooks/
```

### Dashboard

Para ejecutar el dashboard interactivo:
```bash
cd dashboard
streamlit run app.py
```

Consulta el [README del dashboard](dashboard/README.md) para más detalles.

## 🔧 Tecnologías Utilizadas

- **Análisis de datos:** Pandas, NumPy
- **Visualización:** Matplotlib, Seaborn, Plotly
- **Dashboard:** Streamlit
- **Perfilado:** ydata-profiling
- **Control de versiones:** Git

## 📈 Etapas del Proyecto

### Etapa 1: Limpieza y Preparación de Datos
- Carga y exploración inicial
- Detección de valores nulos
- Estandarización de nombres
- Creación de columnas derivadas

### Etapa 2: Análisis Exploratorio
- Análisis comparativo entre países
- Cálculo de tasas de letalidad
- Identificación de tendencias
- Perfilado automático de datos

### Etapa 3: Visualizaciones Avanzadas
- Evolución temporal global
- Comparativas por región
- Heatmaps de correlación
- Análisis geográfico

### Etapa 4: Dashboard Interactivo
- Filtros dinámicos
- Indicadores principales
- Visualizaciones interactivas
- Análisis de rebrotes

### Etapa 5: Optimización
- Mejora en tiempos de carga
- Reducción de uso de memoria
- Operaciones vectorizadas
- Documentación de mejoras

## 👥 Equipo

- [Nombre Estudiante 1]
- [Nombre Estudiante 2]
- [Nombre Estudiante 3]

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- Johns Hopkins University CSSE por proporcionar los datos
- Universidad Católica de la Santísima Concepción
- Profesor Lorenzo Paredes Grandón

## 📧 Contacto

Para preguntas o sugerencias, por favor contactar a través de:
- GitHub Issues
- Email institucional

---

**Nota:** Este proyecto es de carácter académico y tiene fines educativos.
