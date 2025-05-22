import random
#Challenge 31 - Rock, Paper, Scissors Game
Chosen = input("Rock, Paper , Scissors.... Shoot! :")
Choosen = Chosen.lower()
Rock = ("Rock")
Paper = ("Paper")
Scissors =("Scissors")

choice = random.randint(5,7)
#This would observe the users output and show the three results (3^2).
#Rock
if choice == Rock:
    if Choosen == "paper":
        print("L BOZO!")
    elif Choosen == "rock":
        print("Aw its a draw!")
    else :
        print("YOU CHEATED!!!")
#Paper
elif choice == Paper:
    if Choosen == "scissors":
        print("L BOZO!")
    elif Choosen == "Paper":
        print("Aw its a draw!")
    else :
        print("YOU CHEATED!!!")
#Scissors
else:
    if Choosen == "rock":
        print("L BOZO!")
    elif Choosen == "scissors":
        print("Aw its a draw!")
    else :
        print("YOU CHEATED!!!")

        