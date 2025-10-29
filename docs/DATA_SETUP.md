# Descargar datos JHU CSSE (automático)

Este proyecto usa los datos de JHU CSSE. Para facilitar reproducibilidad, incluimos un script que descarga y deja los datos locales en `data/raw/COVID-19`.

Pasos rápidos (después de clonar este repo):

1. Ejecutar (modo clonación shallow, recomendado):

```fish
./scripts/fetch_jhu_data.sh clone
```

2. Alternativa (descargar ZIP sin crear `.git`):

```fish
./scripts/fetch_jhu_data.sh zip
```

Qué hace el script:
- Si `data/raw/COVID-19/csse_covid_19_data` ya existe, no hace nada.
- En modo `clone` realiza `git clone --depth 1` (rápido). Puedes eliminar el directorio `.git` para ahorrar espacio con:

```fish
rm -rf data/raw/COVID-19/.git
```

- En modo `zip` descarga el ZIP del repo y extrae los archivos sin crear metadata Git.

Rutas útiles después de la descarga:

- `data/raw/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/`  — CSV diarios
- `data/raw/COVID-19/csse_covid_19_data/csse_covid_19_time_series/`  — time series (3 archivos: confirmed, deaths, recovered)

Recomendación: Añade `data/raw/` a `.gitignore` (ya se agregó en el proyecto) para evitar subir datos pesados.
