
peso = float
altura = float

# Fiz algumas pesquisas e percebi que você não deve declarar variaveis como eu fiz (peso = float),
#  porque o Python entende automaticamente o tipo de variável quando você atribui um valor.
# Então eu deveria remover as Linhas 5 e 6 para tornar o código mais suave e limpo.



print('Welcome to the BMI calculator ')


peso =  float(input('type your weight please: '))
altura = float(input('Great!, Now type your height please:  '))

imcResult = peso / (altura ** 2)
imcResult = round(imcResult, 2) # comando que vi no gemini para limitar a quantidade
#             de algarismos decimais após o cálculo do IMC (pra não ficar um número gigante)

print("Your BMI is: ", imcResult)

if imcResult <= 18.5:
    print('You are Underweight!')
elif imcResult <= 25 and  imcResult > 18.5:
    print('You the ideal weight for your health, congrats!')
elif imcResult > 25  and  imcResult <= 29.9:
    print('You are slightly overweight... ')
elif imcResult > 29.9  and  imcResult <= 34.9:
    print('You have class 1 obesity')
elif imcResult > 34.9 and  imcResult <= 39.9:
    print('You have class 2 obesity')
elif imcResult > 39.9  and  imcResult <= 40:
    print('You have class 3 SEVERE OBESITY, go see a doctor')
    # Há também um pequeno problema com este último ELIF, onde limitei a apenas 40 quando, na verdade, queria que fosse maior que 39,9 e assim por diante
    # Em vez disso, limitou a comparação à única diferença de 0,1 entre 39,9 e 40 :(
    # Também descobri que você não precisa colocar parênteses após um IF ou uma declaração de variável. Isso é legal

# Gemini fez-me sugestoes de como fazer o código funcionar melhor entao em outro arquivo eu fiz uma certificao dos Dados e um ‘loop’ para certificar
# que os Dados inseridos fazem sentido. Também melhorei a lógica dos IFS porque nao e necessario os AND que tem ali.

