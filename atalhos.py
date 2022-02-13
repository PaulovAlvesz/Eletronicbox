
n = int(input("Digite o Numero de Pessoas: "))

cont = 0

while cont <= n:
		
	dia = int(input("Pessoa %i Digite o dia de seu Nascimento: "%(cont+1)))
	mes = int(input("Digite o mes Agora da Pessoa %i : "%(cont+1)))
	ano = int(input("Digite o Ano da Pessoa %i : "%(cont+1)))
	idade = int(input("Digite a Idade da Pessoa %i a ser completada: "%(cont+1)))
	
	cont += 1
	
	print("A pessoa %i fara %i anos no dia %i/%i/%i"%(cont, idade, dia, mes, idade + ano))
	
	print("a pessoa {} fara {} anos nesse ano . ".format(cont, 2021 - 2004))
	
	
	
print("Você fara", idade, 'no dia', dia, '/', mes,'/', ano + idade)




#"atalhos"estre asspassssss

# 1 × 2 × 3 == 6
# 2 × 3 × 4 == 24
# 3 × 4 × 5 == 69

#num = int(input("Digite um Nunero: "))

#i, j, k = 1, 2, 3
#ou i = 1, 2, 3
#i * (i + 1)
#

#while i * j * k < num:
#	i += 1
#	j += 1
#	k += 1
#if i * j * k != num:
#	print(num,"Não é triangular")
#else :
#	print(num, "ele é Triangular")