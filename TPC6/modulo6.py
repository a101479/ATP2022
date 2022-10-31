import csv

def modularobras(ficheiro):
    file = open(ficheiro,"r", encoding='utf-8')
    file.readline()
    csvfile = csv.reader(file,delimiter=";")
    obras = []
    for obra in csvfile:
        obras.append(obra)
    remover = "\n        "
    for obra in obras:
        obra[1] = obra[1].replace("\n        ","")
        obra = tuple(obra)
    file.close()
    return obras

def numobras(obras):
    print("O numero de obras: ",len(obras))
    return len(obras)

def tabelaobras(obras):
    print("|NOME                          |DESCRIÇÃO           |ANO                 |PERIODO             |COMPOSITOR                       |DURAÇÃO             |ID                  |")
    print("")
    for obra in obras:
        nome,descricao,ano,periodo,compositor,duracao,id = tuple(obra)
        print(f"|{nome[:30]:30}|{descricao[:20]:20}|{ano:20}|{periodo:20}|{compositor:33}|{duracao:20}|{id:20}|")

def listordalfa(obras):
    nomeano1 = []
    nomeano2 = []
    listafinal = []
    for obra in obras:
        nome, descricao, ano, periodo, compositor, duracao, id = tuple(obra)
        str = nome + ";" + ano
        nomeano1.append(str)
    nomeano1.sort()
    for conjunto in nomeano1:
        conjunto = conjunto.split(";")
        conjunto = tuple(conjunto)
        nome, ano = conjunto
        tupulo = (nome, ano)
        listafinal.append(tupulo)
        str = f"|{nome[:30]:30}    |    {ano:20}|"
        nomeano2.append(str)
    for conjunto in nomeano2:
        print(conjunto)
    return listafinal

def listordano(obras):
    anonome1 = []
    anonome2 = []
    listafinal = []
    for obra in obras:
        nome, descricao, ano, periodo, compositor, duracao, id = tuple(obra)
        str = ano + ";" + nome
        anonome1.append(str)
    anonome1.sort()
    for conjunto in anonome1:
        conjunto = conjunto.split(";")
        conjunto = tuple(conjunto)
        ano, nome = conjunto
        tupulo = (nome,ano)
        listafinal.append(tupulo)
        str = f"|{nome[:30]:30}    |    {ano:20}|"
        anonome2.append(str)
    for conjunto in anonome2:
        print(conjunto)
    return listafinal

def listordcomp(obras):
    listafinal = []
    for obra in obras:
        nome, descricao, ano, periodo, compositor, duracao, id = tuple(obra)
        listafinal.append(compositor)
    listafinal.sort()
    return listafinal

def maxmin(obras):
    max = -9999999999999999999
    min = 99999999999999999999
    for obra in obras:
        nome, descricao, ano, periodo, compositor, duracao, id = tuple(obra)
        if int(ano)>max:
            max = int(ano)
        if int(ano)<min:
            min = int(ano)
    return [max,min]

def criardicionario(obras):
    max = -9999999999999999999
    min = 99999999999999999999
    for obra in obras:
        nome, descricao, ano, periodo, compositor, duracao, id = tuple(obra)
        if int(ano) > max:
            max = int(ano)
        if int(ano) < min:
            min = int(ano)
    md = min
    dicfinal = {}
    for i in list(range(min,max+1)):
        dic = {md:0}
        md += 1
        dicfinal.update(dic)
    return dicfinal

def distano(obras,quanto):
    dic = criardicionario(obras)
    dicfinal = {}
    i = 1
    soma = 0
    for obra in obras:
        nome, descricao, ano, periodo, compositor, duracao, id = tuple(obra)
        dic[int(ano)] +=1

    max = -9999999999999999999
    min = 99999999999999999999
    for obra in obras:
        nome, descricao, ano, periodo, compositor, duracao, id = tuple(obra)
        if int(ano) > max:
            max = int(ano)
        if int(ano) < min:
            min = int(ano)
    soma = 0
    i = 0
    mp = min
    while min <= max:
        if i == quanto:
            soma += dic[min]
            somas = {mp:soma}
            dicfinal.update(somas)
            soma = 0
            i = 0
            mp = min
        else:
            soma += dic[min]
        min += 1
        i += 1
    somas = {mp: soma}
    dicfinal.update(somas)

    return dicfinal