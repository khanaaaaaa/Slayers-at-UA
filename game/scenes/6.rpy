label memory_scene:

    scene black
    with dream_fade

    play sound "heartbeat.wav" fadein 2.0
    pause 0.8

    thought "Okay."
    thought "I'll remember."
    thought "I don't know where to start."
    pause 0.6

    scene black
    with flash_white

    thought "There was a city. big. loud."
    thought "The kind that hums at 3am and never actually goes dark."
    thought "I lived there. I had a room. I had a window."
    thought "I had a name that wasn't [player_name]."
    thought "..."
    thought "I can't remember it. I've been trying for a while now."
    pause 0.6

    scene black
    with hard_cut

    thought "I had a quirk."
    thought "Everyone does. Where i'm from."
    thought "Mine was the kind people don't talk about at dinner."
    thought "The kind that gets you a separate room at the training facility."
    thought "..."
    thought "Training facility. That's a word i know from before."
    thought "From the other world. The one that was real."
    thought "..."
    thought "They're both real. That's the problem."
    pause 0.6

    scene black
    with flash_white

    play sound "fire_crackle.wav" fadein 0.5

    thought "There was an argument."
    thought "I don't remember what it was about. I never do."
    thought "I remember the kitchen. The overhead light. The way it buzzed."
    thought "My mother's hands on the counter."
    thought "And then—"
    thought "..."
    thought "And then my hands. Shaking. And then not shaking."
    thought "And then—"
    pause 0.4

    stop sound
    with flash_white

    thought "..."
    thought "I don't want to say it."
    thought "I've never said it. not out loud."
    pause 0.6

    menu:
        "...say it.":
            thought "I lost control of my quirk. In the kitchen, with my parents."
            thought "..."
            thought "I ran before I could find out what happened."
            thought "That's the part I'm least proud of."
            thought "The running."

        "...Not yet.":
            thought "Not yet. I'll get there."
            thought "Just. Not yet."

        "...I already know. I've always known.":
            thought "I already know, I've always known."
            thought "There's no surprise left, just the same fact sitting there every time."

    pause 0.6

    scene bg river_night at bg_fit
    with water_cut

    play sound "river_flow.wav" fadein 2.0
    pause 0.6

    thought "I ran for a long time."
    thought "Until there was water. a river."
    thought "Cold."
    pause 0.4

    thought "I stood at the edge."
    thought "I don't know how long."
    thought "Long enough that the sky changed color."
    pause 0.4

    thought "Did i jump, or did i fall?"
    thought "..."
    thought "I've been asking myself that for a while."
    thought "I don't think the answer matters."
    thought "What matters is that I went in, and I didn't come back out."
    thought "Atleast, not the same way."
    pause 0.6

    thought "The water was black."
    thought "And then it was white."
    thought "And then—"
    pause 0.4

    menu:
        "...Come back up.":
            thought "I come back up. I always come back up."
            thought "That's the thing about me."
            thought "I keep surfacing, even when I don't want to."
            jump memory_surface

        "...Stay.":
            jump ending_fade_out


label memory_surface:

    stop sound fadeout 2.0

    scene black
    with Fade(1.0, 0.5, 1.5)

    thought "..."
    thought "Oh."
    thought "Oh no."
    pause 0.6

    thought "I know why I know everything."
    thought "I know why I knew his name."
    thought "His brother, the demons, all of it."
    pause 0.5

    thought "Because it wasn't real... Where i came from."
    thought "It was a story... something people read..."
    thought "..."
    thought "I read every chapter."
    thought "Every death, every name."
    pause 0.6

    thought "And then i fell into the river."
    thought "And i woke up inside it."
    pause 0.6

    thought "..."
    thought "Muichiro."
    thought "In the story... he was supposed to die."
    pause 0.6

    thought "He didn't... because I was there."
    thought "Because I knew... and I couldn't let it happen."
    pause 0.5

    thought "I don't know if that was right."
    thought "I don't know if i had the right."
    thought "To change someone's story just because i knew how it ended..."
    pause 0.6

    thought "But i did it anyway."
    thought "And now we're both here."
    thought "In a world that was also fiction... once."
    thought "And i don't know what i've changed here... just by existing."
    pause 0.6

    thought "..."
    thought "I'm so tired of knowing things."
    thought "And not knowing what to do with them."
    pause 0.8

    scene black
    with Fade(1.2, 0.5, 1.8)

    jump anchor_scene
