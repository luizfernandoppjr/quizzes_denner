'''
Questao 1: (2 pontos)
Dado um parâmetro n, a funcão deve retornar True se n é primo e False caso contrário

Ex:
    11 -> True
    15 -> False
'''
def prime(n):
    x=0
    for i in range(3,n):
        if n % i==0:
            x=1
    if x==0:
        y=True
    else:
        y=False

    return y


'''
Questao 2: (2 pontos)
A entrada é uma lista de inteiros e a saida deves ser a lista sem números repetidos

Ex:
    [1,2,3,1,5,2] -> [1,2,3,5]
    [15,15,15,15] -> [15]
'''
def unicos(L):
    x=set(L)
    l=list(x)
    return l

'''
Questao 3: (3 pontos)
Seja d(n) definido como a suma dos divisores inteiros de n. Se d(a) = b e d(b) = a,
sendo a ≠ b, então a e b são um "par amigável" de números.

A funcao tem como entrada uma tupla com 2 inteiros
e saida True ou False se estes números sao um par amigável"

Ex:
    (220, 284) -> True   #Obs: d(220) = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 286, o mesmo para d(284)
    (500, 30) -> False
'''
def amigavel(ab):
    soma_de_divisores_de_a=0
    soma_de_divisores_de_b=0
    for i in range(2,ab[0]):
        if ab[0] % i==0:
            soma_de_divisores_de_a=soma_de_divisores_de_a+i
    for j in range(2,ab[1]):
        if ab[1] % j==0:
            soma_de_divisores_de_b=soma_de_divisores_de_b+j
    if soma_de_divisores_de_b==ab[0] and soma_de_divisores_de_a==ab[1]:
        y=True
    else:
        y=False
    return y


'''
Questao 4: (3 pontos)
Dada uma lista L, retorno ela ordenada. Nao usar o sort interno do python!

Ex:
    [5,8,1,2,0,3,4] - > [0, 1, 2, 3, 4, 5, 8]
    [5,4,3,2,1] -> [1, 2, 3, 4, 5]
'''
def sort(L):
    n_elementos=len(L)
    for i in range(n_elementos):
        while L[i]>L[i+1]:
            aux=L[i+1]
            L[i+1]=L[i]
            L[i]=aux
    return L
