import pandas as pd
import plotly.express as px
import streamlit as st

vehiculos = pd.read_csv('C:\\Users\\sahen\\Proyectos\\notebook\\Spring_7_proyecto\\vehicles_us.csv')

#Dividir la tabla por el model_year debe decir excelentes condiciones y no debe rebasar los 10000usd
lista_modelos = ['truck', 'SUV', 'pickup', 'convertible', 'sedan', 'van']
filtrado_decadas = vehiculos.query("condition == 'excellent' and price < 10000 and days_listed < 30 and type in @lista_modelos and odometer < 60000")[['price', 'model', 'type', 'condition', 'transmission', 'model_year', 'odometer']]
decada_10s = filtrado_decadas.query("model_year >= 2010 and model_year <= 2019")[['price', 'model', 'type', 'condition', 'transmission', 'model_year', 'odometer']]
conteo_por_marca = decada_10s['model'].sort_values(ascending=False)


st.header('Ventas de autos en excelentes condiciones (2010-2019)') #Titulo de la aplicacion

#Crear un botón
hist_boton = st.button('Construir histograma')
dispersion_boton = st.button('Construir una grafica de dispersion')
barras_boton = st.button('Construir un grafico de barras')

if hist_boton: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')# escribir un mensaje
    # crear un histograma
    hist_10s = px.histogram(decada_10s, x="price", nbins=10, title='Distribución de tipos y modelos de autos en excelentes condiciones (años 2010–2019)', color="type", color_discrete_sequence=px.colors.qualitative.Pastel)
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(hist_10s, use_container_width=True)

# crear un botón
if dispersion_boton: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de una grafica de dispersion para el conjunto de datos de anuncios de venta de coches')
    # crear una grafica de dispersion
    scatter_10s = px.scatter(decada_10s, x="odometer", y="model_year", title="Autos de la década del 2010 por kilometraje y año", color_discrete_sequence=["#00CC96"])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(scatter_10s, use_container_width=True)

# crear un botón
if barras_boton: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de una grafica de barras para el conjunto de datos de anuncios de venta de coches')
    # crear una grafica de dispersion
    fig_top25 = px.bar(conteo_por_marca, x=conteo_por_marca.values, y=conteo_por_marca.index, labels={'x': 'Modelo', 'y': 'Cantidad'}, title='Top modelos más buscados', color_discrete_sequence=px.colors.qualitative.Pastel, color='model')  # color azul claro


    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_top25, use_container_width=True)
