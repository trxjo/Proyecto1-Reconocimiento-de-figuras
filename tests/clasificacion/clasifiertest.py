from pathlib import Path

import cv2

from preprocesamiento.preprocess import preprocesar
from deteccion.detector import detectar_figuras

from clasificacion.clasifier import (
    obtener_contorno,
    aproximar_contorno,
    calcular_circularidad
)


# RUTA DEL PROYECTO

BASE_DIR = Path(__file__).resolve().parents[2]

ruta = BASE_DIR / "dataset_figuras" / "01_circulo.bmp"


# PREPROCESAMIENTO

datos = preprocesar(ruta)


# DETECCIÓN

figuras = detectar_figuras(datos.mascara)


print("========================================")
print("ANÁLISIS DE FIGURAS")
print("========================================")

print("Número de figuras:", len(figuras))


# CLASIFICACIÓN - ANÁLISIS

for i, figura in enumerate(figuras, start=1):

    # Obtener contorno
    contorno = obtener_contorno(
        figura.mascara
    )

    # Comprobar que encontramos un contorno
    if contorno is None:
        print(f"\nFigura {i}: no se encontró contorno")
        continue

    # Aproximar contorno
    aproximacion = aproximar_contorno(
        contorno
    )

    # Número de vértices
    vertices = len(aproximacion)

    # Área
    area = cv2.contourArea(
        contorno
    )

    # Perímetro
    perimetro = cv2.arcLength(
        contorno,
        True
    )

    # Circularidad
    circularidad = calcular_circularidad(
        contorno
    )

   
    # MOSTRAR RESULTADOS


    print()
    print("----------------------------------------")
    print(f"Figura {i}")
    print("----------------------------------------")

    print(
        "Posición:",
        f"({figura.x}, {figura.y})"
    )

    print(
        "Tamaño:",
        f"{figura.ancho} x {figura.alto}"
    )

    print(
        "Área detectada:",
        figura.area
    )

    print(
        "Área del contorno:",
        area
    )

    print(
        "Perímetro:",
        perimetro
    )

    print(
        "Vértices:",
        vertices
    )

    print(
        "Circularidad:",
        circularidad
    )

    print(
        "Centroide:",
        figura.centroide
    )