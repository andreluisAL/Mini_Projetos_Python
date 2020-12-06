import random

class Matriz():

    def matriz(self, linhas, colunas):
        matriz = []
        linha = []
            
        while len(matriz) != linhas:
            valor = random.randint(-50, 51)
            linha.append(valor)
            
            if len(linha) == colunas:
                matriz.append(linha)
                linha = []

        return matriz
        self.matriz_variavel = matriz
    
    def soma(self, A , B):
    
        matriz1 = A
        matriz2 = B
        
        linhas1 = len(matriz1)
        colunas1 = len(matriz1[0])
    
        linhas2 = len(matriz2)
        colunas2 = len(matriz2[0])
    
        if linhas1 == linhas2 and colunas1 == colunas2:
            soma = []
            
            for aaa in matriz1:
                print(aaa)
            print('\n')
        
            for bbb in matriz2:
                print(bbb)   
            print('\n')
            
    
            for i in range(linhas1):
                linha = [0] * colunas1
                soma.append(linha)
        
                for j in range(colunas1):
                    soma[i][j] = matriz1[i][j] + matriz2[i][j]
        
            
            for ccc in soma:
                print(ccc) 
        else: 
            print('matrizes não são de mesma ordem!')
               
           
                

matrizA = Matriz()
a = matrizA.matriz(2, 2)

matrizB = Matriz()
b = matrizB.matriz(2, 2)


Soma = Matriz()
Soma.soma(a, b)

