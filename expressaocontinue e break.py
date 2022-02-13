
#marcar o inicio 'opcional''
print()
#pular linhas opcional
print("Inicio")

print()



#criar uma loop e uma condiçao , com atribuicao na variavel

i = 0

#variavel criada 


while(i < 10):
	
	#ciclo while feito
	i = i + 1
	
	if (i % 2 == 0):
		
		# condição estabelecida
		
		continue
		
	if i > 5:
			
			#if = se i for maior que 5 o ciclo while vai parar e a expressao else não vai ser executada.
			#break = finaliza a função if que finaliza o ciclo while
			
		break
		
		#se o if for aberto deve fechar se não a função print nao ira funcionar
			
	print(i)
	
	# o print i é para mostrar os numeros que foram classificados como False.
	
else:
	
	print("Tem numeros pares")

print()
print('Fim')