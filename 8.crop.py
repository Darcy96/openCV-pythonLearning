import numpy as np
import argparse
import cv2

# libreria definir argumentos externos de ejecución
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
# se almacena en un diccinario todos los parametros de entrada que el
args = vars(ap.parse_args())
# entonces despues del código anterior debemos ejecutar este archivo pasando
# argumentos definidos anteriormente
#escriba esto al finalizar el ejercicio -> python 8.crop.py -i ./imagenes/pythonYellow.jpg

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

cropped = image[170:280, 250:380]#[y1:y2, x1:x2] coordenadas a recortar
##en la carpeta imagenes hay una breve explicacion de como estan las coordenadas organizadas
#y como se "recorta"

cv2.imshow("Phyton Face", cropped)
cv2.waitKey(0)

cropped = image[170:380, 250:480]#[y1:y2, x1:x2] coordenadas a recortar
cv2.imshow("Phyton Face and Head", cropped)
cv2.waitKey(0)

