import argparse
import cv2

# libreria definir argumentos externos de ejecución
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
# se almacena en un diccinario todos los parametros de entrada que el
args = vars(ap.parse_args())
#entonces despues del código anterior debemos ejecutar este archivo pasando 
#argumentos definidos anteriormente
#escriba esto al finalizar el ejercicio -> python 7.flipping.py -i ./imagenes/pythonYellow.jpg

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

flipped = cv2.flip(image, 1)# la funcion flip requiere dos argumentos, la imagen original y un número que
#indica hacia que lado queremos hacer el flip de la imagen 
cv2.imshow("Flipped Horizontally", flipped)
cv2.waitKey(0)

flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)
cv2.waitKey(0)

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally and vertically", flipped)
cv2.waitKey(0)


#numeros para flip, ejemplo si tenemos una imagen de una serpiente mirando hacia la derecha
#con 1 quedara mirando hacia la izquierda, con 0 quedara de cabeza mirando hacia la derecha
#con -1 quedara de cabeza mirando hacia la izquierda

