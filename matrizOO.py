import random

class Matriz():

    def matriz(self, linhas, colunas):
        self.matriz = []
        linha = []
            
        while len(self.matriz) != linhas:
            valor = random.randint(-50, 51)
            linha.append(valor)
            
            if len(linha) == colunas:
                self.matriz.append(linha)
                linha = []

        print(self.matriz)



MatrizA = Matriz()

MatrizA.matriz(2, 2)

