"""
Módulo de visualización de datos

Este módulo contiene funciones para crear visualizaciones
de datos epidemiológicos de COVID-19.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from typing import List, Optional, Tuple


# Configuración de estilo por defecto
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")


def plot_time_series(df: pd.DataFrame, 
                    x_column: str = 'date',
                    y_columns: List[str] = None,
                    title: str = 'Evolución Temporal de COVID-19',
                    figsize: Tuple[int, int] = (14, 6)) -> None:
    """
    Crea un gráfico de líneas para evolución temporal.
    
    Args:
        df: DataFrame con datos temporales
        x_column: Columna de fechas
        y_columns: Lista de columnas a graficar
        title: Título del gráfico
        figsize: Tamaño de la figura
    """
    if y_columns is None:
        y_columns = ['confirmed', 'deaths', 'recovered', 'active_cases']
    
    fig, ax = plt.subplots(figsize=figsize)
    
    for col in y_columns:
        if col in df.columns:
            ax.plot(df[x_column], df[col], label=col.replace('_', ' ').title(), linewidth=2)
    
    ax.set_xlabel('Fecha', fontsize=12)
    ax.set_ylabel('Número de Casos', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend(loc='best', fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_top_countries_bar(df: pd.DataFrame,
                          country_column: str = 'country_region',
                          value_column: str = 'confirmed',
                          n: int = 10,
                          title: str = 'Top 10 Países con Más Casos',
                          figsize: Tuple[int, int] = (12, 6)) -> None:
    """
    Crea un gráfico de barras para top N países.
    
    Args:
        df: DataFrame con datos
        country_column: Columna de países
        value_column: Columna de valores a graficar
        n: Número de países a mostrar
        title: Título del gráfico
        figsize: Tamaño de la figura
    """
    top_data = (df.groupby(country_column)[value_column]
                .sum()
                .sort_values(ascending=True)
                .tail(n))
    
    fig, ax = plt.subplots(figsize=figsize)
    colors = sns.color_palette('viridis', n)
    
    top_data.plot(kind='barh', ax=ax, color=colors)
    ax.set_xlabel(value_column.replace('_', ' ').title(), fontsize=12)
    ax.set_ylabel('País', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    
    # Agregar valores en las barras
    for i, v in enumerate(top_data.values):
        ax.text(v, i, f' {v:,.0f}', va='center', fontsize=10)
    
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame,
                            columns: Optional[List[str]] = None,
                            title: str = 'Matriz de Correlación',
                            figsize: Tuple[int, int] = (10, 8)) -> None:
    """
    Crea un heatmap de correlaciones.
    
    Args:
        df: DataFrame con datos
        columns: Columnas a incluir en la correlación
        title: Título del gráfico
        figsize: Tamaño de la figura
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    corr_matrix = df[columns].corr()
    
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(corr_matrix, 
                annot=True, 
                fmt='.2f', 
                cmap='coolwarm', 
                center=0,
                square=True,
                linewidths=1,
                cbar_kws={"shrink": 0.8},
                ax=ax)
    
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.show()


def plot_scatter_with_regression(df: pd.DataFrame,
                                 x_column: str,
                                 y_column: str,
                                 title: str = 'Análisis de Correlación',
                                 figsize: Tuple[int, int] = (10, 6)) -> None:
    """
    Crea un gráfico de dispersión con línea de regresión.
    
    Args:
        df: DataFrame con datos
        x_column: Columna para eje X
        y_column: Columna para eje Y
        title: Título del gráfico
        figsize: Tamaño de la figura
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Gráfico de dispersión
    ax.scatter(df[x_column], df[y_column], alpha=0.6, s=50)
    
    # Línea de regresión
    z = np.polyfit(df[x_column], df[y_column], 1)
    p = np.poly1d(z)
    ax.plot(df[x_column], p(df[x_column]), "r--", linewidth=2, label='Regresión lineal')
    
    # Calcular R²
    correlation = df[[x_column, y_column]].corr().iloc[0, 1]
    ax.text(0.05, 0.95, f'Correlación: {correlation:.3f}', 
            transform=ax.transAxes, 
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    ax.set_xlabel(x_column.replace('_', ' ').title(), fontsize=12)
    ax.set_ylabel(y_column.replace('_', ' ').title(), fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_interactive_map(df: pd.DataFrame,
                        country_column: str = 'country_region',
                        value_column: str = 'confirmed',
                        title: str = 'Distribución Global de Casos COVID-19') -> go.Figure:
    """
    Crea un mapa interactivo con Plotly.
    
    Args:
        df: DataFrame con datos
        country_column: Columna de países
        value_column: Columna de valores a visualizar
        title: Título del mapa
        
    Returns:
        Figura de Plotly
    """
    country_data = df.groupby(country_column)[value_column].sum().reset_index()
    
    fig = px.choropleth(country_data,
                        locations=country_column,
                        locationmode='country names',
                        color=value_column,
                        hover_name=country_column,
                        color_continuous_scale='Reds',
                        title=title)
    
    fig.update_layout(
        geo=dict(showframe=False, showcoastlines=True, projection_type='equirectangular'),
        height=600
    )
    
    return fig


def plot_mortality_rate_comparison(df: pd.DataFrame,
                                   n: int = 10,
                                   figsize: Tuple[int, int] = (12, 6)) -> None:
    """
    Crea un gráfico comparativo de tasas de letalidad.
    
    Args:
        df: DataFrame con datos de mortality_rate
        n: Número de países a mostrar
        figsize: Tamaño de la figura
    """
    top_mortality = df.nlargest(n, 'mortality_rate')
    
    fig, ax = plt.subplots(figsize=figsize)
    colors = sns.color_palette('Reds_r', n)
    
    ax.barh(top_mortality['country_region'], 
            top_mortality['mortality_rate'],
            color=colors)
    
    ax.set_xlabel('Tasa de Letalidad (%)', fontsize=12)
    ax.set_ylabel('País', fontsize=12)
    ax.set_title(f'Top {n} Países con Mayor Tasa de Letalidad', 
                 fontsize=14, fontweight='bold')
    
    # Agregar valores en las barras
    for i, (country, rate) in enumerate(zip(top_mortality['country_region'], 
                                            top_mortality['mortality_rate'])):
        ax.text(rate, i, f' {rate:.2f}%', va='center', fontsize=10)
    
    plt.tight_layout()
    plt.show()


def create_dashboard_summary_plots(df: pd.DataFrame, 
                                  figsize: Tuple[int, int] = (16, 10)) -> None:
    """
    Crea un resumen de múltiples visualizaciones en un solo layout.
    
    Args:
        df: DataFrame con datos
        figsize: Tamaño de la figura
    """
    fig, axes = plt.subplots(2, 2, figsize=figsize)
    
    # Plot 1: Evolución temporal
    # Plot 2: Top países
    # Plot 3: Correlación
    # Plot 4: Distribución
    
    plt.tight_layout()
    plt.show()
