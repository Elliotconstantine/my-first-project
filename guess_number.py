import random
secret_number = random.randint(1, 100)
print("Welcome to the Guess the Number Game!")
while True:
    guess = int(input("Enter your guess (between 1 and 100): "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break   


    