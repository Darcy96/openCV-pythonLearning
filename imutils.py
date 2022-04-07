import numpy as np
import cv2

# funcion para hacer una translacion


def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    return shifted

# funcion para hacer una rotación


def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w // 2, h//2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None #inicializamos la variable dim 
    (h, w) = image.shape[:2]# obtenemos la altura y el ancho de la imagen original

    if width is None and height is None: #nos aseguramos de que exista un valor numerico entregado a la función 
        #para el ancho y el alto
        return image

#las siguientes lineas son para computar el radio y las nuevas dimensiones segun el parametro que nos entreguen

    if width is None:
        r = height/float(h)
        dim = (int(w*r), height)
    else:
        r = width / float(w)
        dim = (width, int(h*r))

    resized = cv2.resize(image, dim, interpolation=inter)

    return resized
