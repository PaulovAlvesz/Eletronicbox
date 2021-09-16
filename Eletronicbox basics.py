
##### Primei pedimos uma quantia inicial de saqye , que seja maior que zero e menor que 600 reais.

saque = int(input("Digite o Valor de Saque ate R$ 600,00: "))

# adicionamos as variaveis para os comandos if funcionarem

notas_dez =  saque // 100 // 10
moedas_umreal = saque // 100 // 10 // 1

print("voce ira receber")


if 10 <= saque <= 600:
	notas_cem = saque // 100
	saque = saque % 100
	
#	notas_dez = saque // 10 para baixo line 16
#	saque = saque % 10
	
	notas_cinquenta = saque // 50
	saque = saque % 50

	
	notas_cinco = saque // 5
	saque = saque % 5
	
	notas_dois = saque // 2
	saque = saque % 2

	
	notas_um = saque // 1 
	
	if notas_cem > 0:
		print(notas_cem,"notas de R$ 100")
	if notas_cinquenta > 0:
		print(notas_cinquenta, "notas de R$ 50")
	if notas_dez > 0:
		print(notas_dez, "notas de R$ 10")
	if notas_cinco > 0:
		print(notas_cinco, " notas de R$ 5,00")
	if notas_dois > 0:
		print(notas_dois, "notas de R$ 2")
	if notas_um > 0:
		print(notas_um, "notas de R$ 1")
if saque > 600:
		print("você so pode sacar um valor abaixo de R$ 600,00")
if saque <= 1:
		print("digite um valor acima de R$ 1")
	

	
#print(" voce pegou ", notas_cem,"notas de cem",notas_dez,"notas de dez e",moedas_umreal,"moedas de um real")




#n1 = int(input("digite um numero"))
#n2 = int(input("agora digite outro))
#n3 = int(input("so mais umzinho baitola"))

#if n1 < n2 < n3:
#	
