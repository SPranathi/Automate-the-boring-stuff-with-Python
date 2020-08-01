#Guessing a number between 1 and 20
import random
mynumber=random.randint(1,20)
name=input("Hello!what is your name: ")
print("Well "+name+",I have selected a number between 1 and 20 .Lets try to guess it.")
#ask the player to guess a number
for guess in range(1,6):
    num=int(input("Guess a number: "))
    if num<mynumber:
        print("Your guess is low.")
    elif num>mynumber:
        print("Your guess is high")
    else:
        break #guessing a correct number
if num==mynumber:
    print("Good job, "+name+" ! you have guessed the number")
else:
    print("Nope the number i was thinking of was "+mynumber)

