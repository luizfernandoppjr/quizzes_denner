"""
Dado um valor (float com 2 casas decimais), retorne a quantidade de 
notas ou moedas ([100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.5, 0.01]) 
mínimo para pagar esse valo"

Ex: quantidade(576.73) -> 15 (5 de 100.00, 1 de 50.00, 1 de 20.00, 1 de 5.00, 1 de 1.00, 
                                1 de 0.50, 2 de 0.10 e 3 de 0.01)
    quantidade(4.00) -> 4 (4 de 1.00)
"""


def quantidade(n):
    valores = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
    notas = 0
    for i in valores:
        contador = 0
        while n > i:
            notas += 1
            contador += 1
            n -= i
        if contador > 0:
            print('Há', contador, 'notas de', i)

    return notas

"""
A classe bola representa uma esfera cheia de agua (com peso 1000g por metro cubico) com um raio r 
e superfice coberta com tinta ou azul (peso 1g por metro quadrado) ou amarelo (2g por metro quadrado) 
ou vermelho (3g por cm quadrado), o paramatro da classe é uma tupla (r, cor),
a funcao da classe "peso" de deve retorna o peso total em kg da bola,
Obs: volume da espera = (4/3)*pi*(r**3), area da superfice = 4*pi*(r**2)

Ex: bola((2, "vermelho")).peso -> 33.66012533333334
    bola((3, "azul")).peso     -> 113.20709400000001
"""
class bola:
    def __init__(self, argumento):
        self.r = argumento[0]
        self.cor = argumento[1]
        self.pi = 3.14159
    def peso(self):
        if self.cor == "azul":
            saida = (4/3)*self.pi*(self.r**3) + 4*self.pi*(self.r**2)*0.001
            return saida
        elif self.cor == "amarelo":
            saida = (4 / 3) * self.pi * (self.r ** 3) + 4 * self.pi * (self.r ** 2) * 0.002
            return saida
        else:
            saida = (4 / 3) * self.pi * (self.r ** 3) + 4 * self.pi * (self.r ** 2) * 0.003
            return saida
"""
Dado um array (numpy) n x m com n >= 3 e m >= 3, qualquer A[i,j] != 0,
a funcao borda deve tornar a soma de todos os valores
da borda do array divido pelo produto de todos os valores interiores

Ex: borda(np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],   -> borda = [1,2,3,4,5,8,9,2,3,4,5,6] -> retorno = 1.2380952380952381
                    [9, 1, 1, 2],      interior = [6,7,0,1]
                    [3, 4, 5, 6]]))
                    
    borda(np.array([[2, 2, 2],
                    [2, 2, 2],   -> 8
                    [2, 2, 2]]))
"""
def borda(array):
    tamanho = np.shape(array)
    soma_borda = 0
    produto_interior = 1
    for i in range(tamanho[0]):
        for j in range(tamanho[1]):
            if (i==0 or i ==(tamanho[0]-1) or j==0 or (j==tamanho[1]-1)):
                soma_borda += array[i][j]
            else:
                produto_interior *= array[i][j]
    return (soma_borda/produto_interior)
