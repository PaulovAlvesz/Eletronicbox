nnotas = int(input("Digite o Numero de Notas: "))

n1 = float(input("Digite Sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite Sua terceira nota:  "))


media = (n1 + n2 + n3) / nnotas

if media == 10:
	print("Aprovadi com Distinção. ")
elif media >= 7:
	print("Aprovado.")
	print("media: %i"%media)
# ou else por ultimo
elif media < 7:
	print("Reprovado.")
	print("media: %i"%media)



float = numeros reais

# Naturais = 1, 2, 3, 4
# Inteiros = -1,0,1,2,3
#Racionais = 3/4 , 4/5 , 7/3
#Irracionais = pi , euler , 2**1/2
"""
a = 1
b = 5
c = -7

"""



# float 
n = int(input("Digite Um Numero Real: "))

soma = 0.0

for i in range(1, n+1):
	soma += i/(n - i + 1)
	
print(" A soma vale: ", soma)
	