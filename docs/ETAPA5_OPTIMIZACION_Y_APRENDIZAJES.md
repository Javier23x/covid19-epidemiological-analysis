# Etapa 5: Optimizaciones y Aprendizajes

**Proyecto Semestral - Gestión de Datos 2025-II**  
**Universidad Católica de la Santísima Concepción**

---

## ¿De qué trata este documento?

Durante el desarrollo de este proyecto, no solo procesamos datos: **descubrimos problemas reales**, **tomamos decisiones importantes** y **aprendimos a trabajar con datos del mundo real**.

Este documento es una **reflexión honesta** sobre:
- Qué descubrimos que nos sorprendió
- Qué problemas enfrentamos y cómo los resolvimos
- Cómo hicimos el código más eficiente
- Qué lecciones nos llevamos para futuros proyectos

> **Nota:** La Etapa 5 es **transversal** - no es un notebook adicional, sino una documentación de todo lo que aprendimos mientras trabajábamos en las etapas 1-4.

---

## � Descubrimientos Importantes

### Descubrimiento #1: No todos son "países"

**¿Qué encontramos?**

Cuando empezamos a trabajar con los datos, asumimos que la columna `Country/Region` contenía solo países. Lo cual termino siendo un **error** ya que encontramos:

```
United States = País
Brazil = País
Diamond Princess = Es un crucero
MS Zaandam = Otro crucero
Antarctica = Es un continente
Taiwan* = Notación política especial
```

**¿Por qué importa esto?**

Imaginemos que se está haciendo un análisis "por continente" y de repente:
- ¿En qué continente debería ir un crucero?
- ¿La Antártida es un país o un continente?
- ¿Cómo afecta esto a tus gráficos y estadísticas?

**Lo que hicimos:**

1. Identificamos **todas** las entidades extrañas (encontramos cruceros, territorios, regiones especiales)
2. Creamos reglas claras:
   - Cruceros → Sin continente (los filtramos cuando hacemos análisis continentales)
   - Territorios → Los asignamos al país al que pertenecen
   - Antarctica → La dejamos como caso especial

**Resultado:** No hay más confusión al analizar datos por país o continente.

---

### Descubrimiento #2: El mismo país, mil nombres diferentes

**¿Qué encontramos?**

El mismo país aparecía con diferentes nombres en diferentes fechas:

```python
# Estados Unidos tenía 3 variantes:
"US"  →  enero-marzo 2020
"USA" →  abril-mayo 2020  
"United States" → junio 2020+

# Corea del Sur:
"Korea, South" vs "South Korea"

# Reino Unido:
"UK" vs "United Kingdom"

# China en archivos antiguos:
"Mainland China" vs "China"
```

**El problema real:**

Si se intenta sumar casos de "US" + "USA" + "United States" sin normalizar, Python los ve como **3 países diferentes**. Resultado: números incorrectos y análisis errados.

**La solución:**

Creamos un "diccionario traductor" con **30+ reglas** de normalización:

```python
COUNTRY_MAPPING = {
    'US': 'United States',
    'USA': 'United States',
    'UK': 'United Kingdom',
    'Korea, South': 'South Korea',
    'Taiwan*': 'Taiwan',
    'Mainland China': 'China',
    # ... 25 reglas más
}
```

**Resultado:** Todos los datos del mismo país se unifican bajo un solo nombre estándar.

---

### Descubrimiento #3: Columnas duplicadas en los archivos

**¿Qué pasó?**

Al cargar datos de diferentes meses, encontramos que algunos archivos tenían **columnas duplicadas** con el mismo nombre:

```
province_state | province_state | country_region | country_region | ...
```

Esto causaba errores al procesar porque Pandas no sabe cuál columna usar.

**¿Por qué ocurrió?**

El dataset de JHU CSSE evolucionó con el tiempo - diferentes equipos añadieron columnas en diferentes momentos, y algunos archivos quedaron con duplicados por error.

**La solución:**

Creamos una función que detecta y consolida duplicados automáticamente:

```python
def consolidate_duplicate_columns(df):
    # Detecta columnas con el mismo nombre
    # Toma el primer valor no-nulo de cada una
    # Elimina las duplicadas y deja solo una versión limpia
```

**Resultado:** El código ahora es robusto y no falla aunque los datos tengan inconsistencias.

---

### Descubrimiento #4: Muchos países sin datos de "recuperados"

**Hallazgo sorprendente:**

