import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice=[rock,paper,scissors]
game_over=False
user_score=0
computer_score=0
while not game_over:
    user_choice=int(input("What is your choice? Enter 0 for rock, 1 for paper or 2 for scissors: "))
    if user_choice!=0 and user_choice!=1 and user_choice!=2:
        print("Invalid input! Please enter 0 for rock, 1 for paper or 2 for scissors")
        continue
    print(choice[user_choice])
    computer_choice=random.randint(0,2)
    print(choice[computer_choice])
    if (user_choice==0 and computer_choice==2) or (user_choice>computer_choice):
        user_score+=1
        print("Hurray! You get 1 point.")
        print(f"Your score is {user_score} and computer score is {computer_score}")
    elif (computer_choice==0 and user_choice==2) or (computer_choice>user_choice):
        print("Alas! Your opponent gets 1 point.")
        computer_score+=1
        print(f"Your score is {user_score} and computer score is {computer_score}")
    elif user_choice==computer_choice:
        print("Its a draw!")

    if user_score==10 or computer_score==10:
        print("Game over")
        game_over=True
        if user_score>computer_choice:
            print("You win!")
        else:
            print("You lost!")
