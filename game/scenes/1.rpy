label prologue_start:

    scene black
    with memory_fade

    play sound "wind_soft.wav" fadein 2.0

    thought "There is someone I know everything about."
    pause 0.6
    thought "His name."
    pause 0.3
    thought "His breathing form."
    pause 0.3
    thought "The way he tilts his head when he's deciding whether to care."
    pause 0.8
    thought "But he doesn't remember me."
    pause 0.5
    thought "..."
    pause 0.4
    thought "Which is fine."
    pause 0.4
    thought "I think."
    pause 0.5
    thought "I don't remember much either."
    pause 1.2

    scene bg forest_sunset at bg_fit
    with slow_dissolve

    play music "memory_theme.mp3" fadein 2.5

    show youngynquiet at right_char
    with dissolve

    pause 0.5

    thought "He'll come from the left."
    pause 0.3
    thought "He always does."
    pause 0.5

    show muiquiet at left_char
    with dissolve

    pause 0.6

    thought "...See."
    pause 0.8

    mui "..."
    pause 0.4

    hide muiquiet
    show muitalking at left_char

    mui "You came again."

    hide muitalking
    show muiquiet at left_char

    pause 0.3

    thought "Don't say his name."
    pause 0.3
    thought "You're not supposed to know it yet."
    pause 0.8

    hide muiquiet
    show muitalking at left_char

    mui "...Don't people usually say their names?"

    hide muitalking
    show muiquiet at left_char

    hide youngynquiet
    show youngyntalkingg at right_char

    "Usually."
    pause 0.4
    "Do you want to know mine?"

    hide youngyntalkingg
    show youngynquiett at right_char

    hide muiquiet
    show muitalking at left_char

    mui "I don't know."
    pause 0.4
    mui "...You come here a lot."
    pause 0.3
    mui "It feels strange not calling you anything."

    hide muitalking
    show muiquiet at left_char

    hide youngynquiett
    show youngyntalkingg at right_char

    "...Then what would you call me?"

    hide youngyntalkingg
    show youngynquiett at right_char

    hide muiquiet
    show muitalking at left_char

    mui "...I haven't decided yet."
    pause 0.3
    mui "Something that fits."

    hide muitalking
    show muiquiet at left_char

    hide youngynquiett
    show youngyntalkingg at right_char

    "That sounds like a lot of pressure."

    hide youngyntalkingg
    show youngynquiett at right_char

    hide muiquiet
    show muitalking at left_char

    mui "...You'll probably disappear before I figure it out anyway."

    hide muitalking
    show muiquiet at left_char

    thought "He says that every time."
    pause 0.4
    thought "..."
    pause 0.3
    thought "Wait."
    pause 0.4
    thought "Every time?"
    pause 0.6
    thought "How many times have we done this?"
    pause 1.0

    hide youngynquiett
    show youngyntalkingg at right_char

    "Then maybe you should hurry."

    hide youngyntalkingg
    show youngynquiett at right_char

    mui "..."
    pause 0.6

    hide muiquiet
    show muitalking at left_char

    mui "...Then tell me."

    hide muitalking
    show muiquiet at left_char

    $ player_name = renpy.input("What is your name?", length=20)
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Player"

    hide muiquiet
    show muitalking at left_char

    mui "...[player_name]."
    pause 0.5
    mui "I'll remember it."

    hide muitalking
    show muiquiet at left_char

    thought "He won't."
    pause 0.5
    thought "He never does."
    pause 0.5
    thought "But I keep telling him anyway."
    pause 1.0

    hide muiquiet
    show muitalking at left_char

    mui "...Why do you always stand in the same place?"

    hide muitalking
    show muiquiet at left_char

    hide youngynquiett
    show youngyntalkingg at right_char

    yn "Why do you always pretend not to look?"

    hide youngyntalkingg
    show youngynquiett at right_char

    hide muiquiet
    show muitalking at left_char

    mui "...You're not from here."

    hide muitalking
    show muiquiet at left_char

    hide youngynquiett
    show youngyntalkingg at right_char

    yn "No."
    pause 0.3
    yn "But neither are you."

    hide youngyntalkingg
    show youngynquiett at right_char

    hide muiquiet
    show muitalking at left_char

    mui "...What does that mean?"

    hide muitalking
    show muiquiet at left_char

    thought "It means—"
    pause 0.3

    scene black
    with flash_white

    thought "—bright lights—"
    pause 0.2
    thought "—a building, glass and steel—"
    pause 0.2
    thought "—someone calling her name—"
    pause 0.2
    thought "—not [player_name]—"
    pause 0.3
    thought "—something else—"
    pause 0.4

    scene bg forest_sunset at bg_fit
    with soft_dissolve

    show muiquiet at left_char
    show youngynquiett at right_char

    pause 0.5

    thought "..."
    pause 0.4
    thought "What was that."
    pause 0.5
    thought "Instinct. Probably."
    pause 0.4
    thought "Just instinct."
    pause 0.8

    hide youngynquiett
    show youngyntalkingg at right_char

    yn "It means..."
    pause 0.4
    yn "You shouldn't be this calm."
    pause 0.3
    yn "Not with demons this close."

    hide youngyntalkingg
    show youngynquiett at right_char

    hide muiquiet
    show muitalking at left_char

    mui "...Demons?"
    pause 0.3
    mui "You're the second person to say that."

    hide muitalking
    show muiquiet at left_char

    hide youngynquiett
    show youngyntalkingg at right_char

    yn "Second?"

    hide youngyntalkingg
    show youngynquiett at right_char

    hide muiquiet
    show muitalking at left_char

    mui "...My brother."
    pause 0.4
    mui "He says things like that."

    hide muitalking
    show muiquiet at left_char

    thought "Yuichiro."
    pause 0.3
    thought "He's protective. Harsh. Loves Muichiro more than he can say."
    pause 0.4
    thought "..."
    pause 0.3
    thought "How do I know that."
    pause 0.8

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
    show youngynquiett at right_char

    hide muiquiet
    show muitalking at left_char

    mui "...I get that a lot."
    pause 0.5
    mui "...Should I trust you?"

    hide muitalking
    show muiquiet at left_char

    menu:
        "...Yes. I think you should.":
            hide muiquiet
            show muitalking at left_char
            mui "...Okay."
            hide muitalking
            show muiquiet at left_char
            hide youngynquiett
            show youngyntalkingg at right_char
            yn "That was easier than I expected."
            hide youngyntalkingg
            show youngynquiett at right_char
            thought "It always is."
            pause 0.4
            thought "..."
            pause 0.3
            thought "Always?"
            pause 0.6

        "...I don't know yet. But I'm still here.":
            hide muiquiet
            show muitalking at left_char
            mui "...Yeah."
            pause 0.3
            mui "That makes sense."
            hide muitalking
            show muiquiet at left_char
            thought "He's not offended."
            pause 0.3
            thought "He never is."
            pause 0.4
            thought "I don't know if that's a good thing."
            pause 0.6

        "...No. But I'll stay anyway.":
            hide muiquiet
            show muitalking at left_char
            mui "...Right."
            pause 0.3
            mui "...I figured."
            hide muitalking
            show muiquiet at left_char
            thought "He says that like he expected it."
            pause 0.4
            thought "Like he's been told no before."
            pause 0.4
            thought "By me."
            pause 0.6

    pause 0.6

    hide youngynquiett
    show youngyntalkingg at right_char

    yn "Then listen carefully."
    pause 0.4
    yn "If something feels wrong..."
    pause 0.5
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

    menu:
        "Yes. Promise me.":
            yn "Yes."
            pause 0.3
            yn "Promise me."
            hide youngyntalkingg
            show youngynquiett at right_char
            pause 0.4
            hide muiquiet
            show muitalking at left_char
            mui "..."
            pause 0.3
            mui "...Okay."
            hide muitalking
            show muiquiet at left_char
            thought "He says it like it's nothing."
            pause 0.3
            thought "Like promises are easy."
            pause 0.3
            thought "He doesn't know what it costs me to ask."
            pause 0.6

        "Yes. Even if you think you don't.":
            yn "Yes."
            pause 0.3
            yn "Even if you think you don't."
            hide youngyntalkingg
            show youngynquiett at right_char
            pause 0.4
            hide muiquiet
            show muitalking at left_char
            mui "..."
            pause 0.4
            mui "...That's a strange way to say it."
            hide muitalking
            show muiquiet at left_char
            thought "I know."
            pause 0.3
            thought "Because I know he won't."
            pause 0.3
            thought "And I'm asking anyway."
            pause 0.6

        "Just... please.":
            yn "Just..."
            pause 0.4
            yn "...please."
            hide youngyntalkingg
            show youngynquiett at right_char
            pause 0.5
            hide muiquiet
            show muitalking at left_char
            mui "..."
            pause 0.5
            mui "...Okay."
            hide muitalking
            show muiquiet at left_char
            thought "He looks at me differently when I say please."
            pause 0.3
            thought "Like it surprises him."
            pause 0.3
            thought "Like he didn't expect me to need something."
            pause 0.6

    pause 0.6

    thought "He won't."
    pause 0.3
    thought "I know he won't."
    pause 0.4
    thought "I know exactly what happens next."
    pause 0.5
    thought "And I still can't stop it."
    pause 1.2

    show yuichiroquiet at right_char
    with dissolve

    pause 0.4

    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "...So this is where you've been disappearing to."

    hide yuichirotalking
    show yuichiroquiet at right_char

    hide muiquiet
    show muitalking at left_char

    mui "...You followed me?"

    hide muitalking
    show muiquiet at left_char

    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "You're not subtle."
    pause 0.3
    yuichiro "You leave at the same time every day."
    pause 0.3
    yuichiro "...And come back oddly calm."
    pause 0.3
    yuichiro "Talking to someone?"

    hide yuichirotalking
    show yuichiroquiet at right_char

    hide muiquiet
    show muitalking at left_char

    mui "...I was just—"

    hide muitalking
    show muiquiet at left_char

    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "...Or staring again?"
    pause 0.3
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
    pause 0.4
    yuichiro "...You gave them that look."

    hide yuichirotalking
    show yuichiroquiet at right_char

    hide muiquiet
    show muitalking at left_char

    mui "...What look?"

    hide muitalking
    show muiquiet at left_char

    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "Like you're trying to memorize them before they're gone."

    hide yuichirotalking
    show yuichiroquiet at right_char

    mui "..."
    pause 0.8

    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "...You like them?"

    hide yuichirotalking
    show yuichiroquiet at right_char

    hide muiquiet
    show muitalking at left_char

    mui "...I don't think that's it."

    hide muitalking
    show muiquiet at left_char

    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "So you {i}do{/i} think about it."

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

    stop music fadeout 3.0
    play sound "wind_hollow.wav" fadein 1.5

    thought "...Something changed."
    pause 0.4
    thought "The air."
    pause 0.3
    thought "It gets heavier before they come."
    pause 0.5
    thought "I know that."
    pause 0.4
    thought "I've always known that."
    pause 0.8

    scene bg forest_night at bg_fit
    with slow_dissolve

    thought "This part..."
    pause 0.5
    thought "...I don't want to remember this part."
    pause 0.8

    play sound "distant_scream.wav"
    pause 0.6

    hide yuichirotalking
    show yuichiroquiet at right_char

    mui "...?"

    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "Stay here."
    pause 0.3
    yuichiro "Don't move."

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

    scene black
    with hard_cut

    play sound "fire_crackle.wav" fadein 0.8

    thought "Fire."
    pause 0.4
    thought "I know this smell."
    pause 0.4
    thought "Not from training."
    pause 0.4
    thought "From somewhere else."
    pause 0.5
    thought "..."
    pause 0.3
    thought "Don't."
    pause 0.8

    show muiquiet at left_char
    with dissolve

    hide muiquiet
    show muitalking at left_char

    mui "...It smells strange."

    hide muitalking
    show muiquiet at left_char

    show yuichiroquiet at right_char
    with dissolve

    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "...Don't look."

    hide yuichirotalking
    show yuichiroquiet at right_char

    hide muiquiet
    show muitalking at left_char

    mui "...Why?"

    hide muitalking
    show muiquiet at left_char

    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "...Just don't."

    hide yuichirotalking
    show yuichiroquiet at right_char

    thought "...But he does."
    pause 0.5

    play sound "heartbeat.wav"

    thought "Red."
    pause 0.4
    thought "That's where it comes from."
    pause 0.5

    scene black
    with flash_white

    thought "—a kitchen—"
    pause 0.2
    thought "—something burning—"
    pause 0.2
    thought "—her mother's voice, sharp—"
    pause 0.2
    thought "—her own hands—"
    pause 0.3
    thought "—something wrong with her hands—"
    pause 0.4

    scene black
    with hard_cut

    thought "No."
    pause 0.4
    thought "Not that."
    pause 0.5
    thought "Not yet."
    pause 1.0

    show muiquiet at left_char
    with dissolve

    show yuichiroquiet at right_char
    with dissolve

    mui "..."
    pause 0.4
    mui "...They're not moving."
    pause 0.5

    hide yuichiroquiet
    show yuichirotalking at right_char

    yuichiro "...I said don't look."
    pause 0.4

    hide muiquiet
    show muitalking at left_char

    mui "...Why aren't they moving?"

    hide muitalking
    show muiquiet at left_char

    hide yuichirotalking
    show yuichiroquiet at right_char

    yuichiro "Because they're—"

    stop sound
    with flash_white

    scene black
    with memory_fade

    thought "...After that..."
    pause 0.5
    thought "...things don't stay in order."
    pause 0.5
    thought "There was something else."
    pause 0.4
    thought "Something wrong."
    pause 0.5
    thought "Something that came {i}after{/i} the fire."
    pause 0.6
    thought "Something with teeth."
    pause 1.2

    scene bg forest_night at bg_fit
    with slow_dissolve

    play sound "low_growl.wav" fadein 1.5

    thought "It wasn't just an attack."
    pause 0.4
    thought "...Something was still there."
    pause 0.8

    show muiquiet at center_char
    with dissolve

    mui "..."
    pause 0.4
    mui "...You told me to run."
    pause 0.4
    mui "...I didn't."
    pause 0.4
    mui "...So now what?"
    pause 0.6

    menu:
        "...I don't know. I never do.":
            yn "...I don't know."
            pause 0.3
            yn "I never do."
            pause 0.5
            hide muiquiet
            show muitalking at center_char
            mui "..."
            pause 0.4
            mui "...That's honest."
            hide muitalking
            show muiquiet at center_char
            thought "He doesn't say it like a compliment."
            pause 0.3
            thought "He says it like a fact."
            pause 0.3
            thought "Like honesty is just a thing that exists."
            pause 0.3
            thought "Not something to be rewarded."
            pause 0.6

        "...We survive. Like we always do.":
            yn "...We survive."
            pause 0.3
            yn "Like we always do."
            pause 0.5
            hide muiquiet
            show muitalking at center_char
            mui "..."
            pause 0.4
            mui "...You say that like it's simple."
            hide muitalking
            show muiquiet at center_char
            thought "It used to be."
            pause 0.3
            thought "Before I knew how it ended."
            pause 0.3
            thought "Before I knew what surviving cost."
            pause 0.6

        "...If something feels wrong — run.":
            yn "...If something feels wrong..."
            pause 0.4
            yn "...run."
            pause 0.5
            hide muiquiet
            show muitalking at center_char
            mui "...Too late."
            hide muitalking
            thought "That's when it starts."
            pause 0.4
            thought "Not the memory."
            pause 0.3
            thought "The forgetting."
            pause 0.5
            thought "His."
            pause 0.3
            thought "And mine."
            pause 0.6

    pause 0.6

    thought "That's when it starts."
    pause 0.4
    thought "Not the memory."
    pause 0.3
    thought "The forgetting."
    pause 0.5
    thought "His."
    pause 0.3
    thought "And mine."
    pause 1.2

    scene black
    with Fade(1.5, 0.5, 2.0)

    jump mission_scene
