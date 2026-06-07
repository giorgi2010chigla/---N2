import random
rannum = random.randint(1,100)
count = 0

while count < 5:
    guess = int(input("Guess a number between 1 and 100(you have 5 tries):45"))
    if guess < rannum:
        print("Too low!")
        count += 1
    elif guess > rannum:
        print("Too high!")  
        count += 1
    elif guess == rannum:
        print(f"Congratulations! You guessed the number in {count} tries.")
        break
else:
    print(f"Sorry, you lost. It was {rannum}.")

 ##   https://github.com/giorgi2010chigla/---N2/tree/main
    