import time 

# tupla = tuple()
tupla = (1)

tupla = (1,)

tupla = 1, 2, 3
print(tupla)

print(tupla[1])

# tupla[0] = 100  erro pois não é possivel alterar uma tupla

# Manipulando dicionários

dic = {"semMundial":"Palmeiras", "1mundial":"Corinthians", "2mundiais":"SaoPaulo"}

print(dic["semMundial"])

notas = {"Mat":5, "Lp":10, "Ef":8}

print(notas)
print(notas["Lp"])

#print(notas["bio"])

print(dir(notas))

print(notas.values())

print(notas.keys())

print(len(notas))

for disciplina in notas.keys():
    print(disciplina)


time.sleep(3)
