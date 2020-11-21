#nesta aula vamos aprneder usar o while
#WHILE , vamos o while para criar uma matriz
#olha que massa vamos aprender a funcianalidade do while
#e aprender como criar uma matriz com python

import random

def Matriz(linhas, colunas):
    matriz = []
    linha = []
    try:
        while len(matriz) != linhas:
            valor = random.randint(0, 101)
            linha.append(valor)

            if len(linha) == colunas:
                matriz.append(linha)
                linha = []
        return matriz
    finally:
        matriz_variavel = matriz
        for k in matriz_variavel:
            print(k)

Matriz(2, 3)