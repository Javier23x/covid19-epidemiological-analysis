# ✅ Checklist de Desarrollo del Proyecto

## 🎯 Setup Inicial

- [x] Crear estructura de directorios
- [x] Configurar .gitignore
- [x] Crear README.md profesional
- [x] Implementar módulos base (src/)
- [x] Configurar dashboard base
- [x] Inicializar Git
- [x] Realizar commit inicial
- [ ] Crear repositorio en GitHub
- [ ] Conectar repositorio local con GitHub
- [ ] Hacer push inicial
- [ ] Crear entorno virtual
- [ ] Instalar dependencias
- [ ] Descargar datos de JHU

## 📊 Etapa 1: Limpieza de Datos (Semana 1)

### Preparación
- [ ] Descargar archivos CSV de enero 2020
- [ ] Guardar en `data/raw/`
- [ ] Crear notebook `01_limpieza_datos.ipynb`

### Tareas del Notebook
- [ ] 1. Cargar y visualizar primeros 5 registros
- [ ] 2. Mostrar número de filas y columnas
- [ ] 3. Describir tipos de datos (dtypes)
- [ ] 4. Detectar valores nulos/faltantes
- [ ] 5. Eliminar columnas irrelevantes
- [ ] 6. Estandarizar nombres de columnas
- [ ] 7. Homogeneizar nombres de países
- [ ] 8. Convertir columna Last_Update
- [ ] 9. Crear columna active_cases
- [ ] 10. Guardar DataFrame limpio + tamaño en MB

### Validación
- [ ] Notebook se ejecuta sin errores
- [ ] Dataset limpio guardado en `data/processed/`
- [ ] Código comentado y documentado
- [ ] Commit con mensaje descriptivo
- [ ] Push a GitHub

## 📈 Etapa 2: Análisis Exploratorio (Semana 2)

### Preparación
- [ ] Descargar CSVs enero-junio 2020
- [ ] Crear notebook `02_analisis_exploratorio.ipynb`
- [ ] Combinar múltiples archivos CSV

### Preguntas a Responder
- [ ] 1. Top 10 países con más casos confirmados
- [ ] 2. Países con mayor tasa de letalidad
- [ ] 3. Países sin datos de recuperados
- [ ] 4. País latinoamericano con más casos activos (junio)
- [ ] 5. Evolución casos en Chile (gráfico líneas)
- [ ] 6. Fecha con más casos nuevos mundial
- [ ] 7. Correlación confirmados vs fallecidos (dispersión)
- [ ] 8. Top 10 mayor crecimiento mayo-junio
- [ ] 9. Identificar países con rebrote
- [ ] 10. Generar reporte de perfilado automático

### Validación
- [ ] Todas las preguntas respondidas
- [ ] Gráficos claros y bien etiquetados
- [ ] Reporte de perfilado generado (`perfilado.html`)
- [ ] Interpretaciones y conclusiones incluidas
- [ ] Commit y push

## 📊 Etapa 3: Visualizaciones Avanzadas (Semana 3)

### Preparación
- [ ] Descargar datos 2020-2021
- [ ] Crear notebook `03_visualizaciones.ipynb`
- [ ] Optimizar carga de datos (si es necesario)

### Visualizaciones Requeridas
- [ ] 1. Evolución temporal global (líneas)
- [ ] 2. Top 10 países casos confirmados (barras)
- [ ] 3. Heatmap de correlaciones
- [ ] 4. Tasas letalidad por continente (barras horizontales)
- [ ] 5. Mapa/gráfico geográfico por continente

### Validación
- [ ] Mínimo 5 visualizaciones creadas
- [ ] Gráficos de alta calidad
- [ ] Análisis e interpretación por gráfico
- [ ] Código limpio y comentado
- [ ] Commit y push

## 🎨 Etapa 4: Dashboard Interactivo (Semana 4)

### Desarrollo del Dashboard
- [ ] Implementar carga de datos en `dashboard/app.py`
- [ ] Crear filtros (continente, país, fechas)
- [ ] Implementar KPIs principales
- [ ] Tab 1: Evolución temporal
- [ ] Tab 2: Comparativa de países
- [ ] Tab 3: Mapa interactivo
- [ ] Tab 4: Análisis avanzado
- [ ] Sección de insights automáticos
- [ ] Indicador de rebrotes
- [ ] Tasa de crecimiento

### Testing
- [ ] Dashboard se ejecuta sin errores
- [ ] Todos los filtros funcionan
- [ ] Visualizaciones se actualizan correctamente
- [ ] Responsive design
- [ ] Documentar en `dashboard/README.md`

### Validación
- [ ] Dashboard funcional
- [ ] Screenshots en README
- [ ] Video demo (opcional)
- [ ] Commit y push

## ⚡ Etapa 5: Optimización (Transversal)

### Preparación
- [ ] Crear notebook `04_optimizacion.ipynb`
- [ ] Instalar herramientas de benchmarking

### Optimizaciones a Implementar (mínimo 3)
- [ ] 1. Lectura eficiente (chunksize/dask)
- [ ] 2. Conversión de tipos (astype)
- [ ] 3. Uso de índices
- [ ] 4. Operaciones vectorizadas
- [ ] 5. Caché de resultados

