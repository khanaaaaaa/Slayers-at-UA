# img
image black_vortex = Solid("#000000")
image bg sky="sky.png"
image bg street="mhastreet.png"

# transition
define wipe = ImageDissolve("black", 0.5, 32)
define snap = vpunch
define cut = MoveTransition(0.4)
transform fall_into_hole:
    yalign 0.5
    zoom 1.0
    alpha 1.0

    linear 0.4 yoffset 600 alpha 0.0 zoom 0.7

# start

label start:

    scene black
    with fade

    "Mui-chan, I really hate the color red..."

    crowyn "CAW CAW"
    crowyn "YOUR NEW MISSION! GO TO THE SOUTH!"
    "I'm coming!"
    mui "Get out of my way!"

    # At the South

    "Moon Breathing, 3rd form, Circadian Slah!"
    show demon1 at center
    pause 0.5
    show slash_effect at center
    with vpunch
    pause 0.1
    hide slash_effect
    hide demon1
    "Whew! Mission over!"
    demon2 "Oh my~ I didn't expect to come across a hashira."
    "Or maybe not!"
    "Moon breathing! 11th form, endless night!"
    demon2 "How sloppy~"
    demon2 "Now it's my turn~"
    mui "Mist breathing, 5th form, Sea of Clouds and Haze."
    show demon2 at center
    pause 0.5
    show slash_effect at center
    with vpunch
    pause 0.1
    hide slash_effect
    hide demon2
    "Oh was not expecting to see you here"
    "Muichiro Tokito"
    mui "What was your name again?"
    yn ""

    mui "BAHAHAHA"
    mui "Of course I remember you"
    mui "Daikon chan~"
    yn "I'm your senior, Muichiro!"
    mui "Daikon-chan, did you not eat enough today?"
    mui "Since when were you so weak?"
    yn "Let's just go home."
    mui "Okay, daikon-chan"
    show mui at center zorder 2
    pause 0.5
    play sound "teleport.wav"
    show demon2 at center zorder 1:
        alpha 0.0
        linear 0.05 alpha 1.0
    show black_vortex
    with Dissolve(0.05)
    pause 0.2
    show mui at fall_into_hole
    with vpunch
    play sound "void.wav"
    hide black_vortex
    hide mui
    yn "Huh what-!"
    demon2 "Your turn now~"
    scene white with Fade(0.1, 0.0, 0.3, color="#fff")
    scene bg street with fade
    #Aizawa
    "Aizawa Shota was doing his night patrol when he saw two kids lying on the cold floor"
    aizawa "I wonder if they're cosplaying or something."
    yn "Where am I? Didn't I die?"
    mui "Loud as ever"
    yn "Muichiro-san, I tho- I thought you died!"
    mui "I'm not that weak."
    aizawa "Okay kids, tell me what's going on"
    yn "Who's this old man?"
    aizawa "Old man?"
    yn "Who are you?"
    yn "I asked who are YOU?"
    mui "Calm down, I explained everything to him."
    yn "What?"
    mui "I think we somehow transported into another world."
    mui "They have something called quirks here, basically special powers they have."
    aizawa "You've been classified as a threat"    
    #goes to



    return