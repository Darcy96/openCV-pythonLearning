import numpy as np
import argparse
import imutils
import cv2

# libreria definir argumentos externos de ejecución //ejm:python load_display_save.py -i ./python.jpg
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
# se almacena en un diccinario todos los parametros de entrada que el
args = vars(ap.parse_args())
# entonces despues del código anterior debemos ejecutar este archivo pasando
# argumentos definidos anteriormente
#escriba esto al finalizar el ejercicio -> python translation.py -i ./imagenes/pythonYellow.jpg

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

M = np.float32([[1, 0, 25], [0, 1, 50]])## definimos la matriz como un punto flotante
# el primer punto de la matriz es 1,0(indica la dirección) y el tercero recordemos que es el numero de pixeles
#que se va a mover la imagen izquierda o derecha (no entendí esta parte) 
#la segunda matriz define lo que se va a desplazar de arriba o abajo.
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))#funcion que realiza la translacion
#primer argumento es la imagen a realizar la translacion, el sgundo argumento es la Matriz de translacion definida
# anteriormente, y luego
#pasamos el ancho y el alto que en este caso usamos las mismas de la imagen.

###descomentar las siguientes dos lineas para ver
#cv2.imshow("Shifted Down and Right", shifted)
#cv2.waitKey(0)

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
#cv2.imshow("Shifted Down and Right", shifted)
#cv2.waitKey(0)

shifted = imutils.translate(image, 0, 100)#aqui le indicamos que se mueva hacia abajo 100 pixeles
cv2.imshow("shifted Down", shifted)
cv2.waitKey(0)