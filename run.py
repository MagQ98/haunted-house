# Users potential responses
yes = ["Yes", "YES", "yes", "y", "Y"]
no = ["No", "NO", "no", "n", "N"]
answer_a = ["A", "a"]
answer_b = ["B", "b"]
answer_c = ["C", "c"]


# Start the game
def start():
    print("Would you like to start the game " + name + "? \n")
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
        house_help()
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
To save time on your journey home you cut off road through thick woods
down an old windy road you’re pretty sure no one has been on in years.
You can barely see the rising moon, over the tops of the thick forest trees.
You’re tired and you just want to get home to relax as soon as possible,
but faith and your car have other plans.
You come to a sudden stop as your car lets out one final groan of exhaustion
with a cloud of smoke coming from the engine.
You quickly get out of the car and open the hood.
You let out a sigh of defeat when you see the state the engine is in.
You’re pretty sure it’s after overheating,
but you don’t think you have any water or coolant to add to it.
Suddenly you realise you stopped at the foot of a large house on a hill.
It seems to be surrounded by waves of little stone statues.
The whole area is enclosed with a large brick wall.
An even bigger Iron rusted gate blocks your pathway in.
    """)
    print("Do you want to see if you can get any help at the House?")
    answer = input("Please enter Yes or No: \n")
    if answer in yes:
        go_inside()
    elif answer in no:
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
        print("Please answer Yes or No")
        house_help()

#  Can go into house or not


def go_inside():
    print("""
You make your way up the hill towards the house,
forcefully push open the big gate and make your way in.
On the walk-up, you have a quick look around your environment
and are horrified to discover those statues you saw were actually gravestones.
As you get closer to the building itself you can see just how dilapidated
and sinister this house is and you also see all the windows are boarded up.
You reach the porch and as you climb the old creaky stairs
you can swear you feel a pair of eyes bearing into the back of your head.
You make it to the door and bang the ancient door knocker,
but hear no response.
The feeling of something behind you is growing stronger
and with each passing second and you can feel the panic set in
    """)
    print("Should you see if the door is open and invite yourself in?")
    answer = input("Please enter Yes or No: \n")
    if answer in yes:
        inside_house()
    elif answer in no:
        print("""
You conclude that you don’t want to break into a random person's house,
regardless of everything in your body screaming at you to take shelter.
You turn around and decide to make your way back to your car
but before you can even step off the porch you find yourself surrounded
by a group of dark figures.
You go to ask them a question but the words don’t get to your lips
before they grab you.
You get a closer look at your assailants
and are disgusted to see they look like zombies,
straight out of a horror movie.
You struggle as much as you can as they pull you into a fresh open grave
but their combined strength mixed with the foul smell of dirt is overpowering
and you find yourself getting lightheaded.
They continue to drag you further and further into the dirt
and as you look up at the sky for the last time,
All you can think about is how maybe you should've been a little bit more rude.
        """)
        try_again()
    else:
        print("Please answer Yes or No")
        go_inside()


# Go to basement or upstairs

def inside_house():
    print("""
You silently pray as you reach for the rusty door handle and try to turn it.
It works, the door is unlocked!
You quickly jump through the open door and slam it shut behind you.
You breathe a sigh of relief and lean against the door
but quickly hear what sounds like a latch clicking in the lock.
You panic slightly and try to turn the door handle,
only to realise you’re now locked in.
You step back and take a look around the dark, cobweb-ridden house
and are greeted by a sprawling staircase as the centerpiece of the hallway.
The room is adorned with large, mostly decayed portraits
that make you feel like they're watching your every move.
Every window is bordered up and the room gives you a feeling of uneasiness,
that you would quickly like to leave behind.
As you look around the hallway you spot a few doors
and can see a few more in the upstairs landing.
    """)
    print("What would you like to do?")
    print("""
A) Check where the doors upstairs lead
B) Look at the door under the stairs
    """)
    answer = input("Please enter A, B or C: \n")
    if answer in answer_a:
        upstairs()
    elif answer in answer_b:
        basement()
    else:
        print("Please answer A or B")
        inside_house()


# Pick what room to go into upstairs

def upstairs():
    print("""
