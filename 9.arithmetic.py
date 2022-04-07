from __future__ import print_function
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
# escriba esto al finalizar el ejercicio -> python 9.arithmetic.py -i ./imagenes/pythonYellow.jpg

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# En las siguientes dos lineas definimos 2 matrices de enteros de 8 bits (rango de [0, 255]).
# la primera matriz tiene un solo valor de 200 y el segundo de 100
# la funcion cv2.add es para sumar matrices
# la funcion cv2.subtract es restar matrices

print("max of 225:{}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("max of 0:{}".format(cv2.subtract(
    np.uint8([50]), np.uint8([100]))))
# el ejercicio anterior nos muestra que al realizar la suma y la resta no nos entrega 300 y -50 como
# lo haría una suma y una resta normalmente, nos entrega 255 y 0, ya que la matriz es de 8 bits
# y debe estar en ese rango. lo anterior pasa solo si lo hacemos con cv2.add o cv2.subtract


#En el caso de realizar operaciones con los modulos de numpy este proceso cambia
print("wrap around:{}".format(np.uint8([200]) + np.uint8([100])))# en este caso donde debería dar
#300 nos da 44, ya que cuando el número 255 es alcanzado, en este caso de 255 a 300 hacen falta 45
#pero como empezamos desde 0 sería 44. (lo que yo haría es hacer una resta de 300-255 y restarle 1)
print("wrap around:{}".format(np.uint8([50]) - np.uint8([100])))
#en este caso nos debería dat -50 pero cuando el 0 es alcanzado realiza lo contrario y empieza a contar
#regresivamente desde 255, (en este caso lo que yo haría es restar 255-|50| y sumarle 1 y ya me da 206)

#LO ANTERIOR ES CONFUSO AUN.

##INTENTAR CON LOS SIGUIENTES 
print("wrap around:{}".format(np.uint8([60]) + np.uint8([200])))
#(en este caso lo que yo haría es restar 260-255 y restarle 1 y ya daría lo que sale en consola)
print("wrap around:{}".format(np.uint8([30]) - np.uint8([90])))
#(en este caso lo que yo haría es restar 255-|60| y sumarle 1 y ya daría lo que sale en consola)

#resultados en consola
#max of 225:[[255]]
#max of 0:[[0]]
#wrap around:[44]
#wrap around:[206]
#wrap around:[4]
#wrap around:[196]