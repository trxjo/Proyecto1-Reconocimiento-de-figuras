import cv2 as cv


def valor_hexadecimal(ruta_img=None):
    img = cv.imread(ruta_img) if ruta_img else None

    if img is None:
        print("La imagen esta vacia")
        return None

    img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Caso para el los colres que se puedes observar en la figura
    # Circulo
    rojo_bajo = (0, 100, 100)
    rojo_alto = (5, 255, 255)

    # Mascara para encontrar los colores
    mask_rojo = cv.inRange(img_HSV, rojo_bajo, rojo_alto)

    # Cuadrado
    naranja_bajo = (10, 100, 100)
    naranja_alto = (20, 255, 255)

    # Mascara de cuadrado
    mask_naranja = cv.inRange(img_HSV, naranja_bajo, naranja_alto)

    # Rectangulo
    amarillo_bajo = (25, 100, 100)
    amarillo_alto = (35, 255, 255)

    # Mascara para el rectangulo
    mask_amarillo = cv.inRange(img_HSV, amarillo_bajo, amarillo_alto)

    # Rombo
    rombo_verde_bajo = (40, 100, 100)
    rombo_verde_alto = (50, 255, 255)

    # Mascara para el rombo
    mask_verde = cv.inRange(img_HSV, rombo_verde_bajo, rombo_verde_alto)

    # Trapecio
    trapecio_verde_bajo = (70, 100, 100)
    trapecio_verde_alto = (80, 255, 255)

    # Mascara para el trapecio
    mask_trapecio_verde = cv.inRange(
        img_HSV, trapecio_verde_bajo, trapecio_verde_alto)

    # Triangulo azul
    azul_bajo = (100, 100, 100)
    azul_alto = (110, 255, 255)

    # Mascara para el triangulo
    mask_azul = cv.inRange(img_HSV, azul_bajo, azul_alto)

    # Triangulo violeta
    violeta_bajo = (120, 100, 100)
    violeta_alto = (130, 255, 255)

    # Mascara para el triangulo
    mask_violeta = cv.inRange(img_HSV, violeta_bajo, violeta_alto)

    # Pentagono
    magenta_bajo = (140, 100, 100)
    magenta_alto = (150, 255, 255)

    # Mascara para el pentagono
    mask_magenta = cv.inRange(img_HSV, magenta_bajo, magenta_alto)

    # Hexagono rosa
    rosa_bajo = (155, 100, 100)
    rosa_alto = (165, 255, 255)

    # Mascara para el hexagono
    mask_rosa = cv.inRange(img_HSV, rosa_bajo, rosa_alto)

    # Diccionario con los colores donde estan sus mascaras
    mascaras = {
        "rojo": mask_rojo,
        "naranja": mask_naranja,
        "amarillo": mask_amarillo,
        "verde": mask_verde,
        "verde_trapecio": mask_trapecio_verde,
        "azul": mask_azul,
        "violeta": mask_violeta,
        "magenta": mask_magenta,
        "rosa": mask_rosa
    }

    for color, mascara in mascaras.items():
        if cv.countNonZero(mascara) > 0:
            colores_extraidos = cv.bitwise_and(img, img, mask=mascara)

            color_hexadecimal = colores_extraidos[mascara == 255]
            if len(color_hexadecimal):
                b, g, r = color_hexadecimal[0]
                color_hexadecimal = f"{r:02x}{g:02x}{b:02x}"
            print(f"Color hexadecimal: {color_hexadecimal}")

    return color_hexadecimal


imagen_uno = valor_hexadecimal('../../img/01_circulo.bmp')

imagen_site = valor_hexadecimal('../../img/06_triangulo_iso.bmp')

imagen_vacia = valor_hexadecimal()
