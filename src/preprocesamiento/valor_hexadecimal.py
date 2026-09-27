import cv2 as cv

img = cv.imread(
    '../../img/imagen-de-prueba.png')
imagen_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Casos del rango de rojo de la escala HSV
rojo_bajo = (0, 150, 150)
rojo_alto = (10, 255, 255)

# Casos del rango de azul de la escala HSV
azul_bajo = (110, 150, 150)
azul_alto = (130, 255, 255)

# Mascaras para encontrar los colores y comparar
mask_rojo = cv.inRange(imagen_HSV, rojo_bajo, rojo_alto)
mask_azul = cv.inRange(imagen_HSV, azul_bajo, azul_alto)
res_rojo = cv.bitwise_and(img, img, mask=mask_rojo)
res_azul = cv.bitwise_and(img, img, mask=mask_azul)

# como ya tenemos los colores exectraidos, los convertimos a rojo_bajo
color_hexadecimal_rojo = res_rojo[mask_rojo == 255]
if len(color_hexadecimal_rojo):
    b, g, r = color_hexadecimal_rojo[0]
    color_hexadecimal_rojo = f"{r:02x}{g:02x}{b:02x}"

print(f"Color hexadecimal: {color_hexadecimal_rojo}")
cv.imshow("imagen", res_rojo)
cv.waitKey(0)
cv.destroyAllWindows()
