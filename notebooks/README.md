# 📓 Notebooks del Proyecto

Esta carpeta contiene los notebooks de Jupyter que implementan las diferentes etapas del análisis.

## 📋 Notebooks

### 01_limpieza_datos.ipynb
**Objetivo:** Comprender la estructura del dataset y generar una base consolidada y limpia.

**Datos:** 1 mes (enero 2020)

**Tareas:**
1. Cargar y visualizar datos
2. Análisis de estructura
3. Detección de valores nulos
4. Limpieza de columnas
5. Estandarización
6. Transformaciones
7. Exportación de datos limpios

**Entregable:** `data/processed/covid_clean_enero2020.csv`

---

### 02_analisis_exploratorio.ipynb
**Objetivo:** Explorar la evolución de los datos y realizar análisis comparativos.

**Datos:** 6 meses (enero-junio 2020)

**Preguntas:**
1. Top 10 países con más casos
2. Tasas de letalidad
3. Países sin recuperados
4. Análisis Latinoamérica
5. Evolución de Chile
6. Pico global de casos
7. Correlaciones
8. Crecimiento porcentual
9. Identificación de rebrotes
10. Perfilado automático

**Entregables:** 
- Análisis completo con gráficos
- `reports/perfilado.html`

---

### 03_visualizaciones.ipynb
**Objetivo:** Profundizar en el análisis visual, comparando regiones y tendencias.

**Datos:** 2 años (2020-2021)

**Visualizaciones:**
1. Evolución temporal global
2. Comparativa Top 10 países
3. Heatmap de correlaciones
4. Tasas de letalidad por continente
5. Mapa geográfico

**Entregable:** Visualizaciones avanzadas con interpretaciones

---

### 04_optimizacion.ipynb
**Objetivo:** Mejorar la eficiencia del código y demostrar dominio técnico.

**Aplicable:** Todas las etapas anteriores

**Optimizaciones:**
- Lectura eficiente de datos
- Conversión de tipos
- Uso de índices
- Operaciones vectorizadas
- Mediciones de rendimiento

**Entregable:** Documentación de mejoras con evidencia

---

## 🚀 Cómo Ejecutar

1. **Activar entorno virtual:**
   ```bash
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. **Asegurar dependencias instaladas:**
   ```bash
   pip install -r ../requirements.txt
   ```

3. **Iniciar Jupyter:**
   ```bash
   jupyter notebook
   ```

4. **Ejecutar notebooks en orden:**
   - Primero `01_limpieza_datos.ipynb`
   - Luego `02_analisis_exploratorio.ipynb`
   - Después `03_visualizaciones.ipynb`
   - Finalmente `04_optimizacion.ipynb`

## 📝 Convenciones

- **Imports al inicio:** Todas las importaciones al comienzo
- **Comentarios:** Explicar secciones complejas
- **Markdown cells:** Títulos y explicaciones
- **Outputs visibles:** Mantener outputs de gráficos
- **Código limpio:** Seguir PEP 8

## 🔍 Estructura Sugerida de Notebooks

```python
# 1. Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src import data_processing, analysis, visualization

# 2. Configuración
%matplotlib inline
pd.set_option('display.max_columns', None)

# 3. Carga de Datos
df = pd.read_csv('../data/raw/archivo.csv')

# 4. Exploración Inicial
df.head()
df.info()
df.describe()

# 5. Análisis/Procesamiento
# Tu código aquí...

# 6. Visualizaciones
# Tus gráficos aquí...

# 7. Conclusiones
# Interpretación de resultados...

# 8. Exportación
df_clean.to_csv('../data/processed/archivo_limpio.csv', index=False)
```

## 💡 Tips

- **Ejecutar celda por celda:** No ejecutar todo de una vez inicialmente
- **Guardar frecuentemente:** Jupyter puede fallar
- **Kernel restart:** Si algo sale mal, reiniciar kernel
- **Clear outputs:** Limpiar outputs antes de commit (opcional)
- **Documentar decisiones:** Explicar por qué haces algo

## 🐛 Troubleshooting

### Error: Module not found
```bash
pip install <nombre-paquete>
```

### Kernel muerto
- Restart Kernel
- Verificar uso de memoria
- Reducir tamaño de datos en pruebas

### Gráficos no se muestran
```python
%matplotlib inline  # Agregar al inicio
```

### Datos muy grandes
```python
# Usar sample para pruebas
df_sample = df.sample(n=10000, random_state=42)
```

## 📚 Recursos Útiles

- [Jupyter Documentation](https://jupyter-notebook.readthedocs.io/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Examples](https://seaborn.pydata.org/examples/index.html)

---

**Nota:** Los notebooks deben ejecutarse en orden, ya que cada uno puede depender de los datos generados por el anterior.
