label mission_scene:
    scene bg forest_night
    play sound "wind.wav"
    with fade
    thought "We trained here."
    thought "Back when he still laughed."
    "Moon Breathing, Third Form... Lunar Rings."
    show demon1 at center:
        zoom 0.8
        ease 0.2 zoom 1.0
    pause 0.2
    show slash_effect at center
    with vpunch
    hide slash_effect
    hide demon1
    thought "Too easy... just like old times."
    demon2 "Ara~ a Hashira?"
    demon2 "And you... I sense something familiar."
    thought "...No."
    thought "Don't say it."
    show demon2 at center
    demon2 "That scent... regreat?"
    mui "Mist Breathing, Fifht Form... Sea of Clouds and Haze."
    show slash_effect at center
    with hpunch
    hide slash_effect
    hide demon2
    pause 0.3

    show mui at center:
        zoom 1.1
    mui "...You're still alive."
    thought "Nice to meet you too!"
    mui "You got slower."
    mui "What was your name again?"
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()
    if player_name = "":
        $ player_name = "Y/N"
    $ p = Character("[player_name]", color="#ffffff")
    p "...It's [player_name]."
    mui "Right."
    mui "You used to hate when I forgot it."
    pause 0.3
    p "You never used to forget it."
    mui "People change."
    thought "That wasn't an answer."
    p "You used to call me 'sparrow'."
    mui "..I don't remember that."
    pause
    mui "...I don't remember a lot of things."

    play sound "rumble.wav"
    show demon2 at center:
        alpha 0.0
        linear 0.1 alpha 1.0
    demon2 "A bond.. How delicious."
    mui "Shut up."
    thought "He's angry."
    thought "He never used to get angry."
    show black_vortex:
        zoom 0.5
        linear 0.2 zoom 1.2
    with vpunch
    demon2 "Fall apart together."
    show mui at fall_into_hole
    with hpunch
    p "Muichiro-!"
    mui "..Don't call me that like you used to."
    scene white with Fade(0.1, 0.0, 0.3)
    jump mha_intro