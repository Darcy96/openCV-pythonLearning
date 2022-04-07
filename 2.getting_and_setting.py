from __future__ import print_function
import argparse
import cv2

# libreria definir argumentos externos de ejecución 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
# se almacena en un diccinario todos los parametros de entrada que el
args = vars(ap.parse_args())
# entonces despues del código anterior debemos ejecutar este archivo pasando
# argumentos definidos anteriormente
#escriba esto al finalizar el ejercicio -> python 2.getting_and_setting.py -i ./imagenes/pythonYellow.jpg
image = cv2.imread(args["image"])

#cv2.imshow("Original", image)
# cv2.waitKey(0)

# nos trae el pixel localizado en la esquina superior de la imagen,
(b, g, r) = image[0, 0]
# representado como una tupla, se debe tener en cuenta que este esta en modo BGR y no RGB
# Pixel at (0,0) -Red: 15, Green:39, Blue:41
print("Pixel at (0,0) -Red: {}, Green:{}, Blue:{}".format(r, g, b))
# blue color (rgb) //aqui vamos a setear el valor que queremos en la tupla en el punto 0,0
image[0, 0] = (0, 0, 255)
# pero en este caso no sería azul si no rojo porque recordemos que se lee como BGR
(b, g, r) = image[0, 0]  # Pixel at (0,0) -Red: 255, Green:0, Blue:0
print("Pixel at (0,0) -Red: {}, Green:{}, Blue:{}".format(r, g, b))
cv2.imshow("Original", image)
cv2.waitKey(0)

# y SI no solamente queremos acceder a un pixel si no  a un conjunto de esos que forman un gran rectángulo
# se hace así:

corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)
cv2.waitKey(0)

image[0:100, 0:100] = (128, 0, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)
