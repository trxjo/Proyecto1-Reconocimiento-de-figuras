import cv2
import numpy as np
import os
#Creamos el banco de imagenes solicitadas en el proyecto para poder probarlas
#Y ver que funcionen correctamente
def crear_banco_imagenes(directorio_salida="imagenes_prueba"):

    os.makedirs(directorio_salida, exist_ok=True)
    
    # 1. Configuración general
    ancho, alto = 800, 600
    color_fondo = (224, 224, 224) # Gris claro en BGR (Hex: #E0E0E0)
    
    # De acuerdo con la escala BGR inicializaremos cada color para poder asignarlo a una figura
    colores = {
        "rojo": (0, 0, 255),
        "verde": (0, 200, 0),
        "azul": (255, 0, 0),
        "amarillo": (0, 215, 255),
        "magenta": (255, 0, 255),
        "cian": (255, 255, 0),
        "naranja": (0, 128, 255),
        "morado": (128, 0, 128)
    }

    # Imagenes de Prueba
    escenas = [
        {
            "nombre": "imagenPrueba_1.bmp",
            "figuras": [
                {"tipo": "circulo", "centro": (200, 300), "radio": 80, "color": colores["rojo"]},
                {"tipo": "triangulo", "puntos": [(400, 150), (350, 350), (500, 350)], "color": colores["verde"]},
                {"tipo": "cuadrilatero", "puntos": [(580, 200), (720, 200), (720, 380), (580, 380)], "color": colores["azul"]}
            ]
        },
        {
            "nombre": "imagenPrueba_2.bmp",
            "figuras": [
                {"tipo": "poligono", "puntos": [(150, 150), (250, 100), (200, 300), (100, 250)], "color": colores["amarillo"]}, 
                {"tipo": "poligono", "puntos": [(350, 200), (500, 200), (550, 350), (300, 350)], "color": colores["magenta"]}, 
                {"tipo": "poligono", "puntos": [(600, 400), (700, 450), (650, 550), (550, 500)], "color": colores["cian"]}    
            ]
        },
        {
            "nombre": "imagenPrueba_3.bmp",
            "figuras": [
                {"tipo": "circulo", "centro": (150, 150), "radio": 60, "color": colores["naranja"]},
                {"tipo": "circulo", "centro": (650, 450), "radio": 100, "color": colores["morado"]},
                {"tipo": "triangulo", "puntos": [(300, 400), (450, 400), (300, 200)], "color": colores["rojo"]}, 
                {"tipo": "triangulo", "puntos": [(550, 100), (500, 250), (650, 200)], "color": colores["verde"]} 
            ]
        },
        {
            "nombre": "imagenPrueba_4.bmp",
            "figuras": [
                {"tipo": "circulo", "centro": (150, 400), "radio": 75, "color": colores["azul"]},
                {"tipo": "poligono", "puntos": [(350, 100), (450, 100), (500, 250), (400, 350), (300, 250)], "color": colores["amarillo"]},
                {"tipo": "poligono", "puntos": [(650, 150), (675, 230), (750, 230), (690, 280), (715, 360), (650, 310), (585, 360), (610, 280), (550, 230), (625, 230)], "color": colores["magenta"]}
            ]
        },
        {
            "nombre": "imagen_05_mixta_compleja.bmp",
            "figuras": [
                {"tipo": "circulo", "centro": (120, 120), "radio": 50, "color": colores["cian"]},
                {"tipo": "triangulo", "puntos": [(300, 80), (220, 220), (380, 220)], "color": colores["naranja"]},
                {"tipo": "cuadrilatero", "puntos": [(500, 100), (700, 100), (700, 220), (500, 220)], "color": colores["morado"]},
                {"tipo": "poligono", "puntos": [(100, 350), (250, 350), (280, 500), (150, 550), (70, 450)], "color": colores["verde"]}, # Pentágono (X)
                {"tipo": "poligono", "puntos": [(400, 350), (520, 300), (600, 420), (480, 500)], "color": colores["rojo"]} # Cuadrilátero irregular (C)
            ]
        }
    ]

    # 2. Generación y guardado de imágenes
    for idx, escena in enumerate(escenas, start=1):
        # Crear lienzo plano
        img = np.full((alto, ancho, 3), color_fondo, dtype=np.uint8)
        
        for fig in escena["figuras"]:
            color = fig["color"]
            if fig["tipo"] == "circulo":
                # Aqui se verifica si una figura es circulo, si lo es, dibujael circulo sin
                # anti-alaising y poder conectarlo a 4 vecinos (Line_4)
                cv2.circle(img, fig["centro"], fig["radio"], color, -1, lineType=cv2.LINE_4)
            elif fig["tipo"] in ["triangulo", "cuadrilatero", "poligono"]:
                # Se encarga de reformar o reorganizar la figura para poder obtener los
                # vertices de una manera mas senciila y para poder ver
                # imagen en una matriz
                pts = np.array(fig["puntos"], np.int32).reshape((-1, 1, 2))
                cv2.fillPoly(img, [pts], color, lineType=cv2.LINE_4)

        # Guardar en formato BMP
        ruta_archivo = os.path.join(directorio_salida, escena["nombre"])
        cv2.imwrite(ruta_archivo, img)
        print(f"[{idx}/5] Imagen guardada exitosamente: {ruta_archivo}")

if __name__ == "__main__":
    crear_banco_imagenes()