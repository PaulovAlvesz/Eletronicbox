






""" manter a condicao e a variavel
cont = 0 , e no final a condicao cont = cont + 1

"""

n = int(input("Digite um Numero para Saber a Sua Taboada: "))

print("A tabuada de ", n , " é: ")

cont = 0

while cont < 11:
	resultado = n * cont 
	if cont < 11:
		
		print(" %i × %i = %i "%(n, cont, resultado))
		cont = cont + 1
	



#n = int(input("Digite o tamanho da sequencia: "))
#ant = int(input("Digite o numero 1 da sequencia: "))

#cont = seq = seqMAX = 1
#while cont <  n :
#	prox = int(input("digite o numero %i da sequencia: "%(cont+1)))
#	if prox > ant:
#		seq += 1
#	else:
#		if seq > seqMAX:
#			seqMAX = seq	
#		seq = 1			
#	cont += 1	
#	ant = prox
#		
#print("O Maior Seguimento da Sequencia É ", seqMAX)		



#n = int(input("Digite um Numero: "))
#aux = n
#reverso = 0

#while aux != 0:
#	reverso = reverso*10 + aux%10
#	aux //=10
#if reverso == n:
#	print(n, "é palindromo")
#else:
#	print(n, "não é Palindromo")
