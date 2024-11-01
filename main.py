import random
option = ["rock","paper","scissors"]
print("Lets play rock paper scissors!")

computerchoice = random.choice(option)
playerchoice = input("Rock paper or scissors? ")

if playerchoice == computerchoice:
    print("Its a tie!")
elif (playerchoice=="rock" and computerchoice=="scissors"):
    print("You win!!!")
elif (playerchoice=="paper" and computerchoice=="rock"):
    print("You win!!!")
elif (playerchoice=="scissors" and computerchoice=="paper"):
    print("You win!!!")
else:
    print("You lose!!!")
    print("Your opponant chose ",computerchoice)




