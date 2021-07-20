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
    answer = input("Please enter Yes or No: \n")
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
    answer = input("Please enter Yes or No: \n")
    if answer in yes:
        start()
    elif answer in no:
        exit()
    else:
        print("Please answer Yes or No")
        try_again()

# Car breaks down. Can try go to house or not


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
    answer = input("Please enter A or B: \n")
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

#  Can go into house or not


def go_inside():
    print("House is empty. Gravestones in garden. Do you want to go inside?")
    answer = input("Please enter Yes or No: \n")
    if answer in yes:
        inside_house()
    elif answer in no:
        print("Zombies get you.You die")
        try_again()
    else:
        print("Please answer Yes or No")
        go_inside()


# Pick where to go inside house

def inside_house():
    print("You make it inside the house. Where do you go now?")
    print("""
A) Check where the doors upstairs lead
B) Look at the door under the stairs
C) Check what’s in the room connected to the hall
    """)
    answer = input("Please enter A, B or C: \n")
    if answer in answer_a:
        upstairs()
    elif answer in answer_b:
        basement()
    elif answer in answer_c:
        print("Kitchen")
    else:
        print("Please answer A, B or C")
        inside_house()


# Pick what room to go into upstairs

def upstairs():
    print("You go upstairs. There are 3 rooms. What room do you go into?")
    print("""
A) Left
B) The door in the middle
C) Right
    """)
    answer = input("Please enter A, B or C: \n")
    if answer in answer_a:
        bathroom()
    elif answer in answer_b:
        middleroom()
    elif answer in answer_c:
        bedroom()
    else:
        print("Please answer A, B or C: ")
        upstairs()

# Go down into basement or upstairs


def basement():
    print("Its a basement. Are you sure you want to go down?")
    answer = input("Please enter Yes or No: \n")
    if answer in yes:
        basement_down()
    elif answer in no:
        print("""
You decide to go up a floor instead
and head towards the large staircase.
    """)
        upstairs()

    else:
        print("Please answer Yes or No")
        basement()

# What to do at end of basement stairs


def basement_down():
    print("You climb down the stairs. What should you do?")
    print("""
A) Look for a light
B) Keep going in dark
    """)
    answer = input("Please enter A or B: \n")
    if answer in answer_a:
        basement_end()
    elif answer in answer_b:
        print("You die")
        try_again()
    else:
        print("Please answer A or B")
        basement_down()

# Basement room endings


def basement_end():
    print("You find a light and see a hole. What do you want to do")
    print("""
A) Look down the hole
B) Leave the basement
    """)
    answer = input("Please enter A or B: \n")
    if answer in answer_a:
        print("You fall in hole and die")
        try_again()
    elif answer in answer_b:
        print("Monster grabs your leg and you die")
        try_again()
    else:
        print("Please answer A or B")
        basement_end()

# Pick option in bathroom or go to middleroom


def bathroom():
    print("""
It's a bathroom. The tub is full and your name is written on the mirror
What would you like to do?
    """)
    print("""
A) Wipe away your name
B) Pull the plug
C) Check the room next to you instead
    """)
    answer = input("Please enter A, B or C: \n")
    if answer in answer_a:
        print("Doppelganger in mirror swaps places")
        try_again()
    elif answer in answer_b:
        print("Creature in tub drowns you")
        try_again()
    elif answer in answer_c:
        print("You leave the bathroom and try the room nextdoor.")
        middleroom()
    else:
        print("Please answer A, B or C")
        bathroom()


# Pick options in bedroom

def bedroom():
    print("""
It's a bedroom. There's a vanity in the corner and a scratching noise
coming from under the bed.
    """)
    print("""
A) Check the vanity
B) Look under the bed
    """)
    answer = input("Please enter A or B: \n")
    if answer in answer_a:
        print("Doppelganger in mirror swaps places. You die")
        try_again()
    elif answer in answer_b:
        print("Something drags you under the bed. You die")
        try_again()
    else:
        print("Please answer A or B")
        bedroom()

# Investigate middleroom or go to attic


def middleroom():
    print("""
Old dusty room with a bunch of furniture and a ladder to the attic
What do you want to do?
    """)
    print("""
A) Climb up the ladder
B) Investigate the furniture
    """)
    answer = input("Please enter A or B: \n")
    if answer in answer_a:
        attic()
        try_again()
    elif answer in answer_b:
        hat_stand()
    else:
        print("Please answer A or B")
        middleroom()


# Check the hatstand or go to attic

def hat_stand():
    print("""
You see a hat stand covered in a cloth moving,
but you don't feel a breeze. Investigate?
    """)
    print("""
A) No I'll just check out the attic
B) Yes I'll remove the fabric
    """)
    answer = input("Please enter A or B: \n")
    if answer in answer_a:
        attic()
    elif answer in answer_b:
        print("Man hiding under cloth grabs you")
        try_again()
    else:
        print("Please answer A or B")
        hat_stand()


# In attic check balcony or painting

def attic():
    print("""
Old dusty attic with a large window balcony.
Light is shining through except onto a covered painting
How would you like to proceed?
    """)
    print("""
A) Open the window and go onto the balcony
B) Look at the painting
    """)
    answer = input("Please enter A or B: \n")
    if answer in answer_a:
        balcony()
    elif answer in answer_b:
        print("Painting sucks you into it")
        try_again()
    else:
        print("Please answer A or B")
        attic()


# Balcony, climb down or go back and check painting

def balcony():
    print("""
You step out onto the balcony and see the side of the house
It has an overgrown but climbable lattice
Do you want to try climb down?
    """)
    print("""
A) Yes, it looks like it'll be worth the risk
B) No, I really want to look at the painting I saw before
    """)
    answer = input("Please enter A or B: \n")
    if answer in answer_a:
        lattice()
    elif answer in answer_b:
        print("Painting sucks you into it. You die")
        try_again()
    else:
        print("Please answer A or B")
        balcony()


# Climb down lattice, pick speed

def lattice():
    print("""
You make your way down the lattice
but you swear you can feel the ivy wrapping around your wrists
Do you think you should speed up?
    """)
    print("""
A) Yes, the sooner I'm out of here the better
B) No I'll take my name, I must be imagining things
    """)
    answer = input("Please enter A or B: \n")
    if answer in answer_a:
        print("You quickly but carefully climb down")
        congrats()
    elif answer in answer_b:
        print("Vines wrap around you. You die")
        try_again()
    else:
        print("Please answer A or B")
        lattice()


# End game congratulations

def congrats():
    print("Congratualtions, YOU WIN!")


# Stores users name for later use
name = input("Before we begin, what's your name? \n")

# Call functions to start game


def main():
    start()


# Function to test specific parts of game

main()
# inside_house()
