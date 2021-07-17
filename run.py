# Users potential responses
yes = ["Yes", "YES", "yes", "y", "Y"]
no = ["No", "NO", "no", "n", "N"]

# Stores users name for later use
name = input("Before we begin, what's your name?")


# Start the game
def start():
    print("Would you like to start the game " + name + "?")
    answer = input()
    if answer in yes:
        print("Success!")
    elif answer in no:
        print("Failure!")
    else:
        print("Please answer Yes or No")
        start()


# Call function to start game
start()
