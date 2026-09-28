from preprocesamiento.preprocess import preprocesar


datos = preprocesar(
    "banco_de_imagenes/img_2.bmp"
)

print("Fondo:", datos.color_fondo)

print(
    "Colores:",
    datos.colores_figuras
)

print(
    "Tamaño máscara:",
    datos.mascara.shape
)