````markdown
# 🦠 COVID-19 Dashboard Interactivo

Dashboard interactivo completo para la exploración y análisis de datos epidemiológicos de COVID-19.

**Proyecto Semestral - Gestión de Datos 2025-II**  
Universidad Católica de la Santísima Concepción

---

## 📊 Características Principales

### 🔍 Filtros Dinámicos
- **Selector de Continente:** Filtra datos por continente o visualiza todos
- **Selector Múltiple de Países:** Selecciona uno o varios países para análisis comparativo
- **Rango de Fechas:** Personaliza el período de análisis con selector de fechas
- **Filtrado en Tiempo Real:** Todas las visualizaciones se actualizan automáticamente

### 📈 Indicadores Clave (KPIs)
- **Casos Confirmados:** Total acumulado con variación diaria
- **Casos Activos:** Casos actuales en tratamiento con tendencia
- **Recuperados:** Total de casos recuperados
- **Fallecidos:** Total de fallecimientos con variación diaria
- **Tasa de Letalidad:** Porcentaje calculado automáticamente

### 🎨 Visualizaciones Interactivas (4 Tabs)

#### 1️⃣ Evolución Temporal
- Gráfico de líneas múltiples con casos confirmados, activos y fallecidos
- Análisis de series temporales con Plotly
- Detección automática del pico de casos
- Cálculo de promedios diarios
- Tooltips interactivos con información detallada

#### 2️⃣ Comparativa de Países
- **Top 10 Países por Casos Confirmados:** Gráfico de barras horizontales
- **Top 10 Países por Tasa de Letalidad:** Análisis estadístico (>1,000 casos)
- Visualización con escalas de colores
- Valores formateados con separadores de miles

#### 3️⃣ Mapa de Calor de Correlaciones
- Matriz de correlación entre variables clave
- Análisis de relaciones entre confirmados-fallecidos
- Análisis de relaciones entre confirmados-activos
- Visualización intuitiva con escala de colores

#### 4️⃣ Análisis Avanzado
- **Nuevos Casos Diarios:** Gráfico de barras
- **Tasa de Crecimiento:** Gráfico de líneas con porcentaje diario
- **Detección de Rebrotes:** Algoritmo automático (percentil 90)
- **Tabla de Eventos Significativos:** Últimos 5 días con mayor crecimiento

### 💡 Insights Automáticos

- **Top 5 Países Afectados:** Ranking actualizado dinámicamente
- **Estadísticas Generales:**
  - Número de países analizados
  - Días totales en el análisis
  - Promedio de casos por día
  - Tasa de letalidad promedio
- **Alertas de Tendencias:**
  - 🟢 Crecimiento controlado (<5%)
  - 🟡 Crecimiento moderado (5-10%)
  - 🔴 Crecimiento acelerado (>10%)
- **Países con Mayor Crecimiento Reciente:** Top 3 últimos 7 días

---

## 🚀 Instalación y Uso

### Requisitos Previos

1. **Python 3.8+** instalado
2. **Datos de JHU CSSE** descargados en la carpeta correcta:
   ```
   data/raw/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/
   ```

### Instalación de Dependencias

#### Opción 1: Usar el entorno virtual del proyecto
```bash
# Desde el directorio raíz del proyecto
source venv/bin/activate  # En Linux/Mac
# o
venv\Scripts\activate     # En Windows

# Las dependencias ya están instaladas
```

#### Opción 2: Instalar manualmente
```bash
pip install -r requirements.txt
```

### Ejecutar el Dashboard

```bash
# Desde el directorio raíz del proyecto
streamlit run dashboard/app.py
```

O si estás en el directorio del dashboard:
```bash
cd dashboard
streamlit run app.py
```

El dashboard se abrirá automáticamente en tu navegador en:
- **Local:** http://localhost:8501
- **Red:** http://[tu-ip]:8501

---

## 🎯 Guía de Uso

### 1. Selección de Filtros (Sidebar)

