import streamlit as st
import math
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🧵 Corta las cuerdas")
st.write(
    "Juana tiene una cuerda de 16 cm y otra de 40 cm desea cortarlas, de modo que, todos los trozos sea iguales pero lo más largo posibles.\n")
st.write(
    "**¿Cuántos pedazos de cuerda puede cortar en cada cuerda?**")


# ------------------------
# Funciones
# ------------------------
def divisores(n):
    return sorted([i for i in range(1, n + 1) if n % i == 0])

def dibujar_cuerda(ax, longitud, corte, y, etiqueta):
    ax.plot([0, longitud], [y, y], linewidth=8)
    for x in range(0, longitud + 1, corte):
        ax.plot([x, x], [y - 0.15, y + 0.15])
    ax.text(longitud + 0.5, y, f"{longitud} cm", va="center")
    ax.text(-1.5, y, etiqueta, va="center", ha="right")

# ------------------------
# Longitudes fijas del problema
# ------------------------
cuerda1 = 40
cuerda2 = 16

factores1 = divisores(cuerda1)
factores2 = divisores(cuerda2)


col1, col2 = st.columns(2)

with col1:
    # ------------------------
    # Sliders SOLO con factores
    # ------------------------
    st.subheader("🎛️ Selecciona el tamaño del corte")
    st.write(
        "Los sliders solo permiten elegir **factores (divisores)** de cada cuerda.\n"
        "El valor seleccionado representa el **tamaño de cada corte**."
    )
    corte1 = st.select_slider(
        "Cuerda de 40 cm",
        options=factores1,
        value=factores1[0]
    )

    corte2 = st.select_slider(
        "Cuerda de 16 cm",
        options=factores2,
        value=factores2[0]
    )

    # ------------------------
    # Visualización
    # ------------------------
    st.subheader("✂️ Representación visual de las cuerdas")

    fig, ax = plt.subplots(figsize=(10, 3))

    dibujar_cuerda(ax, cuerda1, corte1, 2, "Cuerda 40 cm")
    dibujar_cuerda(ax, cuerda2, corte2, 1, "Cuerda 16 cm")

    ax.set_xlim(0, max(cuerda1, cuerda2) + 5)
    ax.set_ylim(0.5, 2.5)
    ax.set_xlabel("Centímetros")
    ax.set_yticks([])
    ax.set_title("Cortes según el factor seleccionado")
    ax.grid(True, axis="x", linestyle="--", alpha=0.4)

    st.pyplot(fig)
with col2:
        
    # ------------------------
    # Análisis matemático
    # ------------------------
    st.subheader("🔍 Análisis")

    st.write(f"- Cuerda 40 cm → {cuerda1 // corte1} trozos de {corte1} cm")
    st.write(f"- Cuerda 16 cm → {cuerda2 // corte2} trozos de {corte2} cm")

    # ------------------------
    # Detección visual del MCD
    # ------------------------
    if corte1 == corte2:
        st.success(
            f"✅ Ambos cortes coinciden en **{corte1} cm**.\n\n"
            f"Este valor es un **divisor común**."
        )

        if corte1 == math.gcd(cuerda1, cuerda2):
            st.balloons()
            st.success("🎉 ¡Este es el MCD! Es el mayor tamaño posible para que los trozos sean iguales.")
    else:
        st.info(
            "🔎 Ajusta los sliders hasta que ambos tengan el **mismo valor**.\n"
            "Luego busca el **mayor valor posible**."
        )
