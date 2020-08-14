import numpy as np
''' Resolvere el siguiente sistema de ecuaciones lineales de 3x3:

 4x + 3y + 2z =  25
-2x + 2y + 3z = -10
 3x - 5y + 2z = -4

Numpy tiene el metodo linalg.solve(), el cual, puede ser usado para encontrar 
las soluciones de un sistema de ecuaciones lineales
'''
A = np.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
B = np.array([25, -10, -4])
X = np.linalg.solve(A,B)

print(X)
#Entrega el resultado en una lista:
#[ 5.  3. -2.] donde x=5, y=3, z=-2
