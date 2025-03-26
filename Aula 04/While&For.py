# While loop and how does it work

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name ") #
    name = input("Enter your name: ")  ## THESE TWO ARE UNDER THE LOOP CONDITION


## HOWEVER, IF WE REMOVE THE CHANCE OF THE USER TO EXIT, WE'LL BE CREATING A INFINITE LOOP
print(f"Hello {name}")  ## YOU DON'T NEED A SPECIFIC ALGORITHM TO STOP THE LOOP


# So, a step-by-step guide to use while would be

#1 have an input
age = int(input("type in your age: "))

#2 insert the while loop for verification
while age < 0:
    print("age cant be negative") #print the problem
    age = int(input("type in your age: ")) # Give the user a way to exit the loop

print(f"You are {age} years old")