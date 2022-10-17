file = open("cinema.txt", "r")
parques = []
for i in file:
    i = i.split(";")
    var= i[2].split(",")
    var[0] = var[0].replace("[","")
    var[-1] = var[-1].replace("]","")
    for v in range(len(var)):
        var[v] = int(var[v])
    parque = (int(i[1]),var,str(i[3]))
    parques.append(parque)
    print(parque)
file.close()

def listar(listap):
    for i in listap:
        nlugares, ocupados, nome = i
        print("No cinema", nome, "temos:")
        print(nlugares, "lugares")
        ocupados.sort()
        print("Os lugares ocupados sao", ocupados)
        print("")
    return


def disponivel(listap, nomep, lugar):
    var = True
    check = True
    va = True
    v = True
    for i in listap:
        nlugares, ocupados, nome = i
        if nome == nomep:
            if lugar > nlugares:
                print("o lugar", lugar, "do cinema", nomep, "nao existe")
                check = False
                va = False
                v = False
            else:
                if lugar in ocupados:
                    var = False
    if check == True:
        if var == True:
            print("o lugar", lugar, "do cinema", nomep, "encontra-se disponivel")
        else:
            print("o lugar", lugar, "do cinema", nomep, "encontra-se indisponivel")
            va = False
    return va


def senta(listap, nomep, lugar):
    disp = disponivel(listap, nomep, lugar)
    if disp == True:
        for i in listap:
            nlugares, ocupados, nome = i
            if nome == nomep:
                ocupados.append(lugar)
                ocupados.sort()
                print(ocupados)
        print("")
    else:
        for i in listap:
            nlugares, ocupados, nome = i
    return ocupados


def listardisponibilidades(listap):
    for i in listap:
        nlugares, ocupados, nome = i
        print(nome)
        print(nlugares - len(ocupados))
    print("")
    return


def listarp(listap, nomep):
    for i in listap:
        nlugares, ocupados, nome = i
        if nome == nomep:
            print("cinema: ", nome)
            print("numero de lugares: ", nlugares)
            print("lugares ocupados: ", ocupados)
            print("")
    return


def libertalugar(listap, nomep, lugar):
    disp = disponivel(listap, nomep, lugar)
    if disp == False:
        for i in listap:
            nlugares, ocupados, nome = i
            if lugar > nlugares:
                print("o lugar", lugar, "do cinema", nomep, "nao existe")
            else:
                if nome == nomep:
                    ocupados.remove(lugar)
                    print("o lugar foi libertado")
                    print(ocupados)
                    print("")
    else:
        print("o lugar ja se encontra livre")
        for i in listap:
            nlugares, ocupados, nome = i
    return ocupados


def criarcinema(listap, nomep, lugar):
    par = (lugar, [], nomep)
    listap.append(par)
    return listap


def removecinema(listap, nomep):
    for i in listap:
        nlugares, ocupados, nome = i
        if nome == nomep:
            if ocupados == []:
                listap.remove(i)
    return listap


oc1 = [1, 5, 4, 3, 2]
oc2 = [1, 6, 4, 2, 10, 7]
oc3 = [4, 2]
oc4 = [15, 16, 18, 20, 3, 5, 6]
p1 = (8, oc1, "CINEMATH1")
p2 = (10, oc2, "CINEMATH2")
p3 = (5, oc3, "CINEMATH3")
p4 = (20, oc4, "CINEMATH4")
pt = parques

escolha = 20

while escolha != 0:
    escolha = int(input("""
	(1) Listar cinemas
	(2) Disponibilidade
	(3) Sentar
	(4) Listar disponibilidades
	(5) Listar um cinema
	(6) Libertar lugar
	(7) Criar cinema
	(8) Remover cinema
	"""))
    print("")

    if escolha == 1:
        listar(pt)
    if escolha == 2:
        nome = input("nome do cinema ")
        lugar = int(input("lugar: "))
        disponivel(pt, nome, lugar)
    if escolha == 3:
        nome = input("nome do cinema ")
        lugar = int(input("lugar: "))
        senta(pt, nome, lugar)
    if escolha == 4:
        listardisponibilidades(pt)
    if escolha == 5:
        nome = input("nome do cinema ")
        listarp(pt, nome)
    if escolha == 6:
        nome = input("nome do cinema: ")
        lugar = int(input("lugar: "))
        libertalugar(pt, nome, lugar)
    if escolha == 7:
        nome = input("nome do cinema: ")
        lugar = int(input("capacidade: "))
        criarcinema(pt, nome, lugar)
    if escolha == 8:
        nome = input("nome do cinema: ")
        removecinema(pt, nome)

print("Programa terminado")

file = open("cinema.txt", "w")
for p in pt:
    nlugares, ocupados, nome = p
    nlugares = str(nlugares)
    ocupados = str(ocupados)
    soma = ""
    soma = soma + ";" + nlugares + ";" + ocupados + ";" + nome + ";" + "\n"
    file.write(soma)
file.close()
