# Users potential responses
yes = ["Yes", "YES", "yes", "y", "Y"]
no = ["No", "NO", "no", "n", "N"]
answer_a = ["A", "a"]
answer_b = ["B", "b"]
answer_c = ["C", "c"]

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
    print("Yes or No?")
    answer = input()
    if answer in yes:
        house_help()
    elif answer in no:
        print("""
You’re probably better off. Most who play this game don’t make it out alive.
Maybe next time..?
            """)
    else:
        print("Please answer Yes or No")
        start()

# Try again


def try_again():
    print("Would you like to try again?")
    print("Yes or No?")
    answer = input()
    if answer in yes:
        start()
    if answer in no:
        try_again()
    else:
        print("Please answer Yes or No")
        try_again()

# Car breaks down and user can go into house


def house_help():
    print("Unfortunately " + name + ", your day hasn’t been going so well.")
    print("""
You’ve spent your entire afternoon traveling halfway around the country,
only to find out you’ve been going the wrong direction the whole time!
(It’s not your fault your GPS doesn’t have spell check).
To save time on your journey home you cut off the main road through thick woods
down an old windy road you’re pretty sure no one has been on in years.
You can barely see the rising moon, over the tops of the thick forest trees.
You’re tired and you just want to get home to relax as soon as possible,
but faith and your car have other plans.
You come to a sudden stop as your car lets out one final groan of exhaustion
with a cloud of smoke coming from the engine.
You quickly get out of the car and open the hood.
You let out a sigh of defeat when you see the state the engine is in.
Suddenly you realise you stopped at the foot of a large house on a hill.
It seems to be surrounded by waves of little statues.
The whole area is enclosed with a large stone wall.
An even bigger Iron rusted gate blocks your pathway in.
    """)
    print("Do you want to see if you can get any help at the House?")
    print("""
A) Yeah, I don’t really feel safe out here in the dark
B) No that looks a bit ominous, I’d rather take my chances out in the woods
    """)
    answer = input()
    if answer in answer_a:
        print("Yes")
    elif answer in answer_b:
        print("""
You decide the house is a little too much for you
You would rather try to walk home in the opposite direction.
Unfortunately the woods are too thick for any moonlight to shine through,
so you're left wandering through the dark brush for hours until
you finally collapse with exhaustion and are never heard from again.
Maybe you would have had a little more luck at the house?
        """)
        try_again()
    else:
        print("Please answer A or B")
        house_help()


# Call function to start game
start()
