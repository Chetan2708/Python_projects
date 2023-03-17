import random
name = input("What is your name?\n")
print("Hii, " + name + " I am thinking of a number betwween 1 to 20 , Wanna guess?")
secret_num = random.randint(1, 20)
print(secret_num)
for guessTaken in range(1, 7):
    print("\nTake a guess, You have 6 tries ")
    guess = int(input())
    if guess < secret_num:
        print("Your guess is too low, try again")
    elif guess > secret_num:
        print("Your guess is too high, try again")
    
    elif guess == secret_num:
        print(f"Your guess is Perfect , Damnn {name} , You guessed the number in  "+str(guessTaken)+" guesses")
        break
else:
    print(f"Nahh ,  I was thinking {secret_num} ")
    
print(" You took " + str(guessTaken) + " guesses")
