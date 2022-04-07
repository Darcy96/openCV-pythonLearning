import numpy as np
import argparse
import imutils
import cv2

# libreria definir argumentos externos de ejecución //ejm:python load_display_save.py -i ./python.jpg
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
# se almacena en un diccinario todos los parametros de entrada que el
args = vars(ap.parse_args())
#entonces despues del código anterior debemos ejecutar este archivo pasando 
#argumentos definidos anteriormente
#escriba esto al finalizar este ejercicio-> python resize.py -i ./imagenes/pythonYellow.jpg

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#cuando cambiamos el tamaño a una imagen debemos tener en cuenta la relación aspecto de esta
#la relacion aspecto es la relacion proporcional del ancho y la altura de la imagen 
#sin esto la imagen lucira mal
#la siguiente linea hace lo mencionado anteriormente
r= 150.0/image.shape[1]#en esta linea se define que el ancho de la nueva imagen será de 150 pixeles
#Para calcular el radio de la nueva altura a la altura anterior, simplemente definimos nuestra relación r 
#para que sea el ancho nuevo (150 píxeles) dividido por el ancho anterior, al que accedemos usando image.shape[1]

dim = (150, int(image.shape[0]*r))#teniendo el nuevo radio ya se pueden calcular las nuevas
#dimensiones de la imagen.
#En resumen el ancho de la nueva imagen será de 150 px y la altura es computada multiplicando
#la altura de la imagen original por nuestro radio y luego convirtiendolo a un entero.
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)#funcion para cambiar el tamaño
#recibe como primer argumento la imagen original, luego las dimensiones calculadas anteriormente
# el tercer parametro es un metodo de interpolacion que es el algoritmo que trabaja "behind the scenes"
#quien se encargara de manejar como sera el "resize" de la imagen . En este caso usar el cv2.INTER_AREA
#nos entregara un resultado agradable a la vista
cv2.imshow("Resized (Width)", resized)
cv2.waitKey(0)


#AHORA CAMBIAREMOS EL TAMAÑO DE LA IMAGEN PERO USANDO ESTA VEZ LA ALTURA
r= 50.0/image.shape[0] ##aqui usamos la posición 0 recordando que la altura se ubica en esta posición
dim = (int(image.shape[1]*r), 50)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Heigth)", resized)
cv2.waitKey(0)

##Creamos una función en imutils.py llamada resize para reutilizarla

resized = imutils.resize(image, width=100)
cv2.imshow("Resized resized via function(Width)", resized)
cv2.waitKey(0)

resized = imutils.resize(image, height=50)
cv2.imshow("Resized resized via function (Height)", resized)
cv2.waitKey(0)