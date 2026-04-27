label prologue_start:

    scene black
    with memory_fade

    play sound "wind_soft.wav" fadein 2.0

    thought "There is someone I know everything about."
    thought "The way he tilts his head when he's deciding whether to care."
    thought "But he doesn't remember me."
    thought "..."
    thought "Which is kinda insulting."
    pause 1.0

    scene bg forest_sunset at bg_fit
    with slow_dissolve

    play music "memory_theme.mp3" fadein 2.5

    with dissolve

    thought "He'll come from the left. He always does."
    pause 0.4

    show muiquiet at center_char
    with dissolve

    thought "...See."
    pause 0.6

    hide muiquiet
    show muitalking at center_char
    mui "You came again."
    hide muitalking
    show muiquiet at center_char


    hide muiquiet
    show muitalking at center_char
    mui "...Don't people usually say their names?"
    hide muitalking
    show muiquiet at center_char

    yn "Usually."
    yn "Do you want to know mine?"

    hide muiquiet
    show muitalking at center_char
    mui "I don't know."
    mui "...You come here a lot."
    mui "It feels strange not calling you anything."
    hide muitalking
    show muiquiet at center_char

    yn "...Then what would you call me?"

    hide muiquiet
    show muitalking at center_char
    mui "...I haven't decided yet. Something that fits."
    hide muitalking
    show muiquiet at center_char

    yn "That sounds like a lot of pressure."

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

    yn "Then maybe you should hurry."

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

    yn "Why do you always pretend not to look?"

    hide muiquiet
    show muitalking at center_char
    mui "...You're not from here."
    hide muitalking
    show muiquiet at center_char

    yn "No. But neither are you."

    hide muiquiet
    show muitalking at center_char
    mui "...What does that mean?"
    hide muitalking
    show muiquiet at center_char

    thought "It means—"
    pause 0.2

    scene black
    with flash_white

    thought "—Bright lights—"
    thought "—A building, glass and steel—"
    thought "—Someone calling my name—"
    thought "—Not [player_name]—"
    thought "—Something else—"
    pause 0.3

    scene bg forest_sunset at bg_fit
    with soft_dissolve

    show muiquiet at center_char

    thought "What was that."
    thought "I don't know. I never know."
    pause 0.6

    yn "It means... you shouldn't be this calm."
    yn "Not with demons this close."

    hide muiquiet
    show muitalking at center_char
    mui "...Demons? You're the second person to say that."
    hide muitalking
    show muiquiet at center_char

    yn "Second?"

    hide muiquiet
    show muitalking at center_char
    mui "...My brother. He says things like that."
    hide muitalking
    show muiquiet at center_char

    thought "His brother."
    thought "I know that without knowing how."
    thought "Protective. Harsh. Loves him more than he can say."
    thought "...Why do I know that."
    pause 0.6

    yn "Then you should listen to him."

    hide muiquiet
    show muitalking at center_char
    mui "...I wanted to hear it from someone else."
    hide muitalking
    show muiquiet at center_char

    yn "You're strange."

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
            yn "That was easier than I expected."
            thought "It always is."
            thought "...Always?"

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
            thought "He says it like he expected it."
            thought "Like he's been told no before. By me."
            thought "He probably has."

    pause 0.5

    yn "Then listen carefully."
    yn "If something feels wrong..."
    yn "...run."

    hide muiquiet
    show muitalking at center_char
    mui "...Do I need to?"
    hide muitalking
    show muiquiet at center_char

    menu:
        "Yes. Promise me.":
            yn "Yes. Promise me."
            hide muiquiet
            show muitalking at center_char
            mui "...Okay."
            hide muitalking
            show muiquiet at center_char
            thought "He says it like it's nothing."
            thought "He doesn't know what it costs me to ask."

        "Yes. Even if you think you don't.":
            yn "Yes. Even if you think you don't."
            hide muiquiet
            show muitalking at center_char
            mui "...That's a strange way to say it."
            hide muitalking
            show muiquiet at center_char
            thought "I know. Because I know he won't."
            thought "And I'm asking anyway."

        "Just... please.":
            yn "Just... please."
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

    yuichiro "...So this is where you've been disappearing to."

    hide muiquiet
    show muitalking at center_char
    mui "...You followed me?"
    hide muitalking
    show muiquiet at center_char

    yuichiro "You're not subtle."
    yuichiro "You leave at the same time every day."
    yuichiro "...And come back oddly calm. Talking to someone?"

    hide muiquiet
    show muitalking at center_char
    mui "...I was just—"
    hide muitalking
    show muiquiet at center_char

    yuichiro "...Or staring again? Who's the ghost?"

    hide muiquiet
    show muitalking at center_char
    mui "...They're not a ghost."
    hide muitalking
    show muiquiet at center_char

    yuichiro "Mm. ...You gave them that look."

    hide muiquiet
    show muitalking at center_char
    mui "...What look?"
    hide muitalking
    show muiquiet at center_char

    yuichiro "Like you're trying to memorize them before they're gone."

    mui "..."
    pause 0.6

    yuichiro "...You like them?"

    hide muiquiet
    show muitalking at center_char
    mui "...I don't think that's it."
    hide muitalking
    show muiquiet at center_char

    yuichiro "So you {i}do{/i} think about it."

    hide muiquiet
    show muitalking at center_char
    mui "...You're annoying."
    hide muitalking
    show muiquiet at center_char

    yuichiro "...You're obvious."

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

    show muiquiet at center_char

    mui "...?"

    yuichiro "Stay here. Don't move."

    hide muiquiet
    show muitalking at center_char
    mui "...What was that?"
    hide muitalking
    show muiquiet at center_char

    yuichiro "...Inside."

    scene black
    with Fade(2.5, 0.5, 2.0)

    play sound "fire_crackle.wav" fadein 2.0

    thought "It's dark."
    pause 0.8
    thought "I can't see anything."
    pause 0.6
    thought "...But I can smell it."
    pause 1.0
    thought "Something burning. Something else underneath that."
    pause 0.8
    thought "Something that doesn't belong in a house."
    pause 1.2
    thought "Yuichiro is ahead of me. I can hear him stop."
    pause 0.8
    thought "He doesn't say anything."
    pause 0.6
    thought "That's worse than if he had."
    pause 1.0

    play sound "heartbeat.wav"
    pause 0.5

    thought "My eyes adjust."
    pause 0.8
    thought "I wish they hadn't."
    pause 1.2
    thought "...Something on the floor."
    pause 0.6
    thought "Two somethings."
    pause 0.6
    thought "They're not moving."
    pause 1.0
    thought "They're not moving."
    pause 0.4
    thought "Why aren't they—"
    pause 1.5
    thought "..."
    pause 1.0


    yuichiro "...Don't look."
    mui "...Why aren't they moving?"
    pause 0.6

    yuichiro "..."
    pause 0.8
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

    thought "It wasn't just an attack. ...Something was still there."
    pause 0.6

    mui "..."
    mui "...You told me to run."
    mui "...I didn't."
    mui "...So now what?"
    
    menu:
        "...I don't know. I never do.":
            yn "...I don't know. I never do."
            mui "...That's honest."
            thought "He doesn't say it like a compliment."
            thought "He says it like a fact."

        "...We survive. Like we always do.":
            yn "...We survive. Like we always do."
            mui "...You say that like it's simple."
            thought "It used to be."
            thought "Before I knew how it ended."
            thought "...How do I know how it ends."

        "...If something feels wrong — run.":
            yn "...If something feels wrong..."
            yn "...run."
            mui "...Too late."
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
