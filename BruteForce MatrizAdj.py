from math import sqrt
import time

def fatorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact = fact * num
    return(fact)


def Custo(ind, Mtrx, Rx, size):

    total = Rx[ind[0]]
    for i in range(size):
            total += Mtrx[ind[i]][ind[i+1]]
    total += Rx[ind[size]]

    return total

def GerarMatriz(lista):
    matriz = []

    for i in range(len(lista)):
        matriz.append(list())
        for j in range(len(lista)):
            matriz[i].append(sqrt(((lista[i][0] - lista[j][0]) ** 2) + ((lista[i][1] - lista[j][1]) ** 2)))

    return matriz

def GerarLRx(lista, Rc):
    LRx = []

    for i in range(len(lista)):
        LRx.append(sqrt(((lista[i][0] - Rc[0]) ** 2) + ((lista[i][1] - Rc[1]) ** 2)))

    return LRx

def permutacao(lista):
    if len(lista) <= 1:
        yield lista

    else:

        for perm in permutacao(lista[1:]):
            for i in range(len(perm) + 1):
                yield perm[:i] + lista[0:1] + perm[i:]




#######################################################################################################################################

listaNomes = []
listaCoord = []
listaIndex = []
listaFinal = []
custoMin = float('inf')


CoordR = [40.7, 53.5]#list(map(float, input("Insira as coordenadas x e y do centro de distribuiçao R, separadas apenas por espaço:\n").split()))

listaTemp = list(input("Insira o nome dos pontos de entrega e suas coordenadas no formato: Ponto1 x y, Ponto2 x y,...\n").split(", "))


for i, item in enumerate(listaTemp): # tratamento das entradas
    listaIndex.append(i)        #lista de indices a se permutar, evitando a movimentação constante de dados grandes
    subList = item.split()
    listaNomes.append(subList[0])
    listaCoord.append(list(map(float, subList[1:])))


print("Processando...")
start = time.time()

matrizAdj = GerarMatriz(listaCoord)
RtoAll = GerarLRx(listaCoord, CoordR)

limite = fatorial(i + 1) // 2
lenInput = i


for contador, perm in enumerate(permutacao(listaIndex)):
    if contador >= limite:
        break

    custoAtual = Custo(perm, matrizAdj, RtoAll, lenInput)
    if custoAtual <= custoMin:
        listaMin = perm
        custoMin = custoAtual


for t in listaMin:  # organização da lista de nomes dos pontos
    listaFinal.append(listaNomes[t])
listaFinal = ["R"] + listaFinal + ["R"]


print(f"melhor caminho é {listaFinal} custo: {custoMin}")

end = time.time()
print(end-start)