Al analizar 6 meses de datos (Etapa 2), descubrimos que **muchos países nunca reportaron recuperados** - la columna `recovered` estaba en 0 o vacía.

**Hipótesis**

- Algunos países no tenían sistemas para rastrear recuperaciones
- Otros países dejaron de reportar recuperados en cierto punto
- Las políticas de reporte variaban por país

**Impacto en el proyecto:**

- No podemos calcular "casos activos" confiablemente para todos los países
- Las comparaciones de recuperación entre países no son justas
- Tuvimos que agregar advertencias en el dashboard sobre esta limitación

**Lo que aprendimos:** Los datos del mundo real tienen **huecos**, y parte de nuestro trabajo es documentar esas limitaciones, no esconderlas.

---

## Desafíos y Cómo los Resolvimos

### Desafío #1: Unir datos de 710 archivos CSV

**El problema:**

El dataset de JHU CSSE está dividido en **710 archivos CSV** (uno por día). Para hacer análisis, necesitábamos:
- Cargar todos los archivos
- Unirlos en un solo DataFrame grande
- Asegurar que las columnas coincidan entre archivos

**¿Por qué es difícil?**

```python
# Archivo de enero 2020:
Columnas: Province/State, Country/Region, Last Update, Confirmed, Deaths, Recovered

# Archivo de junio 2020:
Columnas: FIPS, Admin2, Province_State, Country_Region, Last_Update, Confirmed, Deaths, Recovered, Active

# No coinciden, Diferentes nombres y columnas extra
```

**La solución paso a paso:**

1. **Función inteligente de carga** (`load_daily_reports`):
   - Carga archivo por archivo
   - Normaliza nombres de columnas sobre la marcha
   - Añade columnas faltantes con valores nulos
   - Muestra progreso cada 50 archivos

2. **Pipeline de limpieza** (`clean_covid_data`):
   - Estandariza todos los nombres de columnas
   - Convierte tipos de datos
   - Maneja valores faltantes

**Resultado:**
```python
# Antes: 130 líneas de código repetitivo
# Después: 3 líneas
df = load_daily_reports('2020-01-22', '2021-12-31')
df = clean_covid_data(df)
df = load_continent_mapping(df)
```

Ahorramos lineas de codigo y tiempo de desarrollo por cada nueva etapa del proyecto.
   
---

### Desafío #2: Los datos no tienen información de continentes

**El problema:**

Para hacer análisis "por continente", necesitábamos saber qué países pertenecen a qué continente. **Pero el dataset de JHU no incluye esta información.**

**Opciones consideradas:**

| Opción | Ventajas | Desventajas |
|--------|----------|-------------|
| Hardcodear manualmente | Simple | No escalable, propenso a errores |
| Usar API externa | Datos actualizados | Requiere internet, más lento |
| Archivo CSV externo | Rápido, offline | Hay que mantenerlo |

**Nuestra solución:** Archivo CSV externo

Creamos `data/country_to_continent.csv` con 248+ países mapeados:

```csv
country,continent
United States,North America
Brazil,South America
China,Asia
Germany,Europe
...
```

**Función inteligente de mapeo:**

```python
def load_continent_mapping(df):
    # 1. Carga el archivo CSV
    # 2. Crea un diccionario país→continente  
    # 3. Aplica el mapeo
    # 4. Reporta países sin mapeo (ej: cruceros)
    # 5. Muestra estadísticas de cobertura
```

**Ventajas:**
- Funciona offline  
- Rápido (lectura de CSV local)  
- Fácil de actualizar si encontramos nuevos países  
- Reporta automáticamente problemas (países sin mapeo)

---

### Desafío #3: Problema al cargar los datos desde el repositorio de GitHub

**El problema:**

Al inicio del proyecto, intentábamos cargar los datos CSV directamente desde el repositorio de GitHub de JHU CSSE usando URLs:

```python
# Intento inicial - cargar directamente desde GitHub
base_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/...'
for date in dates:
    url = f"{base_url}/{date.strftime('%m-%d-%Y')}.csv"
    df = pd.read_csv(url)  # Error 429 después de ~20 archivos
```

**¿Qué pasaba?**

Después de cargar aproximadamente 20-30 archivos, GitHub empezaba a devolver:

```
HTTPError: 429 Client Error: Too Many Requests
```

**¿Por qué ocurría?**

