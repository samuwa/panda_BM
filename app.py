import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime

st.set_page_config(layout='wide')

st.title("PanDa :panda_face:")
st.write("**Panama Data Consulting**")
st.markdown("##")

cl1, cl2, cl3 = st.columns([3,3,3])



cl2.subheader("1. Chatbots Brillantes")
cl2.write("Asistentes virtuales potenciados por *ChatGPT*")
cl2.write(" - Entrenados con información pública y privada")
cl2.write(" - Disponibilidad 24/7")
cl2.write(" - Capacidad de captar datos y generar reportes")



cl2.video("WhatsApp Video 2024-01-29 at 10.22.07 AM.mp4", 'rb')

st.markdown("##")

st.subheader("2. Análisis de Datos para Todos")
st.write("Tableros de inteligencia de negocios personalizados.")

def cargar_datos():
    df = pd.read_csv('datos_dummy_vehiculos.csv')
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df['Mes'] = df['Fecha'].dt.month
    return df

df = cargar_datos()

# Sidebar con MultiSelect para los productos
productos_seleccionados = st.multiselect(
    "Selecciona los productos",
    options=df['Producto'].unique(),
    default=df['Producto'].unique()
)

# Si no se selecciona ningún producto, se muestran todos
if not productos_seleccionados:
    productos_seleccionados = df['Producto'].unique()

# Filtrar datos basado en la selección
df_filtrado = df[df['Producto'].isin(productos_seleccionados)]

# Line Chart - Ventas por mes en términos de valor monetario

col1, col2 = st.columns(2)
ventas_por_mes = df_filtrado.groupby(['Mes', 'Producto'])['Precio'].sum().reset_index(name='Ventas ($)')
fig_line = px.line(ventas_por_mes, x='Mes', y='Ventas ($)', color='Producto', title='Ventas por Mes ($)')
fig_line.update_layout(legend=dict(orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
col1.plotly_chart(fig_line)

# Bar Chart - Ventas Totales por Producto en términos de valor monetario
ventas_totales = df_filtrado.groupby('Producto')['Precio'].sum().reset_index(name='Ventas Totales ($)')
fig_bar = px.bar(ventas_totales, x='Producto', y='Ventas Totales ($)', color='Producto', title='Ventas Totales por Producto ($)')
fig_bar.update_layout(legend=dict(orientation="h", y=1, yanchor="bottom", x=0.5, xanchor="center"))
col2.plotly_chart(fig_bar)

# Pie Chart - Unidades Vendidas por Producto (sin leyenda)
unidades_vendidas = df_filtrado.groupby('Producto').size().reset_index(name='Unidades Vendidas')
fig_pie = px.pie(unidades_vendidas, names='Producto', values='Unidades Vendidas', title='Unidades Vendidas por Producto')
fig_pie.update_layout(showlegend=False)
col1.plotly_chart(fig_pie)

# Pivot Table - Ventas totales, unidades vendidas y porcentaje del total
total_ventas = ventas_totales['Ventas Totales ($)'].sum()
unidades_por_producto = df_filtrado.groupby('Producto').size().reset_index(name='Unidades Vendidas')
ventas_y_unidades = pd.merge(ventas_totales, unidades_por_producto, on='Producto')
ventas_y_unidades['Porcentaje del Total (%)'] = ((ventas_y_unidades['Ventas Totales ($)'] / total_ventas) * 100).round(2)
ventas_y_unidades['Porcentaje del Total (%)'] = ventas_y_unidades['Porcentaje del Total (%)'].astype(str) + '%'

col2.write("**Tabla Resumen**")
col2.dataframe(ventas_y_unidades)

st.markdown("####")

st.subheader("3. Automatización de Procesos y Aplicaciones Inegrales")
st.write("Utilizando las herramientas más versátiles y avanzadas del mercado, desarrollamos soluciones a la medida a una velocidad incomparable.")
st.markdown("###")
col1, col2, col3 = st.columns(3)

col1.image("python logo.jpeg")
col2.image("bubble logo.jpeg")
col3.image("chatgpt logo.png")


col1, col2, col3 = st.columns(3)

with col1.expander("Python"):
    st.write("Python es el lenguaje número 1 entre desarroladores de software. En PanDa :panda_face:, Python es la base de todas nuestras soluciones.")


with col2.expander("Bubble.io"):
    st.write("Existen infinitas alternativas para desarrollar aplicaciones, pero ninguna como Bubble. Por su velocidad y versatilidad, Bubble es nuestra herramienta de elección para el desarrollo de *business apps* personalizadas.")


with col3.expander("ChatGPT"):
    st.write("El mundo cambió con ChatGPT, aunque no todo el mundo se haya dado cuenta. La innovación del presente depende de implementar inteligencia artificial en la operación continua de cualquier organización. ChatGPT abrió el universo de la inteligencia artificial para todo el que quiera aprovecharlo, nosotros ya nos montamos en la ola. :surfer:")

