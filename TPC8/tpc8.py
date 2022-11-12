import matplotlib.pyplot as plt

def inicDiferente(s1,s2):
	sb = []
	for letra in s1:
		if not letra in s2:
			sb.append(letra)
	return len(sb)

def acimaMedia(n):
	lista = []
	listamedia = []
	soma = 0
	m = n
	print(n,"NUMEROS")
	while n > 0:
		num = int(input("--->"))
		lista.append(num)
		n -= 1
	for n in lista:
		soma += n
	media = soma/m
	for n in lista:
		if n > media:
			listamedia.append(n)
	return listamedia

def merge(l1,l2):
	for num in l2:
		cond = True
		l1.append(num)
		i = len(l1) - 1
		while  cond:
			if l1[i] < l1[i-1]:
				l1[i],l1[i-1]=l1[i-1],l1[i]
			else:
				cond = False
			i -= 1
	return l1
		
def figuais(f1,f2):
	file1=open(f1)
	file2=open(f2)
	list1=[]
	list2=[]
	for linha in file1:
		list1.append(linha)
	for linha in file2:
		list2.append(linha)
	if list1 == list2:
		return True
	else:
		return False

def atores(cinemateca):
	la = []
	for filme in cinemateca:
		tit,ano,ele,gen=filme
		for ator in ele:
			if ator not in la:
				la.append(ator)
	la.sort()
	return la

def listarPorGenero(cinemateca, genero):
	lpg = []
	for filme in cinemateca:
		tit, ano, ele, gen = filme
		if genero in gen:
			lpg.append(tit)
	lpg.sort()
	return lpg

def filmePorGenero( cinemateca ):
	dist = {}
	for filme in cinemateca:
		tit, ano, ele, gen = filme
		for genero in gen:
			if genero in dist.keys():
				dist[genero] += 1
			else:
				dist[genero] = 1
	return dist

def graficar (cinemateca, dist):
	plt.bar(dist.keys(),dist.values())
	plt.show()

####################################################################################################

s1 = "Esta um bom dia..."
s2 = "Hoje e um dia alegre."
print(inicDiferente(s1,s2))
print("\n")


print(acimaMedia(5))
print("\n")


l1 = [1,2,6,9]
l2 = [3,4,7,12]
print(merge(l1,l2))
print("\n")


print(figuais("f1.txt","f2.txt"))
print("\n")


Filme1 = ("Meet the Parents", 2000, ["Ben Stiller","Robert De Niro","Blythe Danner","Teri Polo","Owen Wilson"], ["Comedy", "Drama"])
Filme2 = ("Men of Honor", 2000, ["Robert De Niro","Cuba Gooding, Jr.","Charlize Theron"], ["Biography", "Drama", "Thriller"])
Filme3 = ("Analyze That", 2002, ["Robert De Niro","Billy Crystal","Lisa Kudrow"], ["Comedy"])
CineUM = [Filme1, Filme2, Filme3]
print(atores(CineUM))
print("\n")


print(listarPorGenero(CineUM, "Comedy"))
print("\n")


dist = filmePorGenero(CineUM)
print(dist)
print("\n")


graficar(CineUM,dist)
print("\n")
