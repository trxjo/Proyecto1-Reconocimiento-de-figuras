from pathlib import Path

import cv2

from preprocesamiento.preprocess import preprocesar
from deteccion.detector import detectar_figuras

from clasificacion.clasifier import (
    obtener_contorno,
    aproximar_contorno,
    calcular_circularidad,
    analizar_vertices,
    calcular_relacion_aspecto,
    clasificar_figura,
    obtener_color,
    rgb_a_hex
)


# CONFIGURACIÓN

BASE_DIR = Path(__file__).resolve().parents[2]

ruta = (
    BASE_DIR
    / "dataset_figuras"
    / "10_octagono.bmp"
)


# LEER IMAGEN ORIGINAL

imagen = cv2.imread(str(ruta))

if imagen is None:
    raise FileNotFoundError(
        f"No se pudo leer la imagen: {ruta}"
    )


# PREPROCESAMIENTO

datos = preprocesar(ruta)


# DETECCIÓN

figuras = detectar_figuras(
    datos.mascara
)


# RESULTADOS GENERALES

print()
print("========================================")
print("     PRUEBA FINAL DE CLASIFICACIÓN")
print("========================================")

print()
print("Imagen:", ruta.name)
print("Número de figuras:", len(figuras))


# ANALIZAR CADA FIGURA

for i, figura in enumerate(
    figuras,
    start=1
):

    print()
    print("----------------------------------------")
    print(f"FIGURA {i}")
    print("----------------------------------------")

    # CONTORNO

    contorno = obtener_contorno(
        figura.mascara
    )

    if contorno is None:

        print("No se encontró contorno.")
        print("Clasificación: X")

        continue


    # VERTICES

    aproximacion = aproximar_contorno(
        contorno,
        0.02
    )

    vertices = len(
        aproximacion
    )

    # CIRCULARIDAD

    circularidad = calcular_circularidad(
        contorno
    )


    # ANÁLISIS DE EPSILON

    vertices_epsilon = analizar_vertices(
        contorno
    )


    # RELACIÓN DE ASPECTO

    aspecto = calcular_relacion_aspecto(
        figura
    )


    # CLASIFICACIÓN

    tipo = clasificar_figura(
        figura
    )


    # COLOR

    color_rgb = obtener_color(
        imagen,
        figura.mascara
    )

    color_hex = rgb_a_hex(
        color_rgb
    )


    # MOSTRAR INFORMACIÓN

    print()
    print("Información geométrica")
    print("----------------------")

    print(
        "Posición:",
        f"({figura.x}, {figura.y})"
    )

    print(
        "Tamaño:",
        f"{figura.ancho} x {figura.alto}"
    )

    print(
        "Área:",
        figura.area
    )

    print(
        "Centroide:",
        figura.centroide
    )

    print(
        "Vértices (ε=0.02):",
        vertices
    )

    print(
        "Circularidad:",
        round(circularidad, 4)
    )

    print(
        "Relación ancho/alto:",
        round(aspecto, 4)
    )


    # EPSILON

    print()
    print("Vértices según epsilon")
    print("-----------------------")

    for epsilon, cantidad in (
        vertices_epsilon.items()
    ):

        print(
            f"ε={epsilon}: "
            f"{cantidad} vértices"
        )


    # COLOR

    print()
    print("Color")
    print("-----")

    print(
        "RGB:",
        color_rgb
    )

    print(
        "Hexadecimal:",
        color_hex
    )


    # RESULTADO

    print()
    print("Resultado")
    print("---------")

    print(
        "Clasificación:",
        tipo
    )