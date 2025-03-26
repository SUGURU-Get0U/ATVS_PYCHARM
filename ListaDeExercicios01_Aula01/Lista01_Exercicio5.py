# Calcular sua idade em Meses



while True:
    try:
        InfoAno = int(input("Digite o seu ano de nascimento: "))
        if InfoAno <= 0:
            print("O ano tem que ser maior que 0")
            continue
        break
    except ValueError:
        print("O ano deve ser um número")

anoAtual = 2025

Idade = anoAtual - InfoAno
IdadeMeses = Idade * 12

print(f'voce tem {IdadeMeses:.1f} meses')






