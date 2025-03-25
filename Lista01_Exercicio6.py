# Calcular o preço de um produto por quilo

ValorKilo = float(input("Digite o valor do quilo: "))
PesoProduto = float(input("Digite o peso de produto: "))

ValorTotal = PesoProduto / ValorKilo

print(f"O preço é de: R${ValorTotal:.2f} reais")