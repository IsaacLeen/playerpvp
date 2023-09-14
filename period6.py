import random
options = ["block", "punch", "takedown", "sleep"]

npc_choice = random.choice(options)

player_choice = input("Do you wanna block, punch, takedown, or sleep")

print("The npc picked ", npc_choice)
def pvp(npc_choice, player_choice):
    if player_choice == "block" and npc_choice == "block" or player_choice == "punch" and npc_choice == "punch" or player_choice == "takedown" and npc_choice == "takedown":
        print("NEGAHOW did you pick the same option")
    if player_choice and npc_choice == "sleep":
        print("nap time, mimimimimi")
    elif player_choice == "sleep":
        print("NEGAWATT. You died")
    elif npc_choice == "sleep":
        print("Not worth my trouble pipsqueak")


    if player_choice == "block":
        if npc_choice == "punch":
            print("You blocked and countered, you win!")
        if npc_choice == "takedown":
            print("You are a monke and got takendown, you lost!")

    if player_choice == "punch":
        if npc_choice == "takedown":
            print("You punched and knocked them out, you win!")
        if npc_choice == "block":
            print("You punched and got countered, you lost!")

    if player_choice == "takedown":
        if npc_choice == "block":
            print("You took him down, you win!")
        if npc_choice == "punch":
            print("You got knocked out, better luck next time")
pvp(npc_choice, player_choice)