# Users potential responses
yes = ["Yes", "YES", "yes", "y", "Y"]
no = ["No", "NO", "no", "n", "N"]

# Stores users name for later use
name = input("Before we begin, what's your name?")

# Empty muliline string
# print("""
# You’re probably better off. Most who play this game don’t make it out alive.
# Maybe next time..?
#            """)

# Empty game function
# def game():
#     print()
#     answer= input()
#     if answer in yes:
#         print()
#     elif answer in no:
#         print()
#     else:
#         print()


# Start the game
def start():
    print("Would you like to start the game " + name + "?")
    answer = input()
    if answer in yes:
        print("Success!")
    elif answer in no:
        print("""
You’re probably better off. Most who play this game don’t make it out alive.
Maybe next time..?
            """)
    else:
        print("Please answer Yes or No")
        start()


# Call function to start game
start()
