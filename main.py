import random
import math
#player_1 refers to the user and player_2 refers to the computer
def rock_paper_game():
     #main user selects the letter to play with
    player_1 = input("Select of these Characters\n R for rock \n P for paper \n S for scissors ")
    player_1 = player_1.lower()
    #computer randomly selects its own letter
    play_list = ["r","p","s"]
    player_2 = random.choice(["r","p","s"])
    for player in play_list:
        if player == player_1:
            if player_1 == player_2:
                print(f"You and the Computer have choosen {player_1.upper()}, it is a Tie")
                break
            if check_winner(player_1,player_2):
                print(f"You have chosen {player_1.upper()} and the computer has chosen {player_2.upper()}. You won")
            else:
                print(f"You have chosen {player_1.upper()} and the computer has chosen {player_2.upper()}. You lost")
            break
    else:
        print(f"Error, Please enter correct Input")

def check_winner(user,cpu):
    if(user=="r" and cpu =="s") or (user == "s" and cpu =="p") or (user =="p" and cpu=="r"):
        return True
    return False

rock_paper_game()