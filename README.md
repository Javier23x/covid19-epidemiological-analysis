# COVID-19 Epidemiological Analysis

**Análisis y Visualización de Tendencias Epidemiológicas Globales**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Descripción

Este proyecto realiza un análisis exhaustivo de datos epidemiológicos de COVID-19 utilizando los datos oficiales de Johns Hopkins University (JHU CSSE). El análisis incluye limpieza de datos, análisis exploratorio, visualizaciones avanzadas y un dashboard interactivo desarrollado con Streamlit para la exploración de tendencias globales.

**Universidad Católica de la Santísima Concepción**  
**Curso:** Gestión de Datos 2025-II  
**Profesor:** Lorenzo Paredes Grandón  
**Autores:** Javier Pino Herrera, Camilo Campos González

## Objetivos del Proyecto

- Procesar y limpiar grandes volúmenes de datos epidemiológicos (710 archivos CSV)
- Realizar análisis exploratorio de tendencias globales de COVID-19
- Generar visualizaciones avanzadas e informativas
- Desarrollar un dashboard interactivo para exploración de datos
- Implementar optimizaciones para mejorar la eficiencia del procesamiento

## Fuente de Datos

Los datos provienen del repositorio oficial de Johns Hopkins University:
- **Repositorio:** [CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19)
- **Formato:** Archivos CSV con reportes diarios
- **Periodo analizado:** Enero 2020 - Diciembre 2021
- **Total de archivos:** 710 archivos CSV (uno por día)

## Estructura del Proyecto

```
covid19-epidemiological-analysis/
│
├── data/
│   ├── raw/                      # Datos originales de JHU CSSE
│   │   └── COVID-19/             # Repositorio clonado de JHU
│   ├── processed/                # Datos procesados (generados por notebooks)
│   └── country_to_continent.csv  # Mapeo de países a continentes (248+ países)
│
├── notebooks/
│   ├── Etapa1.ipynb             # Limpieza y preparación de datos
│   ├── Etapa2.ipynb             # Análisis exploratorio (6 meses)
│   ├── Etapa3.ipynb             # Visualizaciones avanzadas (2 años)
│   └── README.md                # Documentación de notebooks
│
├── dashboard/
│   ├── app.py                   # Aplicación Streamlit del dashboard
│   ├── requirements.txt         # Dependencias específicas del dashboard
│   └── README.md                # Documentación del dashboard
│
├── src/
│   ├── __init__.py              # Inicialización del paquete
│   └── config.py                # Funciones centralizadas (10 funciones)
│
├── scripts/
│   └── fetch_jhu_data.sh        # Script para descargar datos de JHU
│
├── docs/
│   ├── ETAPA5_OPTIMIZACION_Y_APRENDIZAJES.md  # Documentación de aprendizajes
│   ├── project_instructions.md                 # Instrucciones originales del proyecto
│   └── PROYECTO SEMESTRAL GESTION DE DATOS 2025-II.pdf  # Requisitos oficiales
│
├── reports/                      # Reportes generados (perfilado, análisis)
│
├── .gitignore                   # Archivos ignorados por Git
├── requirements.txt             # Dependencias del proyecto
├── LICENSE                      # Licencia MIT
└── README.md                    # Este archivo
```

## Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- Git
- pip (gestor de paquetes de Python)
- Mínimo 4 GB de RAM disponible
- Aproximadamente 500 MB de espacio en disco para datos

### Pasos de Instalación

#### 1. Clonar el repositorio

```bash
git clone https://github.com/Javier23x/covid19-epidemiological-analysis.git
cd covid19-epidemiological-analysis
```

#### 2. Crear y activar entorno virtual (recomendado)

**En Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

#### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

Las principales dependencias incluyen:
- pandas (2.3.3)
- numpy (2.1.3)
- matplotlib (3.10.0)
- seaborn (0.13.2)
- plotly (6.3.1)
- streamlit (1.50.0)
- jupyter
- ydata-profiling (para reportes automáticos)

#### 4. Descargar los datos de JHU CSSE

El proyecto incluye un script automatizado para descargar los datos:

```bash
# Opción 1: Clonar repositorio de JHU (recomendado)
bash scripts/fetch_jhu_data.sh clone

# Opción 2: Descargar como ZIP
bash scripts/fetch_jhu_data.sh zip
```

Este script descargará automáticamente los datos en `data/raw/COVID-19/`.

**Nota:** El repositorio de JHU ocupa aproximadamente 350 MB después de limpiar archivos innecesarios.

#### Estructura de datos esperada:

```
data/raw/COVID-19/
└── csse_covid_19_data/
    └── csse_covid_19_daily_reports/
        ├── 01-22-2020.csv
        ├── 01-23-2020.csv
        ├── ...
        └── 12-31-2021.csv
```

## Uso del Proyecto

### Ejecutar los Notebooks

Los notebooks están diseñados para ejecutarse en orden secuencial:

#### Iniciar Jupyter Notebook

```bash
# Con el entorno virtual activado
jupyter notebook
```

Esto abrirá Jupyter en tu navegador en `http://localhost:8888`.

