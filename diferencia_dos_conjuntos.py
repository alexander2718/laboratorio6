#Diferencia entre 2 conjuntos
A = {1,2,3,4,5}
B = {4,5,25,100,125}

# A-B
diferencia = A.difference(B)
#B-A
diferencia1 = B.difference(A)

print('La diferencia de los conjuntos: {} y {} es: {}'.format(A,B,diferencia))
print('La diferencia de los conjuntos: {} y {} es: {}'.format(B,A,diferencia1))