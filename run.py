# Users potential responses
yes = ["Yes", "YES", "yes", "y", "Y"]
no = ["No", "NO", "no", "n", "N"]
answer_a = ["A", "a"]
answer_b = ["B", "b"]
answer_c = ["C", "c"]

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
    answer = input("Please enter Yes or No: ")
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

# Try the game again


def try_again():
    print("Would you like to try again?")
    answer = input("Please enter Yes or No: ")
    if answer in yes:
        start()
    elif answer in no:
        exit()
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
    answer = input("Please enter A or B: ")
    if answer in answer_a:
        go_inside()
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


def go_inside():
    print("House is empty. Do you want to go inside?")
    answer = input("Please enter Yes or No: ")
    if answer in yes:
        inside_house()
    elif answer in no:
        print("You die")
        try_again()
    else:
        print("Please answer Yes or No")
        go_inside()


def inside_house():
    print("You make it inside the house. Where do you go now?")
    print("""
A) Check where the doors upstairs lead
B) Look at the door under the stairs
C) Check what’s in the room connected to the hall
    """)
    answer = input("Please enter A, B or C: ")
    if answer in answer_a:
        upstairs()
    elif answer in answer_b:
        basement()
    elif answer in answer_c:
        print("Kitchen")
    else:
        print("Please answer A, B or C")
        inside_house()


def upstairs():
    print("You go upstairs. There are 3 rooms. What room do you go into?")
    print("""
A) Left
B) The door in the middle
C) Right
    """)
    answer = input("Please enter A, B or C: ")
    if answer in answer_a:
        print("Left")
    elif answer in answer_b:
        print("The middle")
    elif answer in answer_c:
        print("Right")
    else:
        print("Please answer A, B or C: ")
        upstairs()


def basement():
    print("Its a basement. Are you sure you want to go down?")
    answer = input("Please enter Yes or No: ")
    if answer in yes:
        basement_down()
    elif answer in no:
        print("""
You decide to go up a floor instead
and head towards the large staircase.
    """)
        upstairs()

    else:
        print("Please answer A or B")
        basement()


def basement_down():
    print("You climb down the stairs. What should you do?")
    print("""
A) Look for a light
B) Keep going in dark
    """)
    answer = input("Please enter A or B: ")
    if answer in answer_a:
        basement_end()
    elif answer in answer_b:
        print("You die")
        try_again()
    else:
        print("Please answer Yes or No")
        basement_down()


def basement_end():
    print("You find a light and see a hole. What do you want to do")
    print("""
A) Look down the hole
B) Leave the basement
    """)
    answer = input("Please enter A or B: ")
    if answer in answer_a:
        print("You fall in hole and die")
        try_again()
    elif answer in answer_b:
        print("Monster grabs your leg and you die")
        try_again()
    else:
        print("Please answer Yes or No")
        basement_end()


# Stores users name for later use
name = input("Before we begin, what's your name? ")

# Call functions to start game


def main():
    start()


# Function to test specific parts of game

# main()
inside_house()
