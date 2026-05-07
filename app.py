import streamlit as st
import pandas as pd
from datetime import date
from PIL import Image

# Configuración de la página para dispositivos móviles
st.set_page_config(page_title="Voltaic - Control de Albaranes", page_icon="⚡")

# --- 1. LOGO DE LA EMPRESA ---
# Si tienes el logo en la misma carpeta de GitHub, usa: st.image("logo.png")
# Por ahora usamos un placeholder con el nombre de tu empresa
st.image("https://via.placeholder.com/400x150.png?text=VOLTAIC+ALTA+TENSION", width=250)

st.title("Registro de Presupuesto")
st.markdown("Use este formulario para registrar los gastos de obra y adjuntar el albarán.")

# --- 2. FORMULARIO DE ENTRADA ---
with st.form("registro_gasto", clear_on_submit=True):
    
    st.subheader("Datos del Albarán")
    
    # Número de albarán
    n_albaran = st.text_input("Número de Albarán", placeholder="Ej: ALB-12345")
    
    # Fecha
    fecha = st.date_input("Fecha", value=date.today())
    
    # Trabajador (Campo de texto libre como solicitaste)
    trabajador = st.text_input("Nombre del Trabajador", placeholder="Escriba su nombre completo")
    
    # Partida del presupuesto
    partida = st.selectbox(
        "Partida del presupuesto asociada",
        ["Líneas de Alta Tensión", "Subestaciones", "Mantenimiento", "Equipos de Medida", "Otros"]
    )
    
    # Gastos
    gasto = st.number_input("Gastos de esta partida (€)", min_value=0.0, step=0.01, format="%.2f")
    
    # Comentarios
    comentarios = st.text_area("Comentarios o detalles de la obra")
    
    # --- 3. REGISTRO CON IMAGEN ---
    st.subheader("Documentación Visual")
    foto_albaran = st.file_uploader("Capturar o subir imagen del albarán", type=["jpg", "jpeg", "png"])
    
    if foto_albaran is not None:
        st.image(foto_albaran, caption="Vista previa del albarán cargado", use_container_width=True)

    # Botón de envío
    enviar = st.form_submit_button("Registrar y Guardar")

# --- 4. LÓGICA DE PROCESAMIENTO ---
if enviar:
    if n_albaran and trabajador and gasto > 0:
        st.success(f"✅ Albarán {n_albaran} registrado con éxito por {trabajador}.")
        
        # Aquí puedes ver los datos que se procesarían
        resumen = {
            "Albarán": n_albaran,
            "Fecha": str(fecha),
            "Trabajador": trabajador,
            "Partida": partida,
            "Importe": f"{gasto} €",
            "Imagen adjunta": "Sí" if foto_albaran else "No"
        }
        st.json(resumen)
    else:
        st.error("⚠️ Por favor, rellene los campos obligatorios (Nº Albarán, Trabajador e Importe).")

# Pie de página
st.markdown("---")
st.caption("App Interna - Voltaic Infraestructuras de Alta Tensión")
