#Criar um algoritimo que faça um robo se mover do canto
#superior esquerdo da tela para o canto inferior direito




robo = '!°•°!'
    
lista = []

for a in range(1, 10):
    lista.append("         ")

cont = 0

for j in lista:
    print(cont * j + robo + '\n')
    cont += 1
    
