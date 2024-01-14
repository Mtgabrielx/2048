import random
direcao = 0
matrix = [0] * 16
disponivel = list(map(lambda x: x, range(16)))

def esquerda(matrix):
    for x in range(16):
        if (x)%4+1<4 and (matrix[x] == matrix[x+1]):
            matrix[x] = matrix[x]*2
            matrix[x+1] = 0
        if (x)%4-1>=0 and (matrix[x-1] == 0):
            matrix[x-1] = matrix[x]
            matrix[x] = 0

def cima(matrix):
    for x in range(16):
        if x-4>= 0 and (matrix[x] == matrix[x-4]):
            matrix[x-4] = matrix[x-4]*2
            matrix[x] = 0
        if x-4>= 0 and (matrix[x-4] == 0):
            matrix[x-4] = matrix[x]
            matrix[x] = 0

def baixo(matrix):
    for x in range(15,-1,-1):
        if x-4>= 0 and (matrix[x-4] == matrix[x]):
            matrix[x] = matrix[x]*2
            matrix[x-4] = 0
        if x+4<16 and matrix[x+4] == 0 :
            matrix[x+4] = matrix[x]
            matrix[x] = 0  

def direita(matrix):
    for x in range(15,-1,-1):
        if (x)%4-1>= 0 and (matrix[x-1] == matrix[x]):
            matrix[x] = matrix[x]*2
            matrix[x-1] = 0
        if (x)%4+1<4 and matrix[x+1] == 0 :
            matrix[x+1] = matrix[x]
            matrix[x] = 0  

def verificar_disponibilidade(matrix):
    disponivel = []
    for i in range(0,16):
        if matrix[i] == 0:
            disponivel.append(i)
    return disponivel

def escolha_aleatoria(matrix,disponivel):
    i = random.randint(0, len(disponivel)-1)
    matrix[disponivel[i]] = 2

while True:
    if len(disponivel)>0:
        escolha_aleatoria(matrix,disponivel)
        print(matrix)
        for x in range(16):
            if (x)%4 == 0:
                print()
            print(matrix[x],end="  ")
        direcao = input("\nDigite a direção da ação: ")
        if direcao == "a":
            for _ in range(3):
                esquerda(matrix)
        elif direcao == "w":
            for _ in range(3):
                cima(matrix)
        elif direcao == "s":
            for _ in range(3):
                baixo(matrix)
        elif direcao == "d":
            for _ in range(3):
                direita(matrix) 
        print(matrix)
        disponivel = verificar_disponibilidade(matrix)
    else:
        print("Fim de jogo, Tente novamente!")
        break