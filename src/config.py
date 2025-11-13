"""
Configuración centralizada para el proyecto de análisis COVID-19

Este archivo contiene configuraciones compartidas entre todas las etapas:
- Mapeo de nombres de países
- Rutas de datos
- Configuraciones generales
"""

import os

# ============================================================================
# MAPEO DE NOMBRES DE PAÍSES
# ============================================================================
# Diccionario para homogeneizar variantes de nombres de países
# Formato: 'Nombre en datos originales': 'Nombre estandarizado'
COUNTRY_MAPPING = {
    # America
    'US': 'United States',
    'USA': 'United States',
    
    # Asia
    'Taiwan*': 'Taiwan',
    'Mainland China': 'China',
    'Burma': 'Myanmar',
    'East Timor': 'Timor-Leste',
    'Korea, South': 'South Korea',
    'Korea, North': 'North Korea',
    'West Bank and Gaza': 'Palestine',
    
    # África
    'Cape Verde': 'Cabo Verde',
    'Congo (Brazzaville)': 'Republic of the Congo',
    'Congo (Kinshasa)': 'Democratic Republic of the Congo',
    'Swaziland': 'Eswatini',
    'Gambia, The': 'Gambia',
    
    # Europa
    'Czechia': 'Czech Republic',
    'Holy See': 'Vatican City',
    'North Macedonia': 'Macedonia',
    'UK': 'United Kingdom',
    ' Azerbaijan': 'Azerbaijan',
    'Macedonia': 'North Macedonia',
        
    # Oceanía
    'Bahamas, The': 'Bahamas',
}

# ============================================================================
# RUTAS DE DATOS
# ============================================================================
# Directorio base del proyecto (asumiendo que config.py está en src/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ruta a los datos locales del repositorio COVID-19
DATA_RAW_COVID = os.path.join(BASE_DIR, 'data', 'raw', 'COVID-19', 'csse_covid_19_data', 'csse_covid_19_daily_reports')

# Ruta al archivo de mapeo de continentes
CONTINENT_MAPPING_FILE = os.path.join(BASE_DIR, 'data', 'country_to_continent.csv')

# Directorio para datos procesados
DATA_PROCESSED = os.path.join(BASE_DIR, 'data', 'processed')

# Directorio para reportes
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')

# ============================================================================
# CONFIGURACIONES GENERALES
# ============================================================================
# Columnas a eliminar en la limpieza de datos
COLUMNS_TO_DROP = ['fips', 'admin2', 'lat', 'long_', 'latitude', 'longitude', 'combined_key']

# Columnas numéricas para convertir
NUMERIC_COLUMNS = ['confirmed', 'deaths', 'recovered']

# Formato de fecha para archivos CSV de JHU
DATE_FORMAT = '%m-%d-%Y'  # MM-DD-YYYY

# ============================================================================
# FUNCIONES DE PROCESAMIENTO DE DATOS
# ============================================================================

import pandas as pd
import numpy as np