1. **Elige un Continente:**
   - "Todos" para análisis global
   - O selecciona un continente específico

2. **Selecciona Países (Opcional):**
   - Deja vacío para ver todos los países del continente
   - O selecciona uno o varios países específicos

3. **Define el Rango de Fechas:**
   - Usa el selector de fechas
   - Por defecto: Todo el período disponible (2020-2021)

4. **Observa las Métricas:**
   - Los KPIs se actualizan automáticamente
   - Las flechas indican cambios respecto al día anterior

### 2. Exploración de Visualizaciones

Navega por los **4 tabs** en la parte central:

- **Tab 1 - Evolución Temporal:**
  - Observa tendencias a lo largo del tiempo
  - Identifica picos y valles
  - Compara confirmados vs activos vs fallecidos

- **Tab 2 - Comparativa:**
  - Identifica los países más afectados
  - Compara tasas de letalidad
  - Analiza diferencias regionales

- **Tab 3 - Correlaciones:**
  - Entiende relaciones entre variables
  - Identifica patrones estadísticos

- **Tab 4 - Análisis Avanzado:**
  - Detecta rebrotes automáticamente
  - Analiza tasas de crecimiento
  - Identifica días críticos

### 3. Lectura de Insights

Revisa la sección **"Insights Automáticos"** al final:
- Top 5 países más afectados
- Estadísticas generales del período
- Alertas de crecimiento reciente
- Países con mayor crecimiento

---

## 🛠️ Estructura Técnica

```
dashboard/
├── app.py              # Aplicación principal
├── requirements.txt    # Dependencias
└── README.md          # Esta documentación
```

### Arquitectura del Código

```python
# Módulos principales
├── Importaciones
│   ├── streamlit (UI)
│   ├── pandas (procesamiento)
│   ├── plotly (visualizaciones)
│   └── src.config (funciones centralizadas)
│
├── Funciones de Carga
│   ├── load_complete_dataset() [cacheado]
│   ├── get_available_countries()
│   ├── get_available_continents()
│   ├── filter_data()
│   └── calculate_kpis()
│
└── Interfaz de Usuario
    ├── Header & Título
    ├── Sidebar (Filtros)
    ├── KPIs (5 métricas)
    ├── Tabs (4 visualizaciones)
    ├── Insights (3 columnas)
    └── Footer
```

### Funciones Centralizadas Utilizadas

Del módulo `src/config.py`:
- `load_daily_reports()` - Carga datos por rango de fechas
- `clean_covid_data()` - Pipeline de limpieza
- `load_continent_mapping()` - Mapeo geográfico
- `COUNTRY_MAPPING` - Diccionario de homogeneización

---

## ⚡ Optimizaciones Implementadas

### 1. Caché de Datos
```python
@st.cache_data(show_spinner=False)
def load_complete_dataset(start_date, end_date):
    # Los datos se cargan una sola vez
    # Siguientes accesos son instantáneos
```

### 2. Filtrado Eficiente
- Operaciones vectorizadas con pandas
- Filtros aplicados secuencialmente
- Sin iteraciones innecesarias

### 3. Visualizaciones Optimizadas
- Plotly con renderizado eficiente
- Datos agregados antes de graficar
- Limitación de puntos en gráficos grandes

### 4. Carga Progresiva
- Indicadores de progreso durante carga inicial
- Feedback visual al usuario
- Mensajes informativos en cada paso

---

## 🐛 Solución de Problemas

### ❌ El dashboard no carga los datos

**Problema:** Error al cargar archivos CSV

**Soluciones:**
1. Verifica que los datos estén en:
   ```
   data/raw/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/
   ```

2. Ejecuta el script de descarga:
   ```bash
   ./scripts/fetch_jhu_data.sh clone
   ```

3. Verifica permisos de lectura en la carpeta

### ❌ "Module not found: src.config"

**Problema:** No encuentra el módulo personalizado