### Documentación de Mejoras
- [ ] Medir tiempos ANTES de optimizar
- [ ] Implementar optimizaciones
- [ ] Medir tiempos DESPUÉS de optimizar
- [ ] Documentar uso de memoria (antes/después)
- [ ] Crear gráficos comparativos
- [ ] Análisis de mejoras

### Validación
- [ ] Mínimo 3 optimizaciones implementadas
- [ ] Evidencia documentada (tiempos, memoria)
- [ ] Mejoras aplicadas en todos los notebooks
- [ ] Commit y push

## 📝 Entregables Finales

### Repositorio GitHub
- [ ] Todos los notebooks (01-04)
- [ ] Dashboard funcional
- [ ] Módulos src/ completos
- [ ] Datos procesados (muestras)
- [ ] README.md actualizado
- [ ] requirements.txt actualizado
- [ ] .gitignore apropiado

### Informe Técnico (PDF)
- [ ] Portada con datos del equipo
- [ ] Introducción y objetivos
- [ ] Marco teórico (opcional)
- [ ] Desarrollo Etapa 1
- [ ] Desarrollo Etapa 2
- [ ] Desarrollo Etapa 3
- [ ] Desarrollo Etapa 4
- [ ] Evidencias de optimización (Etapa 5)
- [ ] Resultados y gráficos principales
- [ ] Conclusiones y aprendizajes
- [ ] Bibliografía/Referencias
- [ ] Guardar en `reports/informe_tecnico.pdf`

### Presentación Oral
- [ ] Preparar slides (5-7 minutos)
- [ ] Introducción del proyecto
- [ ] Proceso de limpieza de datos
- [ ] Análisis exploratorio destacado
- [ ] Visualizaciones impactantes
- [ ] Demo del dashboard (en vivo)
- [ ] Optimizaciones realizadas
- [ ] Conclusiones y aprendizajes
- [ ] Ensayar presentación

## 🔍 Control de Calidad

### Code Quality
- [ ] Seguir PEP 8
- [ ] Funciones documentadas (docstrings)
- [ ] Código comentado (partes complejas)
- [ ] No hay código duplicado
- [ ] Variables con nombres descriptivos
- [ ] Funciones modulares y reutilizables

### Documentation
- [ ] README.md completo y claro
- [ ] Cada notebook tiene introducción
- [ ] Conclusiones en cada sección
- [ ] Interpretación de gráficos
- [ ] Instrucciones de instalación claras

### Testing
- [ ] Notebook 01 se ejecuta completo
- [ ] Notebook 02 se ejecuta completo
- [ ] Notebook 03 se ejecuta completo
- [ ] Notebook 04 se ejecuta completo
- [ ] Dashboard se ejecuta sin errores
- [ ] Todos los imports funcionan
- [ ] No hay errores en consola

### Git & GitHub
- [ ] Commits frecuentes
- [ ] Mensajes de commit descriptivos
- [ ] Usar conventional commits
- [ ] Branches para features (opcional)
- [ ] Pull requests revisados (opcional)
- [ ] README con badges actualizado
- [ ] Issues cerrados (si aplica)

## 📅 Timeline Sugerido

### Semana 1 (28 oct - 3 nov)
- [x] Setup inicial y estructura
- [ ] Etapa 1 completa
- [ ] Primera revisión en equipo

### Semana 2 (4 nov - 10 nov)
- [ ] Etapa 2 completa
- [ ] Reporte de perfilado
- [ ] Segunda revisión en equipo

### Semana 3 (11 nov - 17 nov)
- [ ] Etapa 3 completa
- [ ] Comenzar dashboard
- [ ] Tercera revisión en equipo

### Semana 4 (18 nov - 24 nov)
- [ ] Etapa 4 completa
- [ ] Etapa 5 completa
- [ ] Informe técnico
- [ ] Presentación preparada
- [ ] Revisión final
- [ ] **ENTREGA**

## 🎯 Criterios de Éxito

- [ ] Todas las etapas completadas
- [ ] Código limpio y documentado
- [ ] Dashboard funcional e interactivo
- [ ] Optimizaciones evidenciadas
- [ ] Informe técnico profesional
- [ ] Presentación clara y concisa
- [ ] Repositorio GitHub ordenado
- [ ] Trabajo en equipo evidente

## 📞 Contactos de Emergencia

**Profesor:** Lorenzo Paredes Grandón  
**Curso:** Gestión de Datos 2025-II  
**Universidad:** UCSC

**Recursos de ayuda:**
- Stack Overflow
- Pandas Documentation
- GitHub Copilot
- Compañeros de clase

---

## 💡 Tips para el Éxito

1. **Empezar temprano**: No dejar todo para última semana
2. **Commits frecuentes**: Guardar progreso constantemente
3. **Comunicación**: Mantener al equipo informado
4. **División clara**: Cada uno responsable de su parte
5. **Revisión cruzada**: Revisar el código de los demás
6. **Documentar mientras desarrollas**: No dejar documentación para el final
7. **Testing continuo**: Probar cada notebook al terminarlo
8. **Backup**: Tener copias en GitHub y localmente
9. **Tiempo buffer**: Dejar tiempo extra para imprevistos
10. **¡Disfrutar el proceso!**: Es un proyecto real con datos reales

---

**¡Éxito en tu proyecto! 🚀📊🎓**
