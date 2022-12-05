import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

st.title("Caso Netflix")
#Expansión
expansión = st.expander("Alumno")
expansión.markdown("""
* **Autor:** Luis Camilo Angel Sesma
* **Matrícula:** A01253231 
""")

sidebar = st.sidebar
sidebar.title("Menú de opciones.")
sidebar.write("Busca tus peliculas o directores favoritos.")

Data_URL="movies.csv"
@st.cache
def load_data(nrows):
    data=pd.read_csv(Data_URL,nrows=nrows)
    return data

data_load_state=st.text("Loading data...")
data=load_data(500)
data_load_state.text("Hecho...")

if sidebar.checkbox("Show dataframe"):
    st.dataframe(data)

Titulo=sidebar.text_input("Titulo de la película:")
btnTitulo=sidebar.button("Buscar películas")
if (btnTitulo):
    data_Titulo=data.copy()
    data_Titulo["name"]=data_Titulo["name"].str.lower()
    filterbyrange=data_Titulo[data_Titulo["name"].str.contains(Titulo.lower())]
    count_row=filterbyrange.shape[0]
    st.write(f"Total items: {count_row}")
    st.dataframe(filterbyrange)

Director = sidebar.selectbox("Seleccionar director:", data['director'].unique())
btnDirector=sidebar.button("Filtrar director")
if (btnDirector):
    filterbyDir=data[data["director"]==Director]
    count_row=filterbyDir.shape[0]
    st.write(f"Total items: {count_row}")
    st.dataframe(filterbyDir)