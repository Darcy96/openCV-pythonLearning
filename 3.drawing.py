import numpy as np  # creamos un alias de numpy como np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
# el comando zp.zeros es para construir un array, en este caso uno con 300 filas y 300 columnas
# o sea una imagen de 300*300 pixeles y el otro valor "3" indicamos el numero de canales o sea RGB
# lo que hace esa linea en resumen es llenar cada elemento en la lista con un valor inicial de 0.
# el segundo parametro, dtype, indica que como vamos a usar imagen RGB con pixeles entre los rangos
# [0, 255], es importante que usemos un entero no asignado de 8 bits.(no entendí muy bien ese segundo
# parametro)

green = (0, 255, 0)  # tupla para representar el color verde
cv2.line(canvas, (0, 0), (300, 300), green)
# luego se dibuja una linea desde el punto 0,0(esquina superior izquierda)
# hastaa la esquina inferior derecha (300,300)
# el primer argumento refiere a la imagen donde vamos a dibujar, luego el punto de inicio
# despues el punto final, el cuarto argumento es el color que deseamos que tenga
# el quinto argumento es el grosor de la linea(thickness) en este caso tiene 3 pixeles de grosor.
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
#
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
# BGR
navy = (128, 0, 0)
crimson = (60, 20, 220)
orange = (0, 140, 255)


# DIBUJAR UN RECTANGULO
cv2.rectangle(canvas, (10, 10), (60, 60), navy)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), crimson, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (200, 50), (225, 125), orange, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# DIBUJAR UN CÍRCULO

canvas = np.zeros((300, 300, 3), dtype="uint8")#reinicializamos la imagen
(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)##calculamos dos variables que se seran llenadas
#respectivamente con las coordenadas del centro de la imagen, que se calculan mediante el resultado del
#shape de numpy y luego dividiendo por 2, la altura de la imagen se encuentra en  canvas.shape[0]
#y el ancho  en canvas.shape[1]
white = (255, 255, 255)#tupla del color blanco

for r in range(0, 150, 25): #se hce un bucle sobre unos valores de radios, comenzando desde 0 y 
    #terminando en 150(incrementando de 25 en cada paso)
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
