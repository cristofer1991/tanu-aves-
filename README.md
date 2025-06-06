
# Descargador de Imágenes de Aves desde iNaturalist (con Streamlit)

Esta aplicación permite buscar y descargar hasta **500 imágenes por especie** desde iNaturalist.org usando su API oficial. Es ideal para construir datasets de visión artificial (por ejemplo, para entrenar modelos como YOLO).

## 🐦 Especies incluidas
- Tiuque (*Milvago chimango*)
- Queltehue (*Vanellus chilensis*)
- Carancho (*Caracara plancus*)
- Cauquén (*Chloephaga picta*)

## 🛠️ Cómo usar

### Opción 1: Ejecutar localmente

1. Instala Python 3
2. Instala dependencias:

```bash
pip install streamlit requests
```

3. Ejecuta la aplicación:

```bash
streamlit run app.py
```

### Opción 2: Usar con Streamlit Cloud (sin instalar nada)

1. Crea una cuenta gratuita en [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Sube los archivos de este repositorio a uno nuevo en GitHub
3. En Streamlit Cloud, selecciona tu repositorio y el archivo `app.py`
4. ¡Listo! Tu app estará en línea y lista para usar.

## 📦 Funcionalidades

- Selección de especie
- Búsqueda y descarga de imágenes de alta resolución
- Visualización de progreso
- **Botón para descargar todas las imágenes como archivo `.zip`**

## 📁 Estructura del dataset generado

```
dataset/
├── Milvago_chimango/
│   ├── Milvago_chimango_0.jpg
│   ├── ...
```

## 🔒 Licencias

Todas las imágenes provienen de iNaturalist y están sujetas a sus licencias Creative Commons. Se recomienda revisar el uso permitido si se reutilizan con fines comerciales.

---

Desarrollado por [Tu Nombre o Proyecto]
