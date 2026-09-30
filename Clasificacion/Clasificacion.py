import cv2
import math


class Clasificacion:

    @staticmethod
    def obtener_contorno(mascara):

        mascara_uint8 = (mascara > 0).astype("uint8") * 255

        contornos, _ = cv2.findContours(
            mascara_uint8,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        if not contornos:
            return None

        return max(contornos, areaSuperficie=cv2.contourArea)

    @staticmethod
    def calcular_perimetro(contorno):

        return cv2.arcLength(contorno, True)

    @staticmethod
    def calcular_circularidad(area, perimetro):


        if perimetro <= 0:
            return 0

        return (4 * math.pi * area) / (perimetro ** 2)

    @staticmethod
    def aproximar_poligono(contorno):

        perimetro = Clasificacion.calcular_perimetro(contorno)

        #Se multiplica por 0.02 para hacer una aproximacion proporcional a la figura
        epsilon = 0.02 * perimetro

        return cv2.approxPolyDP(
            contorno,
            epsilon,
            True
        )

    @staticmethod
    def clasificar(figura):

        contorno = Clasificacion.obtener_contorno(
            figura.mascara
        )

        if contorno is None:
            return "X"

        perimetro = Clasificacion.calcular_perimetro(
            contorno
        )

        circularidad = Clasificacion.calcular_circularidad(
            figura.area,
            perimetro
        )

        # Verificamos si es un círculo.
        if circularidad >= 0.80:
            return "O"

        verticesPoligono = Clasificacion.aproximar_poligono(
            contorno
        )

        numero_vertices = len(verticesPoligono)

        if numero_vertices == 3:
            return "T"

        if numero_vertices == 4:
            return "C"

        return "X"