label memory_scene:

    scene black
    with dream_fade

    play sound "heartbeat.wav" fadein 2.0
    pause 0.8

    thought "okay."
    thought "i'll remember."
    thought "i don't know where to start."
    pause 0.6

    scene black
    with flash_white

    thought "there was a city. big. loud."
    thought "the kind that hums at 3am and never actually goes dark."
    thought "i lived there. i had a room. i had a window."
    thought "i had a name that wasn't [player_name]."
    thought "..."
    thought "i can't remember it. i've been trying for a while now."
    pause 0.6

    scene black
    with hard_cut

    thought "i had a quirk."
    thought "everyone does. where i'm from."
    thought "mine was the kind people don't talk about at dinner."
    thought "the kind that gets you a separate room at the training facility."
    thought "..."
    thought "training facility. that's a word i know from before."
    thought "from the other world. the one that was real."
    thought "..."
    thought "they're both real. that's the problem."
    pause 0.6

    scene black
    with flash_white

    play sound "fire_crackle.wav" fadein 0.5

    thought "there was an argument."
    thought "i don't remember what it was about. i never do."
    thought "i remember the kitchen. the overhead light. the way it buzzed."
    thought "my mother's hands on the counter."
    thought "and then—"
    thought "..."
    thought "and then my hands. shaking. and then not shaking."
    thought "and then—"
    pause 0.4

    stop sound
    with flash_white

    thought "..."
    thought "i don't want to say it."
    thought "i've never said it. not out loud."
    pause 0.6

    menu:
        "...say it.":
            thought "i lost control. of my quirk. in the kitchen. with my parents."
            thought "..."
            thought "i ran before i could find out what happened."
            thought "that's the part i'm least proud of."
            thought "not the accident. the running."

        "...not yet.":
            thought "not yet. i'll get there."
            thought "just. not yet."

        "...i already know. i've always known.":
            thought "i already know. i've always known."
            thought "that's the worst part."
            thought "there's no surprise left. just the same fact. sitting there. every time."

    pause 0.6

    scene bg river_night at bg_fit
    with water_cut

    play sound "river_flow.wav" fadein 2.0
    pause 0.6

    thought "i ran. for a long time."
    thought "until there was water. a river."
    thought "wide. cold. the kind that doesn't care about you."
    pause 0.4

    thought "i stood at the edge."
    thought "i don't know how long."
    thought "long enough that my feet went numb."
    thought "long enough that the sky changed color."
    pause 0.4

    thought "did i jump. or did i fall."
    thought "..."
    thought "i've been asking myself that for a while."
    thought "i don't think the answer matters."
    thought "what matters is that i went in. and i didn't come back out."
    thought "not the same way."
    pause 0.6

    thought "the water was black."
    thought "and then it was white."
    thought "and then—"
    pause 0.4

    menu:
        "...come back up.":
            thought "i come back up. i always come back up."
            thought "that's the thing about me."
            thought "i keep surfacing. even when i don't want to."
            jump memory_surface

        "...stay.":
            jump ending_fade_out


label memory_surface:

    stop sound fadeout 2.0

    scene black
    with Fade(1.0, 0.5, 1.5)

    thought "..."
    thought "oh."
    thought "oh no."
    pause 0.6

    thought "i know why i know everything."
    thought "i know why i knew his name. his breathing form."
    thought "his brother. the demons. all of it."
    pause 0.5

    thought "because it wasn't real. where i came from."
    thought "it was a story. something people read. something people watched."
    thought "..."
    thought "i watched it. i read every chapter."
    thought "every death. every name."
    pause 0.6

    thought "and then i fell into the river."
    thought "and i woke up inside it."
    pause 0.6

    thought "..."
    thought "muichiro."
    thought "in the story — he was supposed to die."
    pause 0.6

    thought "he didn't. because i was there."
    thought "because i knew. and i couldn't let it happen."
    pause 0.5

    thought "i don't know if that was right."
    thought "i don't know if i had the right."
    thought "to change someone's story just because i knew how it ended."
    pause 0.6

    thought "but i did it anyway."
    thought "and now we're both here."
    thought "in a world that was also fiction. once."
    thought "and i don't know what i've changed here. just by existing."
    pause 0.6

    thought "..."
    thought "i'm so tired of knowing things."
    thought "and not knowing what to do with them."
    pause 0.8

    scene black
    with Fade(1.2, 0.5, 1.8)

    jump anchor_scene
