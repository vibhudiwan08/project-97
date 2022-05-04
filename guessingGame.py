import random
rand=random.randint(1,9)
chance=0

while chance<5 :

    guess= int(input("Enter a number between 0 to 10"))


    if (guess == rand):
        print("You Won")
        break

    elif (guess<rand):
        print("Your number is small, guess higher than :", guess)

    else :
        print("Your guess is big, guess smaller than :",guess)

    chance+=1
        
    if not chance<5:
        print("You lose", "the number is:", rand)
