import random

print("Rules of the game \n"
"\n"
"You have three input to choose from \n"
"R : Rock \nP : Paper \nS : Scissors \n"
"Paper always beat Rock \nRock always beat Scissors \n"
"While Scissors always beat Paper \n"
"You will be playing against a computer \n"
"So Brace yourself \n"
)

while True:
    choices = ["P", "R", "S"]
    cpu = random.choice(choices)
    players_choice = None


    while players_choice not in choices:
        players_choice = input("Rock, Paper or Scissors? : ").upper()
        if players_choice not in choices:
            print()
            print("Pick From the available Option")
            print()


    if players_choice == cpu:
        print()
        print(f"CPU  ({cpu}) : Player ({players_choice}) \nTaaaaaa!!! It is a tie, try again")
        print()
        

# For if player picks Paper
    elif players_choice == "P":
        if cpu == "S":
            print()
            print(f"CPU  ({cpu}) : Player ({players_choice}) \nHaha, You suck!!!")
            print ()

        if cpu == "R":
            print()
            print(f"CPU  ({cpu}) : Player ({players_choice}) \nDon't feel too important because you WON!!!")
            print()

# For if player picks Rock

    elif players_choice == "R":
        if cpu == "P":
            print()
            print(f"CPU  ({cpu}) : Player ({players_choice}) \nHaha, You suck!!!")
            print ()

        if cpu == "S":
            print()
            print(f"CPU  ({cpu}) : Player ({players_choice}) \nDon't feel too important because you WON!!!")
            print()

# For if player picks Scissors
    
    elif players_choice == "S":
        if cpu == "R":
            print()
            print(f"CPU  ({cpu}) : Player ({players_choice}) \nHaha, You suck!!!")
            print ()

        if cpu == "P":
            print()
            print(f"CPU  ({cpu}) : Player ({players_choice}) \nDon't feel too important because you WON!!!")
            print()

    try_again = input("Do you want to go again? yes(y)/no(n)): ").lower()
    print()

    if try_again != "y":
        break
print()
print("Enjoy Lazy Man!!!")
print()


    
    
    