You slowly make your way up the old creaking stairs,
afraid with each step that you’ll fall through the steps.
After what seems like forever you finally reach the top of the stairs.
Exhausted and pretending not to be out of breath,
you look around and see three doors right in front of you.
The middle door seems to have a gentle light seeping out underneath it
while the other two look quite dark.
    """)
    print("Which door would you like to go through?")
    print("""
A) Left
B) Middle
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
    print("""
There’s a door barely visible under the stairs that catches your attention.
You make your way over and open the door to discover that
it contains a set of stairs that lead down to what you think is the basement.
Staring down into the dark abyss you feel an overwhelming sense of dread.
    """)
    print("Are you sure you want to go down?")
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
    print("""
You anxiously make your way down the basement stairs,
the darkness swallowing you more and more with each step.
You reach the bottom step and can feel a slight pressure on your lungs
like the whole room is covered with dampness and mold.
You gently shuffle forward gripping yourself tightly to the wall,
your anxiety rising slightly as you realise you can’t see in front of you.
The only thing occupying your senses is the slight sound of water
dripping somewhere in the room and a quiet almost gurgling sound.
You swear you can almost feel the presence of something large down here.
You need to figure out how you’re going to move around in this darkness.
    """)
    print("""
A) Look for a light
B) Keep going in the dark
    """)
    answer = input("Please enter A or B: \n")
    if answer in answer_a:
        basement_end()
    elif answer in answer_b:
        print("""
You decide to try your chances in the dark.
You let go from the wall and courageously take a few big strides
to what you hope is the center of the room.
But you don't manage to make it very far,
after a few steps the ground seems to disappear
right from under your feet and you fall for what seems an eternity.
When you finally crash land, the thickness of the air makes you lightheaded
and you’re sure you’re far too hurt to move.
Unfortunately by the sounds of whatever creature is wriggling down there,
you discovered the source of those gurgling noises
and you’re sure your pain won't last long.
        """)
        try_again()
    else:
        print("Please answer A or B")
        basement_down()

# Basement room endings


def basement_end():
    print("""
You make the choice to look for a source of light.
Thankfully, you don’t have to look around too hard.
You slightly step away from the wall,
waving your arms around in the air and manage to get caught up in a string.
Trying to untie yourself results in a switching sound and before you know it,
the room is enveloped in a dim red glow
from a lone flickering lightbulb hanging from a wire.
Looking around your location proves to be a mistake however
as the room makes you feel very unsettled.
The room looks unfinished.
The walls are a decrepit, dark slimy stone
and the floor seems almost sticky with moisture.
There is what looks like a big open sewer grate,
right in the middle of the room,
that you swear you can hear movement in.
Everything about this room makes you regret coming down here
    """)
    print("What would you like to do?")
    print("""
A) Look down the hole
B) Leave the basement
    """)
    answer = input("Please enter A or B: \n")
    if answer in answer_a:
        print("""
Your curiosity gets the better of you as you creep closer
and closer to the edge of the hole.
Each footstep you make towards the unknown creature seems to make it angrier,
it trashes its body around in the sewer grate as it gets louder and louder.
By the time you reach the edge,
it seems to be almost throwing itself from side to side,
shaking the entire room as it does so.
Ignoring everything your body is doing to tell you to run,
you gingerly lean your head over the edge of the hole.
You barely catch a glimpse of a Kraken like monster before
what feels like a massive tentacle wraps itself around your head.
It grips you tightly, beginning to wrap itself around your neck and body.
As it begins to lift you off the ground and down into its sharp,
beak like mouth you begin to lose consciousness.
The last thought in mind is the saying about how curiosity killed the cat.
        """)
        print("I guess now you can say the same for " + name)
        try_again()
    elif answer in answer_b:
        print("""
The atmosphere of the room proves too much for you
and you choose to retreat upstairs.
You turn around and begin to walk towards the staircase,
nearly skidding across the wet floor.
As you begin your ascent, you hear a low moaning noise behind you.
Your heart beat races as you begin to race up the stairs.
You near the top, the light from the doorway enters your vision
but just as quick as you see it, it’s gone.
You feel something warm and moist grab around your leg
as you are forcefully yanked back down the stairs.
The last thing you feel is your head banging off the cold stone steps
as your body is dragged down into the dark.
The final steps knocks you unconscious, ensuring your faith.
You never really were a fan of basements anyway.
        """)
        try_again()
    else:
        print("Please answer A or B")
        basement_end()

