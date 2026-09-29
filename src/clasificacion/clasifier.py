import cv2
import numpy as np

def obtener_contorno(mascara):

    contornos, _ = cv2.findContours(
        mascara,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if not contornos:
        return None

    return max(
        contornos,
        key=cv2.contourArea
    )


def aproximar_contorno(contorno, epsilon=0.02):

    perimetro = cv2.arcLength(
        contorno,
        True
    )

    return cv2.approxPolyDP(
        contorno,
        epsilon * perimetro,
        True
    )


def calcular_circularidad(contorno):

    area = cv2.contourArea(contorno)

    perimetro = cv2.arcLength(
        contorno,
        True
    )

    if perimetro == 0:
        return 0.0

    return (
        4 * 3.141592653589793 * area
        / (perimetro ** 2)
    )


def analizar_vertices(contorno):

    epsilons = [
        0.01,
        0.02,
        0.03,
        0.04
    ]

    resultados = {}

    for epsilon in epsilons:

        aproximacion = aproximar_contorno(
            contorno,
            epsilon
        )

        resultados[epsilon] = len(
            aproximacion
        )

    return resultados


def calcular_relacion_aspecto(figura):

    if figura.alto == 0:
        return 0.0

    return figura.ancho / figura.alto

def clasificar_figura(figura):

    contorno = obtener_contorno(
        figura.mascara
    )

    if contorno is None:
        return "X"

    # Aproximación principal
    aproximacion = aproximar_contorno(
        contorno,
        0.02
    )

    vertices = len(aproximacion)

    # Casos sencillos
    if vertices == 3:
        return "T"

    if vertices == 4:
        return "C"

    # Características para distinguir
    # círculo de otras figuras
    circularidad = calcular_circularidad(
        contorno
    )

    vertices_finos = analizar_vertices(
        contorno
    )[0.01]

    aspecto = calcular_relacion_aspecto(
        figura
    )

    # Criterios para círculo
    es_circular = (
        circularidad >= 0.80
        and vertices_finos >= 12
        and 0.85 <= aspecto <= 1.15
    )

    if es_circular:
        return "O"

    return "X"

def obtener_color(imagen, mascara):

    pixeles = imagen[mascara == 1]

    if len(pixeles) == 0:
        return None

    colores, cantidades = np.unique(
        pixeles,
        axis=0,
        return_counts=True
    )

    indice = np.argmax(cantidades)

    color_bgr = colores[indice]

    color_rgb = (
        int(color_bgr[2]),
        int(color_bgr[1]),
        int(color_bgr[0])
    )

    return color_rgb


def rgb_a_hex(color_rgb):

    if color_rgb is None:
        return None

    r, g, b = color_rgb

    return f"#{r:02X}{g:02X}{b:02X}"