def load_daily_reports(start_date, end_date, data_dir=None, progress_interval=50):
    """
    Carga archivos CSV diarios del repositorio JHU COVID-19 para un rango de fechas.
    
    Args:
        start_date (str): Fecha inicial en formato 'YYYY-MM-DD'
        end_date (str): Fecha final en formato 'YYYY-MM-DD'
        data_dir (str, optional): Ruta al directorio de datos. Si es None, usa DATA_RAW_COVID
        progress_interval (int): Cada cuántos archivos mostrar progreso
    
    Returns:
        pd.DataFrame: DataFrame consolidado con todos los datos del período
    """
    if data_dir is None:
        data_dir = DATA_RAW_COVID
    
    # Generar rango de fechas
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Lista temporal para acumular los DataFrames
    dfs = []
    
    print("Cargando datos desde archivos locales...")
    print(f"{'='*60}")
    print(f"Período: {start_date} → {end_date}")
    print(f"Total de archivos a cargar: {len(dates)}")
    print(f"{'='*60}\n")
    
    # Leer cada archivo CSV diario
    for i, date in enumerate(dates, 1):
        filename = date.strftime(DATE_FORMAT) + '.csv'
        filepath = os.path.join(data_dir, filename)
        
        if not os.path.exists(filepath):
            print(f"⚠ Archivo no encontrado: {filename}")
            continue
        
        try:
            df = pd.read_csv(filepath)
            df.columns = df.columns.str.strip()
            
            # Normalizar nombres de columnas para compatibilidad
            if 'Province/State' in df.columns:
                df.rename(columns={'Province/State': 'Province_State'}, inplace=True)
            if 'Country/Region' in df.columns:
                df.rename(columns={'Country/Region': 'Country_Region'}, inplace=True)
            if 'Province_State' not in df.columns:
                df['Province_State'] = np.nan
            if 'Country_Region' not in df.columns and 'Country' in df.columns:
                df.rename(columns={'Country': 'Country_Region'}, inplace=True)
            
            df['Date'] = date
            dfs.append(df)
            
            # Mostrar progreso
            if i % progress_interval == 0:
                print(f"✓ Cargados {i}/{len(dates)} archivos ({i/len(dates)*100:.1f}%)")
                
        except Exception as e:
            print(f"✗ Error en {filename}: {e}")
    
    # Concatenar todos los DataFrames
    if dfs:
        df_consolidated = pd.concat(dfs, ignore_index=True)
        print(f"\n{'='*60}")
        print(f"✓ Cargados {len(dfs)} archivos diarios")
        print(f"✓ Total de registros: {len(df_consolidated):,}")
        print(f"✓ Período: {df_consolidated['Date'].min().date()} → {df_consolidated['Date'].max().date()}")
        print(f"{'='*60}")
        return df_consolidated
    else:
        print("\n⚠ No se cargó ningún archivo.")
        print("Ejecuta: ./scripts/fetch_jhu_data.sh clone")
        return pd.DataFrame()


def standardize_column_names(df):
    """
    Estandariza nombres de columnas a formato snake_case.
    
    Args:
        df (pd.DataFrame): DataFrame a procesar
    
    Returns:
        pd.DataFrame: DataFrame con columnas estandarizadas
    """
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('/', '_').str.replace('-', '_')
    print("✓ Nombres de columnas estandarizados")
    return df


def consolidate_duplicate_columns(df):
    """
    Consolida columnas duplicadas tomando el primer valor no nulo.
    
    Args:
        df (pd.DataFrame): DataFrame con posibles columnas duplicadas
    
    Returns:
        pd.DataFrame: DataFrame con columnas consolidadas
    """
    duplicated_cols = df.columns[df.columns.duplicated()].unique()
    
    if len(duplicated_cols) > 0:
        print(f"⚠ Encontradas columnas duplicadas: {duplicated_cols.tolist()}")
        
        for col_name in duplicated_cols:
            # Obtener todas las columnas con este nombre
            matching_cols = [i for i, c in enumerate(df.columns) if c == col_name]
            
            # Consolidar: tomar el primer valor no nulo de cada fila
            consolidated = df.iloc[:, matching_cols[0]]
            for col_idx in matching_cols[1:]:
                consolidated = consolidated.fillna(df.iloc[:, col_idx])
            
            # Eliminar todas las columnas duplicadas
            df = df.drop(df.columns[matching_cols], axis=1)
            
            # Agregar la columna consolidada
            df[col_name] = consolidated
            print(f"  ✓ '{col_name}' consolidada")
    else:
        print("✓ No hay columnas duplicadas")
    
    return df


def drop_irrelevant_columns(df, columns_to_drop=None):
    """
    Elimina columnas irrelevantes del DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame a procesar
        columns_to_drop (list, optional): Lista de columnas a eliminar. Si es None, usa COLUMNS_TO_DROP
    
    Returns:
        pd.DataFrame: DataFrame sin columnas irrelevantes
    """
    if columns_to_drop is None:
        columns_to_drop = COLUMNS_TO_DROP
    
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])
    print("✓ Columnas irrelevantes eliminadas")
    return df


def process_dates(df):
    """
    Procesa la columna de fechas last_update.
    
    Args:
        df (pd.DataFrame): DataFrame a procesar
    
    Returns:
        pd.DataFrame: DataFrame con fechas procesadas
    """
    if 'last_update' in df.columns:
        df['last_update'] = pd.to_datetime(df['last_update'], errors='coerce')
        print("✓ Fechas procesadas")
    return df


