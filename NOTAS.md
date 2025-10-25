# Notas del Proyecto

## 🚀 Próximos Pasos

### 1. Configuración del Entorno

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Linux/Mac)
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Obtención de Datos

Los datos deben descargarse del repositorio oficial de Johns Hopkins University:
- **URL:** https://github.com/CSSEGISandData/COVID-19
- **Ubicación:** `/csse_covid_19_data/csse_covid_19_daily_reports/`
- **Guardar en:** `data/raw/`

#### Descarga manual:
```bash
# Clonar repositorio de JHU (opcional)
git clone https://github.com/CSSEGISandData/COVID-19.git temp_jhu

# Copiar archivos necesarios
cp temp_jhu/csse_covid_19_data/csse_covid_19_daily_reports/*.csv data/raw/

# Limpiar
rm -rf temp_jhu
```

### 3. Desarrollo por Etapas

#### Etapa 1: Limpieza de Datos (Semana 1)
- [ ] Crear notebook `notebooks/01_limpieza_datos.ipynb`
- [ ] Cargar datos de enero 2020
- [ ] Implementar 10 tareas de limpieza
- [ ] Guardar dataset limpio

#### Etapa 2: Análisis Exploratorio (Semana 2)
- [ ] Crear notebook `notebooks/02_analisis_exploratorio.ipynb`
- [ ] Responder 10 preguntas guiadas
- [ ] Generar reporte de perfilado
- [ ] Documentar insights

#### Etapa 3: Visualizaciones (Semana 3)
- [ ] Crear notebook `notebooks/03_visualizaciones.ipynb`
- [ ] Generar 5 visualizaciones avanzadas
- [ ] Análisis e interpretación

#### Etapa 4: Dashboard (Semana 4)
- [ ] Implementar dashboard en Streamlit
- [ ] Integrar filtros y visualizaciones
- [ ] Testing y refinamiento

#### Etapa 5: Optimización (Transversal)
- [ ] Crear notebook `notebooks/04_optimizacion.ipynb`
- [ ] Implementar mejoras de rendimiento
- [ ] Documentar mejoras

### 4. Documentación

- [ ] Completar README.md con nombres del equipo
- [ ] Documentar funciones en src/
- [ ] Crear informe técnico (PDF)
- [ ] Preparar presentación

### 5. Control de Versiones

```bash
# Commits frecuentes con mensajes descriptivos
git add .
git commit -m "Descripción del cambio"

# Crear ramas para features
git checkout -b feature/nombre-feature

# Antes de subir a GitHub
git remote add origin https://github.com/tu-usuario/covid19-epidemiological-analysis.git
git push -u origin main
```

## 📋 Checklist de Entregables

- [ ] Repositorio GitHub con estructura completa
- [ ] 4 Notebooks ejecutables (01-04)
- [ ] Dashboard funcional en `/dashboard`
- [ ] Datos procesados en `/data/processed`
- [ ] Reporte de perfilado en `/reports`
- [ ] Informe técnico (PDF) en `/reports`
- [ ] README.md completo
- [ ] requirements.txt actualizado

## 💡 Tips

1. **Commits frecuentes:** Hacer commit después de cada tarea completada
2. **Comentarios:** Documentar el código y las decisiones tomadas
3. **Testing:** Verificar que cada notebook se ejecute sin errores
4. **Optimización temprana:** Implementar mejoras desde el inicio
5. **Colaboración:** Usar branches para trabajo en paralelo

## 🔗 Enlaces Útiles

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Streamlit Docs](https://docs.streamlit.io/)
- [JHU COVID-19 Data](https://github.com/CSSEGISandData/COVID-19)

## 👥 Equipo

- **Estudiante 1:** [Nombre] - [Rol]
- **Estudiante 2:** [Nombre] - [Rol]
- **Estudiante 3:** [Nombre] - [Rol]

## 📅 Calendario

| Semana | Etapa | Tareas Principales |
|--------|-------|-------------------|
| 1 | Etapa 1 | Limpieza de datos, estructura inicial |
| 2 | Etapa 2 | Análisis exploratorio, perfilado |
| 3 | Etapa 3 | Visualizaciones avanzadas |
| 4 | Etapa 4-5 | Dashboard, optimización, documentación final |

## 📝 Notas Adicionales

- Los errores de importación en los archivos .py son normales hasta instalar las dependencias
- El .gitignore está configurado para no subir datasets grandes
- Las carpetas data/, reports/ contienen .gitkeep para mantener la estructura
- El dashboard tiene su propio requirements.txt para facilitar el despliegue

---

**Última actualización:** 24 de octubre de 2025
