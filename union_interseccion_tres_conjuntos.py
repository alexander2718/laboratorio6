A = {1,55,100,1000,10000}
B = {5,55,555,100,55555}
C = [1, 2, 5,88,100,1548] 

#Unión de 3 conjuntos
conjunto_union = A.union(B,C)
print('La unión de los conjuntos: {}, {}, {} es: {}'.format(A,B,C,conjunto_union))

#Intersección de 3 conjuntos
conjunto_interseccion = A.intersection(B,C)
print('\nLa intersección de los conjuntos: {}, {}, {} es: {}'.format(A,B,C,conjunto_interseccion))
