
import streamlit as st
import requests
from pathlib import Path
import zipfile
import io
import shutil

st.title("Descargador de imágenes de aves desde iNaturalist (API)")
st.write("Esta versión usa la API oficial de iNaturalist para obtener imágenes confiables por especie y permite descargar las imágenes en un ZIP.")

especies = {
    "Tiuque (Milvago chimango)": "Milvago chimango",
    "Queltehue (Vanellus chilensis)": "Vanellus chilensis",
    "Carancho (Caracara plancus)": "Caracara plancus",
    "Cauquén (Chloephaga picta)": "Chloephaga picta"
}

especie_seleccionada = st.selectbox("Selecciona una especie", list(especies.keys()))
cantidad = st.slider("Cantidad de imágenes a descargar", min_value=10, max_value=500, value=50)

if st.button("Iniciar descarga"):
    nombre_cientifico = especies[especie_seleccionada]
    carpeta_destino = Path("dataset") / nombre_cientifico.replace(" ", "_")
    if carpeta_destino.exists():
        shutil.rmtree(carpeta_destino)
    carpeta_destino.mkdir(parents=True, exist_ok=True)

    st.write(f"Buscando imágenes para: {nombre_cientifico}...")

    fotos = []
    page = 1
    while len(fotos) < cantidad and page <= 10:
        api_url = f"https://api.inaturalist.org/v1/observations?taxon_name={nombre_cientifico.replace(' ', '%20')}&photos=true&per_page=100&page={page}"
        response = requests.get(api_url)
        if response.status_code != 200:
            break
        data = response.json()
        if not data["results"]:
            break
        for obs in data["results"]:
            for foto in obs.get("photos", []):
                url = foto.get("url", "").replace("square", "original").split("?")[0]
                if url not in fotos:
                    fotos.append(url)
                if len(fotos) >= cantidad:
                    break
            if len(fotos) >= cantidad:
                break
        page += 1

    if not fotos:
        st.error("No se encontraron fotos para esta especie.")
    else:
        progreso = st.progress(0)
        for i, url in enumerate(fotos):
            ext = url.split('.')[-1]
            img_data = requests.get(url).content
            with open(carpeta_destino / f"{nombre_cientifico.replace(' ', '_')}_{i}.{ext}", "wb") as f:
                f.write(img_data)
            progreso.progress((i + 1) / len(fotos))

        st.success(f"Descarga completada: {len(fotos)} imágenes guardadas en {carpeta_destino}")

        # Crear un ZIP para descarga
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for img_file in carpeta_destino.glob("*.*"):
                zip_file.write(img_file, arcname=img_file.name)
        zip_buffer.seek(0)

        st.download_button(
            label="📥 Descargar imágenes en ZIP",
            data=zip_buffer,
            file_name=f"{nombre_cientifico.replace(' ', '_')}_imagenes.zip",
            mime="application/zip"
        )
