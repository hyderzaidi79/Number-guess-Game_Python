import random

def main():
    while True:
        rnum = random.randint(0, 10)

        print("\n\n\t\t\t✨Welcome! to the Number Guessing Game✨\n\n")

        num = int(input("\t\t\t\t🤔Guess a number (0-10): \n"))

        # print("\n\n\t\t\tThe Random Number is:", rnum, "\n\n")

        if rnum < num:
            print("\t\t\t😮Your number is too High! as random number =",rnum ,"\n")

        elif rnum > num:
            print("\t\t\t😔Your number is too Low! as random number =",rnum ,"\n")
                
        else:
            print("\t\t\t🎉Congratulations! You Win the Game.🎊\n")

        print("\n--- MAIN MENU ---")
        print("1. Quit Game")
        print("2. Play Again")

        choice = input("Choose an option (1 or 2): ")

        if choice == "1":
            print("\t\t\t\t✨GAME END!\n")
            break

        elif choice == "2":
            print("\t\t\t\t😎Starting a new round...👉\n")

        else:
            print("\t\t\t😑Invalid choice! Exiting by default.\n")
            break

main()
