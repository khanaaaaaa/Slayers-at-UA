label prologue_start:

    scene black
    with fade

    play sound "wind_soft.wav"

    thought "...Red"

    menu:
        "Maybe he was wrong.":
            thought "People misremember things."
            thought "Even people close to you."
        "Maybe I changed.":
            thought "I wonder if he ever even knew me."

    thought "He used to say I remind him of the color red."
    thought "I wonder what he meant..."

    pause

    scene bg forest_sunset
    with dissolve

    play music "memory_theme.mp3"

    thought "It leaks in… like mist through broken wood."

    show mui at left
    show yuichiro at right

    yuichiro "You swing your blade like you're trying to forget something."
    mui "I don't forget things."
    yuichiro "We both know that's a lie, airhead."

    pause

    menu:
        "Step between them":
            p_child "He's getting better."
            yuichiro "You always say that."
        "Stay where you are":
            thought "I remember this argument..."
            thought "I think."

    yuichiro "You don't think when you fight."
    yuichiro "That's why he's close to you."

    mui "...I don't need anyone close."

    pause

    menu:
        "That's not true.":
            yuichiro "Yeah, Muichiro. What are you saying?"
        "He doesn't mean that.":
            yuichiro "He doesn't know how to express things properly."

    mui "I don't need anyone."

    pause 1.0

    yuichiro "..."
    yuichiro "Don't lose yourself in him."

    pause

    scene black
    with fade

    thought "Yuichiro Tokito."
    thought "Muichiro's older brother."

    menu:
        "A wall built to protect him.":
            thought "Too sharp to approach."
        "A blade pointed the wrong way.":
            thought "Protection and harm look the same to him."

    pause

    thought "And Muichiro..."
    thought "He always stood between both versions of Yuichiro."

    pause

    play sound "crow.wav"

    crowyn "CAW! CAW!"
    crowyn "KASUGAI CROW REPORT!"
    crowyn "NEW MISSION - SOUTHERN DISTRICT!"

    stop music fadeout 1.5

    thought "The past never gets buried."

    menu:
        "Do I have a partner?":
            crowyn "TOKITO MUICHIRO WILL ACCOMPANY YOU."

    menu:
        "Of course.":
            thought "Some things don't change."
        "That's unfortunate.":
            thought "But perhaps necessary."
        "Understood.":
            thought "No room for hesitation."

    pause 0.6

    menu:
        "I hope he remembers.":
            thought "Even a little."
        "It's better if he doesn't.":
            thought "Memories only complicate things."
        "I don't want him to.":
            thought "Some things are easier forgotten."

    pause

    thought "Muichiro Tokito..."
    thought "Please don't remember me..."

    scene black
    with fade

    jump mission_scene