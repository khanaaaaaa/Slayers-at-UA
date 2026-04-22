label prologue_start:

    scene black
    with memory_fade
    play sound "wind_soft.wav"

    thought "There is someone whom I know everything about."

    thought "But they don't remember me.."

    thought "...which feels insulting."    

    scene bg forest_sunset at bg_fit
    with slow_dissolve
    play music "memory_theme.mp3"

    show muiquiet at left_char
    show youngynquiet at right_char

    mui "..."

    hide muiquiet
    show muitalking at left_char

    mui "You came again."

    hide muiquiet
    show muitalking at left_char

    mui "...Don't people usually say their names?"

    hide muitalking
    show muiquiet at left_char
    show youngynquiet at right_char

    hide youngynquiet at right_char
    show youngyntalkingg at right_char

    "Usually."

    hide youngyntalkingg
    show youngynquiett at right_char

    hide youngynquiett
    show youngyntalkingg at right_char

    "Do you want to know mine?"
    hide youngyntalkingg  
    show youngynquiett at right_char

    hide muiquiet
    show muitalking at left_char
    
    mui "I don't know."
    mui "...You come here a lot."
    hide muitalking
    show muiquiet at left_char 
    hide muiquiet
    show muitalking at left_char
    mui "It feels strange not calling you anything."

    hide muitalking
    show muiquiet at left_char

    "...Then what would you call me?"

    hide muiquiet
    show muitalking at left_char

    mui "...I haven't decided yet."
    mui "Something that fits."
    hide muitalking
    show muiquiet at left_char
    hide youngynquiet
    show youngyntalkingg at right_char

    "That sounds like a lot of pressure."
    hide youngyntalkingg
    show youngynquiett at right_char
    
    hide muiquiet
    show muitalking at left_char

    mui "...You'll probably disappear before I figure it out anyway."
    hide muitalking
    show muiquiet at left_char

    hide younynquiett
    show youngyntalkingg at right_char

    "Then maybe you should hurry."
    hide youngyntalkingg

    mui "..."

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

    mui "I'll remember it."

    mui "...Why do you always stand in the same place?"

    yn "Why you always pretend not to look?"

    mui "...You're not from here."

    yn "No."

    yn "But neither are you."

    hide muiquiet
    show muitalking

    mui "...What does that mean?"

    yn "It means..."

    yn "You shouldn't be this calm."

    yn "Not with demons this close."

    mui "...Demons?"
    mui "You're the second person to say that."

    yn "Second?"

    hide muitalking
    show muiquiet at left_char

    mui "...My brother."

    mui "He says things like that."
    hide muitalking
    show muiquiet at left_char

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
    hide muiquiet
    show muitalking at left_char
    mui "... Should I trust you?"
    hide muitalking
    show muiquiet at left_char

    menu:
        "Yes.":
            hide muiquiet
            show muitalking at left_char
            mui "...Okay."
            hide muitalking
            show muiquiet at left_char
            hide youngynquiett
            show youngyntalkingg at right_char
            yn "That was easier than I expected."
        "I don't know.":
            hide muiquiet
            show muitalking at left_char
            mui "...Yeah"
            hide muitalking
            show muiquiet at left_char
            hide youngynquiett
            show youngyntalkingg at right_char
            mui "That makes sense."
        "No.":
            hide muiquiet
            show muitalking at left_char
            mui "...Right."
            hide muitalking
            show muiquiet at left_char
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

    yuichiro "Talking?"

    hide yuichirotalking
    show yuichiroquiet at right_char
    hide muiquiet
    show muitalking at left_char
    
    mui "...I was just—"

    hide muitalking
    show muiquiet at left_char
    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "Talking?"

    yuichiro "...Or staring again?"

    yuichiro "Who's the ghost?"

    hide yuichirotalking
    show yuichiroquiet at right_char
    hide muiquiet
    show muitalking at left_char

    mui "...They're not a ghost."

    hide muitalking
    show muiquiet at left_char
    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "Mm."

    yuichiro "...You gave them that look too."

    hide yuichirotalking
    show yuichiroquiet at right_char
    hide muiquiet
    show muitalking at left_char

    mui "...What look?"

    hide muitalking
    show muiquiet at left_char
    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "Like you’re trying to remember them before they’re gone."

    hide yuichirotalking
    show yuichiroquiet at right_char

    mui "..."

    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "...You like them?"

    hide yuichirotalking
    show yuichiroquiet at right_char
    hide muiquiet
    show muiquiet at left_char

    mui "...I don’t think that’s it."

    hide muitalking
    show muiquiet at left_char
    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "So you *do* think about it."

    hide yuichirotalking
    show yuichiroquiet at right_char
    hide muiquiet
    show muitalking at left_char

    mui "...You're annoying."

    hide muitalking
    show muiquiet at left_char
    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "...You're obvious."

    stop music fadeout 2.0

    play sound "wind_hollow.wav"

    thought "...Something changed here."

    thought "The air gets heavier."

    scene bg night_forest at bg_fit
    with slow_dissolve

    thought "This part..."

    thought "...I don't want to remember this part."
    play sound "distant_scream.wav"

    hide yuichirotalking
    show yuichiroquiet at right_char

    mui "...?"

    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "Stay here."

    yuichiro "Don’t move."

    hide yuichirotalking
    show yuichiroquiet at right_char
    hide muiquiet
    show muitalking at left_char

    mui "...What was that?"

    hide muitalking
    show muiquiet at left_char
    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "...Inside."

    hide yuichirotalking
    show yuichiroquiet at right_char


    scene bg house_night at bg_fit
    with hard_cut

    play sound "fire_crackle.wav"

    hide muiquiet
    show muitalking at left_char

    mui "...It smells strange."

    hide muitalking
    show muiquiet at left_char
    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "...Don’t look."

    hide yuichirotalking
    show yuichiroquiet at right_char
    hide muiquiet
    show muitalking at left_char

    mui "...Why?"

    hide muitalking
    show muiquiet at left_char
    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "...Just don’t."

    hide yuichirotalking
    show yuichiroquiet at right_char

    thought "...But he does."

    play sound "heartbeat.wav"

    thought "Red."

    thought "That’s where it comes from."

    hide muiquiet
    show yuichirotalking

    scene black

    mui "..."

    mui "...They're not moving."

    yuichiro "...I said don’t look."

    mui "...Why aren’t they moving?"
    yuichiro "Because they’re—"

    stop sound
    with flash_white

    scene black
    with memory_fade

    thought "...After that..."

    thought "...things don’t stay in order."

    thought "There was something else."

    thought "Something wrong."

    scene bg forest_dark at bg_fit
    with slow_dissolve

    play sound "low_growl.wav"

    thought "It wasn’t just an attack."

    thought "...Something was still there."

    mui "..."

    mui "...You told me to run."

    mui "...I didn’t."

    mui "...So now what?"

    yn "...If something feels wrong..."

    yn "...run."

    mui "...Too late."

    thought "That’s when it starts."
    thought "Not the memory."
    thought "The forgetting."

    scene black
    with Fade(1.5, 0.5, 2.0)

    jump mission_scene