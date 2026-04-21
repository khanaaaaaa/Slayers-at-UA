label prologue_start:

    scene black
    with memory_fade
    play sound "wind_soft.wav"

    thought "There is someone whom I know everything about."

    pause 0.5

    thought "But they don't remember me.."

    thought "...which feels insulting."

    pause

    scene bg forest_sunset at bg_fit
    with slow_dissolve
    play music "memory_theme.mp3"

    pause 1.0

    show muiquiet at left_char
    show youngynquiet at right_char

    pause 0.8

    mui "..."

    pause 0.5

    hide muiquiet
    show muitalking at left_char

    mui "You came again."
    pause 0.5

    hide muiquiet
    show muitalking at left_char

    mui "...Don't people usually say their names?"

    hide muitalking
    show muiquiet at left_char
    show youngynquiet at right_char
    pause

    hide youngynquiet at right_char
    show youngyntalkingg at right_char

    "Usually."

    hide youngyntalkingg
    show youngynquiett at right_char

    pause 0.3

    hide youngynquiett
    show youngyntalkingg at right_char

    "Do you want to know mine?"
    hide youngyntalkingg  
    show youngynquiett at right_char with slow_dissolve

    pause

    hide muiquiet
    show muitalking at left_char with slow_dissolve
    
    mui "I don't know."
    mui "...You come here a lot."
    hide muitalking
    show muiquiet at left_char with slow_dissolve
    pause
    hide muiquiet
    show muitalking at left_char
    mui "It feels strange not calling you anything."

    hide muitalking
    show muiquiet at left_char

    pause 0.8

    "...Then what would you call me?"

    pause

    hide muiquiet
    show muitalking at left_char

    mui "...I haven't decided yet."
    mui "Something that fits."
    hide muitalking
    show muiquiet at left_char

    pause
    hide youngynquiet
    show youngyntalkingg at right_char

    "That sounds like a lot of pressure."
    hide youngyntalkingg
    show youngynquiett at right_char

    pause
    hide muiquiet
    show muitalking at right_char

    mui "...You'll probably disappear before I figure it out anyway."
    hide muitalking
    show muiquiet at left_char

    pause 1.0
    hide younynquiett
    show youngyntalkingg at right_char

    "Then maybe you should hurry."
    hide youngyntalkingg

    pause

    mui "..."

    pause 0.5
    hide muiquiet
    show muitalking at left_char

    mui "...Then tell me."

    hide muitalking
    show muiquiet at left_char

    define e = Character("[player_name]")

    default player_name = "Player"
    $ player_name = renpy.input("What is your name?")
    $ player_bame = player_name.strip()

    if player_name == "":
        $ player_name = "Player"


    hide muiquiet 
    show muitalking at left_char

    mui "...[player_name]."

    pause

    mui "I'll remember it."

    pause 0.6

    pause 0.4

    mui "...Why do you always stand in the same place?"

    yn "Why you always pretend not to look?"
    pause

    hide muitalking
    show muiquiet

    pause 0.8

    mui "...You're not from here."

    yn "No."

    pause 0.3

    yn "But neither are you."

    pause

    hide muiquiet
    show muitalking

    mui "...What does that mean?"

    pause

    yn "It means..."

    pause 0.5

    yn "You shouldn't be this calm."

    yn "Not with demons this close."

    pause

    mui "...Demons?"

    pause 0.4

    mui "You're the second person to say that."

    pause

    yn "Second?"

    pause

    hide muitalking
    show muiquiet at left_char

    mui "...My brother."

    mui "He says things like that."
    hide muitalking
    show muiquiet at left_char

    pause

    hide youngynquiett
    show youngyntalkingg at right_char
    yn "Then you should listen to him."
    hide youngyntalkingg
    show youngynquiett at right_char
    hide muiquiet
    show muitalking at left_char

    mui "...I wanted to hear it from someone else."
    hide muitalking
    show muiquiet at left_char
    hide youngynquiett
    show youngyntalkingg at right_char
    yn "You're strange."
    hide youngyntalkingg
    show youngynquiet at right_char
    hide muiquiet
    show muitalking at left_char
    mui "...I get that a lot."
    hide muitalkingg
    show muiquiet at right_char
    pause
    hide muiquiet
    show muitalking at left_char
    mui "... Should I trust you?"
    hide muitalking
    show muiquiet at left_char

    pause

    menu:
        "Yes.":
            hide muiquiet
            show muitalking at left_char
            mui "...Okay."
            hide muitalking
            show muiquiet at left_char
            pause 0.3
            hide youngynquiett
            show youngyntalkingg at right_char
            yn "That was easier than I expected."
        "I don't know.":
            hide muiquiet
            show muitalking at left_char
            mui "...Yeah"
            hide muitalking
            show muiquiet at left_char
            pause 0.3
            hide youngynquiett
            show youngyntalkingg at right_char
            mui "That makes sense."
        "No.":
            hide muiquiet
            show muitalking at left_char
            mui "...Right."
            hide muitalking
            show muiquiet at left_char
            pause 0.3
            hide youngynquiett
            show youngyntalkingg at right_char
            mui "...I figured."

    yn "Then listen carefully."

    yn "If something feels wrong..."

    yn "...run."
    hide youngyntalkingg
    show youngynquiett at right_char
    hide muiquiet
    show muitalking at left_char

    mui "...Do I need to?"
    hide muitalking
    show muiquiet at left_char
    hide youngynquiett
    show youngyntalkingg at right_char

    yn "Yes."


    scene bg forest_sunset at bg_fit

    show yuichiroquiet at right_char
    show muiquiet at right_char
    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "...So this is where you've been disappearing to."


    hide muiquiet
    show muitalking at left_char

    mui "...You followed me?"


    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "You’re not subtle."

    yuichiro "You leave at the same time every day."

    yuichiro "...And come back oddly happy, yet disturbed."


    yn "..."

    
    mui "...I was just—"

    pause

    yuichiro "Talking?"

    pause

    yuichiro "...Or staring again?"

    pause 0.4

    yuichiro "Who's the ghost?"

    pause

    mui "...They're not a ghost."

    pause

    yuichiro "Mm."

    pause 0.3

    yuichiro "...You gave them that look too."

    pause

    mui "...What look?"

    pause

    yuichiro "Like you’re trying to remember them before they’re gone."

    pause 1.0

    mui "..."

    pause

    yuichiro "...You like them?"

    pause 0.4

    mui "...I don’t think that’s it."

    pause

    yuichiro "So you *do* think about it."

    pause 0.5

    mui "...You're annoying."

    pause

    yuichiro "...You're obvious."

    pause 1.0


    stop music fadeout 2.0

    play sound "wind_hollow.wav"

    thought "...Something changes here."

    thought "The air gets heavier."

    pause

    scene bg night_forest at bg_fit
    with slow_dissolve

    thought "This part..."

    thought "...I don't want to remember this part."

    pause 1.0

    play sound "distant_scream.wav"

    mui "...?"

    pause

    yuichiro "Stay here."

    pause 0.3

    yuichiro "Don’t move."

    pause

    mui "...What was that?"

    pause

    yuichiro "...Inside."

    pause

    scene bg house_night at bg_fit
    with hard_cut

    play sound "fire_crackle.wav"

    pause 0.5

    mui "...It smells strange."

    pause

    yuichiro "...Don’t look."

    pause

    mui "...Why?"

    pause 0.5

    yuichiro "...Just don’t."

    pause 1.0

    thought "...But he does."

    pause

    play sound "heartbeat.wav"

    thought "Red."

    thought "That’s where it comes from."

    pause

    mui "..."

    pause 0.5

    mui "...They're not moving."

    pause

    yuichiro "...I said don’t look."

    pause

    mui "...Why aren’t they moving?"

    pause 0.8

    yuichiro "Because they’re—"

    pause

    stop sound
    with flash_white

    pause 1.0

    scene black
    with memory_fade

    thought "...After that..."

    thought "...things don’t stay in order."

    pause

    thought "There was something else."

    thought "Something wrong."

    pause

    scene bg forest_dark at bg_fit
    with slow_dissolve

    play sound "low_growl.wav"

    thought "It wasn’t just an attack."

    thought "...Something was still there."

    pause

    mui "..."

    pause

    mui "...You told me to run."

    pause

    mui "...I didn’t."

    pause 0.5

    mui "...So now what?"

    pause

    yn "...If something feels wrong..."

    yn "...run."

    pause

    mui "...Too late."

    pause

    thought "That’s when it starts."
    thought "Not the memory."
    thought "The forgetting."

    pause

    scene black
    with Fade(1.5, 0.5, 2.0)

    jump mission_scene