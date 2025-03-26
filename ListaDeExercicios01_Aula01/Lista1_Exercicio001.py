# ESCREVA UM ALGORITIMO EM PYTHON PARA CALCULAR A IDADE DE ALGUÉM, SABENDO-SE SEU ANO DE NASCIMENTO

AnoAtual = 2025

while True:
    try:
        AnoNascimento = int(input('digite seu ano de nascimento por favor: '))
        if AnoNascimento <= 0:
            print("O ano de nascimento tem que ser um numero positivo ")
            continue
        break
    except ValueError:
        print('Input invalido, por favor digite um número')

Idade = AnoAtual - AnoNascimento

print('Sua Idade é: ', Idade)