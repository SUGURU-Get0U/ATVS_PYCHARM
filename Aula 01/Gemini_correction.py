print('Welcome to the BMI calculator ')

while True: # to keep asking till we get a valid response
    try:
        peso = float(input('Type your weight in kilograms: '))
        if peso <= 0:
            print('The weight must be a positive number. Please try again.')
            continue # go back to the beginning of the loop
        break # stops the loop, when we get valid inputs
    except ValueError:
        print('Invalid input, please type in a number. ')

while True: # to keep asking till we get a valid response
    try:
        altura = float(input('Great! Now type your height please: '))
        if altura <= 0:
            print('The height must be a positive number. Please try again.')
            continue # go back to the beginning of the loop
        break # stops the loop, when we get valid inputs
    except ValueError:
        print('Invalid input, please type in a number. ')

imcResult = peso / (altura ** 2)
imcResult = round(imcResult, 2)

print("Your BMI is: ", imcResult)

if imcResult <= 18.5:
    print('You are Underweight!')
elif imcResult <= 25:
    print('You have the ideal weight for your health, congrats!')
elif imcResult <= 29.9:
    print('You are slightly overweight...')
elif imcResult <= 34.9:
    print('You have class 1 obesity')
elif imcResult <= 39.9:
    print('You have class 2 obesity')
else:
    print('You have class 3 SEVERE OBESITY, go see a doctor')