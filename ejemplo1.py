# Author: Jose Angel Garcia Gomez
# Date: 27/10/2020
# Description: Example of how to reed an image and display it on the screen

import cv2

if __name__ == "__main__":
    imagen = cv2.imread("imagen.jpg")
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    print(imagen.shape)
    print(imagen[0][0][0])
    imagen = cv2.resize(imagen, (256, 256))

    imagen = cv2.cvtColor(imagen, cv2.COLOR_RGB2BGR)

    cv2.imwrite("resizeimagen.jpg", imagen)

    imagen = cv2.imread("imagen.jpg")
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("grayimagen.jpg", imagen)