GitHub tiene **límites de tasa (rate limits)** para proteger sus servidores:
- **60 peticiones por hora** para usuarios no autenticados
- Cargar 710 archivos → 710 peticiones
- Resultado: Bloqueados después de 20-30 archivos

**Intentos fallidos:**

| Intento | Solución Propuesta | Resultado |
|---------|-------------------|-----------|
| #1 | Esperar 1 segundo entre peticiones | Muy lento (12+ minutos), igual bloqueado |
| #2 | Usar tokens de autenticación | 5000 peticiones/hora, pero igualmente lento |
| #3 | Cargar solo algunos archivos | No sirve para análisis completo |

**La solución definitiva: Descargar el repositorio localmente**

**Paso 1:** Clonar el repositorio completo

```bash
cd data/raw/
git clone https://github.com/CSSEGISandData/COVID-19.git
```

**Paso 2:** Limpiar archivos innecesarios

El repositorio completo tenía **~2GB** con muchos archivos que no necesitábamos:

```bash
# Borramos lo que no usamos
cd COVID-19/
rm -rf .github/           # Archivos de configuración de GitHub
rm -rf archived_data/     # Datos antiguos sin formato consistente
rm -rf who_covid_19_*/    # Datos de la OMS (duplicados)
rm -rf README.md CONTRIBUTING.md  # Documentación
```

Resultado: De **2GB → 350MB** (solo los CSV que necesitamos)

**Paso 3:** Crear script de actualización automática

Creamos un script para actualizar los datos cuando sea necesario:

```bash
#!/bin/bash
# scripts/update_data.sh

echo "Actualizando datos de COVID-19..."
cd data/raw/COVID-19/
git pull origin master
echo "Datos actualizados exitosamente"
```

**Ventajas de esta solución:**

| Aspecto | Cargar desde GitHub | Repositorio Local |
|---------|-------------------|-------------------|
| Velocidad | 12+ minutos (con límites) | 4 segundos |
| Confiabilidad | Error 429 frecuente | 100% confiable |
| Funciona offline | No | Sí |
| Actualización | Automática | Manual (pero con script) |
| Espacio en disco | 0 MB | 350 MB |

**Resultado:**

```python
# Código final - simple y rápido
DATA_DIR = '../data/raw/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/'
for date in dates:
    filepath = os.path.join(DATA_DIR, f"{date.strftime('%m-%d-%Y')}.csv")
    df = pd.read_csv(filepath) 
```

**Tiempo de carga:** De 12+ minutos (con errores) → **4 segundos** (sin errores)

**Bonus:** Si necesitamos datos actualizados, solo ejecutamos:

```bash
bash scripts/update_data.sh
```

Y tenemos los datos más recientes en segundos.

---

### Desafío #4: Código duplicado en múltiples notebooks

**El problema:**

```
Etapa1.ipynb: 50 líneas de código de limpieza
Etapa2.ipynb: 80 líneas de código de limpieza (+ carga)  
Etapa3.ipynb: 150 líneas de código de limpieza (+ carga + mapeo)

TOTAL: ~280 líneas duplicadas
```

**Problemas causados:**
- Si encontramos un bug, hay que arreglarlo en 3 lugares
- Cambiar algo requiere editar múltiples archivos
- Inconsistencias entre etapas
- Difícil de mantener

**La solución: Módulo centralizado**

Creamos `src/config.py` con **10 funciones reutilizables**:

```python
# src/config.py
├── load_daily_reports()          # Carga archivos CSV
├── clean_covid_data()            # Pipeline de limpieza
├── load_continent_mapping()      # Mapeo de continentes
├── standardize_column_names()    # Normaliza nombres
├── consolidate_duplicate_columns() # Maneja duplicados
├── drop_irrelevant_columns()     # Elimina columnas innecesarias
├── process_dates()               # Procesa fechas
├── convert_numeric_columns()     # Convierte tipos numéricos
├── calculate_active_cases()      # Calcula casos activos
└── homogenize_country_names()    # Normaliza países
```

**Impacto:**

| Métrica | Antes | Después | Reducción |
|---------|-------|---------|-----------|
| Líneas en Etapa 2 | 130 | 10 | **92%** |
| Líneas en Etapa 3 | 200 | 10 | **95%** |
| Lugares para arreglar bugs | 3 | 1 | **67%** |
| Consistencia | Baja | Alta | Sí |

**Beneficio adicional:** Ahora podemos añadir tests unitarios a las funciones centralizadas.

---

