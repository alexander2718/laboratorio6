#Diferencia simétrica de 3 conjuntos
A = {1,2,3,4,5}
B = {4,5,25,100,125}
C = {25,100,200,455}
dif = A.symmetric_difference(B)
diferencia_simetrica = dif.symmetric_difference(C)

print('La diferencia de los conjuntos: {}, {} y {} es: {}'.format(A,B,C,diferencia_simetrica))