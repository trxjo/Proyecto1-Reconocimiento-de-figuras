from pathlib import Path
import cv2

from preprocesamiento.preprocess import (
    cargar_imagen,
    obtener_color_fondo,
    crear_mascara
)


# Obtener la carpeta raíz del proyecto
BASE_DIR = Path(__file__).resolve().parents[2]

# Ruta de la imagen
ruta = BASE_DIR / "dataset_figuras" / "02_cuadrado.bmp"


# Leer imagen
imagen = cargar_imagen(ruta)

# Obtener fondo
color_fondo = obtener_color_fondo(imagen)

# Crear máscara
mascara = crear_mascara(
    imagen,
    color_fondo
)


# Mostrar información
print("Imagen:", imagen.shape)
print("Color de fondo:", color_fondo)
print("Máscara:", mascara.shape)


# Mostrar máscara
cv2.imshow(
    "Mascara",
    mascara * 255
)

cv2.waitKey(0)
cv2.destroyAllWindows()