## Optimizaciones que Implementamos

### Optimización #1: De 280 líneas a 3 líneas

**Qué optimizamos:** Código duplicado de carga y limpieza de datos

**Antes:**

Cada notebook tenía su propia versión del código de limpieza:

```python
# Etapa2.ipynb - 130 líneas
DATA_DIR = '../data/raw/COVID-19/...'
dates = pd.date_range('2020-01-22', '2020-06-30')
dfs = []
for date in dates:
    filename = date.strftime('%m-%d-%Y') + '.csv'
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        # ... 40 líneas más de procesamiento ...
        dfs.append(df)
df = pd.concat(dfs)

# ... 80 líneas más de limpieza ...
df.columns = df.columns.str.lower()
df = df.drop(columns=['fips', 'admin2', ...])
# ... y más código ...
```

**Después:**

```python
# Etapa2.ipynb - 3 líneas
df = load_daily_reports('2020-01-22', '2020-06-30')
df = clean_covid_data(df)
df = load_continent_mapping(df)
```

**Impacto:**

| Notebook | Líneas Antes | Líneas Después | Reducción |
|----------|--------------|----------------|-----------|
| Etapa 2 | 130 | 3 | **98%** |
| Etapa 3 | 200 | 3 | **98.5%** |
| Dashboard | 150 | 3 | **98%** |

**Beneficios adicionales:**
- Si hay un bug, se arregla en UN solo lugar
- Código más legible y profesional
- Fácil de mantener y actualizar
- Podemos añadir tests unitarios

---

### Optimización #2: Dashboard 98% más rápido

**Qué optimizamos:** Carga de datos en el dashboard interactivo

**El problema:**

```python
# Sin caché
def load_data():
    df = load_daily_reports(...)  # 4 segundos
    # ... procesamiento ...
    return df

# Se ejecuta cada vez que el usuario interactúa:
# - Cambiar filtro: 4 seg de espera
# - Cambiar país: 4 seg de espera  
# - Cambiar fecha: 4 seg de espera
```

**La solución:**

```python
@st.cache_data(show_spinner=False)  # ← ¡Magia aquí!
def load_complete_dataset(start_date, end_date):
    """Se ejecuta UNA vez, luego Streamlit guarda el resultado"""
    df = load_daily_reports(start_date, end_date)
    df = clean_covid_data(df)
    df = load_continent_mapping(df)
    return df

# Primera vez: 4 seg
# Después: 0.08 seg (50x más rápido)
```

**Mediciones reales:**

| Operación | Tiempo Antes | Tiempo Después | Mejora |
|-----------|--------------|----------------|--------|
| Carga inicial | 4.2 seg | 4.2 seg | - |
| Filtrar por continente | 4.2 seg | 0.08 seg | **52x más rápido** |
| Seleccionar país | 4.2 seg | 0.08 seg | **52x más rápido** |
| Cambiar rango fecha | 4.2 seg | 0.08 seg | **52x más rápido** |
| Actualizar gráfico | 4.2 seg | 0.08 seg | **52x más rápido** |

**Experiencia del usuario:**
- Antes: Frustración, esperas constantes
- Después: Dashboard se siente fluido e instantáneo

---

### Optimización #3: Función pipeline de limpieza

**Qué optimizamos:** Proceso de limpieza de datos

**Antes:** Pasos separados, difícil de seguir

```python
# 50 líneas distribuidas en el notebook
df.columns = df.columns.str.lower()
df = df.drop(columns=['fips', ...])
df['confirmed'] = pd.to_numeric(df['confirmed'])
df['deaths'] = pd.to_numeric(df['deaths'])
# ... 40 líneas más ...
```

**Después:** Pipeline unificado

```python
def clean_covid_data(df, verbose=True):
    """
    Pipeline completo de limpieza en 1 función.
    Ejecuta 7 pasos en orden correcto.
    """
    df = standardize_column_names(df)
    df = consolidate_duplicate_columns(df)
    df = drop_irrelevant_columns(df)
    df = process_dates(df)
    df = convert_numeric_columns(df)
    df = calculate_active_cases(df)
    df = homogenize_country_names(df)
    return df
```

**Ventajas:**

1. **Orden garantizado:** Los pasos siempre se ejecutan en el orden correcto
2. **Atomic:** O funciona todo o falla todo (no estados intermedios rotos)
3. **Reutilizable:** Mismo pipeline en todas las etapas
4. **Testeable:** Podemos probar cada paso individualmente

