import cv2
import numpy as np
import os

# Crear carpeta de salida
output_dir = "dataset_figuras"
os.makedirs(output_dir, exist_ok=True)

# Dimensiones de las imágenes
width, height = 400, 400

# Colores en HSV para OpenCV: Hue [0-179], Saturation [0-255], Value [0-255]
# Cada figura tiene un tono (Hue) y color único
figures = [
    {"name": "01_circulo", "hsv": (0, 255, 255), "type": "circle"},          # Rojo
    {"name": "02_cuadrado", "hsv": (15, 255, 255), "type": "square"},        # Naranja
    {"name": "03_rectangulo", "hsv": (30, 255, 255), "type": "rectangle"},    # Amarillo
    {"name": "04_rombo", "hsv": (45, 255, 255), "type": "rhombus"},          # Verde Lima
    {"name": "05_trapezoide", "hsv": (75, 255, 255), "type": "trapezoid"},    # Cian
    {"name": "06_triangulo_iso", "hsv": (105, 255, 255), "type": "tri_iso"},  # Azul
    {"name": "07_triangulo_esc", "hsv": (125, 255, 255), "type": "tri_esc"},  # Violeta
    {"name": "08_pentagono", "hsv": (145, 255, 255), "type": "pentagon"},    # Magenta
    {"name": "09_hexagono", "hsv": (160, 255, 255), "type": "hexagon"},     # Rosa
    {"name": "10_octagono", "hsv": (90, 255, 180), "type": "octagon"}        # Verde Oscuro
]

for fig in figures:
    # 1. Crear lienzo en HSV con fondo blanco (H=0, S=0, V=255)
    img_hsv = np.zeros((height, width, 3), dtype=np.uint8)
    img_hsv[:, :] = [0, 0, 255]

    color = fig["hsv"]
    f_type = fig["type"]

    # 2. Dibujar la figura correspondiente sin anti-aliasing (LINE_4 o LINE_8)
    if f_type == "circle":
        cv2.circle(img_hsv, (200, 200), 120, color, -1, lineType=cv2.LINE_4)

    elif f_type == "square":
        pts = np.array([[100, 100], [300, 100], [300, 300], [100, 300]])
        cv2.fillPoly(img_hsv, [pts], color, lineType=cv2.LINE_4)

    elif f_type == "rectangle":
        pts = np.array([[60, 140], [340, 140], [340, 260], [60, 260]])
        cv2.fillPoly(img_hsv, [pts], color, lineType=cv2.LINE_4)

    elif f_type == "rhombus":
        pts = np.array([[200, 60], [340, 200], [200, 340], [60, 200]])
        cv2.fillPoly(img_hsv, [pts], color, lineType=cv2.LINE_4)

    elif f_type == "trapezoid":
        pts = np.array([[120, 100], [280, 100], [340, 300], [60, 300]])
        cv2.fillPoly(img_hsv, [pts], color, lineType=cv2.LINE_4)

    elif f_type == "tri_iso":
        pts = np.array([[200, 70], [330, 330], [70, 330]])
        cv2.fillPoly(img_hsv, [pts], color, lineType=cv2.LINE_4)

    elif f_type == "tri_esc":
        pts = np.array([[100, 80], [350, 280], [120, 340]])
        cv2.fillPoly(img_hsv, [pts], color, lineType=cv2.LINE_4)

    elif f_type == "pentagon":
        pts = np.array([[200, 60], [330, 160], [280, 330], [120, 330], [70, 160]])
        cv2.fillPoly(img_hsv, [pts], color, lineType=cv2.LINE_4)

    elif f_type == "hexagon":
        pts = np.array([[130, 70], [270, 70], [340, 200], [270, 330], [130, 330], [60, 200]])
        cv2.fillPoly(img_hsv, [pts], color, lineType=cv2.LINE_4)

    elif f_type == "octagon":
        pts = np.array([[140, 60], [260, 60], [340, 140], [340, 260], [260, 340], [140, 340], [60, 260], [60, 140]])
        cv2.fillPoly(img_hsv, [pts], color, lineType=cv2.LINE_4)

    # 3. Convertir de HSV a BGR para guardar como BMP
    img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    # 4. Guardar archivo en formato BMP
    file_path = os.path.join(output_dir, f"{fig['name']}.bmp")
    cv2.imwrite(file_path, img_bgr)
    print(f"Imagen guardada: {file_path}")