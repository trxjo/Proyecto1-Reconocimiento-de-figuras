import cv2


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


def aproximar_contorno(contorno):

    perimetro = cv2.arcLength(
        contorno,
        True
    )

    aproximacion = cv2.approxPolyDP(
        contorno,
        0.02 * perimetro,
        True
    )

    return aproximacion


def calcular_circularidad(contorno):

    area = cv2.contourArea(
        contorno
    )

    perimetro = cv2.arcLength(
        contorno,
        True
    )

    if perimetro == 0:
        return 0

    return (
        4 * 3.141592653589793 * area
        / (perimetro ** 2)
    )