# Pick option in bathroom or go to middleroom


def bathroom():
    print("""
You push open the leftmost door and it leads you into a dark, cold bathroom.
An ornate bathtub sits in the middle of the room and on further inspection,
it seems to be full with something.
You cautiously look around the bathroom
and are surprised when you see something move in front of you,
but sigh with relief when you realise
it was just your foggy reflection in the mirror.
Looking at the mirror, it seems strange to you
that it’s fogged up like that when it’s so cold in here.
That's when you notice there’s something written in the corner of the mirror.
    """)
    print(name + "...")
    print("""
What would you like to do?
    """)
    print("""
A) Wipe away your name
B) Pull the plug
C) Check the room next to you instead
    """)
    answer = input("Please enter A, B or C: \n")
    if answer in answer_a:
        print("""
Seeing your name written on the mirror like that makes you feel very uneasy.
You decide to try to wipe it off.
You step closer to the mirror and use your sleeve to wipe away the letters.
As you do so, you spot something that makes your blood run cold.
Your reflection never moved when you did.
You look up, only to make eye contact with your doppelgänger in the mirror.
It is smirking wickedly at you.
It reaches through, grabs you by the shoulders
and lifts you through the mirror,
swapping places with you as it does so.
All you can do now is watch from the otherside of the glass
as it wipes itself down, smiles at you one last time
and then leaves you behind forever.
You watch yourself walk away as a final thought enters your mind,
What happens if that thing finds its way to your home...
        """)
        try_again()
    elif answer in answer_b:
        print("""
You walk over to the bathtub, curiosity getting the better of you.
As you reach the edge you swear you can see slight movement
under the surface of the water.
You lean in closer to the tub
and dip your fingers into the freezing, thick liquid.
You reach further into the bath
and can just feel the chain of the plug at your fingertips.
As you stretch even further, to get a grip of the plug,
you feel something grab your arm.
An unknown force pulls you into the murky tub,
as you trash and fight for your life it tightens its grip on you.
The last thing you feel is your body being dragged further down into the water.
Never to be seen again.
        """)
        try_again()
    elif answer in answer_c:
        print("You leave the bathroom to try the room nextdoor.")
        middleroom()
    else:
        print("Please answer A, B or C")
        bathroom()


# Pick options in bedroom

def bedroom():
    print("""
You decide to open the door on the far right.
It feels heavy and makes an awful creaking noise as it’s pushed inwards.
You enter the room and examine your surroundings.
In front of you is a large and very regal four poster bed.
To your side is an elegant vanity with a large circular mirror,
covered in scattered pieces of jewellery.
You walk further into the room and the closer you get to the bed,
the more you can hear a faint scratching noise.
    """)
    print("What do you think you should do?")
    print("""
A) Check the vanity
B) Look under the bed
    """)
    answer = input("Please enter A or B: \n")
    if answer in answer_a:
        print("""
You turn around to face the vanity and spot all the jewelry thrown across it.
Gold, Diamonds, and Pearls adorn the dresser.
As you get closer something shimmering in the light catches your eye.
A ruby glistening pendant lays in the center of the vanity
and once you lay your eyes on it, you can't take them away.
You feel almost like you're under some spell by this necklace,
and you feel an overwhelming need to put it on.
You reach for it, tie the clasps behind your neck
and can feel yourself losing control immediately.
As you fade out of consciousness for the last time,
you catch a final glimpse of your blood-red eyes in the mirror,
your mind disappears entirely.
Whatever took over your body now leaves the room.
Red never really was your color anyway.
        """)
        try_again()
    elif answer in answer_b:
        print("""
You continue even further into the room and approach the bed.
The scratching noises start to become slightly louder and more frequent.
You slow down and begin to inch yourself closer to the bed frame.
You are about to crouch down for a better look,
when all the noises suddenly stop.
Panicking at the abrupt silence, you take a step back. But it’s too late.
A disheveled hand suddenly reaches out and grabs you by your ankle.
It pulls you hard, forcing you to crash onto the ground landing on your back.
The hand violently yanks on you and your body slides across the floor,
underneath the bed.
In your final moments,
you realise your childhood fear of something lurking under your bed,
might have actually been founded.
        """)
        try_again()
    else:
        print("Please answer A or B")
        bedroom()

