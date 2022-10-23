import matplotlib.pyplot as plt

def recolha(populacao):
    # /storage/emulated/0/Download/myheart.cs
    file = open("myheart.csv", "r")
    file.readline()
    stop = True
    while stop:
        linha = file.readline()
        if linha == "":
            stop = False
        else:
            lista = linha.split(",")
            lista[5] = lista[5].replace("\n", "")
            pessoa = (lista[0], lista[1], lista[2], lista[3], lista[4], lista[5])
            populacao.append(pessoa)
    return populacao


def max(populacao, i):
    max = -9999999999999999999999999999
    for pessoa in populacao:
        a = int(pessoa[i])
        if a > max:
            max = a
    return max


def min(populacao, i):
    min = 9999999999999999999999999999
    for pessoa in populacao:
        a = int(pessoa[i])
        if a < min:
            min = a
    return min


def criarniveis(populacao, j, tam):
    a = max(populacao, j)
    b = min(populacao, j)
    b = b - 1
    niveis = []
    while a > b:
        i = 0
        lista = list(range(0, tam))
        while i < len(lista):
            lista[i] = b + 1
            b = lista[i]
            i += 1
        niveis.append(lista)
    return niveis


def dds(populacao):
    distdoesex = [["M", 0], ["F", 0]]
    distsex = [["M", 0], ["F", 0]]
    d = 0
    nd = 0
    for pessoa in populacao:
        idade, sexo, tensao, colesterol, batimento, temdoenca = pessoa
        temdoenca = int(temdoenca)
        if temdoenca == 0:
            nd += 1
            for grupo in distsex:
                if sexo in grupo:
                    grupo[-1] += 1
        if temdoenca == 1:
            d += 1
            for grupo in distdoesex:
                if sexo in grupo:
                    grupo[-1] += 1
    print("doentes: ", d, "total: ", d + nd)
    print("doentes: ", distdoesex)
    print("nao doentes: ", distsex)
    for i in range(len(distdoesex)):
        grupod = distdoesex[i]
        grupond = distsex[i]
        grupond[-1] = grupond[-1] + grupod[-1]
    return [distdoesex,distsex]


def ddi(populacao, tam):
    distdoeida = criarniveis(populacao, 0, tam)
    for i in distdoeida:
        i.append(0)
    distida = criarniveis(populacao, 0, tam)
    for i in distida:
        i.append(0)
    d = 0
    nd = 0
    for pessoa in populacao:
        idade, sexo, tensao, colesterol, batimento, temdoenca = pessoa
        temdoenca = int(temdoenca)
        idade = int(idade)
        if temdoenca == 0:
            nd += 1
            for grupo in distida:
                if idade in grupo:
                    grupo[-1] += 1
        if temdoenca == 1:
            d += 1
            for grupo in distdoeida:
                if idade in grupo:
                    grupo[-1] += 1
    print("doentes: ", d, "total: ", d + nd)
    for i in range(len(distdoeida)):
        grupod = distdoeida[i]
        grupond = distida[i]
        print(grupod[0], "-->", grupod[-1], grupond[-1] + grupod[-1])
    for i in range(len(distdoeida)):
        grupod = distdoeida[i]
        grupond = distida[i]
        grupond[-1] = grupond[-1] + grupod[-1]
    return [distdoeida,distida]


def ddc(populacao, tam):
    distdoecol = criarniveis(populacao, 3, tam)
    for i in distdoecol:
        i.append(0)
    distcol = criarniveis(populacao, 3, tam)
    for i in distcol:
        i.append(0)
    d = 0
    nd = 0
    for i in populacao:
        idade, sexo, tensao, colesterol, batimento, temdoenca = i
        temdoenca = int(temdoenca)
        colesterol = int(colesterol)
        if temdoenca == 0:
            nd += 1
            for grupo in distcol:
                if colesterol in grupo[0:-2]:
                    grupo[-1] += 1
        if temdoenca == 1:
            d += 1
            for grupo in distdoecol:
                if colesterol in grupo[0:-2]:
                    grupo[-1] += 1
    print("doentes: ", d, "total: ", d + nd)
    for i in range(len(distdoecol)):
        grupod = distdoecol[i]
        grupond = distcol[i]
        print(grupod[0], "-->", grupod[-1], grupond[-1] + grupod[-1])
    for i in range(len(distdoecol)):
        grupod = distdoecol[i]
        grupond = distcol[i]
        grupond[-1] = grupond[-1] + grupod[-1]
    return [distdoecol,distcol]

def graficar(LISTAO):
    max = 0
    i = 0
    for listadelistas in LISTAO:
        lista1 = listadelistas[1]
        x = []
        y = []
        if type(lista1[0]) == str:
            for lista in listadelistas:
                x.append(lista[0])
                y.append(lista[-1])
            print(x,y)
            if i == 0:
                plt.plot(x, y, color='white', linestyle='dashed', linewidth=1, marker='o', markerfacecolor='orange',
                         markersize=10)
            else:
                plt.plot(x, y, color='white', linestyle='dashed', linewidth=1, marker='o', markerfacecolor='green',
                         markersize=10)
            for lista in listadelistas:
                if lista[-1] > max:
                    max = lista[-1]
            print(max)
            plt.ylim(0, (max + max / 4))
            plt.xlabel('DOENTES(laranja) e TOTAL(verde)')
            plt.ylabel('FREQUENCIA')
            i += 1
        if type(lista1[0]) == int:
            for lista in listadelistas:
                x.append(lista[0])
                y.append(lista[-1])
            print(x, y)
            if i == 0:
                plt.plot(x, y, color='orange', linestyle='dashed', linewidth=1, marker='o', markerfacecolor='green',markersize=4)
            else:
                plt.plot(x, y, color='green', linestyle='dashed', linewidth=1, marker='o', markerfacecolor='orange',markersize=4)
            for lista in listadelistas:
                if lista[-1] > max:
                    max = lista[-1]
            print(max)
            plt.ylim(0, (max + max / 4))
            plt.xlabel('DOENTES(laranja) e TOTAL(verde)')
            plt.ylabel('FREQUENCIA')
            i += 1
    plt.show()

########################################################################################################################################

populacao = []
recolha(populacao)
escolha = 1

while escolha != 0:
    escolha = int(input("""
(1) distribuição doença sexo
(2) distribuição doença idade
(3) distribuição doença colesterol
(0) terminar programa
"""))
    print("")
    if escolha == 1:
        dds(populacao)
        graficar(dds(populacao))
    if escolha == 2:
        j = int(input("grupos de quantas pessoas: "))
        ddi(populacao, j)
        graficar(ddi(populacao, j))
    if escolha == 3:
        j = int(input("grupos de quantas pessoas: "))
        ddc(populacao, j)
        graficar(ddc(populacao, j))

print("programa terminado")
