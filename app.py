import streamlit as st
import pandas as pd
from datetime import date

# Configuración de la página para móvil
st.set_page_config(page_title="Control de Presupuesto", layout="centered")

# --- 1. INCORPORAR LOGO DE LA EMPRESA ---
# Puedes usar una URL de imagen o una ruta local
st.image("https://via.placeholder.com/150x50?text=LOGO+EMPRESA", width=200)

st.title("📊 Seguimiento de Presupuesto")
st.markdown("Introduce los datos del albarán para el control de gastos.")

# --- 2. FORMULARIO DE INPUTS ---
with st.form("formulario_gastos", clear_on_submit=True):
    col1, col2 = st.columns(2)
    
    with col1:
        n_albaran = st.text_input("Número de Albarán")
        fecha = st.date_input("Fecha", value=date.today())
        trabajador = st.selectbox("Trabajador", ["Juan Pérez", "María García", "Carlos Ruiz", "Ana Belén"])

    with col2:
        partida = st.selectbox("Partida del Presupuesto", ["Materiales", "Mano de Obra", "Transporte", "Dietas", "Otros"])
        gasto = st.number_input("Gastos de la partida (€)", min_value=0.0, step=0.01, format="%.2f")
    
    comentarios = st.text_area("Comentarios")
    
    submit_button = st.form_submit_button("Registrar Albarán")

# --- 3. LÓGICA DE ALMACENAMIENTO (Simulada) ---
if submit_button:
    if n_albaran:
        st.success(f"✅ Albarán {n_albaran} registrado correctamente.")
        
        # Ejemplo de cómo se verían los datos capturados
        datos = {
            "Albarán": n_albaran,
            "Fecha": fecha,
            "Trabajador": trabajador,
            "Partida": partida,
            "Gasto": gasto,
            "Comentarios": comentarios
        }
        st.write("### Resumen del registro:")
        st.json(datos)
    else:
        st.error("Por favor, introduce el número de albarán.")

# --- 4. VISUALIZACIÓN RÁPIDA ---
st.divider()
st.info("Nota: Para guardar datos de forma permanente en la nube, podrías conectar este formulario a un Google Sheet o una base de datos.")