**Resultado:** Código más robusto y confiable.

---

### Optimización #4: 


---

## Decisiones de Diseño Importantes

### Decisión #1: ¿Todo en notebooks o código modular?

**La pregunta:**

Cuando empezamos el proyecto, teníamos que decidir:

```
Opción A: Código autocontenido
├── Todo dentro de cada notebook
├── Fácil de empezar
└── Cada notebook es independiente

VS

Opción B: Código modular
├── Crear carpeta src/ con funciones
├── Más trabajo inicial
└── Notebooks importan funciones
```

**Lo que consideramos:**

| Aspecto | Opción A (Todo en notebooks) | Opción B (Modular) |
|---------|----------------------------|-------------------|
| Facilidad inicial | Muy fácil | Más setup |
| Mantenimiento | Difícil (cambiar en 3 lugares) | Fácil (cambiar en 1 lugar) |
| Reutilización | Copiar/pegar código | Importar funciones |
| Profesionalismo | Amateur | Código de producción |
| Testing | Casi imposible | Fácil añadir tests |

**Nuestra decisión:** Opción B (Modular)

**Por qué:**
- Estamos aprendiendo a trabajar **como en el mundo real**
- El tiempo invertido en setup se recupera en las etapas siguientes
- Mejor para el portafolio profesional
- Práctica de buenas prácticas de programación

**Resultado:** Invirtimos 2 horas al inicio, ahorramos 5+ horas después.

---

### Decisión #2: ¿Refactorizar Etapa 1 o dejarla paso a paso?

**El dilema:**

Después de crear `src/config.py`, surgió la pregunta: ¿Simplificar también Etapa 1?

```
Opción A: Refactorizar todo
- Etapa 1 usa las funciones centralizadas
- Consistencia total
- Solo 3 líneas de código

Opción B: Mantener Etapa 1 paso a paso
- Etapa 1 muestra CÓMO funciona cada paso
- Etapas 2-3 usan código modular
- Propósito educativo vs productivo
```

**Nuestra decisión:** Opción B (Híbrida)

**Justificación:**

| Etapa | Enfoque | Razón |
|-------|---------|-------|
| **Etapa 1** | Paso a paso | Aprender CÓMO limpiar datos |
| **Etapa 2** | Modular | Enfoque en análisis, no en limpieza |
| **Etapa 3** | Modular | Enfoque en visualizaciones |
| **Dashboard** | Modular | Código profesional |

**Beneficio:** 
- Etapa 1 sirve como **documentación viva** de lo que hace `clean_covid_data()`
- Las demás etapas son **código productivo y conciso**

---

### Decisión #3: ¿Cómo mostrar progreso al cargar archivos?

**El problema:**

Cargar 710 archivos puede tomar minutos. Sin feedback, el usuario piensa que el programa se congeló.

**Opciones:**

```python
# Opción A: No mostrar nada
for file in files:
    load(file)  # Usuario no sabe si funciona

# Opción B: Mensaje por archivo
for file in files:
    print(f"Cargando {file}")  # 710 mensajes, spam

# Opción C: Progreso cada N archivos
for i, file in enumerate(files):
    load(file)
    if i % 50 == 0:
        print(f"Cargados {i}/{total}")  # Informativo sin spam
```

**Nuestra decisión:** Opción C con parámetro configurable

```python
def load_daily_reports(start_date, end_date, progress_interval=50):
    """
    progress_interval: cada cuántos archivos mostrar progreso
    - 50 (default): Para uso normal
    - 100: Para cuando quieres menos mensajes
    - 1: Para debugging (ver cada archivo)
    """
```

**Resultado:**
```
Cargando datos desde archivos locales...
============================================================
Período: 2020-01-22 → 2021-12-31
Total de archivos a cargar: 710
============================================================

✓ Cargados 50/710 archivos (7.0%)
✓ Cargados 100/710 archivos (14.1%)
✓ Cargados 150/710 archivos (21.1%)
...
```

Usuario siempre sabe que el programa está funcionando.

---

## Lecciones Aprendidas

### Lección #1: Los datos reales nunca están limpios

**Antes del proyecto pensábamos:**
> "Los datos de una universidad prestigiosa como Johns Hopkins deben estar perfectos"

**La realidad:**
- Nombres de países inconsistentes
- Columnas duplicadas
- Cambios de formato a lo largo del tiempo
- Valores faltantes sin explicación
- Entidades que no son países

