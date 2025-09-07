# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define DEBUG = False

define ybf = Character("Yuviiin bal Favijra")
define rvb = Character("Rayjk vu Beoplae")

# The game starts here.

label start:
    scene bg podium

    show podium1 podium

    show podium2 step

    play music "audio/music/podium buildup.wav" loop

    play audio "audio/se/crowd ambience.mp3" volume 0.5
    
    play audio "audio/se/yuviiin walking stairs.wav"

    if DEBUG:
        pause 0.0
    else:
        $ renpy.pause(14.0, hard=True)

    show yuviiin podium hands behind podium1, podium2

    ybf "Fairykind one and all."

    show yuviiin podium fist behind podium1, podium2
    
    play sound "audio/se/yuviiin tighten fist.wav"

    ybf "We were scattered across here, there and everywhere."

    ybf "Under the strugglehold of tyrants and degenerates."

    ybf "Not to serve for the greater good, but to suck at the Juuvket's tet and hide like cowards in their shadow."
    
    show yuviiin podium hands behind podium1, podium2

    ybf "And as your loyal Uvvjual, I have chained those madmen."

    ybf "I have brought them to the new order."

    ybf "I have brought all of Fairkind together under one banner."

    ybf "One truth of this world."

    scene cg podium yuviiin close up
    
    ybf "UNITY."

    ybf "Only together can we fight our real enemy."

    play sound "audio/se/yuviiin slam fist.wav"

    show cg podium yuviiin slam fist with vpunch

    stop music fadeout 1.0

    ybf "THE HUMAN!"
    
    play music "audio/music/podium cheer.wav" loop

    ybf "WHILE WE WERE SUFFERING AND BRINGING THE WORLD TO ORDER."

    ybf "THESE HUMANS WERE POISONING OUR WATER, BURNING OUR FORESTS AND PLUNDERING OUR LAND."

    scene bg podium

    show podium1 podium yuviiin

    show podium2 step

    ybf "As such with the world united and Fairykind prospering."

    ybf "I have taken the initiative to exterminating their foul race once and for all."

    ybf "So I ask you who is your Uvvjual and what are we going to do?"

    scene cg army cheer

    play sound "audio/se/army scream.wav" fadeout 0.1 loop

    "AOU AOU AOU!"

    ybf "AND SO... {w}THE CLEANSING BEGINS!"

    stop sound fadeout 0.5

    stop music fadeout 1.0

    scene cg yuviiin coach with dissolve
    
    pause 2.0

    play sound "audio/se/coach door close.wav"

    scene bg coach inside with dissolve

    play music "audio/music/coach chat.mp3" loop

    show rayjk rubhands at right

    show yuviiin at left
    
    play sound "audio/se/horse walking.wav" loop

    rvb "What is the next plan."

    ybf "There is no next plan."

    rvb "So we exterminate the humans and then we have achieved world peace."

    ybf "Yes, for a simple as it may seem, once the humans are no longer an issue we can proceed restoring the world."

    rvb "There is an old saying:{p}\"A fairy toils the field when he is hungry.\"{p}\"A mad fairy toils the field until all he can be is hungry.\""

    ybf "We must do something...{p}I have lost so much to become the Uvvjual...{p}This will be the greatest push for Fairykind to reaching eternal peace."

    rvb "At the cost of distrupting the natural order."

    ybf "There is no natural order for humans!"

    ybf "They are like a illness, they enter and then exit once there is no more blood to spill."

    rvb "Let us hope that you are right, I thought you mad once."

    rvb "But you have shown that madness is the only way to bring the ultimate good."

    ybf "I am happy you trust me so, I only wish that I had acted sooner."

    return
