"""
COVID-19 Dashboard Interactivo

Dashboard principal para visualización y análisis de datos epidemiológicos.
Desarrollado como parte del Proyecto Semestral - Gestión de Datos 2025-II
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import numpy as np
import sys
from pathlib import Path

# Agregar el directorio raíz al path para importar módulos
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

# Importar funciones centralizadas
from src.config import (
    load_daily_reports, 
    clean_covid_data, 
    load_continent_mapping,
    COUNTRY_MAPPING
)


# Configuración de la página
st.set_page_config(
    page_title="COVID-19 Dashboard",
    page_icon="🦠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================================
# FUNCIONES DE CARGA Y PROCESAMIENTO DE DATOS
# ============================================================================

@st.cache_data(show_spinner=False)
def load_complete_dataset(start_date='2020-01-22', end_date='2021-12-31'):
    """
    Carga y procesa el dataset completo de COVID-19.
    
    Args:
        start_date: Fecha de inicio (formato 'YYYY-MM-DD')
        end_date: Fecha de fin (formato 'YYYY-MM-DD')
    
    Returns:
        DataFrame procesado y limpio con datos de COVID-19
    """
    with st.spinner('🔄 Cargando datos...'):
        # Cargar datos usando función centralizada
        df = load_daily_reports(start_date=start_date, end_date=end_date, progress_interval=100)
        
        # Limpiar datos
        df = clean_covid_data(df, verbose=False)
        
        # Cargar mapeo de continentes
        df = load_continent_mapping(df)
        
        return df


@st.cache_data
def get_available_countries(df):
    """Obtiene lista única de países en el dataset."""
    return sorted(df['country_region'].dropna().unique().tolist())


@st.cache_data
def get_available_continents(df):
    """Obtiene lista única de continentes en el dataset."""
    continents = df['continent'].dropna().unique().tolist()
    return ['Todos'] + sorted(continents)


def filter_data(df, continent, countries, date_range):
    """
    Filtra el dataset según los criterios seleccionados.
    
    Args:
        df: DataFrame completo
        continent: Continente seleccionado
        countries: Lista de países seleccionados
        date_range: Tupla (fecha_inicio, fecha_fin)
    
    Returns:
        DataFrame filtrado
    """
    filtered = df.copy()
    
    # Filtrar por continente
    if continent != 'Todos':
        filtered = filtered[filtered['continent'] == continent]
    
    # Filtrar por países
    if countries:
        filtered = filtered[filtered['country_region'].isin(countries)]
    
    # Filtrar por rango de fechas
    filtered = filtered[
        (filtered['date'] >= pd.to_datetime(date_range[0])) &
        (filtered['date'] <= pd.to_datetime(date_range[1]))
    ]
    
    return filtered


def calculate_kpis(df):
    """
    Calcula los indicadores principales (KPIs).
    
    Returns:
        dict con las métricas calculadas
    """
    # Obtener el último día disponible
    latest_data = df[df['date'] == df['date'].max()]
    
    # Sumar totales
    total_confirmed = int(latest_data['confirmed'].sum())
    total_deaths = int(latest_data['deaths'].sum())
    total_recovered = int(latest_data['recovered'].sum())
    total_active = int(latest_data['active_cases'].sum())
    
    # Calcular tasa de letalidad
    fatality_rate = (total_deaths / total_confirmed * 100) if total_confirmed > 0 else 0
    
    # Calcular cambios (comparar con día anterior)
    if len(df['date'].unique()) > 1:
        previous_date = df['date'].unique()[-2]
        previous_data = df[df['date'] == previous_date]
        
        delta_confirmed = total_confirmed - int(previous_data['confirmed'].sum())
        delta_deaths = total_deaths - int(previous_data['deaths'].sum())
        delta_active = total_active - int(previous_data['active_cases'].sum())
    else:
        delta_confirmed = delta_deaths = delta_active = 0
    
    return {
        'total_confirmed': total_confirmed,
        'total_deaths': total_deaths,
        'total_recovered': total_recovered,
        'total_active': total_active,
        'fatality_rate': fatality_rate,
        'delta_confirmed': delta_confirmed,
        'delta_deaths': delta_deaths,
        'delta_active': delta_active
    }


# ============================================================================
# INTERFAZ PRINCIPAL
# ============================================================================



# Título principal
st.title("🦠 COVID-19 Epidemiological Dashboard")
st.markdown("**Análisis Global de Tendencias Epidemiológicas | Johns Hopkins University Data**")
st.markdown("---")


# ============================================================================
# CARGA DE DATOS
# ============================================================================

# Cargar dataset completo (cacheado para mejor rendimiento)
try:
    df_complete = load_complete_dataset(start_date='2020-01-22', end_date='2021-12-31')
    data_loaded = True
except Exception as e:
    st.error(f"❌ Error al cargar datos: {e}")
    st.info("💡 Asegúrate de que los archivos de datos estén en la carpeta correcta.")
    data_loaded = False


# Solo continuar si los datos se cargaron correctamente
if data_loaded:
    
    # ============================================================================
    # SIDEBAR - FILTROS
    # ============================================================================
    
    st.sidebar.header("🔍 Filtros de Búsqueda")
    
    # Obtener opciones disponibles
    available_continents = get_available_continents(df_complete)
    available_countries = get_available_countries(df_complete)
    
    # Filtro de continente
    continent_filter = st.sidebar.selectbox(
        "Seleccionar Continente",
        available_continents,
        index=0
    )
    
    # Filtro de países (multiselect)
    country_filter = st.sidebar.multiselect(
        "Seleccionar Países (opcional)",
        available_countries,
        default=[],
        help="Deja vacío para ver todos los países del continente seleccionado"
    )
    
    # Filtro de rango de fechas
    min_date = df_complete['date'].min().date()
    max_date = df_complete['date'].max().date()
    
    date_range = st.sidebar.date_input(
        "Rango de Fechas",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Validar rango de fechas
    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date = end_date = date_range[0] if date_range else min_date
    
    st.sidebar.markdown("---")
    
    # Información adicional
    st.sidebar.info(f"""
    � **Datos Disponibles**
    - Período: {min_date} a {max_date}
    - Registros: {len(df_complete):,}
    - Países: {len(available_countries)}
    - Continentes: {len(available_continents) - 1}
    """)
    
    
    # ============================================================================
    # APLICAR FILTROS
    # ============================================================================
    
    df_filtered = filter_data(df_complete, continent_filter, country_filter, (start_date, end_date))
    
    # Verificar que hay datos después del filtrado
    if len(df_filtered) == 0:
        st.warning("⚠️ No hay datos disponibles para los filtros seleccionados. Intenta con otros criterios.")
        st.stop()
    
    # Calcular KPIs
    kpis = calculate_kpis(df_filtered)

    
    # ============================================================================
    # KPIs PRINCIPALES
    # ============================================================================
    
    st.header("📊 Indicadores Principales")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            label="🦠 Casos Confirmados",
            value=f"{kpis['total_confirmed']:,}",
            delta=f"{kpis['delta_confirmed']:+,}" if kpis['delta_confirmed'] != 0 else None,
            delta_color="inverse"
        )
    
    with col2:
        st.metric(
            label="🔴 Casos Activos",
            value=f"{kpis['total_active']:,}",
            delta=f"{kpis['delta_active']:+,}" if kpis['delta_active'] != 0 else None,
            delta_color="inverse"
        )
    
    with col3:
        st.metric(
            label="💚 Recuperados",
            value=f"{kpis['total_recovered']:,}",
            delta=None
        )
    
    with col4:
        st.metric(
            label="💀 Fallecidos",
            value=f"{kpis['total_deaths']:,}",
            delta=f"{kpis['delta_deaths']:+,}" if kpis['delta_deaths'] != 0 else None,
            delta_color="inverse"
        )
    
    with col5:
        st.metric(
            label="📉 Tasa de Letalidad",
            value=f"{kpis['fatality_rate']:.2f}%",
            delta=None
        )
    
    st.markdown("---")

    
    # ============================================================================
    # VISUALIZACIONES PRINCIPALES
    # ============================================================================
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📈 Evolución Temporal",
        "🌍 Comparativa de Países",
        "� Mapa de Calor",
        "📊 Análisis Avanzado"
    ])
    
    with tab1:
        st.subheader("📈 Evolución Temporal de Casos")
        
        # Agregar datos por fecha
        evolution_data = df_filtered.groupby('date').agg({
            'confirmed': 'sum',
            'deaths': 'sum',
            'recovered': 'sum',
            'active_cases': 'sum'
        }).reset_index()
        
        # Crear gráfico de líneas múltiples
        fig1 = go.Figure()
        
        fig1.add_trace(go.Scatter(
            x=evolution_data['date'],
            y=evolution_data['confirmed'],
            mode='lines',
            name='Confirmados',
            line=dict(color='#1f77b4', width=2),
            hovertemplate='<b>Confirmados</b><br>Fecha: %{x}<br>Total: %{y:,}<extra></extra>'
        ))
        
        fig1.add_trace(go.Scatter(
            x=evolution_data['date'],
            y=evolution_data['active_cases'],
            mode='lines',
            name='Activos',
            line=dict(color='#ff7f0e', width=2),
            hovertemplate='<b>Activos</b><br>Fecha: %{x}<br>Total: %{y:,}<extra></extra>'
        ))
        
        fig1.add_trace(go.Scatter(
            x=evolution_data['date'],
            y=evolution_data['deaths'],
            mode='lines',
            name='Fallecidos',
            line=dict(color='#d62728', width=2),
            hovertemplate='<b>Fallecidos</b><br>Fecha: %{x}<br>Total: %{y:,}<extra></extra>'
        ))
        
        fig1.update_layout(
            title='Evolución Global de COVID-19',
            xaxis_title='Fecha',
            yaxis_title='Número de Casos',
            hovermode='x unified',
            template='plotly_white',
            height=500,
            legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
        )
        
        st.plotly_chart(fig1, use_container_width=True)
        
        # Estadísticas resumidas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info(f"📅 **Período analizado:** {len(evolution_data)} días")
        with col2:
            peak_date = evolution_data.loc[evolution_data['confirmed'].idxmax(), 'date']
            st.info(f"📈 **Pico de casos:** {peak_date.strftime('%Y-%m-%d')}")
        with col3:
            avg_daily = int(evolution_data['confirmed'].diff().mean())
            st.info(f"📊 **Promedio diario:** {avg_daily:,} casos")
    
    with tab2:
        st.subheader("🌍 Comparativa entre Países")
        
        # Top 10 países por casos confirmados
        top_countries = df_filtered.groupby('country_region')['confirmed'].max().nlargest(10).reset_index()
        
        # Gráfico de barras horizontales
        fig2 = px.bar(
            top_countries,
            x='confirmed',
            y='country_region',
            orientation='h',
            title='Top 10 Países con Más Casos Confirmados',
            labels={'confirmed': 'Casos Confirmados', 'country_region': 'País'},
            color='confirmed',
            color_continuous_scale='Reds',
            text='confirmed'
        )
        
        fig2.update_traces(texttemplate='%{text:,}', textposition='outside')
        fig2.update_layout(
            height=500,
            showlegend=False,
            yaxis={'categoryorder':'total ascending'},
            template='plotly_white'
        )
        
        st.plotly_chart(fig2, use_container_width=True)
        
        # Comparativa de tasas de letalidad
        st.markdown("### 📊 Tasas de Letalidad por País")
        
        latest_by_country = df_filtered[df_filtered['date'] == df_filtered['date'].max()].groupby('country_region').agg({
            'confirmed': 'sum',
            'deaths': 'sum'
        }).reset_index()
        
        latest_by_country['fatality_rate'] = (latest_by_country['deaths'] / latest_by_country['confirmed'] * 100).round(2)
        latest_by_country = latest_by_country[latest_by_country['confirmed'] > 1000].nlargest(10, 'fatality_rate')
        
        fig2b = px.bar(
            latest_by_country,
            x='country_region',
            y='fatality_rate',
            title='Top 10 Países con Mayor Tasa de Letalidad (mínimo 1,000 casos)',
            labels={'fatality_rate': 'Tasa de Letalidad (%)', 'country_region': 'País'},
            color='fatality_rate',
            color_continuous_scale='Oranges',
            text='fatality_rate'
        )
        
        fig2b.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig2b.update_layout(height=400, showlegend=False, template='plotly_white')
        
        st.plotly_chart(fig2b, use_container_width=True)
    
    with tab3:
        st.subheader("🔥 Mapa de Calor - Correlaciones")
        
        # Preparar datos para correlación
        correlation_data = df_filtered.groupby('date').agg({
            'confirmed': 'sum',
            'deaths': 'sum',
            'recovered': 'sum',
            'active_cases': 'sum'
        })
        
        # Calcular matriz de correlación
        corr_matrix = correlation_data.corr()
        
        # Crear heatmap
        fig3 = px.imshow(
            corr_matrix,
            labels=dict(color="Correlación"),
            x=['Confirmados', 'Fallecidos', 'Recuperados', 'Activos'],
            y=['Confirmados', 'Fallecidos', 'Recuperados', 'Activos'],
            color_continuous_scale='RdBu_r',
            aspect='auto',
            title='Matriz de Correlación entre Variables',
            text_auto='.2f'
        )
        
        fig3.update_layout(height=500, template='plotly_white')
        
        st.plotly_chart(fig3, use_container_width=True)
        
        # Análisis de correlaciones
        st.markdown("### 🔍 Análisis de Correlaciones")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success(f"""
            **Correlación Confirmados-Fallecidos:** {corr_matrix.loc['confirmed', 'deaths']:.3f}
            
            Una correlación alta indica que el aumento de casos confirmados 
            está fuertemente asociado con el aumento de fallecidos.
            """)
        
        with col2:
            st.info(f"""
            **Correlación Confirmados-Activos:** {corr_matrix.loc['confirmed', 'active_cases']:.3f}
            
            Muestra la relación entre casos totales y casos activos actuales.
            """)
    
    with tab4:
        st.subheader("📊 Análisis Avanzado - Tendencias y Crecimiento")
        
        # Calcular tasa de crecimiento diaria
        daily_data = df_filtered.groupby('date')['confirmed'].sum().reset_index()
        daily_data['new_cases'] = daily_data['confirmed'].diff().fillna(0)
        daily_data['growth_rate'] = (daily_data['new_cases'] / daily_data['confirmed'].shift(1) * 100).fillna(0)
        
        # Gráfico de nuevos casos diarios
        fig4a = go.Figure()
        
        fig4a.add_trace(go.Bar(
            x=daily_data['date'],
            y=daily_data['new_cases'],
            name='Nuevos Casos Diarios',
            marker_color='indianred',
            hovertemplate='<b>Fecha:</b> %{x}<br><b>Nuevos casos:</b> %{y:,}<extra></extra>'
        ))
        
        fig4a.update_layout(
            title='Nuevos Casos Diarios',
            xaxis_title='Fecha',
            yaxis_title='Nuevos Casos',
            height=400,
            template='plotly_white'
        )
        
        st.plotly_chart(fig4a, use_container_width=True)
        
        # Tasa de crecimiento
        st.markdown("### 📈 Tasa de Crecimiento")
        
        fig4b = go.Figure()
        
        fig4b.add_trace(go.Scatter(
            x=daily_data['date'],
            y=daily_data['growth_rate'],
            mode='lines',
            name='Tasa de Crecimiento',
            line=dict(color='green', width=2),
            fill='tozeroy',
            hovertemplate='<b>Fecha:</b> %{x}<br><b>Tasa:</b> %{y:.2f}%<extra></extra>'
        ))
        
        fig4b.update_layout(
            title='Tasa de Crecimiento Diaria (%)',
            xaxis_title='Fecha',
            yaxis_title='Tasa de Crecimiento (%)',
            height=400,
            template='plotly_white'
        )
        
        st.plotly_chart(fig4b, use_container_width=True)
        
        # Detección de rebrotes
        st.markdown("### ⚠️ Detección de Rebrotes")
        
        # Identificar días con crecimiento significativo
        threshold = daily_data['growth_rate'].quantile(0.9)
        rebrotes = daily_data[daily_data['growth_rate'] > threshold].tail(10)
        
        if len(rebrotes) > 0:
            st.warning(f"Se detectaron **{len(rebrotes)}** días con crecimiento superior al percentil 90 ({threshold:.2f}%)")
            st.dataframe(
                rebrotes[['date', 'new_cases', 'growth_rate']].rename(columns={
                    'date': 'Fecha',
                    'new_cases': 'Nuevos Casos',
                    'growth_rate': 'Tasa de Crecimiento (%)'
                }).tail(5),
                use_container_width=True
            )
        else:
            st.success("✅ No se detectaron rebrotes significativos en el período seleccionado.")

    
    # ============================================================================
    # SECCIÓN DE INSIGHTS AUTOMÁTICOS
    # ============================================================================
    
    st.markdown("---")
    st.header("💡 Insights Automáticos")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🔝 Top 5 Países Afectados")
        
        top5_countries = df_filtered.groupby('country_region')['confirmed'].max().nlargest(5)
        
        for i, (country, cases) in enumerate(top5_countries.items(), 1):
            st.write(f"**{i}.** {country}: **{cases:,}** casos")
    
    with col2:
        st.subheader("📊 Estadísticas Generales")
        
        total_countries = df_filtered['country_region'].nunique()
        total_days = df_filtered['date'].nunique()
        avg_cases_per_day = int(df_filtered.groupby('date')['confirmed'].sum().mean())
        
        st.write(f"🌍 **Países analizados:** {total_countries}")
        st.write(f"📅 **Días analizados:** {total_days}")
        st.write(f"📈 **Promedio casos/día:** {avg_cases_per_day:,}")
        st.write(f"💀 **Tasa letalidad promedio:** {kpis['fatality_rate']:.2f}%")
    
    with col3:
        st.subheader("⚠️ Alertas y Tendencias")
        
        # Análisis de tendencia reciente
        recent_days = 7
        if len(df_filtered['date'].unique()) >= recent_days:
            recent_dates = sorted(df_filtered['date'].unique())[-recent_days:]
            recent_data = df_filtered[df_filtered['date'].isin(recent_dates)]
            
            recent_growth = recent_data.groupby('date')['confirmed'].sum()
            growth_pct = ((recent_growth.iloc[-1] - recent_growth.iloc[0]) / recent_growth.iloc[0] * 100)
            
            if growth_pct > 10:
                st.error(f"🔴 Crecimiento acelerado: +{growth_pct:.1f}% en últimos {recent_days} días")
            elif growth_pct > 5:
                st.warning(f"🟡 Crecimiento moderado: +{growth_pct:.1f}% en últimos {recent_days} días")
            else:
                st.success(f"🟢 Crecimiento controlado: +{growth_pct:.1f}% en últimos {recent_days} días")
        
        # Países con mayor crecimiento reciente
        st.write("**📈 Mayor crecimiento:**")
        country_growth = df_filtered.groupby('country_region')['confirmed'].agg(['first', 'last'])
        country_growth['growth'] = ((country_growth['last'] - country_growth['first']) / country_growth['first'] * 100).fillna(0)
        top_growth = country_growth.nlargest(3, 'growth')
        
        for country in top_growth.index:
            growth = top_growth.loc[country, 'growth']
            if growth > 0:
                st.write(f"• {country}: +{growth:.1f}%")

    
    # ============================================================================
    # FOOTER
    # ============================================================================
    
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: #666;'>
            <p><strong>COVID-19 Epidemiological Dashboard</strong></p>
            <p>Proyecto Semestral - Gestión de Datos 2025-II</p>
            <p>Datos: <a href="https://github.com/CSSEGISandData/COVID-19" target="_blank">Johns Hopkins University CSSE</a></p>
            <p>Universidad Católica de la Santísima Concepción | Facultad de Ingeniería</p>
            <p>© 2025 | Desarrollado con Streamlit 🚀</p>
        </div>
    """, unsafe_allow_html=True)


# ============================================================================
# MENSAJE CUANDO NO HAY DATOS
# ============================================================================

else:
    st.warning("⚠️ No se pudieron cargar los datos.")
    st.info("""
    ### 📝 Instrucciones para cargar los datos:
    
    1. Asegúrate de tener los datos de JHU CSSE en la carpeta correcta:
       ```
       data/raw/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/
       ```
    
    2. Si no tienes los datos, ejecuta el script de descarga:
       ```bash
       ./scripts/fetch_jhu_data.sh clone
       ```
    
    3. Verifica que los notebooks previos (Etapa 1-3) se ejecutaron correctamente.
    
    4. Reinicia el dashboard después de cargar los datos.
    """)


# ============================================================================
# SCRIPT PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    # El dashboard se ejecuta automáticamente con: streamlit run app.py
    pass
