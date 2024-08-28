import random

computerScore = 0
userScore = 0

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

guess = [rock, paper, scissors]


def rps(userChoice, compChoice):
    global computerScore
    global userScore
    if userChoice == 0 and compChoice == 0:
        return
    elif userChoice == 0 and compChoice == 1:
        computerScore += 1
    elif userChoice == 0 and compChoice == 2:
        userScore += 1
    elif userChoice == 1 and compChoice == 0:
        userScore += 1
    elif userChoice == 1 and compChoice == 1:
        return
    elif userChoice == 1 and compChoice == 2:
        computerScore += 1
    elif userChoice == 2 and compChoice == 0:
        computerScore += 1
    elif userChoice == 2 and compChoice == 1:
        userScore += 1
    elif userChoice == 2 and compChoice == 2:
        return


while computerScore <3 and userScore <3:
    userChoice = int(input("Please make a choice\n0 for Rock"
                       "\n1 for Paper"
                       "\n2 for Scissors"
                       "\n:"))
    computerChoice = random.randint(0,2)
    print(guess[userChoice])
    print(guess[computerChoice])
    rps(userChoice, computerChoice)
    print("User score is: " + str(userScore))
    print("Computer score is " + str(computerScore))

if(userScore == 3):
    print("*** Congrats, you won!! ***")
else:
    print("~~~ Sorry, you lost. Please try again. ~~~")