# Investigate middleroom or go to attic


def middleroom():
    print("""
You push open the door to the middle room and step inside.
The room is full of old dusty furniture, most of it covered in sheets.
There's a massive gap in the ceiling
with old wooden stairs leading up through it,
you assume it leads up to the attic.
The light you saw under the door is pouring in through the gap,
making all the floating dust particles in the air glisten.
    """)
    print("How would you like to proceed?")
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
You cautiously continue walking in to the room,
making your way around all the unidentifiable covered furniture.
As you go deeper into the room
the furniture starts to become more densely packed,
forcing you to squeeze your body through any gaps.
The dust begins to slowly fill your lungs, causing you to cough.
Your chest gets tight and when you cough to relieve it,
You spot a movement in the corner of your eye.
You turn to see what seems like a coatstand covered in more cloth,
but it’s shifting and looks almost like it’s breathing.
You don't feel a breeze coming in anywhere.
    """)
    print("What would you like to do?")
    print("""
A) Go back and investigate the attic
B) Remove the cloth from the coatstand
    """)
    answer = input("Please enter A or B: \n")
    if answer in answer_a:
        attic()
    elif answer in answer_b:
        print("""
Your curiosity gets the better of you as you make your way to the coatstand
You begin to hold your breath in anticipation as you inch closer.
You reach your hand out to grab onto the cloth.
But just as you are about to pull it,
a large pair of arms shoot out and wrap themselves around you.
You can feel yourself being lifted up off the ground,
and as your assailant pulls you close and begins to violently squeeze your body
you realise it wasn’t a stand under the cloth at all, It was a person.
And your doom.
        """)
        try_again()
    else:
        print("Please answer A or B")
        hat_stand()


# In attic check balcony or painting

def attic():
    print("""
You climb up the steep wooden stairs and find yourself in the attic.
There’s a large window that lights up the room,
with a glass door that leads out onto a balcony.
You can see the sunlight start to shine through as the sun begins to rise.
How long have you been in this house?
As you are thinking about where the time went,
you notice something partially covered with a dirty paint splatter sheet.
It looks like the outline of a large painting on an easel
    """)
    print("What do you want to do?")
    print("""
A) Open the window and go onto the balcony
B) Peek at the painting
    """)
    answer = input("Please enter A or B: \n")
    if answer in answer_a:
        balcony()
    elif answer in answer_b:
        print("""
Something about the unknown piece of art piques your interest.
You walk across the room towards it,
with each step your heart beats faster with anticipation.
Standing in front of it now,
the painting is intimidatingly bigger than you thought it was.
The covered canvas towers above you as you gently reach out and pull the cover.
You stand still, observing the dark crimson brush strokes
and the overall unsettling nature of the painting
That’s when you spot two figures hidden in the center of the painting.
One of them looks like you.
The other a hulking shadow figure standing directly behind you,
hand on your shoulder.
The sight of it makes you feel anxious and you are about to turn around,
when you feel a cold icy grip on your shoulder.
You try to spin around but are suddenly frozen in place, unable to move.
A frosty breeze encases your entire body, making you shiver
The grip on your shoulder tightens and becomes incredibly painful,
forcing you to start blacking out.
The last thing you see before the pain and cold take over,
is your final breath, visible in the icy cold air.
        """)
        try_again()
    else:
        print("Please answer A or B")
        attic()


# Balcony, climb down or go back and check painting

def balcony():
    print("""
You walk across the room and push open the large glass doors.
Stepping out onto the stone balcony, the wind hits your face
as you take a deep breath of fresh air and look around.
The thick forest surrounding the house doesn't seem as intimidating now,
as it did last night in the dark.
Leaning over the edge of the balcony,
you can see an old lattice attached to the side of the house.
It’s overgrown with vines and ivy and doesn’t look very stable.
The plants intertwine around the lattice and
almost seem to dance as they twist in the wind.
You reach out and grip the lattice, giving it a slight shake.
It doesn't seem very sturdy but it could be your only way out.
    """)
    print("What do you think you should do?")
    print("""
