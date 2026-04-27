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

    thought "There was a city. Big. Loud."
    thought "The kind that hums at 3am and never actually goes dark."
    thought "I didn't have a room there. Not really."
    thought "I had a bed. In a building with a lot of other beds."
    thought "..."
    thought "An orphanage. That's the word."
    thought "I always hated that word."
    pause 0.6

    scene black
    with hard_cut

    thought "I had a quirk."
    thought "Everyone does. Where I'm from."
    thought "Mine wasn't dangerous. It wasn't impressive either."
    thought "It was just... mine."
    thought "The only thing that was."
    pause 0.6

    scene black
    with flash_white

    thought "I left when I was old enough to leave."
    thought "No one stopped me."
    thought "That's the thing about growing up in a place like that."
    thought "You learn early that no one is going to come looking."
    thought "So you stop expecting it."
    pause 0.6

    scene black
    with hard_cut

    thought "I don't know what I was looking for."
    thought "I don't think I was looking for anything."
    thought "I was just... moving."
    thought "The way you move when staying still feels worse."
    pause 0.6

    scene bg river_night at bg_fit
    with water_cut

    play sound "river_flow.wav" fadein 2.0
    pause 0.6

    thought "I found the river by accident."
    thought "Or maybe not. I don't know."
    thought "It was late. The sky was that color it gets right before it gives up on being dark."
    pause 0.5

    thought "I sat at the edge for a while."
    thought "Not thinking about anything in particular."
    thought "Just... sitting."
    pause 0.5

    thought "And then I was in it."
    thought "I don't remember deciding."
    thought "I don't remember falling."
    thought "I just remember the cold."
    pause 0.6

    thought "The water was black."
    thought "And then it was white."
    thought "And then—"
    pause 0.4

    menu:
        "...Come back up.":
            thought "I come back up. I always come back up."
            thought "That's the thing about me."
            thought "I keep surfacing, even when I don't mean to."
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

    thought "Because it wasn't real. Where I came from."
    thought "It was a story. Something people read."
    thought "..."
    thought "I read every chapter."
    thought "Every death, every name."
    pause 0.6

    thought "And then I fell into the river."
    thought "And I woke up inside it."
    pause 0.6

    thought "..."
    thought "Muichiro."
    thought "In the story... he was supposed to die."
    pause 0.6

    thought "He didn't. Because I was there."
    thought "Because I knew. And I couldn't let it happen."
    pause 0.5

    thought "I don't know if that was right."
    thought "I don't know if I had the right."
    thought "To change someone's story just because I knew how it ended."
    pause 0.6

    thought "But I did it anyway."
    thought "And now we're both here."
    thought "In a world that was also fiction. Once."
    thought "And I don't know what I've changed here just by existing."
    pause 0.6

    thought "..."
    thought "I'm so tired of knowing things."
    thought "And not knowing what to do with them."
    pause 0.8

    scene black
    with Fade(1.2, 0.5, 1.8)

    jump anchor_scene
