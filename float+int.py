# OU USAR... ROUND... round(3.4) = 3 , round(3.7)
# == (4)

num = float(input("Digite Num: "))


if num!= int(num):
	decimal = num - int(num)
	arredondado = int(num)
	
	if decimal >= 0.5:
		arredondado += 1
		
	print(num, " É Decimal")
	print("Arredondando da: %i"%arredondado)
else:
	print(num, "é inteiro")




"""haver arredondamento ou nao haver arredondamento
"""

int1 = int(input("Digite o primeiro numero inteiro: "))
int2 = int(input("Digite o segundo numero inteiro: "))
Real = float(input("Digite um numero Real: "))

print((2*int1)*(int2/2))
print(3*int1 + Real)
print(Real**3)
