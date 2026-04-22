label mission_scene:
    scene bg forest_night at bg_fit
    play sound "wind.wav"
    with fade

    pause 0.5

    thought "The forest remembers..."
    thought "Even if you don't."
    pause
    thought "We once trained here."
    thought "And he still laughed."
    pause 1.0
    play sound "leaves_rustle.wav"
    yn "Moon Breathing..."
    yn "...Third Form"
    yn "...Lunar Rings"
    show demon1 at center:
        zoom 0.8
        ease 0.2 zoom 1.0
    pause 0.2

    show slash_effect at center
    with vpunch

    hide slash_effect
    hide demon1

    silence 0.5

    thought "Too clean."
    thought "My body moved before I could even think."
    thought "...Just like before."

    pause 1.0

    show ynquiet at right_char
    show demon2talking at left_char

    demon2 "Ara..."
    demon2 "I can sense a Hashira."
    demon2 "And someone else."
    pause 0.1
    demon2 "And you..."
    pause 0.2
    demon2 "Your scent tells me that you don't belong to the present."
    pause 0.5
    thought "...Stop"
    pause
    demon2 "...Anger?"
    demon2 "...No."
    demon2 "...Regret."
    pause 0.5
    play sound "mist.wav"
    show muichiro at right_char
    mui "Mist Breathing..."
    pause
    mui "...Sea of Clouds and Haze."
    show slash effect at lwft_char
    with hpunch
    hide slash_effect
    hide demon2
    pause 0.5
    show mui at center:
        zoom 1.1
    pause 1.0
    mui "You're still alive..."
    thought "Not surprised."
    mui "You got slower."
    pause
    mui "...What was your name again?"
    pause 1.0
    thought "...Of course."
    yn "...It's [player_name]"
    pause 0.5
    mui "Right."
    mui "You used to dislike it when I forgot."
    thought "Used to."
    yn "Well you never forgot before..."
    mui "..."
    thought "No answer as always."
    yn "You used to call me something."
    pause
    yn "...Sparrow"
    mui "...Why would I call anyone something that stupid."
    show demon2 at center:
        alpha 0.0
        linear 0.2 alpha 1.0
    demon2 "How cruel."
    demon2 "To stand before someone who is everything to you..."
    demon2 "...and be nothing to them."
    demon2 "Humans believe bonds are permanent."
    demon2 "but memory is the most fragile flesh."
    mui "Shut up."
    pause 0.3
    thought "He's angry."
    thought "He never used to be..."
    pause 0.5
    demon2 "Ah..."
    demon2 "So even mist can bleed..."
    demon2 "Hashira boy, I was just joking around."
    demon2 "Tell me, Hashira..."
    demon2 "...will you be stubborn forever?"
    pause 0.5
    show back_vortex:
        zoom 0.5
        linear 0.3 zoom 1.3
    with vpunch
    demon2 "Fall."
    demon2 "...together."
    show mui at fall_into_hole
    with hpunch
    yn "Muichiro-!"
    pause 0.3
    mui "...Don't."
    pause 0.2
    mui "...call me like you used to."
    pause 0.5
    thought "...Too late."
    thought "For a moment-"
    thought "...his eyes changed."
    thought "Like we returned..."
    thought "...to that forest."
    thought "And I let it slip away again."
    scene white with Fade(0.2, 0.0, 0.5)
    pause 1.0
    jump mha_intro


