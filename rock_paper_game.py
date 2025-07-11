import random
def computer_choice():
    options=['rock','paper','scissor']
    return random.choice(options)

def decide_winner(player_choice_,computer_choice_):
    if player_choice == computer_choice_:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissor') or\
         (player_choice=='scissor' and computer_choice=='paper') or\
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You won!"
    else:
        return "Computer won!"
print("Welcome to Rock, Paper, Scissor Game!")
while True:
    player_choice=input("Enter your choice(rock, paper, scissor)--->")
    if player_choice=='exit':
        print("Thank you for playing")
        break
    if player_choice not in ['rock', 'paper', 'scissor']:
        print("Invalid choice, please try again")
        continue
    computer_CH=computer_choice()
    print(f"Computer choice is {computer_CH}")
    result = decide_winner(player_choice,computer_CH)
    print(result)
    print("_"*30)
    play_again=input("Would you like to play again?(yes/no)")
    if play_again!='yes':
        print("Thank you for playing")
        break

