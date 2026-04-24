label mission_scene:
    scene bg forest_night at bg_fit
    play sound "wind.wav"
    with fade

    pause 0.5

    thought "The forest remembers..."
    thought "It always does."
    pause
    thought "Even when people forget."
    thought "Even wen promises turn into something unrecognizeable."
    pause 1.0
    play sound "leaves_rustle.wav"
    thought "We met here once."
    pause 0.1
    thought "Back when the nights felt shorter."
    thought "Back when everything didn't feel so heavy."
    pause 0.1
    thought "Back when he still laughed."
    pause 1.2
    yn "Moon Breathing..."
    pause 0.3
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

    thought "Too clean."
    thought "My body moved before I could even think."
    thought "...Just like before."

    pause 1.0

    show ynquiet at right_char
    show demon2talking at left_char

    demon2 "Ara..."
    demon2 "What an unpleasent stillness."
    demon2 "The kind that follows someone who has too much blood on their hands."
    pause 0.1
    demon2 "I can sense it clearly now..."
    pause 0.4
    demon2 "I can sense it clearly now..."
    pause 0.4
    demon2 "A Hashira."
    pause 0.4
    demon2 "...and something distorted standing beside him."
    pause 0.5
    demon2 "Your scent is wrong."
    pause 0.2
    demon2 "Not old... not new..."
    pause 0.6
    demon2 "...as if you slipped out of time and forgot how to return."
    pause 0.5
    thought "...Stop"
    pause 0.6
    thought "Don't listen."
    pause 0.6
    demon2 "...Ah."
    demon2 "That reaction..."
    demon2 "...regret?"
    pause 1.0
    play sound "mist.wav"
    show muichiro at right_char
    mui "Mist Breathing..."
    pause 0.8
    mui "...Seventh Form."
    pause 0.6
    mui "...Obscuring Clouds."
    show slash_effect at left_char
    hide slash_effect
    hide demon2
    pause 0.8
    show mui at center:
        zoom 1.1
    pause 1.2
    show slash effect at left_char
    with hpunch
    hide slash_effect
    hide demon2
    pause 0.5
    show mui at center:
        zoom 1.1
    pause 1.0
    mui "You're still alive."
    pause 0.8
    thought "Not surprised."
    mui "You got slower."
    pause 0.5
    mui "Thought you would die eventually."
    pause 0.8
    mui "You were always slower to adapt."
    pause 0.8
    mui "...What was your name again?"
    pause 1.0
    thought "...Right."
    thought "This is who he is now."
    yn "...It's [player_name]"
    pause 0.5
    mui "Right."
    mui "You used to dislike it when I forgot."
    thought "Used to."
    yn "Well you never forgot before..."
    mui "..."
    thought "No answer as always."
    yn "You used to call me something."
    pause 0.5
    yn "...Sparrow"
    mui "...Why would I call anyone that?"
    pause 1.0
    thought "Of course."
    thought "To him now-"
    thought "It probably is."
    show demon2 at center:
        alpha 0.0
        linear 0.2 alpha 1.0
    demon2 "How cruel."
    demon2 "To stand before someone who once held your entrie world."
    pause 0.2
    demon2 "...and be nothing to them."
    pause 0.2
    demon2 "Humans cling to bonds as if they are eternal."
    pause 0.5
    demon2 "but memory is the most fragile flesh."
    pause 0.5 
    demon2 "It rots."
    pause 0.6
    demon2 "And eventually..."
    pause 0.6
    demon2 "...it forgets why it ever held on."
    pause 0.2
    mui "Shut up."
    pause 0.3
    thought "He's angry."
    pause 0.3
    thought "That's new..."
    pause 0.5
    demon2 "Ah..."
    demon2 "So even mist can bleed..."
    pause 0.3
    demon2 "Tell me, Hashira..."
    demon2 "...how long will you run away?"
    pause 0.1
    show back_vortex:
        zoom 0.5
        linear 0.3 zoom 1.3
    with vpunch
    demon2 "Fall."
    pause 0.5
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
    pause 0.3
    thought "For a moment-"
    pause 0.3
    thought "...his eyes changed."
    pause 0.3
    thought "Like we returned..."
    pause 0.3
    thought "...to that forest."
    pause 0.3
    thought "And I let it slip away again."
    scene white with Fade(0.2, 0.0, 0.5)
    pause 1.0
    jump mha_intro