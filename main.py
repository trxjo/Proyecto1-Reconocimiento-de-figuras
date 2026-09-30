from pathlib import Path

import cv2

from src.preprocesamiento.preprocess import preprocesar
from src.deteccion.detector import detectar_figuras

from src.clasificacion.clasifier import (
    clasificar_figura,
    obtener_color,
    rgb_a_hex
)


def cargar_imagen(ruta):
    """
    Lee la imagen BMP y comprueba que exista
    y que pueda ser leída correctamente.
    """

    if not ruta.exists():
        raise FileNotFoundError(
            f"No existe la imagen: {ruta}"
        )

    if ruta.suffix.lower() != ".bmp":
        raise ValueError(
            "El archivo debe tener extensión .bmp"
        )

    imagen = cv2.imread(str(ruta))

    if imagen is None:
        raise ValueError(
            f"No se pudo leer la imagen: {ruta}"
        )

    return imagen


def main():

    # ========================================
    # RUTA DE LA IMAGEN
    # ========================================

    ruta = (
        Path(__file__).resolve().parent
        / "banco_de_imagenes"
        / "prueba.bmp"
    )

    # ========================================
    # LEER IMAGEN
    # ========================================

    imagen = cargar_imagen(ruta)

    # ========================================
    # PREPROCESAMIENTO
    # ========================================

    datos = preprocesar(ruta)

    # ========================================
    # DETECCIÓN
    # ========================================

    figuras = detectar_figuras(
        datos.mascara
    )

    # ========================================
    # RESULTADO
    # ========================================

    print()
    print("                                        ")
    print("       RECONOCIMIENTO DE FIGURAS")
    print("                                        ")
    print()

    print(
        f"Imagen: {ruta.name}"
    )

    print(
        f"Figuras detectadas: {len(figuras)}"
    )

    print()

    # ========================================
    # PROCESAR FIGURAS
    # ========================================

    for i, figura in enumerate(
        figuras,
        start=1
    ):

        # Clasificar forma
        tipo = clasificar_figura(
            figura
        )

        # Obtener color
        color_rgb = obtener_color(
            imagen,
            figura.mascara
        )

        # Convertir RGB a hexadecimal
        color_hex = rgb_a_hex(
            color_rgb
        )

        # Mostrar resultado
        print(
            f"Figura {i} → "
            f"{color_hex} → "
            f"{tipo}"
        )

    print()


# ========================================
# EJECUCIÓN
# ========================================

if __name__ == "__main__":
    main()