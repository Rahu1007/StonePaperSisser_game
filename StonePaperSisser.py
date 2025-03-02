import random

while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
1. YES I WANT TO PLAY
2. NO | EXIT PLEASE
'''))
    if uc == 1:
        for a in range(1, 6):
            userinput = int(input('''
1. STONE
2. PAPER
3. SCISSOR
'''))
            if userinput == 1:
                uchoice = "rock"
            elif userinput == 2:
                uchoice = "paper"
            elif userinput == 3:
                uchoice = "scissor"

            Cchoice = random.randint(1, 3)
            if Cchoice == 1:
                cchoice = "rock"
            elif Cchoice == 2:
                cchoice = "paper"
            else:
                cchoice = "scissor"

            print("Your choice:", uchoice)
            print("Computer's choice:", cchoice)

            if cchoice == uchoice:
                print("It's a tie!")
            elif (uchoice == "rock" and cchoice == "scissor") or (uchoice == "paper" and cchoice == "rock") or (
                    uchoice == "scissor" and cchoice == "paper"):
                print("You win!")
                ucount += 1
            else:
                print("Computer wins!")
                ccount += 1

        print("User score:", ucount)
        print("Computer score:", ccount)

    else:
        break