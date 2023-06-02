# Rock smashes scissors
# Paper covers rock
# Scissors cut paper
print("*Options*: \n 1)rock \n 2)paper  \n 3)scissor \n")

Player1 = int(input("Enter your option: "))
Player2 = int(input("Enter your option: "))
if Player1 == 1 and Player2 == 2:
    print("Player2 wins!")
elif Player1 == 1 and Player2 == 3:
    print("Player1 wins!")
elif Player1 == Player2:
    print("It's a tie!")
elif Player1 == 2 and Player2 == 3:
    print("Player2 wins!")
elif Player1 == 2 and Player2 == 1:
    print("Player1 wins!")
elif Player1 == 3 and Player2 == 2:
    print("Player1 wins!")
elif Player1 == 3 and Player2 == 1:
    print("Player2 wins!")

#-------------------------------------

print("==>WELCOME<==")
print("1) rock\n" +
      "2) paper\n" +
      "3) scissors")
print("...How many rounds do you want to play this game?...")
n = int(input(">Enter number of rounds: "))
while True:

    for i in range(n):
        u = int(input("Enter your choice: "))
        if u == 1:
            choice_name = "rock"
        elif u == 2:
            choice_name = "paper"
        elif u == 3:
            choice_name = "scissors"

        print("user choice is : " + choice_name)
        print("...now it is computer's turn...")

        import random

        cmp_choice = random.randint(1, 3)
        if cmp_choice == 1:
            cmp_choice_name = "rock"
        elif cmp_choice == 2:
            cmp_choice_name = "paper"
        else:
            cmp_choice_name = "scissors"

        print("Computer choice is :" + cmp_choice_name)
        u2 = 0
        cmp_choice2 = 0
        if (u == 1 and cmp_choice == 2):
            print("computer wins")
            cmp_choice2 += 1
        elif (u == 1 and cmp_choice == 3):
            print("you win")
            u2 += 1
        elif (u == cmp_choice):
            print("It's a tie")
        elif (u == 2 and cmp_choice == 1):
            print("you win")
            u2 += 1
        elif (u == 2 and cmp_choice == 3):
            print("computer wins")
            cmp_choice2 += 1
        elif (u == 3 and cmp_choice == 1):
            print("computer wins")
            cmp_choice2 += 1
        elif (u == 3 and cmp_choice == 2):
            print("you win")
            u2 += 1

        print("Your wins" + str(u2))
        print("Computer wins" + str(cmp_choice2))
        print("continue?(yes/no)")
        e = int(input("1/2?:"))
        if e == 2:
            break
    break

