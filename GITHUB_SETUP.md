# 🚀 Instrucciones para subir a GitHub

## Paso 1: Crear repositorio en GitHub

1. Ve a [GitHub](https://github.com) e inicia sesión
2. Haz clic en el botón "+" (arriba a la derecha) y selecciona "New repository"
3. Configura el repositorio:
   - **Repository name:** `covid19-epidemiological-analysis`
   - **Description:** Análisis y Visualización de Tendencias Epidemiológicas Globales - COVID-19
   - **Visibility:** Public (o Private según preferencias)
   - **NO marcar** "Initialize this repository with:"
     - ❌ NO agregar README
     - ❌ NO agregar .gitignore
     - ❌ NO agregar license
   - (Ya tenemos estos archivos en nuestro proyecto)
4. Haz clic en "Create repository"

## Paso 2: Conectar el repositorio local con GitHub

Después de crear el repositorio, GitHub te mostrará instrucciones. Usa las siguientes (reemplaza `TU-USUARIO` con tu nombre de usuario de GitHub):

```bash
# Agregar el remote de GitHub
git remote add origin https://github.com/TU-USUARIO/covid19-epidemiological-analysis.git

# Verificar que se agregó correctamente
git remote -v
```

## Paso 3: Subir el código a GitHub

```bash
# Subir la rama main a GitHub
git push -u origin main
```

Si es la primera vez que usas GitHub desde esta máquina, te pedirá autenticación:
- **Opción 1:** Personal Access Token (recomendado)
- **Opción 2:** SSH key

### Configuración de Personal Access Token (si es necesario)

1. Ve a GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generar nuevo token con permisos de `repo`
3. Copia el token y úsalo como contraseña cuando hagas push

### Configuración de SSH (alternativa)

```bash
# Generar SSH key (si no tienes una)
ssh-keygen -t ed25519 -C "tu-email@ejemplo.com"

# Copiar la clave pública
cat ~/.ssh/id_ed25519.pub

# Agregar la clave en GitHub Settings → SSH and GPG keys → New SSH key

# Cambiar remote a SSH
git remote set-url origin git@github.com:TU-USUARIO/covid19-epidemiological-analysis.git
```

## Paso 4: Verificar que se subió correctamente

1. Ve a `https://github.com/TU-USUARIO/covid19-epidemiological-analysis`
2. Deberías ver todos tus archivos y la estructura del proyecto
3. El README.md se mostrará automáticamente en la página principal

## 📝 Comandos Git útiles para el proyecto

### Workflow diario

```bash
# Ver estado actual
git status

# Ver cambios
git diff

# Agregar archivos modificados
git add .

# Hacer commit
git commit -m "tipo: descripción del cambio"

# Subir cambios a GitHub
git push

# Ver historial de commits
git log --oneline --graph
```

### Tipos de commits (Conventional Commits)

- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Cambios en documentación
- `style:` Cambios de formato (no afectan código)
- `refactor:` Refactorización de código
- `test:` Agregar o modificar tests
- `chore:` Tareas de mantenimiento

**Ejemplos:**
```bash
git commit -m "feat: agregar función de limpieza de datos"
git commit -m "docs: actualizar README con instrucciones de instalación"
git commit -m "fix: corregir cálculo de tasa de letalidad"
```

### Trabajar con branches

```bash
# Crear y cambiar a una nueva rama
git checkout -b feature/nombre-feature

# Ver ramas disponibles
git branch

# Cambiar de rama
git checkout main

# Fusionar rama en main
git checkout main
git merge feature/nombre-feature

# Subir rama a GitHub
git push -u origin feature/nombre-feature
```

## 🎯 Próximos commits sugeridos

Después del commit inicial, tu workflow podría ser:

1. **Etapa 1 - Limpieza de Datos**
   ```bash
   git commit -m "feat: agregar notebook 01_limpieza_datos.ipynb"
   git commit -m "feat: implementar funciones de limpieza en data_processing.py"
   git commit -m "docs: agregar análisis de valores nulos en notebook 01"
   ```

2. **Etapa 2 - Análisis Exploratorio**
   ```bash
   git commit -m "feat: agregar notebook 02_analisis_exploratorio.ipynb"
   git commit -m "feat: implementar cálculo de tasas de letalidad"
   git commit -m "docs: agregar reporte de perfilado"
   ```

3. Y así sucesivamente...

## ⚠️ Importante

### Antes de cada push:

```bash
# 1. Ver qué archivos has modificado
git status

# 2. Ver los cambios específicos
git diff

# 3. Agregar solo los archivos relevantes
git add archivo1.py archivo2.ipynb

# 4. Hacer commit descriptivo
git commit -m "tipo: descripción clara"

# 5. Subir a GitHub
git push
```

### No subir archivos grandes

El `.gitignore` ya está configurado para ignorar:
- Datasets CSV grandes
- Reportes HTML/PDF pesados
- Archivos de entornos virtuales
- Archivos temporales

Si necesitas compartir archivos grandes:
- Usa GitHub Releases
- Usa Git LFS (Large File Storage)
- Documenta dónde descargarlos en el README

## 🔍 Verificar antes de finalizar

- [ ] README.md tiene información completa del equipo
- [ ] Todos los notebooks se ejecutan sin errores
- [ ] El dashboard funciona correctamente
- [ ] La documentación está actualizada
- [ ] No hay datos sensibles en el repositorio
- [ ] Los archivos grandes están en .gitignore
- [ ] El informe técnico está en /reports

## 📞 Ayuda

Si tienes problemas:
1. Revisa la [documentación de Git](https://git-scm.com/doc)
2. Usa `git --help` o `git <comando> --help`
3. Consulta [GitHub Docs](https://docs.github.com)

---

**¡Tu proyecto está listo para ser compartido con el mundo! 🎉**