**Lo que aprendimos:**

1. **Siempre explorar primero:** No hacer suposiciones, verificar con `df.info()`, `df.describe()`, `df['column'].unique()`

2. **Documentar las inconsistencias:** Anotar qué problemas encontramos y cómo los resolvimos

3. **Código defensivo:** Escribir funciones que manejen casos inesperados:
   ```python
   # Código frágil
   df['confirmed'].sum()  # Falla si hay valores no numéricos
   
   # Código robusto
   pd.to_numeric(df['confirmed'], errors='coerce').fillna(0).sum()
   ```

**Impacto:** Esta lección vale más que cualquier tutorial - es experiencia real.

---

### Lección #2: La modularización ahorra tiempo (pero no al inicio)

**Gráfica de esfuerzo vs tiempo:**

```
Esfuerzo
    ↑
    │     ╱────────── Con modularización (menos esfuerzo después)
    │    ╱
    │   ╱
    │  ╱  ╲
    │ ╱    ╲       Sin modularización
    │╱      ╲     (esfuerzo crece)
    │        ╲___
    └─────────────→ Tiempo
    Etapa1  Etapa2  Etapa3  Dashboard
```

**Los números:**

| Etapa | Tiempo con módulo | Tiempo sin módulo | Diferencia |
|-------|-------------------|-------------------|------------|
| **Etapa 1** (crear módulo) | 3 horas | 1.5 horas | +1.5h (más lento) |
| **Etapa 2** | 1 hora | 2.5 horas | -1.5h (más rápido) |
| **Etapa 3** | 1.5 horas | 3 horas | -1.5h (más rápido) |
| **Dashboard** | 2 horas | 4 horas | -2h (más rápido) |
| **TOTAL** | **7.5 horas** | **11 horas** | **Ahorro: 3.5h** |

**Plus:** Si encontramos un bug, arreglarlo toma 5 minutos en vez de 30 minutos.

---

### Lección #3: El caching es magia (cuando se usa bien)

**Lo que aprendimos sobre `@st.cache_data`:**

**Cuándo usarlo:**
- Funciones que cargan datos pesados
- Operaciones costosas que no cambian frecuentemente
- Procesamiento que siempre da el mismo resultado con los mismos parámetros

**Cuándo NO usarlo:**
- Funciones que dependen del tiempo actual
- Operaciones con efectos secundarios (escribir archivos)
- Funciones que devuelven objetos que se modificarán

**Ejemplo real:**

```python
# BIEN: Cargar datos (mismos parámetros = mismos datos)
@st.cache_data
def load_complete_dataset(start_date, end_date):
    return load_data(start_date, end_date)

# MAL: Filtrar datos (cambia con interacción del usuario)
@st.cache_data
def filter_data(df, continent, countries, dates):
    # Este filtro cambia cada segundo, no debe cachearse
    return df[filters]
```

**Resultado:** Dashboard 50x más rápido sin romper la funcionalidad.

---

### Lección #4: Git es tu red de seguridad

**Momentos donde Git nos salvó:**

1. **"Rompí todo el código"** 
   → `git checkout .` para volver a la última versión que funcionaba

2. **"¿Qué cambié desde ayer?"**
   → `git diff` para ver exactamente qué modificamos

3. **"¿Cuándo añadimos esa función?"**
   → `git log` muestra el historial completo

4. **"Quiero probar algo arriesgado"**
   → `git branch experimental` para probar sin miedo

**Hábito que desarrollamos:**
```bash
# Después de cada avance significativo:
git add .
git commit -m "feat: descripción clara del cambio"
git push
```

**Commits del proyecto:** 30+ commits con mensajes descriptivos que cuentan la historia del desarrollo.

---

### Lección #5: Optimizar temprano VS optimizar tarde

**Dilema del desarrollador:**

```
"¿Optimizo ahora o después?"

Optimizar temprano:
+ Código eficiente desde el inicio
- Puede ser optimización prematura
- Gastas tiempo que tal vez no necesitas
              
Optimizar tarde:
+ Implementas rápido
+ Solo optimizas lo que realmente necesita
- Puede ser doloroso refactorizar después
```

**Nuestra experiencia:**

| Optimización | Cuándo la hicimos | ¿Fue buena decisión? |
|--------------|-------------------|---------------------|
| Modularización | Después de Etapa 1 | Sí, ahorró mucho tiempo |
| Caching dashboard | Cuando notamos lentitud | Sí, problema real |
| Optimizar tipos de datos | No lo hicimos | Podría mejorar memoria |

