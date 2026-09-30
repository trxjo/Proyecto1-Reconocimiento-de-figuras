import sys

import preprocess
import detector

from clasificacion import Clasificacion
from valor_hexadecimal import obtener_hexadecimal


class Main:

    def __init__(self, ruta_imagen):
        self.ruta_imagen = ruta_imagen

    def ejecutar(self):
        
        print("=========================")
        print("\nRECONOCIMIENTO DE FIGURAS")
        print("=========================")

        try:
            imagen_preprocesada = preprocess.preprocesar(
                self.ruta_imagen
            )

        except ValueError as error:
            print(f"\nError no se encontró la imagen: {error}")
            return

        imagen = imagen_preprocesada.imagen
        mascara = imagen_preprocesada.mascara

        figuras = detector.detectar_figuras(
            mascara
        )

        if not figuras:
            print("\nNo se encontraron figuras en la imagen :( .")
            return

        print(
            f"\nSe encontraron {len(figuras)} figura(s) :D .\n"
        )

        for numero, figura in enumerate(
            figuras,
            start=1
        ):

            categoria = Clasificacion.clasificar(
                figura
            )

            color = obtener_hexadecimal(
                imagen,
                figura.mascara
            )

            print(f"La figura es: {numero}")
            print(f"El tipo de la figura es: {categoria}")
            print(f"El color de la figura es:     {color}")
            print()


if __name__ == "__main__":

    if len(sys.argv) != 2:

        print(
            "Se utilizaron las imagenes del Banco :D ."
        )

        sys.exit(1)

    ruta_imagen = sys.argv[1]

    programa = Main(ruta_imagen)

    programa.ejecutar()