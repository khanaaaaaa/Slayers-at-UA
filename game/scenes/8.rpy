label epilogue_scene:

    scene bg rooftop at bg_fit
    with slow_dissolve

    play music "memory_theme.mp3" fadein 3.0
    pause 0.8

    thought "I don't know how this ends."
    thought "I used to. I knew every ending for every story."
    thought "..."
    thought "But I changed things. And now I don't know."
    thought "And I think — I think that might be okay."
    pause 0.6

    show muichiroquiet at center_char
    with dissolve

    thought "He's still here. He keeps being here."
    thought "Even when he forgets. He comes back."
    pause 0.5

    hide muichiroquiet
    show muichirotalking at center_char
    mui "...What are you thinking about."
    hide muichirotalking
    show muichiroquiet at center_char

    yn "...Endings."
    pause 0.3

    hide muichiroquiet
    show muitalking at center_char
    mui "Do you know how this one goes."
    hide muichirotalking
    show muichiroquiet at center_char

    thought "No. For the first time. No."
    pause 0.5

    yn "...No. Not this one."
    pause 0.4

    hide muichiroquiet
    show muichirotalking at center_char
    mui "Good."
    hide muichirotalking
    show muichiroquiet at center_char

    pause 0.6

    thought "There are things I still haven't told him."
    thought "About what I did. About what I left behind."
    thought "About whether any of this is real."
    thought "Or whether I'm still in the river. Sinking. Dreaming."
    thought "..."
    thought "But I'm here. And he's here."
    thought "And for now — that's enough."
    pause 0.6

    hide muichiroquiet
    show ochakotalking at center_char
    with dissolve

    ochako "There you two are!"
    ochako "Aizawa-sensei's been looking for you."
    ochako "Training starts in ten minutes."
    hide ochacotalking
    show ochacoquiet at center_char

    thought "Right. The world keeps moving."
    thought "Even when you're not ready."
    pause 0.4

    hide ochacoquiet 

    yn "...We'll be right down."
    pause 0.3

    show ochacotalking at center_char

    ochako "Okay!"
    ochako "..."
    ochako "You look better, by the way."
    ochako "More... present."
    pause 0.4

    hide ochacotalking
    show ochacoquiet at center_char

    thought "She noticed. Of course she noticed."
    pause 0.4

    hide ochacoquiet

    yn "...Thanks."
    pause 0.4

    hide ochako

    pause 0.5

    hide muichiroquiet
    show muichirotalking at center_char
    mui "...Sparrow."
    hide muichirotalking
    show muichiroquiet at center_char

    thought "..."
    thought "He said it. On his own. Without me asking."
    pause 0.5

    hide muichiroquiet

    yn "...Yeah?"
    pause 0.4

    show muichiroquiet at center_char
    mui "..."
    hide muichiroquiet
    show muichirotalking at center_char
    mui "Don't disappear."
    hide muichirotalking
    show muichiroquiet at center_char

    pause 0.8

    thought "...I'll try."
    pause 0.5

    hide muichiroquiet

    yn "...I'll try."
    pause 0.6

    show muichirotalking at center_char
    mui "That's enough."
    hide muichirotalking
    show muichiroquiet at center_char

    pause 0.8

    scene black
    with Fade(1.5, 1.0, 2.0)

    stop music fadeout 3.0

    thought "There is someone I know everything about."
    thought "His name. His breathing form."
    thought "The way he tilts his head when he's deciding whether to care."
    thought "He doesn't remember me. Not all of it. Not yet."
    thought "..."
    thought "But he's trying."
    thought "And I'm still here."
    thought "Which is more than I expected."
    thought "When I went into that river."
    thought "..."
    thought "I think that counts for something."
    pause 1.0
    hide muichiroquiet

    scene black
    with end_fade

    pause 1.5

    return