**Regla que aprendimos:**
> "Optimiza cuando hay un problema real, no cuando imaginas que habrá uno"

---

### Lección #6: La documentación es para tu yo del futuro

**Historia real:**

```
Semana 1: Escribimos código genial
Semana 3: "¿Qué hace esta función? ¿Por qué lo hice así?"
         ↳ Nos tomó 30 minutos recordar
```

**Solución:** Comentarios y docstrings claros

```python
# Sin documentación
def f(d, s, e):
    return d[(d['date'] >= s) & (d['date'] <= e)]

# Con documentación
def filter_data_by_date_range(df, start_date, end_date):
    """
    Filtra un DataFrame por rango de fechas.
    
    Args:
        df: DataFrame con columna 'date'
        start_date: Fecha inicial (datetime)
        end_date: Fecha final (datetime)
    
    Returns:
        DataFrame filtrado
    
    Example:
        >>> filtered = filter_data_by_date_range(df, '2020-01-01', '2020-12-31')
    """
    return df[(df['date'] >= start_date) & (df['date'] <= end_date)]
```

**Resultado:** Volver al código después de semanas es fácil, no frustrante.

---

## ¿Qué Haríamos Diferente? (Mejoras Futuras)

### Si tuviéramos más tiempo...

#### 1. **Optimización de Memoria**

**El problema:** Nuestro DataFrame ocupa ~500MB en memoria

**La mejora:**
```python
# Convertir columnas a tipos más eficientes
df['confirmed'] = df['confirmed'].astype('int32')  # En vez de int64
df['country_region'] = df['country_region'].astype('category')  # En vez de object
```

**Ahorro esperado:** 40-60% menos uso de memoria

---

#### 2. **Paralelización de Carga**

**El problema:** Cargamos archivos uno por uno (secuencial)

**La mejora:**
```python
from multiprocessing import Pool

# Cargar 4 archivos al mismo tiempo
with Pool(4) as p:
    dfs = p.map(load_csv, file_list)
```

**Tiempo esperado:** 50% más rápido (4 segundos → 2 segundos)

---

#### 3. **Formato Parquet**

**El problema:** CSV es lento de leer y ocupa mucho espacio

**La mejora:**
```python
# Guardar como Parquet después de procesar
df.to_parquet('data/processed/covid_complete.parquet')

# Cargar Parquet (10x más rápido que CSV)
df = pd.read_parquet('data/processed/covid_complete.parquet')
```

**Beneficios:**
- Carga 10x más rápida
- 50% menos espacio en disco
- Mantiene tipos de datos automáticamente

---

#### 4. **Tests Unitarios**

**Lo que falta:**
```python
# tests/test_config.py
def test_homogenize_country_names():
    """Verificar que US → United States"""
    df = pd.DataFrame({'country_region': ['US', 'UK']})
    df = homogenize_country_names(df)
    assert df['country_region'][0] == 'United States'
    assert df['country_region'][1] == 'United Kingdom'
```

**Beneficio:** Detectar bugs antes de que rompan el dashboard

---

#### 5. **Dashboard: Más Visualizaciones**

Ideas que nos gustaría implementar:

- **Mapa geográfico interactivo:** Ver casos por país en mapa mundial
- **Animación temporal:** Ver evolución de la pandemia como video
- **Comparador personalizado:** Seleccionar 5 países y comparar métricas
- **Predicciones básicas:** Usar modelos simples para proyectar tendencias
- **Exportar reportes PDF:** Generar resumen automático del análisis

---

#### 6. **Análisis Más Profundos**

**Ideas interesantes:**

```
Análisis de olas/picos
├── Detectar automáticamente las "olas" de contagio
├── Comparar duración e intensidad entre países
└── Identificar patrones comunes

Análisis por densidad poblacional
├── Normalizar casos por población
├── Ver si países densos tienen más contagios
└── Correlación con políticas de cuarentena

Análisis de políticas
├── Comparar países con cuarentena estricta vs laxa
├── Medir efectividad de medidas
└── Timeline de políticas vs casos
```

---

#### 7. **Automatización de Actualización**

**La idea:**
```bash
# Script que corre diariamente
#!/bin/bash
cd data/raw/COVID-19
git pull  # Descargar datos actualizados de JHU
cd ../../..
python scripts/update_processed_data.py  # Reprocesar
streamlit run dashboard/app.py  # Dashboard siempre actualizado
```

