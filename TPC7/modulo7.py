import csv
import matplotlib.pyplot as plt

def leFicheiro():
    file = open ("alunos.csv", "r", encoding = "UTF8")
    file.readline()
    csv_file = csv.reader(file, delimiter = ",")
    lista = []
    for linha in csv_file:
        lista.append(tuple(linha))
    file.close()
    return lista

def distcursos(lista):
    cursos = {}
    for aluno in lista:
        if len(aluno) == 7:
            id, nome, curso, tpc1, tpc2, tpc3, tpc4 = aluno
        elif len(aluno) == 8:
            id, nome, curso, tpc1, tpc2, tpc3, tpc4, media = aluno
        else:
            id, nome, curso, tpc1, tpc2, tpc3, tpc4, media, escalao = aluno
        if curso in cursos.keys():
            cursos[curso] += 1
        else:
            cursos[curso] = 1
    return [lista,cursos]

def media(lista):
    lista1 = []
    if len(lista[1]) >= 8:
        lista1 = lista
        print("a media já foi feita")
    else:
        for aluno in lista:
            id, nome, curso, tpc1, tpc2, tpc3, tpc4 = aluno
            media1 = (int(tpc1) + int(tpc2) + int(tpc3)+ int(tpc4))/4
            aluno = list(aluno)
            aluno.append(media1)
            aluno = tuple(aluno)
            lista1.append(aluno)
        file = open("alunos.csv", "w", encoding = "UTF8")
        file.write("id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4")
        for aluno in lista1:
            id, nome, curso, tpc1, tpc2, tpc3, tpc4, media = aluno
            media = str(media)
            soma = ""
            soma = id + "," + nome + "," + curso + "," + tpc1 + "," + tpc2 + "," + tpc3 + "," + tpc4 + "," + media + "\n"
            file.write(soma)
        file.close()
    return lista1

def distescaloes(lista):
    if len(lista[1]) >= 9:
        lista1 = lista
        print("os escaloes ja foram atribuidos")
        notas = [
            ["A", 17, 18, 19, 20],
            ["B", 13, 14, 15, 16],
            ["C", 9, 10, 11, 12],
            ["D", 5, 6, 7, 8],
            ["E", 1, 2, 3, 4],
        ]
        listamedesc = []
        for aluno in lista:
            id, nome, curso, tpc1, tpc2, tpc3, tpc4, media, escalao = aluno
            for escalao in notas:
                if round(float(media)) in escalao:
                    mediaesc = (media, escalao[0])
                    listamedesc.append(mediaesc)
        distnotas = {}
        for mediaesc in listamedesc:
            media, escalao = mediaesc
            if escalao in distnotas.keys():
                distnotas[escalao] += 1
            else:
                distnotas[escalao] = 1
    else:
        lista1=[]
        notas =[
            ["A",17,18,19,20],
            ["B",13,14,15,16],
            ["C",9,10,11,12],
            ["D",5,6,7,8],
            ["E",1,2,3,4],
        ]
        if len(lista[1]) == 7:
            print("primeiro é necessario fazer a media")
            distnotas = {}
            lista1 = lista
        else:
            listamedesc = []
            for aluno in lista:
                id, nome, curso, tpc1, tpc2, tpc3, tpc4, media = aluno
                for escalao in notas:
                    if round(float(media)) in escalao:
                        mediaesc= (media,escalao[0])
                        listamedesc.append(mediaesc)
                        aluno = list(aluno)
                        aluno.append(escalao)
                        aluno = tuple(aluno)
                        lista1.append(aluno)
            distnotas = {}
            for mediaesc in listamedesc:
                media,escalao=mediaesc
                if escalao in distnotas.keys():
                    distnotas[escalao] += 1
                else:
                    distnotas[escalao] = 1
            file = open("alunos.csv", "w", encoding="UTF8")
            file.write("id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4")
            for aluno in lista1:
                id, nome, curso, tpc1, tpc2, tpc3, tpc4, media, escalao = aluno
                media = str(media)
                soma = ""
                soma = id + "," + nome + "," + curso + "," + tpc1 + "," + tpc2 + "," + tpc3 + "," + tpc4 + "," + media + "," + escalao[0] + "\n"
                file.write(soma)
            file.close()
    return [lista1,distnotas]

def graficar(n,lista):
    if n == 1:
        dist = distcursos(lista)[1]
    if n == 2:
        dist = distescaloes(lista)[1]
    x = dist.keys()
    y = dist.values()
    plt.plot(x,y)
    plt.show()

def tabelar(n,lista):
    if n == 1:
        dist = distcursos(lista)[1]
    if n == 2:
        dist = distescaloes(lista)[1]
    x = list(dist.keys())
    y = list(dist.values())
    for i in range(len(x)):
        print(f"|{x[i]:^11}-{y[i]:^11}|")







#################################################################################################################################################################################################################################################################################################################################

lista = leFicheiro()
menu = print("""
(2) Distribuição por cursos
(3) Medias
(4) Escalões
(5) Grafico da distribuição
(6) Tabela da distribuição
""")
escolha=1
while escolha != 0:
    escolha = int(input("----> "))
    if escolha == 2:
        grupo = distcursos(lista)
        lista = grupo[0]
        dist = grupo[1]
        print(dist,"<><><><><><>",lista)
        print("")
        print("")
    if escolha == 3:
        lista = media(lista)
        print(lista)
        print("")
        print("")
    if escolha == 4:
        grupo = distescaloes(lista)
        lista = grupo[0]
        dist = grupo[1]
        print(dist,"<><><><><><>",lista)
        print("")
        print("")
    if escolha == 5:
        n = int(input("""
        QUAL GRAFICO?
        (1) distribuição por cursos
        (2) distribuição por escalões
        """))
        graficar(n,lista)
        print("")
        print("")
    if escolha == 6:
        n = int(input("""
        QUAL TABELA?
        (1) distribuição por cursos
        (2) distribuição por escalões
        """))
        tabelar(n,lista)
        print("")
        print("")