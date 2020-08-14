
'''
Haremos una matriz 3D (tridimensional) con este código a continuación. 
Aquí organizaré los números del 0 al 44 como tres matrices bidimensionales de forma 3 × 5. 
El orden de las dimensiones es x>filas que se representan por la cantidad de listas 
que hay en la gran lista, y>columnas que se representan por la cantidad de listas de cada fila y
z>capas que representan la cantidad de elementos en las posiciones verticales. 
'''
import numpy as np
x = np.arange(45).reshape(3,3,5)
print(x)
#output:
'''
array([[[ 0,  1,  2,  3,  4],
        [ 5,  6,  7,  8,  9],
        [10, 11, 12, 13, 14]],

       [[15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29]],

       [[30, 31, 32, 33, 34],
        [35, 36, 37, 38, 39],
        [40, 41, 42, 43, 44]]])
        '''
print(x.shape)
