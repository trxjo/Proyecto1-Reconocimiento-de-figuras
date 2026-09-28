import cv2


class FiguraDetectada:

    def __init__(
        self,
        mascara,
        x,
        y,
        ancho,
        alto,
        area,
        centroide
    ):
        self.mascara = mascara
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.area = area
        self.centroide = centroide


def detectar_figuras(mascara):

    num_labels, labels, stats, centroids = (
        cv2.connectedComponentsWithStats(
            mascara,
            connectivity=8
        )
    )

    figuras = []

    for i in range(1, num_labels):

        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        ancho = stats[i, cv2.CC_STAT_WIDTH]
        alto = stats[i, cv2.CC_STAT_HEIGHT]
        area = stats[i, cv2.CC_STAT_AREA]

        centroide = tuple(centroids[i])

        mascara_figura = (
            labels == i
        ).astype("uint8")

        figura = FiguraDetectada(
            mascara_figura,
            x,
            y,
            ancho,
            alto,
            area,
            centroide
        )

        figuras.append(figura)

    return figuras