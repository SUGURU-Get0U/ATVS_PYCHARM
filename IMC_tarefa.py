from docutils.io import Input

from imc import altura

peso = float
altura = float



print('Welcome to the BMI calculator ')
#Print('Please choose your language:')
peso =  float(input('type your weight please: '))
altura = float(input('Great!, Now type your height please:  '))

imcResult = peso / (altura ** 2)
imcResult = round(imcResult, 2) # comando q eu vi no chat gpt para limitar a quantidade
#             de algarismos decimais após o calculo do IMC (pra não ficar um número gigante)

print("Your BMI is: ", imcResult)

if (imcResult <= 18.5):
    print('You are Underweight!')
elif (imcResult <= 25 and  imcResult > 18.6):
    print('You the ideal weight for your health, congrats!')
elif (imcResult > 25  and  imcResult <= 29.9):
    print('You are slightly overweight... ')
elif (imcResult > 29.9  and  imcResult <= 34.9):
    print('You have class 1 obesity')
elif (imcResult > 34.9 and  imcResult <= 39.9):
    print('You have class 2 obesity')
elif (imcResult > 39.9  and  imcResult <= 40):
    print('You have class 3 SEVERE OBESITY, go see a doctor')

