# COVID-19 Dashboard Interactivo

Dashboard interactivo para la exploración y análisis de datos epidemiológicos de COVID-19.

## 📊 Características

- **Filtros dinámicos:** Por continente, país y rango de fechas
- **Indicadores principales:** Casos confirmados, activos, recuperados y fallecidos
- **Visualizaciones interactivas:** Gráficos que se actualizan según filtros
- **Análisis de tendencias:** Identificación de rebrotes y tasas de crecimiento
- **Insights automáticos:** Conclusiones generadas dinámicamente

## 🚀 Instalación

1. Asegúrate de tener instaladas las dependencias del proyecto principal:
```bash
pip install -r ../requirements.txt
```

2. Instala las dependencias específicas del dashboard (si las hay):
```bash
pip install -r requirements.txt
```

## 💻 Uso

Para ejecutar el dashboard localmente:

```bash
streamlit run app.py
```

El dashboard se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 🎯 Funcionalidades

### Panel Principal

- **KPIs Globales:** Resumen de casos a nivel mundial
- **Filtros de Búsqueda:**
  - Selector de continente
  - Selector múltiple de países
  - Selector de rango de fechas

### Visualizaciones

1. **Evolución Temporal:** Gráfico de líneas con evolución de casos
2. **Comparativa de Países:** Gráficos de barras comparativos
3. **Mapa Interactivo:** Distribución geográfica de casos
4. **Análisis de Tendencias:** Tasas de crecimiento y rebrotes

### Insights

- Detección automática de tendencias
- Identificación de países con mayor crecimiento
- Alertas de rebrotes
- Análisis de tasas de letalidad

## 🛠️ Estructura de Archivos

```
dashboard/
├── app.py              # Aplicación principal de Streamlit
├── requirements.txt    # Dependencias específicas
├── README.md          # Este archivo
└── utils/             # Funciones auxiliares (opcional)
    ├── __init__.py
    ├── data_loader.py
    └── plots.py
```

## 📝 Configuración

Puedes personalizar el dashboard editando los siguientes parámetros en `app.py`:

- Tema de colores
- Rango de fechas por defecto
- Métricas a mostrar
- Tipos de gráficos

## 🐛 Solución de Problemas

### El dashboard no carga los datos

- Verifica que los archivos procesados estén en `/data/processed/`
- Asegúrate de haber ejecutado los notebooks de procesamiento previos

### Errores de memoria

- Reduce el rango de fechas seleccionado
- Usa datos agregados en lugar de datos diarios completos

### Gráficos no se actualizan

- Recarga la página (F5)
- Limpia el caché de Streamlit (opción en menú hamburguesa)

## 📚 Recursos

- [Documentación de Streamlit](https://docs.streamlit.io/)
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## 👥 Autores

[Equipo del Proyecto]

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](../LICENSE) para más detalles.