def convert_numeric_columns(df, numeric_columns=None):
    """
    Convierte columnas a tipo numérico.
    
    Args:
        df (pd.DataFrame): DataFrame a procesar
        numeric_columns (list, optional): Lista de columnas numéricas. Si es None, usa NUMERIC_COLUMNS
    
    Returns:
        pd.DataFrame: DataFrame con columnas convertidas
    """
    if numeric_columns is None:
        numeric_columns = NUMERIC_COLUMNS
    
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
    
    print("✓ Columnas numéricas convertidas")
    return df


def calculate_active_cases(df):
    """
    Calcula casos activos (confirmados - fallecidos - recuperados).
    
    Args:
        df (pd.DataFrame): DataFrame con columnas confirmed, deaths, recovered
    
    Returns:
        pd.DataFrame: DataFrame con columna active_cases
    """
    df['active_cases'] = df['confirmed'] - df['deaths'] - df['recovered']
    print("✓ Casos activos calculados")
    return df


def homogenize_country_names(df, country_mapping=None, country_column='country_region'):
    """
    Homogeniza nombres de países usando un mapeo predefinido.
    
    Args:
        df (pd.DataFrame): DataFrame a procesar
        country_mapping (dict, optional): Diccionario de mapeo. Si es None, usa COUNTRY_MAPPING
        country_column (str): Nombre de la columna de países
    
    Returns:
        pd.DataFrame: DataFrame con nombres de países homogeneizados
    """
    if country_mapping is None:
        country_mapping = COUNTRY_MAPPING
    
    if country_column in df.columns:
        df[country_column] = df[country_column].replace(country_mapping)
        print("✓ Nombres de países homogeneizados")
    
    return df


def clean_covid_data(df, verbose=True):
    """
    Pipeline completo de limpieza de datos COVID-19.
    Aplica todas las operaciones de limpieza en secuencia.
    
    Args:
        df (pd.DataFrame): DataFrame crudo a limpiar
        verbose (bool): Si True, muestra mensajes de progreso
    
    Returns:
        pd.DataFrame: DataFrame limpio y procesado
    """
    if verbose:
        print("Iniciando limpieza de datos...\n")
    
    # 1. Estandarizar nombres de columnas
    df = standardize_column_names(df)
    
    # 2. Consolidar columnas duplicadas
    df = consolidate_duplicate_columns(df)
    
    # 3. Eliminar columnas irrelevantes
    df = drop_irrelevant_columns(df)
    
    # 4. Procesar fechas
    df = process_dates(df)
    
    # 5. Convertir columnas numéricas
    df = convert_numeric_columns(df)
    
    # 6. Calcular casos activos
    df = calculate_active_cases(df)
    
    # 7. Homogeneizar nombres de países
    df = homogenize_country_names(df)
    
    if verbose:
        print(f"\n{'='*60}")
        print(f"✓ Dataset limpio: {len(df):,} registros")
        print(f"✓ Columnas: {list(df.columns)}")
        print(f"{'='*60}")
    
    return df


def load_continent_mapping(df, mapping_file=None, country_column='country_region'):
    """
    Carga el mapeo de países a continentes y agrega columna de continente.
    
    Args:
        df (pd.DataFrame): DataFrame con columna de países
        mapping_file (str, optional): Ruta al archivo de mapeo. Si es None, usa CONTINENT_MAPPING_FILE
        country_column (str): Nombre de la columna de países
    
    Returns:
        pd.DataFrame: DataFrame con columna 'continent' agregada
    """
    if mapping_file is None:
        mapping_file = CONTINENT_MAPPING_FILE
    
    try:
        df_continents = pd.read_csv(mapping_file)
        print(f"✓ Mapeo de continentes cargado: {len(df_continents)} países")
        print(f"\nContinentes disponibles: {df_continents['continent'].unique()}")
        
        # Crear diccionario de mapeo
        country_to_continent = dict(zip(df_continents['country'], df_continents['continent']))
        
        # Agregar columna de continente
        df['continent'] = df[country_column].map(country_to_continent)
        
        # Verificar países sin mapeo
        unmapped = df[df['continent'].isna()][country_column].unique()
        if len(unmapped) > 0:
            print(f"\n⚠ Países sin mapeo de continente ({len(unmapped)}):")
            print(unmapped[:10])  # Mostrar solo los primeros 10
        else:
            print("\n✓ Todos los países tienen continente asignado")
        
        print(f"\n✓ Distribución por continente:")
        print(df['continent'].value_counts())
        
    except Exception as e:
        print(f"✗ Error al cargar mapeo de continentes: {e}")
        df['continent'] = None
    
    return df