#### Notebooks disponibles

1. **Etapa1.ipynb** - Limpieza y preparación de datos
   - Carga datos de enero 2020
   - Realiza 10 tareas de limpieza
   - Genera dataset limpio

2. **Etapa2.ipynb** - Análisis exploratorio
   - Analiza 6 meses de datos (enero-junio 2020)
   - Responde 10 preguntas analíticas
   - Genera reporte de perfilado automático

3. **Etapa3.ipynb** - Visualizaciones avanzadas
   - Procesa 2 años de datos (2020-2021)
   - Crea 5 visualizaciones avanzadas
   - Análisis por continentes

### Ejecutar el Dashboard

El dashboard interactivo está desarrollado con Streamlit y permite explorar los datos de forma dinámica.

```bash
cd dashboard
streamlit run app.py
```

El dashboard se abrirá automáticamente en tu navegador en `http://localhost:8501`.

#### Características del dashboard:

- Filtros interactivos por continente, país y rango de fechas
- 5 KPIs principales (casos confirmados, fallecidos, recuperados, activos, tasa de letalidad)
- 4 pestañas de análisis:
  - Evolución temporal
  - Comparativa de países
  - Análisis por continente
  - Estadísticas avanzadas
- Visualizaciones interactivas con Plotly
- Caché optimizado para carga rápida (50x más rápido después de primera carga)

## Funcionalidades Principales

### Módulo de Configuración Centralizado (src/config.py)

El proyecto utiliza un módulo centralizado con 10 funciones reutilizables para evitar duplicación de código:

1. **load_daily_reports()** - Carga múltiples archivos CSV con barra de progreso
2. **standardize_column_names()** - Normaliza nombres de columnas
3. **consolidate_duplicate_columns()** - Maneja columnas duplicadas
4. **drop_irrelevant_columns()** - Elimina columnas innecesarias
5. **process_dates()** - Procesa y formatea fechas
6. **convert_numeric_columns()** - Convierte tipos de datos numéricos
7. **calculate_active_cases()** - Calcula casos activos
8. **homogenize_country_names()** - Estandariza nombres de países (30+ reglas)
9. **clean_covid_data()** - Pipeline completo de limpieza
10. **load_continent_mapping()** - Carga mapeo de países a continentes

### Optimizaciones Implementadas

- **Reducción de código:** De 280 líneas duplicadas a 3 líneas (reducción del 98%)
- **Caching del dashboard:** 52x más rápido después de la primera carga
- **Pipeline de limpieza unificado:** 7 pasos automatizados
- **Normalización temprana:** Detección robusta de columnas inconsistentes

### Datos Procesados

- **248+ países** mapeados a continentes
- **710 archivos CSV** consolidados
- **Periodo completo:** Enero 2020 - Diciembre 2021
- **Columnas estandarizadas:** date, country_region, continent, confirmed, deaths, recovered, active
- **Casos especiales manejados:** Cruceros, territorios, nombres inconsistentes

## Etapas del Proyecto

### Etapa 1: Limpieza y Preparación de Datos

**Objetivo:** Comprender la estructura del dataset y generar una base consolidada y limpia.

**Rango temporal:** 1 mes (enero 2020)

**Tareas realizadas:**
- Carga y visualización de datos iniciales
- Detección y manejo de valores nulos
- Estandarización de nombres de columnas (snake_case)
- Homogeneización de nombres de países
- Conversión de formatos de fecha
- Creación de columna de casos activos
- Eliminación de columnas irrelevantes

**Resultado:** Dataset limpio guardado en `data/processed/`

---

### Etapa 2: Análisis Exploratorio

**Objetivo:** Explorar la evolución de los datos y realizar análisis comparativos.

**Rango temporal:** 6 meses (enero-junio 2020)

**Análisis realizados:**
- Top 10 países con más casos confirmados
- Países con mayor tasa de letalidad
- Identificación de países sin datos de recuperados
- Análisis de países latinoamericanos
- Evolución temporal de casos en Chile
- Identificación de fecha pico de contagios
- Análisis de correlación casos-fallecidos
- Detección de rebrotes
- Generación de reporte de perfilado automático (ydata-profiling)

**Resultado:** 10 preguntas analíticas respondidas con visualizaciones

---

### Etapa 3: Visualizaciones Avanzadas

**Objetivo:** Crear visualizaciones informativas de tendencias globales.

**Rango temporal:** 2 años (2020-2021)

**Visualizaciones creadas:**
1. Evolución temporal global (gráfico de líneas)
2. Top 10 países con más casos confirmados (gráfico de barras)
3. Heatmap de correlaciones entre variables
4. Tasas de letalidad por continente (barras horizontales)
5. Análisis geográfico por continente

**Tecnologías:** Matplotlib, Seaborn, Plotly

---

### Etapa 4: Dashboard Interactivo

**Objetivo:** Desarrollar una aplicación web interactiva para exploración de datos.

**Características:**
- Filtros dinámicos (continente, país, fechas)
- 5 KPIs principales
- 4 pestañas de análisis
- Gráficos interactivos con Plotly
- Indicadores de rebrotes
- Cálculo de tasas de crecimiento

