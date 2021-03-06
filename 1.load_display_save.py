from __future__ import print_function
import argparse
import cv2

# libreria definir argumentos externos de ejecución 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
# se almacena en un diccinario todos los parametros de entrada que el
args = vars(ap.parse_args())
#entonces despues del código anterior debemos ejecutar este archivo pasando 
#argumentos definidos anteriormente
#escriba esto al finalizar el ejercicio -> python 1.load_display_save.py -i ./imagenes/pythonYellow.jpg

image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))#console width: 1920 pixels
print("heigth: {} pixels".format(image.shape[0]))#console heigth: 1175 pixels
print("channels: {} pixels".format(image.shape[2]))#console channels: 3 pixels  (se refiere a RGB)
#IN THIS CASE our image has a shape of (1175, 1920, 3) (#of rows x #of columns)

cv2.imshow("Image", image)#linea que muestra en una ventana el resultado con el nombre que queramos
cv2.waitKey(0)
cv2.imwrite("./resultados/newimage.jpg", image)#linea que guarda la imagen en la ubicacion y con 
#el nombre que queramos