**Soluciones:**
1. Ejecuta desde el directorio raíz del proyecto
2. Verifica que `src/config.py` existe
3. Asegúrate de usar el entorno virtual correcto

### ❌ Streamlit no se encuentra

**Problema:** `streamlit: command not found`

**Soluciones:**
1. Activa el entorno virtual:
   ```bash
   source venv/bin/activate
   ```

2. O instala streamlit:
   ```bash
   pip install streamlit
   ```

### ❌ Error de memoria

**Problema:** El sistema se queda sin memoria

**Soluciones:**
1. Reduce el rango de fechas seleccionado
2. Filtra por continente o país específico
3. Cierra otras aplicaciones

### ❌ Gráficos no se actualizan

**Problema:** Los filtros no afectan las visualizaciones

**Soluciones:**
1. Recarga la página (F5)
2. Limpia el caché: menú ≡ → "Clear cache"
3. Reinicia el servidor de Streamlit

### ❌ Dashboard muy lento

**Problema:** Respuesta lenta al cambiar filtros

**Soluciones:**
1. Espera a que termine la carga inicial
2. Reduce el rango de fechas
3. Selecciona países específicos en lugar de "Todos"

---

## 📊 Datos y Fuentes

### Fuente de Datos
- **Proveedor:** Johns Hopkins University CSSE
- **Repositorio:** [COVID-19 GitHub](https://github.com/CSSEGISandData/COVID-19)
- **Actualización:** Datos históricos 2020-2021
- **Formato:** CSV diarios con estructura estandarizada

### Cobertura de Datos
- **Período:** 22 de enero 2020 - 31 de diciembre 2021
- **Registros:** 2,548,545 puntos de datos
- **Países:** 248+ naciones y territorios
- **Continentes:** Todos los continentes principales

### Variables Principales
- `confirmed`: Casos confirmados acumulados
- `deaths`: Fallecimientos acumulados
- `recovered`: Casos recuperados
- `active_cases`: Casos activos (confirmados - fallecidos - recuperados)
- `date`: Fecha del reporte
- `country_region`: País o región
- `continent`: Continente

---

## 📚 Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|-----------|---------|-----------|
| **Python** | 3.13+ | Lenguaje base |
| **Streamlit** | 1.50.0 | Framework web interactivo |
| **Pandas** | 2.3+ | Procesamiento de datos |
| **Plotly** | 6.3+ | Visualizaciones interactivas |
| **NumPy** | 2.1+ | Operaciones numéricas |

### Librerías Adicionales
- `pathlib` - Manejo de rutas
- `datetime` - Manejo de fechas
- `sys` - Configuración de paths

---

## 🎓 Créditos y Licencia

### Desarrollado por
**Proyecto Semestral - Gestión de Datos 2025-II**

**Universidad Católica de la Santísima Concepción**  
Facultad de Ingeniería - Ingeniería Civil Informática

### Profesor
Lorenzo Paredes Grandón

### Fuente de Datos
Johns Hopkins University Center for Systems Science and Engineering (CSSE)

### Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](../LICENSE) para más detalles.

---

## 📞 Soporte

Si encuentras problemas o tienes sugerencias:

1. Revisa la sección de **Solución de Problemas**
2. Verifica que cumples todos los **Requisitos Previos**
3. Consulta la documentación del proyecto principal
4. Revisa los logs en la terminal donde ejecutaste Streamlit

---

## 🚀 Próximas Mejoras (Futuro)

- [ ] Mapa geográfico interactivo con Plotly Mapbox
- [ ] Exportación de gráficos a PNG/PDF
- [ ] Descarga de datos filtrados a CSV
- [ ] Comparación de múltiples países en gráfico único
- [ ] Predicciones con modelos de ML
- [ ] Análisis de variantes del virus (si hay datos disponibles)
- [ ] Dashboard en tiempo real con API de datos actuales

---

**¡Gracias por usar el COVID-19 Dashboard! 🦠📊**

````