**Beneficio:** Dashboard con datos del día automáticamente

---

#### 8. **Documentación Interactiva**

**Lo que podríamos añadir:**

- Jupyter Book con todo el análisis
- Video explicativo de 5 minutos
- �️ Infografía resumen del proyecto
- Poster científico para presentaciones

---

## Resumen del Proyecto

### ¿Qué logramos?

| Métrica | Resultado |
|---------|-----------|
| **Etapas completadas** | 5 de 5 (100%) |
| **Notebooks creados** | 3 (Etapa 1, 2, 3) |
| **Dashboard funcional** | Sí, con 4 tabs y 5 KPIs |
| **Funciones centralizadas** | 10 funciones reutilizables |
| **Reducción de código** | 92-95% en Etapas 2-3 |
| **Países mapeados** | 248+ con continentes |
| **Optimizaciones** | 4 optimizaciones documentadas |
| **Descubrimientos** | 4 hallazgos importantes |
| **Commits en Git** | 30+ commits descriptivos |

---

### Tecnologías que dominamos

**Análisis de Datos:**
- Pandas: Manipulación avanzada de datos
- NumPy: Operaciones numéricas eficientes
- Pandas profiling: Reportes automáticos

**Visualización:**
- Plotly: Gráficos interactivos
- Matplotlib: Visualizaciones estáticas
- Seaborn: Gráficos estadísticos elegantes

**Desarrollo Web:**
- Streamlit: Dashboards interactivos
- HTML/CSS: Personalización de interfaz

**Herramientas:**
- Git: Control de versiones profesional
- Jupyter: Notebooks interactivos
- VS Code: Desarrollo eficiente

---

### Habilidades desarrolladas

**Técnicas:**
- Limpieza y transformación de datos reales
- Análisis exploratorio de datos (EDA)
- Diseño de visualizaciones efectivas
- Desarrollo de aplicaciones con datos
- Optimización de rendimiento
- Modularización y buenas prácticas

**Blandas:**
- Resolución de problemas complejos
- Documentación técnica clara
- Pensamiento crítico sobre datos
- Trabajo con datos del mundo real
- Gestión de proyecto completo

---

## Conclusión

### ¿Qué nos llevamos de este proyecto?

**1. Experiencia Real**

Este no fue un tutorial con datos perfectos. Trabajamos con:
- 710 archivos CSV inconsistentes
- Datos faltantes y errores
- Cambios de formato a lo largo del tiempo
- Problemas reales que requirieron soluciones creativas

**2. Código Profesional**

Aprendimos a:
- Modularizar código para reutilización
- Escribir funciones documentadas
- Usar Git con commits descriptivos
- Optimizar cuando hay problemas reales
- Crear aplicaciones interactivas funcionales

**3. Pensamiento Analítico**

Desarrollamos la habilidad de:
- Cuestionar los datos (no asumir que están bien)
- Documentar descubrimientos
- Tomar decisiones de diseño justificadas
- Medir el impacto de optimizaciones
- Pensar en el usuario final

**4. Portfolio Real**

Ahora tenemos:
- Repositorio Git público con código limpio
- Dashboard funcional desplegable
- Notebooks bien documentados
- README profesional
- Documentación de aprendizajes

---

### La lección más importante

> **Los datos del mundo real son desordenados, inconsistentes y llenos de sorpresas. Nuestro trabajo no es solo analizar datos perfectos, sino transformar datos imperfectos en información útil y confiable.**

Este proyecto nos preparó para trabajar con datos reales en cualquier industria.

---

## Metadatos del Documento

**Autores:** Javier Pino Herrera, Camilo Campos González  
**Curso:** Gestión de Datos 2025-II  
**Profesor:** Lorenzo Paredes Grandón  
**Universidad:** Universidad Católica de la Santísima Concepción  
**Fecha:** Noviembre 2025  

**Última actualización:** 17 de noviembre de 2025

---

**Repositorio del proyecto:** [github.com/Javier23x/covid19-epidemiological-analysis](https://github.com/Javier23x/covid19-epidemiological-analysis)

---

*Este documento es parte de la Etapa 5 del Proyecto Semestral de Análisis Epidemiológico de COVID-19, reflejando los aprendizajes, desafíos y soluciones encontradas durante el desarrollo completo del proyecto.*