**Tecnología:** Streamlit

**Rendimiento:** Carga inicial 4 segundos, interacciones subsecuentes 0.08 segundos (caché)

---

### Etapa 5: Optimización y Documentación

**Objetivo:** Documentar aprendizajes, desafíos y optimizaciones implementadas.

**Logros documentados:**
- 4 descubrimientos importantes en los datos
- 4 desafíos técnicos resueltos
- 4 optimizaciones implementadas con métricas
- 6 lecciones aprendidas
- Decisiones de diseño justificadas

**Documento:** `docs/ETAPA5_OPTIMIZACION_Y_APRENDIZAJES.md`

## Tecnologías y Herramientas

### Lenguajes y Frameworks
- **Python 3.8+** - Lenguaje principal
- **Jupyter Notebook** - Desarrollo y documentación interactiva
- **Streamlit** - Framework para dashboard web

### Bibliotecas de Análisis
- **Pandas 2.3.3** - Manipulación y análisis de datos
- **NumPy 2.1.3** - Operaciones numéricas
- **ydata-profiling 4.17.0** - Perfilado automático de datos

### Bibliotecas de Visualización
- **Matplotlib 3.10.0** - Gráficos estáticos
- **Seaborn 0.13.2** - Visualizaciones estadísticas
- **Plotly 6.3.1** - Gráficos interactivos

### Control de Versiones
- **Git** - Control de versiones
- **GitHub** - Repositorio remoto

### Gestión de Datos
- **CSV** - Formato de datos de entrada
- **Mapeo personalizado** - country_to_continent.csv (248+ países)

## Resultados y Métricas del Proyecto

- **Total de archivos procesados:** 710 archivos CSV
- **Países analizados:** 248+ países mapeados a continentes
- **Periodo de análisis:** 2 años (enero 2020 - diciembre 2021)
- **Líneas de código escritas:** 1,600+ líneas
- **Funciones reutilizables:** 10 funciones centralizadas
- **Reducción de código:** 98% (de 280 a 3 líneas por notebook)
- **Optimización de velocidad:** 52x más rápido (dashboard con caché)
- **Commits realizados:** 30+ commits descriptivos
- **Notebooks completados:** 3 notebooks principales
- **Visualizaciones creadas:** 5+ visualizaciones avanzadas

## Documentación Adicional

- **Instrucciones originales:** `docs/project_instructions.md`
- **Requisitos oficiales:** `docs/PROYECTO SEMESTRAL GESTION DE DATOS 2025-II.pdf`
- **Aprendizajes y optimizaciones:** `docs/ETAPA5_OPTIMIZACION_Y_APRENDIZAJES.md`
- **Documentación del dashboard:** `dashboard/README.md`
- **Documentación de notebooks:** `notebooks/README.md`

## Solución de Problemas

### Error al cargar datos

Si encuentras errores al cargar los datos:

```bash
# Verificar que los datos estén descargados
ls data/raw/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/

# Si no existen, descargar nuevamente
bash scripts/fetch_jhu_data.sh clone
```

### Problemas con el entorno virtual

```bash
# Recrear el entorno virtual
rm -rf venv
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### Error al ejecutar el dashboard

```bash
# Verificar que estés en el directorio correcto
cd dashboard

# Verificar que Streamlit esté instalado
pip install streamlit

# Ejecutar dashboard
streamlit run app.py
```

### Problemas con importaciones en notebooks

Asegúrate de ejecutar esta celda al inicio de cada notebook:

```python
import sys
import os
sys.path.insert(0, os.path.join('..', 'src'))
from config import *
```

## Contribuciones

Este proyecto fue desarrollado como parte del curso de Gestión de Datos. Para sugerencias o mejoras:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'feat: agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Autores

**Javier Pino Herrera**  
**Camilo Campos González**

Universidad Católica de la Santísima Concepción  
Ingeniería Civil Informática  
Gestión de Datos 2025-II

## Profesor

**Lorenzo Paredes Grandón**  
Universidad Católica de la Santísima Concepción

## Licencia

Este proyecto está bajo la Licencia MIT. Consultar el archivo [LICENSE](LICENSE) para más detalles.

## Agradecimientos

- **Johns Hopkins University CSSE** por proporcionar los datos epidemiológicos
- **Universidad Católica de la Santísima Concepción** por el apoyo académico
- **Profesor Lorenzo Paredes Grandón** por la guía y orientación durante el proyecto

## Contacto

Para consultas sobre el proyecto:

- **Repositorio:** [https://github.com/Javier23x/covid19-epidemiological-analysis](https://github.com/Javier23x/covid19-epidemiological-analysis)
- **Issues:** Para reportar problemas o sugerencias
- **Email:** A través de GitHub

---

**Nota:** Este proyecto es de carácter académico y tiene fines exclusivamente educativos. Los datos utilizados son de dominio público y provienen de fuentes oficiales reconocidas internacionalmente.

**Fecha de finalización:** Noviembre 2025  
**Versión:** 1.0.0
