"""
Módulo de procesamiento de datos

Este módulo contiene funciones para la limpieza, transformación y
preparación de datos epidemiológicos de COVID-19.
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Optional
from pathlib import Path


def load_covid_data(filepath: str) -> pd.DataFrame:
    """
    Carga un archivo CSV de datos COVID-19.
    
    Args:
        filepath: Ruta al archivo CSV
        
    Returns:
        DataFrame con los datos cargados
    """
    return pd.read_csv(filepath)


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Estandariza los nombres de columnas a formato snake_case.
    
    Args:
        df: DataFrame con columnas a estandarizar
        
    Returns:
        DataFrame con nombres de columnas estandarizados
    """
    df_clean = df.copy()
    df_clean.columns = (
        df_clean.columns
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('/', '_')
        .str.replace('-', '_')
    )
    return df_clean


def standardize_country_names(df: pd.DataFrame, 
                              country_column: str = 'country_region') -> pd.DataFrame:
    """
    Homogeneiza nombres de países según convenciones estándar.
    
    Args:
        df: DataFrame con columna de países
        country_column: Nombre de la columna de países
        
    Returns:
        DataFrame con nombres de países estandarizados
    """
    df_clean = df.copy()
    
    # Diccionario de mapeo de nombres
    country_mapping = {
        'US': 'United States',
        'UK': 'United Kingdom',
        'Korea, South': 'South Korea',
        # Agregar más mapeos según sea necesario
    }
    
    df_clean[country_column] = df_clean[country_column].replace(country_mapping)
    return df_clean


def convert_date_format(df: pd.DataFrame, 
                       date_column: str = 'last_update') -> pd.DataFrame:
    """
    Convierte columna de fecha al formato YYYY-MM-DD.
    
    Args:
        df: DataFrame con columna de fecha
        date_column: Nombre de la columna de fecha
        
    Returns:
        DataFrame con fecha en formato estandarizado
    """
    df_clean = df.copy()
    df_clean[date_column] = pd.to_datetime(df_clean[date_column]).dt.strftime('%Y-%m-%d')
    return df_clean


def create_active_cases_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea columna de casos activos (Confirmed - Deaths - Recovered).
    
    Args:
        df: DataFrame con columnas confirmed, deaths, recovered
        
    Returns:
        DataFrame con columna active_cases
    """
    df_clean = df.copy()
    df_clean['active_cases'] = (
        df_clean.get('confirmed', 0) - 
        df_clean.get('deaths', 0) - 
        df_clean.get('recovered', 0)
    )
    # Asegurar que no haya valores negativos
    df_clean['active_cases'] = df_clean['active_cases'].clip(lower=0)
    return df_clean


def remove_irrelevant_columns(df: pd.DataFrame, 
                              columns_to_remove: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Elimina columnas irrelevantes del DataFrame.
    
    Args:
        df: DataFrame original
        columns_to_remove: Lista de columnas a eliminar
        
    Returns:
        DataFrame sin las columnas especificadas
    """
    if columns_to_remove is None:
        # Columnas típicamente irrelevantes
        columns_to_remove = ['fips', 'admin2', 'combined_key']
    
    df_clean = df.copy()
    columns_to_remove = [col for col in columns_to_remove if col in df_clean.columns]
    df_clean = df_clean.drop(columns=columns_to_remove)
    return df_clean


def detect_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Detecta y resume valores faltantes por columna.
    
    Args:
        df: DataFrame a analizar
        
    Returns:
        DataFrame con resumen de valores faltantes
    """
    missing_summary = pd.DataFrame({
        'columna': df.columns,
        'valores_nulos': df.isnull().sum(),
        'porcentaje': (df.isnull().sum() / len(df) * 100).round(2)
    })
    return missing_summary[missing_summary['valores_nulos'] > 0]


def save_processed_data(df: pd.DataFrame, 
                       output_path: str,
                       show_size: bool = True) -> None:
    """
    Guarda el DataFrame procesado y muestra su tamaño.
    
    Args:
        df: DataFrame a guardar
        output_path: Ruta del archivo de salida
        show_size: Si se debe mostrar el tamaño del archivo
    """
    df.to_csv(output_path, index=False)
    
    if show_size:
        size_mb = Path(output_path).stat().st_size / (1024 * 1024)
        print(f"Archivo guardado: {output_path}")
        print(f"Tamaño: {size_mb:.2f} MB")
