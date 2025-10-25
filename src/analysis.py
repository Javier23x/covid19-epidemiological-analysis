"""
Módulo de análisis de datos

Este módulo contiene funciones para realizar análisis estadísticos
y exploratorios sobre datos epidemiológicos de COVID-19.
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Tuple, Optional


def get_top_countries_by_cases(df: pd.DataFrame, 
                               n: int = 10,
                               case_column: str = 'confirmed') -> pd.DataFrame:
    """
    Obtiene los N países con más casos.
    
    Args:
        df: DataFrame con datos de COVID-19
        n: Número de países a retornar
        case_column: Columna de casos a analizar
        
    Returns:
        DataFrame con top N países ordenados por casos
    """
    return (df.groupby('country_region')[case_column]
            .sum()
            .sort_values(ascending=False)
            .head(n)
            .reset_index())


def calculate_mortality_rate(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula la tasa de letalidad (Deaths / Confirmed * 100).
    
    Args:
        df: DataFrame con columnas deaths y confirmed
        
    Returns:
        DataFrame con tasa de letalidad por país
    """
    mortality = (df.groupby('country_region')
                 .agg({'deaths': 'sum', 'confirmed': 'sum'})
                 .reset_index())
    
    mortality['mortality_rate'] = (
        (mortality['deaths'] / mortality['confirmed'] * 100)
        .round(2)
    )
    
    return mortality.sort_values('mortality_rate', ascending=False)


def identify_countries_without_recovered(df: pd.DataFrame) -> List[str]:
    """
    Identifica países que no registran datos de recuperados.
    
    Args:
        df: DataFrame con columna recovered
        
    Returns:
        Lista de países sin datos de recuperados
    """
    recovered_by_country = df.groupby('country_region')['recovered'].sum()
    return recovered_by_country[recovered_by_country == 0].index.tolist()


def get_latin_america_top_active_cases(df: pd.DataFrame) -> pd.DataFrame:
    """
    Obtiene el país latinoamericano con más casos activos.
    
    Args:
        df: DataFrame con datos de COVID-19
        
    Returns:
        DataFrame con países latinoamericanos ordenados por casos activos
    """
    latin_american_countries = [
        'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia',
        'Costa Rica', 'Cuba', 'Ecuador', 'El Salvador', 'Guatemala',
        'Honduras', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay',
        'Peru', 'Dominican Republic', 'Uruguay', 'Venezuela'
    ]
    
    df_latam = df[df['country_region'].isin(latin_american_countries)]
    
    return (df_latam.groupby('country_region')['active_cases']
            .sum()
            .sort_values(ascending=False)
            .reset_index())


def calculate_growth_rate(df: pd.DataFrame, 
                         start_date: str, 
                         end_date: str) -> pd.DataFrame:
    """
    Calcula el crecimiento porcentual de casos entre dos fechas.
    
    Args:
        df: DataFrame con datos de COVID-19
        start_date: Fecha inicial (formato YYYY-MM-DD)
        end_date: Fecha final (formato YYYY-MM-DD)
        
    Returns:
        DataFrame con tasa de crecimiento por país
    """
    df['date'] = pd.to_datetime(df['date'])
    
    start_data = df[df['date'] == start_date].groupby('country_region')['confirmed'].sum()
    end_data = df[df['date'] == end_date].groupby('country_region')['confirmed'].sum()
    
    growth = pd.DataFrame({
        'country_region': start_data.index,
        'start_cases': start_data.values,
        'end_cases': end_data.values
    })
    
    growth['growth_rate'] = (
        ((growth['end_cases'] - growth['start_cases']) / growth['start_cases'] * 100)
        .round(2)
    )
    
    return growth.sort_values('growth_rate', ascending=False)


def identify_rebound_cases(df: pd.DataFrame) -> pd.DataFrame:
    """
    Identifica países con rebrotes (días sin casos seguidos de incremento).
    
    Args:
        df: DataFrame con datos temporales de COVID-19
        
    Returns:
        DataFrame con países que presentan rebrotes
    """
    # Esta es una implementación simplificada
    # Se puede mejorar con lógica más sofisticada
    pass


def calculate_correlation_matrix(df: pd.DataFrame, 
                                 columns: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Calcula matriz de correlación entre variables numéricas.
    
    Args:
        df: DataFrame con datos
        columns: Columnas específicas a correlacionar
        
    Returns:
        Matriz de correlación
    """
    if columns is None:
        columns = ['confirmed', 'deaths', 'recovered', 'active_cases']
    
    return df[columns].corr()


def get_peak_date_global(df: pd.DataFrame) -> Tuple[str, int]:
    """
    Identifica la fecha con más casos nuevos a nivel mundial.
    
    Args:
        df: DataFrame con datos temporales
        
    Returns:
        Tupla con (fecha, número de casos)
    """
    daily_cases = df.groupby('date')['confirmed'].sum()
    peak_idx = daily_cases.idxmax()
    return peak_idx, daily_cases[peak_idx]


def aggregate_by_continent(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega datos por continente.
    
    Args:
        df: DataFrame con datos de COVID-19
        
    Returns:
        DataFrame agregado por continente
    """
    # Mapeo básico de países a continentes
    # En producción, usar una librería como pycountry-convert
    continent_mapping = {
        'United States': 'America',
        'Brazil': 'America',
        'India': 'Asia',
        'China': 'Asia',
        'Spain': 'Europe',
        'Italy': 'Europe',
        # Agregar más mapeos según sea necesario
    }
    
    df['continent'] = df['country_region'].map(continent_mapping).fillna('Other')
    
    return (df.groupby('continent')
            .agg({
                'confirmed': 'sum',
                'deaths': 'sum',
                'recovered': 'sum',
                'active_cases': 'sum'
            })
            .reset_index())
