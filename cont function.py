

# Criar uma lIsta e atribuir argumentos a ela , lista é assocuada no final

def soma(*lista):
	
	""""
cria uma tupla quando tem asterisco* no começo do argumento da def .	para isso nao pode usar uma variavel no ultimo print
  """
	
	print(lista)
	
#atribui um valor para a execuçao nao falahr
	
	soma_num = 0
	
#cria um ciclo com limite baseado no numero de argumentos na 'lista'
	
	for num in lista:
		
#criar uma condicao para os ciclos
		
		soma_num += num 
		
#return para fechar a função,,,.
		
	return soma_num
	
# agora atrubua os valires presentes em 'lista'
		
a = (1, 2, 3, 4)

# agora finalize a soma da definição atribuindo valores a 'lista'

print(soma(1, 2, 3, 4))
		
		
