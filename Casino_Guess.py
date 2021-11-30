#Damian Oportus

#Casino Game: Guess the number
import random

def guess(n):
    attempts = 1
    r = random.randrange(1, 10)
    while n != r:
        attempts = attempts + 1
        if n < r:
            n = int(input("Try higher: "))
        elif n > r:
            n = int(input("Try lower: "))
    if n == r:
        print("Props to you! It took you: " + str(attempts) + " tries")
        ans = input(("Do you want to play again? "))
        if ans == 'yes':
            x = int(input("Enter a number from 1 to 10: "))
            guess(x)  
        elif ans == 'no':
            print("Adios!")
        else:
            x = int(input("Enter a number from 1 to 10: "))
            guess(x)  
        
        
print("Game: Guess the number I'm thinking of")          
x = int(input("Enter a number from 1 al 10: "))
guess(x)