A)Try to climb down the lattice
B)Go back and look at the painting, it's calling to me
    """)
    answer = input("Please enter A or B: \n")
    if answer in answer_a:
        lattice()
    elif answer in answer_b:
        print("""
Something about the unknown piece of art piques your interest.
You walk across the room towards it,
with each step your heart beats faster with anticipation.
Standing in front of it now,
the painting is intimidatingly bigger than you thought it was.
The covered canvas towers above you as you gently reach out and pull the cover.
You stand still, observing the dark crimson brush strokes
and the overall unsettling nature of the painting
That’s when you spot two figures hidden in the center of the painting.
One of them looks like you.
The other a hulking shadow figure standing directly behind you,
hand on your shoulder.
The sight of it makes you feel anxious and you are about to turn around,
when you feel a cold icy grip on your shoulder.
You try to spin around but are suddenly frozen in place, unable to move.
A frosty breeze encases your entire body, making you shiver
The grip on your shoulder tightens and becomes incredibly painful,
forcing you to start blacking out.
The last thing you see before the pain and cold take over,
is your final breath, visible in the icy cold air.
        """)
        try_again()
    else:
        print("Please answer A or B")
        balcony()


# Climb down lattice, pick speed

def lattice():
    print("""
You decide to try your luck climbing down.
You carefully throw your leg over the edge of the balcony
and grip on tightly to the lattice.
Cautiously, you begin to make your way down,
trying your best not to look straight at the ground.
Your slight fear of heights pumps the adrenaline through your body,
making you pick up speed on your descent.
After a short period your arms are just starting to hurt
when you feel a slight tickle on your wrist.
You pull back your hand to see a thin piece of ivy,
wrapping itself around your wrist.
Then you notice that all the plants around you seem to have started squirming.
It almost looks like some of them are moving towards your direction.
    """)
    print("Should you take your time or be quick?")
    print("""
A) Move quickly, the sooner I leave here the better
B) Move slowly, I must be imagining things
    """)
    answer = input("Please enter A or B: \n")
    if answer in answer_a:
        print("""
You carefully but quickly make your way down the lattice.
You can scarcely feel the vines weak attempts to wrap itself around you
as you keep ripping your hand away from the wall to move quicker.
As you are getting closer to the bottom,
you can feel the plants attempts to constrict you becoming more violent.
More vines begin to shoot out trying to encase you, narrowly missing your face
You are clambering down the lattice at an accelerated pace,
When you see another vine going straight for your neck,
you try to dodge it and in doing so lose your footing.
You fall and hit the ground with a hard crash. Winded and in a lot of pain,
you lie on the ground for a few moments trying to regain your composure.
Exhausted, aching and slightly traumatised
you start to make your way back to where you think your car is,
limping in pain the whole way.
After what seems like hours you finally make it to your car.
You jump into the front seat and pray as you turn the key in the ignition.
Thankfully it works.
You pull away from the house glancing back at it one more time,
to see numerous eyes staring at you through cracks in the windows boards.
You don't know what they had planned for you,
but you’re glad you never had to find out.
        """)
        congrats()
    elif answer in answer_b:
        print("""
You decide you must be imagining things,
you’ve had a long strange night and are just exhausted.
You slow down your climbing and try ignore the plants moving underneath you.
The further you climb down, the thicker the shrub seems to be getting.
You pull your right hand out to change positions when suddenly,
a vine reaches out around your wrist and pulls you into the lattice,
firmly holding you in place.
Before you can react more and more vines shoot out,
each wrapping themselves around your body and pulling you in tighter.
You realise that while you’ve been climbing down,
these plants have been slowly and gently snaking themselves around your limbs
and you can no longer move.
The vines wrap you up and pull you into them,
absorbing you into a sea of branches and ivy. Never to be heard from again.
        """)
        try_again()
    else:
        print("Please answer A or B")
        lattice()


# End game congratulations

def congrats():
    print("""
Congratulations! YOU WIN!
You made it out of the house alive and in one piece.
Well done.
Would you like to test your luck and try again?
    """)
    answer = input("Please enter Yes or No: \n")
    if answer in yes:
        house_help()
    elif answer in no:
        exit()
    else:
        print("Please answer Yes or No")
        try_again()


# Stores users name for later use
name = input("Before we begin, what's your name? \n")

# Call functions to start game


def main():
    start()


main()
