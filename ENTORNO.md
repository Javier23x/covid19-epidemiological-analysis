# 🚀 Guía Rápida de Uso del Entorno

## ✅ Entorno Virtual Configurado

El entorno virtual está **listo para usar** con todas las dependencias instaladas.

### 📦 Paquetes Instalados

**Total:** 163 paquetes

**Principales:**
- ✅ Pandas 2.3.3
- ✅ NumPy 2.1.3
- ✅ Matplotlib 3.10.0
- ✅ Seaborn 0.13.2
- ✅ Plotly 6.3.1
- ✅ Jupyter Notebook/Lab
- ✅ Streamlit 1.50.0
- ✅ ydata-profiling 4.17.0

---

## 🎯 Comandos Esenciales

### 1. Activar el Entorno

```bash
# Desde el directorio raíz del proyecto
source venv/bin/activate.fish

# Deberías ver (venv) en tu prompt
```

**Atajo rápido:**
```bash
source activate.fish  # Script personalizado
```

### 2. Verificar Instalación

```bash
python -c "import pandas, numpy, matplotlib, seaborn; print('✅ Todo OK')"
```

### 3. Iniciar Jupyter Notebook

```bash
# Con el entorno activado
jupyter notebook

# Se abrirá automáticamente en http://localhost:8888
```

**Importante:** Al crear un notebook, selecciona el kernel **"Python (COVID-19 Analysis)"**

### 4. Ejecutar un Notebook Específico

```bash
cd notebooks
jupyter notebook Etapa1.ipynb
```

### 5. Iniciar Dashboard de Streamlit

```bash
cd dashboard
streamlit run app.py

# Se abrirá en http://localhost:8501
```

### 6. Desactivar el Entorno

```bash
deactivate
```

---

## 📓 Trabajar con Notebooks

### Crear un Nuevo Notebook

1. Activar entorno: `source venv/bin/activate.fish`
2. Iniciar Jupyter: `jupyter notebook`
3. En el navegador: New → Python (COVID-19 Analysis)

### Imports Básicos en Notebooks

```python
# Celda 1: Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Configuración
%matplotlib inline
pd.set_option('display.max_columns', None)
sns.set_style('darkgrid')

print("✅ Librerías cargadas correctamente")
```

### Imports de Módulos del Proyecto

```python
# Importar funciones personalizadas
import sys
sys.path.append('..')

from src import data_processing, analysis, visualization
```

---

## 🔧 Solución de Problemas

### El entorno no se activa

```bash
# Verificar que existe
ls venv/

# Recrear si es necesario
python -m venv venv
source venv/bin/activate.fish
pip install -r requirements.txt
```

### Jupyter no encuentra el kernel

```bash
# Reinstalar el kernel
python -m ipykernel install --user --name covid19-analysis --display-name "Python (COVID-19 Analysis)"
```

### Error al importar librerías

```bash
# Verificar que el entorno está activado
which python
# Debería mostrar: .../venv/bin/python

# Reinstalar paquete específico
pip install --upgrade nombre-paquete
```

### Jupyter no inicia

```bash
# Instalar jupyter en el entorno
pip install jupyter notebook

# Verificar instalación
jupyter --version
```

---

## 📊 Comandos Útiles para Desarrollo

### Ver paquetes instalados

```bash
pip list
```

### Buscar un paquete específico

```bash
pip list | grep pandas
```

### Actualizar un paquete

```bash
pip install --upgrade pandas
```

### Instalar paquete adicional

```bash
pip install nombre-paquete

# Actualizar requirements.txt
pip freeze > requirements.txt
```

### Verificar versiones

```bash
python -c "import pandas; print(pandas.__version__)"
```

---

## 🎨 Configuración de Jupyter

### Extensiones Recomendadas (Opcional)

```bash
# Table of Contents
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# Variable Inspector
jupyter nbextension enable varInspector/main
```

### Temas de Jupyter (Opcional)

```bash
pip install jupyterthemes

# Tema oscuro
jt -t onedork -fs 11 -altp -tfs 11 -nfs 115 -cellw 88% -T
```

---

## 💾 Exportar Notebook a otros formatos

### A HTML

```bash
jupyter nbconvert --to html notebook.ipynb
```

### A PDF (requiere LaTeX)

```bash
jupyter nbconvert --to pdf notebook.ipynb
```

### A Python Script

```bash
jupyter nbconvert --to script notebook.ipynb
```

---

## 🚀 Workflow Recomendado

### Para cada sesión de trabajo:

1. **Activar entorno**
   ```bash
   cd /ruta/proyecto
   source venv/bin/activate.fish
   ```

2. **Iniciar Jupyter**
   ```bash
   jupyter notebook
   ```

3. **Trabajar en notebooks**
   - Ejecutar celdas con Shift+Enter
   - Guardar frecuentemente (Ctrl+S)
   - Restart Kernel si hay problemas

4. **Commit de cambios**
   ```bash
   git add notebooks/
   git commit -m "feat: agregar análisis X"
   git push
   ```

5. **Desactivar entorno**
   ```bash
   deactivate
   ```

---

## 📚 Recursos Adicionales

- **Pandas:** https://pandas.pydata.org/docs/
- **NumPy:** https://numpy.org/doc/
- **Matplotlib:** https://matplotlib.org/stable/gallery/
- **Seaborn:** https://seaborn.pydata.org/examples/
- **Plotly:** https://plotly.com/python/
- **Jupyter:** https://jupyter-notebook.readthedocs.io/

---

## ⚡ Tips de Productividad

1. **Usa atajos de teclado en Jupyter:**
   - `Shift+Enter`: Ejecutar celda
   - `A`: Insertar celda arriba
   - `B`: Insertar celda abajo
   - `DD`: Eliminar celda
   - `M`: Cambiar a Markdown
   - `Y`: Cambiar a Code

2. **Magic commands útiles:**
   ```python
   %timeit  # Medir tiempo de ejecución
   %pwd     # Directorio actual
   %ls      # Listar archivos
   %matplotlib inline  # Mostrar gráficos
   %%time   # Tiempo de toda la celda
   ```

3. **Recargar módulos automáticamente:**
   ```python
   %load_ext autoreload
   %autoreload 2
   ```

---

**¡Tu entorno está listo para trabajar! 🎉**

Si tienes algún problema, consulta la sección de Solución de Problemas o revisa los archivos README del proyecto.
