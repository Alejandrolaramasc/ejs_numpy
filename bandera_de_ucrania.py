'''
RGB es la composición del color en términos de la intensidad de los colores primarios de la luz.
RGB: Red Green Blue 
Cada píxel contiene 3 bytes que representan los valores rojo, verde y azul del color del píxel.
Crearé una matriz de 100 por 200 píxels.
La biblioteca Python Imaging Library (PIL) se usa para leer y escribir datos en formatos de archivo estándar.
Así es como puedo crear una matriz para representar una imagen de:
100 píxeles de alto por 200 píxeles de ancho y 3 bytes (1 byte = 8 bits) que es lo que ocupa 1 pixel (RGB).
Las imágenes RGB generalmente se almacenan como matrices 3D de enteros sin signo de 
8 bits cada color(canal) desde 0 a 255, o sea, 256 posibilidades, ésto sale de 2^8
Una profundidad de 8 bits por canal son 24 bits (8x3=24).
Cada canal se representa con 256 números binarios distintos 
(en matemáticas es una variación repetición: 2 elevado a 8)
00000000
00000001
00000010
00000011
00000100
........
11111111
Como son 3 canales (rojo, verde y azul) el resultado es 16.777.216 tonos distintos (256x256x256=16.777.216).
Por lo tanto, mezclando los canales rojo, verde y azul (RGB) en distintas proporciones obtenemos todos los colores.
'''
import numpy as np
from PIL import Image
#1ro debo crear un arreglo 3D sólo con ceros
array = np.zeros([100, 200, 3], dtype=np.uint8)
#Ahora debo asignar un trio ordenado (x, y, z) de una matriz 3D del RGB a cada mitad del array
array[0:50,:] = [0, 0, 255] #lado superior es azul
array[50:100,:] = [255, 240, 50] #lado inferior es amarillo
print(array.shape)

img = Image.fromarray(array)
img.save('bandera_de_ucrania.png')
#¡Les aparecerá la bandera de Ucrania en su directorio!