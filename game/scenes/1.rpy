label prologue_start:

    scene black
    with memory_fade

    play sound "wind_soft.wav" fadein 2.0

    thought "There is someone I know everything about."
    thought "His name. His breathing form."
    thought "The way he tilts his head when he's deciding whether to care."
    thought "But he doesn't remember me."
    thought "..."
    thought "Which is fine. I think."
    thought "I don't remember much either."
    pause 1.0

    scene bg forest_sunset at bg_fit
    with slow_dissolve

    play music "memory_theme.mp3" fadein 2.5

    show youngynquiet at center_char
    with dissolve

    thought "He'll come from the left. He always does."
    pause 0.4

    hide youngynquiet
    show muiquiet at center_char
    with dissolve

    thought "...See."
    pause 0.6

    hide muiquiet
    show muitalking at center_char
    mui "You came again."
    hide muitalking
    show muiquiet at center_char

    thought "Don't say his name. You're not supposed to know it yet."
    pause 0.6

    hide muiquiet
    show muitalking at center_char
    mui "...Don't people usually say their names?"
    hide muitalking
    show muiquiet at center_char

    hide youngynquiet
    show youngyntalking at center_char
    "Usually."
    "Do you want to know mine?"
    hide youngyntalking
    show youngynquiet at center_char

    hide muiquiet
    show muitalking at center_char
    mui "I don't know."
    mui "...You come here a lot."
    mui "It feels strange not calling you anything."
    hide muitalking
    show muiquiet at center_char

    hide youngynquiet
    show youngyntalking at center_char
    "...Then what would you call me?"
    hide youngyntalking
    show youngynquiet at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...I haven't decided yet. Something that fits."
    hide muitalking
    show muiquiet at center_char

    hide youngynquiet
    show youngyntalking at center_char
    "That sounds like a lot of pressure."
    hide youngyntalking
    show youngynquiet at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...You'll probably disappear before I figure it out anyway."
    hide muitalking
    show muiquiet at center_char

    thought "He says that every time."
    thought "..."
    thought "Wait. Every time?"
    thought "How many times have we done this?"
    pause 0.8

    hide youngynquiet
    show youngyntalking at center_char
    "Then maybe you should hurry."
    hide youngyntalking
    show youngynquiet at center_char

    mui "..."
    pause 0.5

    hide muiquiet
    show muitalking at center_char
    mui "...Then tell me."
    hide muitalking
    show muiquiet at center_char

    $ player_name = renpy.input("What is your name?", length=20)
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Player"

    hide muiquiet
    show muitalking at center_char
    mui "...[player_name]."
    mui "I'll remember it."
    hide muitalking
    show muiquiet at center_char

    thought "He won't. He never does."
    thought "But I keep telling him anyway."
    pause 0.8

    hide muiquiet
    show muitalking at center_char
    mui "...Why do you always stand in the same place?"
    hide muitalking
    show muiquiet at center_char

    hide youngynquiett
    show youngyntalkingg at center_char
    yn "Why do you always pretend not to look?"
    hide youngyntalkingg
    show youngynquiett at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...You're not from here."
    hide muitalking
    show muiquiet at center_char

    hide youngynquiett
    show youngyntalkingg at center_char
    yn "No. But neither are you."
    hide youngyntalkingg
    show youngynquiett at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...What does that mean?"
    hide muitalking
    show muiquiet at center_char

    thought "It means—"
    pause 0.2

    scene black
    with flash_white

    thought "—bright lights—"
    thought "—a building, glass and steel—"
    thought "—someone calling her name—"
    thought "—not [player_name]—"
    thought "—something else—"
    pause 0.3

    scene bg forest_sunset at bg_fit
    with soft_dissolve

    show muiquiet at center_char
    show youngynquiet at center_char

    thought "What was that. Instinct. Probably."
    pause 0.6

    hide youngynquiett
    show youngyntalking at center_char
    yn "It means... you shouldn't be this calm."
    yn "Not with demons this close."
    hide youngyntalking
    show youngynquiet at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...Demons? You're the second person to say that."
    hide muitalking
    show muiquiet at center_char

    hide youngynquiett
    show youngyntalkingg at center_char
    yn "Second?"
    hide youngyntalkingg
    show youngynquiett at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...My brother. He says things like that."
    hide muitalking
    show muiquiet at center_char

    thought "Yuichiro. Protective. Harsh. Loves Muichiro more than he can say."
    thought "...How do I know that."
    pause 0.6

    hide youngynquiett
    show youngyntalkingg at center_char
    yn "Then you should listen to him."
    hide youngyntalkingg
    show youngynquiett at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...I wanted to hear it from someone else."
    hide muitalking
    show muiquiet at center_char

    hide youngynquiett
    show youngyntalkingg at center_char
    yn "You're strange."
    hide youngyntalkingg
    show youngynquiett at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...I get that a lot."
    pause 0.4
    mui "...Should I trust you?"
    hide muitalking
    show muiquiet at center_char

    menu:
        "...Yes. I think you should.":
            hide muiquiet
            show muitalking at center_char
            mui "...Okay."
            hide muitalking
            show muiquiet at center_char
            hide youngynquiett
            show youngyntalkingg at center_char
            yn "That was easier than I expected."
            hide youngyntalkingg
            show youngynquiett at center_char
            if route == "meta":
                thought "It always is. I've read this part."
                thought "He says okay. Then he forgets."
                thought "Every time."
            else:
                thought "It always is. ...Always?"

        "...I don't know yet. But I'm still here.":
            hide muiquiet
            show muitalking at center_char
            mui "...Yeah. That makes sense."
            hide muitalking
            show muiquiet at center_char
            if route == "loud":
                thought "I almost said something else."
                thought "Something embarrassing."
                thought "I didn't. Growth."
            else:
                thought "He's not offended. He never is."
                thought "I don't know if that's a good thing."

        "...No. But I'll stay anyway.":
            hide muiquiet
            show muitalking at center_char
            mui "...Right. ...I figured."
            hide muitalking
            show muiquiet at center_char
            if route == "silent":
                thought "He says it like he expected it."
                thought "Like he's been told no before. By me."
                thought "He probably has."
            else:
                thought "He says that like he expected it."
                thought "Like he's been told no before. By me."

    pause 0.5

    hide youngynquiet
    show youngyntalking at center_char
    yn "Then listen carefully."
    yn "If something feels wrong..."
    yn "...run."
    hide youngyntalkingg
    show youngynquiett at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...Do I need to?"
    hide muitalking
    show muiquiet at center_char

    hide youngynquiett
    show youngyntalkingg at center_char

    menu:
        "Yes. Promise me.":
            yn "Yes. Promise me."
            hide youngyntalkingg
            show youngynquiett at center_char
            hide muiquiet
            show muitalking at center_char
            mui "...Okay."
            hide muitalking
            show muiquiet at center_char
            thought "He says it like it's nothing."
            thought "He doesn't know what it costs me to ask."

        "Yes. Even if you think you don't.":
            yn "Yes. Even if you think you don't."
            hide youngyntalkingg
            show youngynquiett at center_char
            hide muiquiet
            show muitalking at center_char
            mui "...That's a strange way to say it."
            hide muitalking
            show muiquiet at center_char
            thought "I know. Because I know he won't."
            thought "And I'm asking anyway."

        "Just... please.":
            yn "Just... please."
            hide youngyntalkingg
            show youngynquiett at center_char
            hide muiquiet
            show muitalking at center_char
            mui "...Okay."
            hide muitalking
            show muiquiet at center_char
            thought "He looks at me differently when I say please."
            thought "Like he didn't expect me to need something."

    pause 0.5

    thought "He won't. I know exactly what happens next."
    thought "And I still can't stop it."
    pause 1.0

    show yuichiroquiet at center_char
    with dissolve

    hide yuichiroquiet
    show yuichirotalking at center_char
    yuichiro "...So this is where you've been disappearing to."
    hide yuichirotalking
    show yuichiroquiet at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...You followed me?"
    hide muitalking
    show muiquiet at center_char

    hide yuichiroquiet
    show yuichirotalking at center_char
    yuichiro "You're not subtle."
    yuichiro "You leave at the same time every day."
    yuichiro "...And come back oddly calm. Talking to someone?"
    hide yuichirotalking
    show yuichiroquiet at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...I was just—"
    hide muitalking
    show muiquiet at center_char

    hide yuichiroquiet
    show yuichirotalking at center_char
    yuichiro "...Or staring again? Who's the ghost?"
    hide yuichirotalking
    show yuichiroquiet at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...They're not a ghost."
    hide muitalking
    show muiquiet at center_char

    hide yuichiroquiet
    show yuichirotalking at center_char
    yuichiro "Mm. ...You gave them that look."
    hide yuichirotalking
    show yuichiroquiet at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...What look?"
    hide muitalking
    show muiquiet at center_char

    hide yuichiroquiet
    show yuichirotalking at center_char
    yuichiro "Like you're trying to memorize them before they're gone."
    hide yuichirotalking
    show yuichiroquiet at center_char

    mui "..."
    pause 0.6

    hide yuichiroquiet
    show yuichirotalking at center_char
    yuichiro "...You like them?"
    hide yuichirotalking
    show yuichiroquiet at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...I don't think that's it."
    hide muitalking
    show muiquiet at center_char

    hide yuichiroquiet
    show yuichirotalking at center_char
    yuichiro "So you {i}do{/i} think about it."
    hide yuichirotalking
    show yuichiroquiet at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...You're annoying."
    hide muitalking
    show muiquiet at center_char

    hide yuichiroquiet
    show yuichirotalking at center_char
    yuichiro "...You're obvious."
    hide yuichirotalking

    stop music fadeout 3.0
    play sound "wind_hollow.wav" fadein 1.5

    thought "...Something changed. The air."
    thought "It gets heavier before they come. I know that."
    pause 0.6

    scene bg forest_night at bg_fit
    with slow_dissolve

    thought "This part... I don't want to remember this part."
    pause 0.6

    play sound "distant_scream.wav"
    pause 0.5

    show yuichiroquiet at center_char

    mui "...?"

    hide yuichiroquiet
    show yuichirotalking at center_char
    yuichiro "Stay here. Don't move."
    hide yuichirotalking
    show yuichiroquiet at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...What was that?"
    hide muitalking
    show muiquiet at center_char

    hide yuichiroquiet
    show yuichirotalking at center_char
    yuichiro "...Inside."
    hide yuichirotalking

    scene black
    with hard_cut

    play sound "fire_crackle.wav" fadein 0.8

    thought "Fire. I know this smell."
    thought "Not from training. From somewhere else."
    thought "...Don't."
    pause 0.6

    show muiquiet at center_char
    with dissolve

    hide muiquiet
    show muitalking at center_char
    mui "...It smells strange."
    hide muitalking
    show muiquiet at center_char

    show yuichiroquiet at center_char
    with dissolve

    hide yuichiroquiet
    show yuichirotalking at center_char
    yuichiro "...Don't look."
    hide yuichirotalking
    show yuichiroquiet at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...Why?"
    hide muitalking
    show muiquiet at center_char

    hide yuichiroquiet
    show yuichirotalking at center_char
    yuichiro "...Just don't."
    hide yuichirotalking
    show yuichiroquiet at center_char

    thought "...But he does."
    pause 0.4

    play sound "heartbeat.wav"

    thought "Red. That's where it comes from."
    pause 0.4

    scene black
    with flash_white

    thought "—a kitchen—"
    thought "—something burning—"
    thought "—her mother's voice, sharp—"
    thought "—her own hands—"
    thought "—something wrong with her hands—"
    pause 0.3

    scene black
    with hard_cut

    thought "No. Not that. Not yet."
    pause 0.8

    show muiquiet at center_char
    with dissolve

    show yuichiroquiet at center_char
    with dissolve

    mui "..."
    mui "...They're not moving."
    pause 0.4

    hide yuichiroquiet
    show yuichirotalking at center_char
    yuichiro "...I said don't look."
    hide yuichirotalking
    show yuichiroquiet at center_char

    hide muiquiet
    show muitalking at center_char
    mui "...Why aren't they moving?"
    hide muitalking
    show muiquiet at center_char

    hide yuichiroquiet
    show yuichiroquiet at center_char
    yuichiro "Because they're—"

    stop sound
    with flash_white

    scene black
    with memory_fade

    thought "...After that... things don't stay in order."
    thought "There was something else. Something wrong."
    thought "Something that came {i}after{/i} the fire."
    thought "Something with teeth."
    pause 1.0

    scene bg forest_night at bg_fit
    with slow_dissolve

    play sound "low_growl.wav" fadein 1.5

    thought "It wasn't just an attack. ...Something was still there."
    pause 0.6

    show muiquiet at center_char
    with dissolve

    hide muiquiet
    show muitalking at center_char
    mui "..."
    mui "...You told me to run."
    mui "...I didn't."
    mui "...So now what?"
    hide muitalking
    show muiquiet at center_char

    menu:
        "...I don't know. I never do.":
            yn "...I don't know. I never do."
            hide muiquiet
            show muitalking at center_char
            mui "...That's honest."
            hide muitalking
            show muiquiet at center_char
            thought "He doesn't say it like a compliment."
            thought "He says it like a fact."

        "...We survive. Like we always do.":
            yn "...We survive. Like we always do."
            hide muiquiet
            show muitalking at center_char
            mui "...You say that like it's simple."
            hide muitalking
            show muiquiet at center_char
            thought "It used to be."
            thought "Before I knew how it ended."

        "...If something feels wrong — run.":
            yn "...If something feels wrong..."
            yn "...run."
            hide muiquiet
            show muitalking at center_char
            mui "...Too late."
            hide muitalking
            thought "That's when it starts."
            thought "Not the memory. The forgetting."
            thought "His. And mine."

    thought "That's when it starts."
    thought "Not the memory. The forgetting."
    thought "His. And mine."
    pause 1.0

    scene black
    with Fade(1.5, 0.5, 2.0)

    jump mission_scene
