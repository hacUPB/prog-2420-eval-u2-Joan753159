'''
Lista = [4,54,66.77,32,11,34,99,73,65,10,40,101]

cont = 0
for elem in Lista:
    cont += 1
print(f"la lista tiene {cont} elementos")


#comprobar
num_elementos = len(Lista)
print(f"usando la funcion len nos da {num_elementos}")

'''
edades []
cont = 0
while cont < 100:
    edad = randit(0,110)
    edades.append(edad)
    cont += 1
print(edades)

notas = []
for i in range(20):
    print(i)
    nota = uniform(0,0,5.00)
    notas.append(nota)
    print(f"nota = {notas[i]:0.2f}")
#print(notas)