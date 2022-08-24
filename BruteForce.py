from math import sqrt
import time

def fatorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact = fact * num
    return(fact)


def distancia(k, val, R): #formula resumida da distancia, omitindo as raizes para economizar operações

    dist = (val[k[0]][0] - R[0])**2 + (val[k[0]][1] - R[1])**2

    for i in range(len(k)-1):
        dist += (val[k[i]][0] - val[k[i+1]][0])**2 + (val[k[i]][1] - val[k[i+1]][1])**2

    dist += (val[k[-1]][0] - R[0])**2 + (val[k[-1]][1] - R[1])**2
    return dist

def distancia_eclid(seq, val, R): #formula completa da distancia euclidiana


    dist = sqrt((val[seq[0]][0] - R[0]) ** 2 + (val[seq[0]][1] - R[1]) ** 2) # de R a primeiro elemento da sequencia

    for i in range(len(seq) - 1):
        dist += sqrt((val[seq[i]][0] - val[seq[i + 1]][0]) ** 2 + (val[seq[i]][1] - val[seq[i + 1]][1]) ** 2) # total dentro da sequencia

    dist += sqrt((val[seq[-1]][0] - R[0]) ** 2 + (val[seq[-1]][1] - R[1]) ** 2) # do ultimo termo da sequencia a R

    return dist


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



CoordR = list(map(float, input("Insira as coordenadas x e y do centro de distribuiçao R, separadas apenas por espaço:\n").split()))

listaTemp = list(input("Insira o nome dos pontos de entrega e suas coordenadas no formato: Ponto1 x y, Ponto2 x y,...\n").split(", "))


for i, item in enumerate(listaTemp): # tratamento das entradas
    listaIndex.append(i)        #lista de indices a se permutar, evitando a movimentação constante de dados grandes
    subList = item.split()
    listaNomes.append(subList[0])
    listaCoord.append(list(map(float, subList[1:])))


print("Processando...")
start = time.time()

limite = fatorial(i + 1) // 2

for contador, perm in enumerate(permutacao(listaIndex)):
    if contador >= limite:
        break

    custoAtual = distancia_eclid(perm, listaCoord, CoordR)
    if custoAtual <= custoMin:
        listaMin = perm
        custoMin = custoAtual


for t in listaMin:  # organização da lista de nomes dos pontos
    listaFinal.append(listaNomes[t])
listaFinal = ["R"] + listaFinal + ["R"]


print(f"melhor caminho é {listaFinal} custo: {distancia_eclid(listaMin, listaCoord, CoordR)}")

end = time.time()
print(end-start)