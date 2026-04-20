label prologue_start:

    scene black
    with memory_fade
    play sound "wind_soft.wav"
    thought "...Red."
    thought "A trace."
    pause 0.5
    thought "Something left behind."
    pause
    scene bg forest_sunset at bg_fit, drift
    with slow_dissolve
    play music "memory_theme.mp3"
    thought "It doesn't return."
    thought "It lingers."
    show muiquiet at left_char
    show yuichiroquiet at right_char
    pause 0.5
    hide yuichiroquiet
    show yuichirotalking at right_char with dissolve
    yuichiro "Your blade is wavering."
    yuichiro "You're looking somewhere else."
    hide yuichirotalking
    show yuichiroquiet at right_char 
    mui "..."
    pause 0.4
    hide muiquiet
    show muitalking at left_char with dissolve
    mui "It's the wind."
    hide muitalking
    show muiquiet at left_char
    hide yuichiroquiet
    show yuichirotalking at right_char 
    yuichiro "Wind doesn't hesitate."
    pause 0.5
    yuichiro "...People do."
    hide yuichirotalking
    show yuichiroquiet at right_char
    pause
    show screen flash_overlay
    with flash_white
    "That's enough."
    yuichiro "Move."
    hide flash_white

    pause 0.5

    hide yuichiroquiet
    show yuichirotalking at right_char with dissolve

    yuichiro "If you keep drifting..."

    yuichiro "...you'll disappear."

    hide yuichirotalking
    show yuichiroquiet at right_char with dissolve

    pause 0.3

    hide muiquiet
    show muitalking at left_char with dissolve

    mui "Then I disappear."

    hide muitalking
    show muiquiet

    pause

    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "That's easy to say."

    yuichiro "You're not the one who stays behind."

    hide yuichirotalking
    show yuichiroquiet at right_char

    pause

    menu:
        "He doesn't mean it.":
            "He just..."
            hide yuichiroquiet
            show yuichirotaling at right_char
            yuichiro "Don't soften it."

    pause 0.5
    hide yuichirotalking
    show yuichiroquiet at right_char with dissolve

    mui "..."

    hide muiquiet
    show muitalking at left_char with dissolve 

    mui "I don't need anything."

    hide muitalking
    show muiquiet

    pause 1.0

    hide yuichiroquiet
    show yuichirotalking with dissolve

    yuichiro "...Then don't lose it."

    pause 0.4

    yuichiro "Whatever's left."

    hide yuichirotalking

    pause

    stop music fadeout 2.0

    scene black
    with memory_fade

    thought "Yuichiro Tokito."

    thought "He spoke like a blade."
    thought "Straight. Unyielding."

    pause

    menu:
        "A wall.":
            thought "Nothing passed through."
        "A wound.":
            thought "Nothing healed either."

    pause

    thought "And Muichiro..."

    thought "Like mist."

    thought "There. But I cannot hold him."

    pause

    play sound "crow.wav"

    crowyn "CAW! CAW!"
    crowyn "KASUGAI CROW REPORT!"

    crowyn "NEW MISSION - SOUTHERN DISTRICT!"

    # sudden reality cut
    stop music
    with hard_cut

    pause 0.3

    thought "..."

    thought "It follows."

    thought "Even now."

    pause

    menu:
        "Do I have a partner?":
            crowyn "TOKITO MUICHIRO WILL ACCOMPANY YOU."

    pause 0.5

    menu:
        "Of course.":
            thought "Some paths repeat."
        "That's unfortunate.":
            thought "So does this."
        "Understood.":
            thought "No deviation."

    pause 0.6

    thought "I hope he remembers."
    thought "Or maybe not."
    thought "Some things fade for a reason."

    pause

    thought "Tokito Muichiro..."

    pause 0.5

    thought "...stay in the mist."

    scene black
    with Fade(1.5, 0.5, 2.0)

    jump mission_scene