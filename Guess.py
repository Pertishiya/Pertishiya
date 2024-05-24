print("Guess the number")
import random

rand_num = random.randint(1,10)
print(rand_num)
turns = 5

def guess_num(rand_num,guess, turns):
    if guess > rand_num:
        print("Too high")
        turns -=1
        print(f"You have only {turns} chances left!")
    if guess < rand_num:
        print("Too Low")
        turns -=1
        print(f"You have {turns} chances left!")
    if guess == rand_num:
        print(f"You guessed it right. Number is {rand_num}")
        turns = -1
    return turns

def set_difficulty:

while turns > 0 :
    guess = int(input("Enter the number you guess: \n"))
    turns = guess_num(rand_num,guess,turns)

if turns == 0:
    print("Chances exhausted. Game Over!")
