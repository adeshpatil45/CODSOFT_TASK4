## Task - 4 Rock-Paper-Scissors Game

import random
def get_computer_choice():
    choices=["rock","paper","scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "scissors" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
        return 'win'
    else:
        return 'lose'
    
def print_result(user_choice, computer_choice, result):
    print (f"\nYou chose: {user_choice}")
    print (f"\nComputer chose: {computer_choice}")
    if result=='win':
        print("you win!")
    elif result=='lose':
        print("you lose!")
    else:
        print("It's a tie")

def main():
    user_score = 0
    computer_score = 0
    print("welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = input("\n Enter rock, paper or scissors: ").lower()
        if user_choice not in['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print_result(user_choice, computer_choice, result)
            
        if result == 'win':
            user_score +=1
        elif result == 'lose':
            computer_score +=1

        print(f"score: You {user_score} - computer {computer_score}")
        play_again = input("Do you want to play again? (Yes/no):").lower()
        if play_again !='yes':
            break
        
        print("\n Thanks for playin!")
        print(f"final score: You {user_score} - Computer {computer_score}")

if __name__ == "__main__":
    main()
