# ESCREVA UM ALGORITIMO EM PYTHON PARA CALCULAR O VALOR, EM REAIS, QUE DEVE SER PAGO
# POR UM CLIENTE DE UMA LOCADORA DE CARROS. SABE-SE QUE:
# O VALOR DE LOCAÇÃO DE CADA CARRO É 100,00
# O CLIENTE PODE LOCAR UM UNICO CARRO POR VARIOS DIAS.





DiasDeLocacao = int(input('Digite por quantos dias voce ira alugar o carro: '))

Carro = 100.00

PrecoPagar = DiasDeLocacao * Carro
PrecoPagar = round(PrecoPagar, 1)

print('OKAY, O preco para alugar o carro por', DiasDeLocacao, 'dias sera de ', PrecoPagar, 'reais')