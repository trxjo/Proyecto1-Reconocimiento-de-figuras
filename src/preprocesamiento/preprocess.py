import cv2
import numpy as np


class ImagenPreprocesada:

    def __init__(
        self,
        imagen,
        color_fondo,
        mascara
    ):
        self.imagen = imagen
        self.color_fondo = color_fondo
        self.mascara = mascara


def cargar_imagen(ruta):

    imagen = cv2.imread(str(ruta))

    if imagen is None:
        raise ValueError(
            f"No se pudo leer la imagen: {ruta}"
        )

    return imagen


def obtener_color_fondo(imagen):

    return imagen[0, 0]


def crear_mascara(imagen, color_fondo):

    mascara = np.any(
        imagen != color_fondo,
        axis=2
    )

    return mascara.astype(np.uint8)


def preprocesar(ruta):

    imagen = cargar_imagen(ruta)

    color_fondo = obtener_color_fondo(
        imagen
    )

    mascara = crear_mascara(
        imagen,
        color_fondo
    )

    return ImagenPreprocesada(
        imagen,
        color_fondo,
        mascara
    )