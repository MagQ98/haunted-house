# Users potential responses
answer_a = ["A", "a"]
answer_b = ["B", "b"]
answer_c = ["C", "c"]
yes = ["Yes", "YES", "yes", "y"]
no = ["No", "NO", "no", "n"]


# Start the game
def start():
    print("Would you like to start the game?")
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
