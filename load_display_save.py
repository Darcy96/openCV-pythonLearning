from __future__ import print_function
import argparse
import cv2

# libreria definir argumentos externos de ejecución //ejm:python load_display_save.py -i ./python.jpg
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
# se almacena en un diccinario todos los parametros de entrada que el
args = vars(ap.parse_args())
#entonces despues del código anterior debemos ejecutar este archivo pasando 
#argumentos definidos anteriormente

image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))#console width: 1920 pixels
print("heigth: {} pixels".format(image.shape[0]))#console heigth: 1175 pixels
print("channels: {} pixels".format(image.shape[2]))#console channels: 3 pixels  (se refiere a RGB)
#IN THIS CASE our image has a shape of (1175, 1920, 3) (#of rows x #of columns)
#cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.imwrite("newimage.jpg", image)
