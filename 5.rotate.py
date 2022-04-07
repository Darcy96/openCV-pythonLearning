import numpy as np
import argparse
import imutils
import cv2

# libreria definir argumentos externos de ejecución
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
# se almacena en un diccinario todos los parametros de entrada que el
args = vars(ap.parse_args())
# entonces despues del código anterior debemos ejecutar este archivo pasando
# argumentos definidos anteriormente
#escriba esto al finalizar el ejercicio -> python 5.rotate.py -i ./imagenes/pythonYellow.jpg

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#las dos siguientes lineas es para sacar el centro de la imagen
(h, w) = image.shape[:2]
center = (w//2, h//2) # se usa // para asegurarnos de que la division nos entregue un entero

M = cv2.getRotationMatrix2D(center, 45, 1.0)
#esta funcion recibe, el punto el cual usaremos para rotar la imagen a su alrededor, luego los grados
#en este caso son 45 grados y el 3 parametro significa que usaremos las mismas dimensiones de la imagen
rotated = cv2.warpAffine(image, M,(w,h))
cv2.imshow("Rotated by 45 Degress", rotated)
cv2.waitKey(0)

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated by -90 Degrees", rotated)
cv2.waitKey(0)

###aplicando la funcion creada en el archivo imutils
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotaded by 180 Degres", rotated)
cv2.waitKey(0)
