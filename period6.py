import random
options = ["persuade", "fight", "scream", "sleep"]

npc_choice = random.choice(options)

player_choice = input("Do you wanna run, hide, fight, sleep")

def pvp():
    if player_choice == npc_choice:
        print("NEGAHOW did you pick the same option")
    if player_choice == "sleep":
        print("NEGAWATT. You died")
    if player_choice == "persuade":
        if npc_choice == "fight":
            print("You persuade him not to beat you up")
        if npc_choice == "scream":
            print("You cant persuade a screamer")
    

pvp()