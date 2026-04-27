label anchor_scene:

    scene bg rooftop at bg_fit
    with slow_dissolve

    play music "memory_theme.mp3" fadein 2.5
    pause 0.6

    show muichiroquiet at center_char
    with dissolve

    thought "He's here. Of course he is."
    thought "I don't know if he came up here for a reason or if he just ended up here."
    thought "With him it's hard to tell."
    pause 0.6

    hide muichiroquiet
    show muichirotalking at center_char
    mui "You look less dead."
    hide muichirotalking
    show muichiroquiet at center_char

    yn "...Thanks."
    pause 0.3

    hide muichiroquiet
    show muichirotalking at center_char
    mui "It wasn't a compliment."
    hide muichirotalking
    show muichiroquiet at center_char

    thought "Yes it was."
    pause 0.5

    yn "...I remembered something. Where I'm from."
    yn "Why I know things I shouldn't."
    pause 0.4

    hide muichiroquiet
    show muichirotalking at center_char
    mui "...Finally."
    hide muichirotalking
    show muichiroquiet at center_char

    yn "...That's all you have to say?"
    pause 0.3

    hide muichiroquiet
    show muichirotalking at center_char
    mui "You've been carrying it around for weeks."
    mui "It was getting obvious."
    hide muichirotalking
    show muichiroquiet at center_char


    yn "...Where I came from, you were a story..."
    yn "Your world... The demons... All of it."
    yn "Someone wrote it... and I read it."
    yn "I knew everything before I ever got there."
    pause 0.4

    hide muichiroquiet
    show muichirotalking at center_char
    mui "...So you knew what would happen to me."
    hide muichirotalking
    show muichiroquiet at center_char

    yn "...Yes."
    pause 0.4

    hide muichiroquiet
    show muichirotalking at center_char
    mui "And you changed it."
    hide muichirotalking
    show muichiroquiet at center_char

    yn "...Yes."
    pause 0.5

    hide muichiroquiet
    show muichirotalking at center_char
    mui "..."
    mui "Okay."
    hide muichirotalking
    show muichiroquiet at center_char

    thought "...Okay?"
    thought "That's it???"
    thought "I spent weeks dreading this conversation and and all he has to say is a okay????"
    pause 0.6

    yn "...That's all?"
    pause 0.3

    hide muichiroquiet
    show muichirotalking at center_char
    mui "What do you want me to say."
    hide muichirotalking
    show muichiroquiet at center_char

    menu:
        "I don't know. Something.":
            yn "...I don't know. Something."
            hide muichiroquiet
            show muichirotalking at center_char
            mui "You read about me. You came to my world. You changed things."
            mui "...And now you're here."
            mui "That's a lot of effort."
            hide muichirotalking
            show muichiroquiet at center_char
            thought "He says it like it's mildly inconvenient."
            thought "Like I rearranged his furniture."

        "Aren't you angry?":
            yn "...Aren't you angry?"
            hide muichiroquiet
            show muichirotalking at center_char
            mui "About what."
            hide muichirotalking
            show muichiroquiet at center_char
            yn "I changed your story. Without asking."
            hide muichiroquiet
            show muichirotalking at center_char
            mui "...You're still here, aren't you."
            mui "So it worked out."
            hide muichirotalking
            show muichiroquiet at center_char
            thought "That's not an answer."
            thought "That's also completely an answer."

        "...There's more.":
            yn "...There's more."
            hide muichiroquiet
            show muichirotalking at center_char
            mui "I assumed."
            hide muichirotalking
            show muichiroquiet at center_char

    pause 0.5

    yn "...Before I came here."
    yn "I didn't have anywhere to be."
    yn "No family. No one waiting."
    yn "I just... ended up at a river one night."
    yn "And then I ended up here."
    pause 0.6

    
    mui "..."
    pause 0.4
    hide muichiroquiet
    show muichirotalking at center_char
    mui "That's it?"
    hide muichirotalking
    show muichiroquiet at center_char

    yn "...That's it."
    pause 0.4

    hide muichiroquiet
    show muichirotalking at center_char
    mui "No grand purpose?"
    mui "You just fell in a river?"
    hide muichirotalking
    show muichiroquiet at center_char

    thought "When he says it like that it sounds almost funny."
    thought "It's not funny."
    thought "...It's a little funny."
    pause 0.5

    yn "...Pretty much."
    pause 0.3

    hide muichiroquiet
    show muichirotalking at center_char
    mui "Tell me your name."
    hide muichirotalking
    show muichiroquiet at center_char

    yn "...You know my name."
    pause 0.3

    hide muichiroquiet
    show muichirotalking at center_char
    mui "Tell me anyway."
    hide muichirotalking
    show muichiroquiet at center_char

    yn "[player_name]."
    pause 0.4

    hide muichiroquiet
    show muichirotalking at center_char
    mui "[player_name]."
    mui "...Sparrow."
    hide muichirotalking
    show muichiroquiet at center_char

    yn "...You remembered."
    pause 0.3

    hide muichiroquiet
    show muichirotalking at center_char
    mui "Fragments."
    mui "The forest... you standing in the same place every time."
    mui "...Annoying habit."
    hide muichirotalking
    show muichiroquiet at center_char

    thought "He remembered and his first instinct was to criticize my posture."
    thought "That's the most him thing."
    pause 0.8

    scene black
    with Fade(1.0, 0.5, 1.5)

    jump epilogue_scene
