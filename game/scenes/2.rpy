label mission_scene:

    scene bg forest_night at bg_fit
    with slow_dissolve

    play sound "wind.wav" fadein 2.0
    pause 0.8

    thought "The forest remembers..."
    pause 0.4
    thought "It always does."
    pause 0.5
    thought "Even when people forget."
    pause 0.5
    thought "Even when promises turn into something unrecognizable."
    pause 0.8

    play sound "leaves_rustle.wav" fadein 1.0

    thought "We met here once."
    pause 0.3
    thought "Back when the nights felt shorter."
    pause 0.3
    thought "Back when everything didn't feel so heavy."
    pause 0.4
    thought "Back when he still laughed."
    pause 1.2

    show youngynquiet at right_char
    with dissolve

    pause 0.5

    yn "Moon Breathing..."
    pause 0.4
    yn "...Third Form."
    pause 0.3
    yn "...Lunar Rings."

    with vpunch
    pause 0.4

    thought "Too clean."
    pause 0.3
    thought "My body moved before I could even think."
    pause 0.3
    thought "...Just like before."
    pause 0.8

    show muiquiet at left_char
    with dissolve

    pause 0.4

    demon2 "Ara..."
    pause 0.4
    demon2 "What an unpleasant stillness."
    pause 0.3
    demon2 "The kind that follows someone who has too much blood on their hands."
    pause 0.5
    demon2 "I can sense it clearly now..."
    pause 0.4
    demon2 "A Hashira."
    pause 0.4
    demon2 "...and something distorted standing beside him."
    pause 0.5
    demon2 "Your scent is wrong."
    pause 0.3
    demon2 "Not old... not new..."
    pause 0.4
    demon2 "...as if you slipped out of time and forgot how to return."
    pause 0.6

    thought "...Stop."
    pause 0.4
    thought "Don't listen."
    pause 0.6

    demon2 "...Ah."
    pause 0.3
    demon2 "That reaction..."
    pause 0.3
    demon2 "...regret?"
    pause 0.5

    menu:
        "...I don't have anything to say to you.":
            thought "..."
            pause 0.3
            thought "I don't give it my face."
            pause 0.3
            thought "I don't give it my voice."
            pause 0.3
            thought "I give it nothing."
            pause 0.5
            demon2 "Silence."
            pause 0.3
            demon2 "How interesting."
            pause 0.3
            demon2 "The ones who go quiet are always the ones with the most to hide."
            pause 0.6

        "...You don't know what you're talking about.":
            hide youngynquiet
            show youngyntalkingg at right_char
            yn "..."
            pause 0.3
            yn "You don't know anything about me."
            hide youngyntalkingg
            show youngynquiet at right_char
            pause 0.4
            demon2 "..."
            pause 0.3
            demon2 "Oh."
            pause 0.3
            demon2 "It speaks."
            pause 0.3
            demon2 "And it's angry."
            pause 0.3
            demon2 "Good."
            pause 0.3
            demon2 "Anger is honest."
            pause 0.6

        "...{i}(Look at Muichiro.){/i}":
            thought "..."
            pause 0.3
            thought "He's not reacting."
            pause 0.3
            thought "He never reacts to things like this."
            pause 0.4
            thought "That used to comfort me."
            pause 0.3
            thought "Now I don't know what it means."
            pause 0.6
            demon2 "Ah."
            pause 0.3
            demon2 "You looked at him."
            pause 0.3
            demon2 "Instinct."
            pause 0.3
            demon2 "Even now."
            pause 0.6

        "...It's not regret. It's something worse.":
            hide youngynquiet
            show youngyntalkingg at right_char
            yn "..."
            pause 0.3
            yn "It's not regret."
            hide youngyntalkingg
            show youngynquiet at right_char
            pause 0.4
            demon2 "..."
            pause 0.3
            demon2 "Oh?"
            pause 0.3
            demon2 "Then what is it."
            pause 0.5
            thought "..."
            pause 0.3
            thought "I don't answer."
            pause 0.3
            thought "Because I don't have a word for it."
            pause 0.3
            thought "Grief, maybe."
            pause 0.3
            thought "But grief for something that hasn't finished happening yet."
            pause 0.6

    pause 0.5

    play sound "mist.wav" fadein 0.5

    hide muiquiet
    show muitalking at left_char

    mui "Mist Breathing..."
    pause 0.5
    mui "...Seventh Form."
    pause 0.4
    mui "...Obscuring Clouds."

    with hpunch
    pause 0.6

    hide muitalking
    show muiquiet at left_char

    pause 0.5

    thought "He moved without hesitation."
    pause 0.3
    thought "He always does."
    pause 0.4
    thought "Even now."
    pause 0.4
    thought "Even without the memories."
    pause 0.4
    thought "His body remembers what his mind won't."
    pause 0.8

    hide muiquiet
    show muitalking at left_char

    mui "You're still alive."
    pause 0.5

    hide muitalking
    show muiquiet at left_char

    thought "Not surprised."
    pause 0.3

    hide muiquiet
    show muitalking at left_char

    mui "You got slower."
    pause 0.4
    mui "Thought you would die eventually."
    pause 0.5
    mui "You were always slower to adapt."
    pause 0.5
    mui "...What was your name again?"

    hide muitalking
    show muiquiet at left_char

    pause 0.8

    thought "...Right."
    pause 0.3
    thought "This is who he is now."
    pause 0.6

    menu:
        "...[player_name]. Same as it's always been.":
            hide youngynquiet
            show youngyntalkingg at right_char
            yn "...[player_name]."
            pause 0.3
            yn "Same as it's always been."
            hide youngyntalkingg
            show youngynquiet at right_char
            pause 0.5
            hide muiquiet
            show muitalking at left_char
            mui "..."
            pause 0.3
            mui "Right."
            pause 0.3
            mui "You used to dislike it when I forgot."
            hide muitalking
            show muiquiet at left_char
            thought "Used to."
            pause 0.3
            thought "I still do."
            pause 0.3
            thought "I just stopped showing it."
            pause 0.6

        "...Does it matter to you?":
            thought "..."
            pause 0.5
            thought "He asked."
            pause 0.3
            thought "Like it's a small thing."
            pause 0.3
            thought "Like it doesn't cost anything."
            pause 0.5
            hide youngynquiet
            show youngyntalkingg at right_char
            yn "...Does it matter to you?"
            hide youngyntalkingg
            show youngynquiet at right_char
            pause 0.4
            hide muiquiet
            show muitalking at left_char
            mui "..."
            pause 0.3
            mui "Probably not."
            pause 0.3
            mui "But I asked."
            hide muitalking
            show muiquiet at left_char
            pause 0.4
            hide youngynquiet
            show youngyntalkingg at right_char
            yn "...[player_name]."
            hide youngyntalkingg
            show youngynquiet at right_char
            pause 0.5
            thought "He asked."
            pause 0.3
            thought "That's something."
            pause 0.3
            thought "Even if he won't remember."
            pause 0.6

        "...[player_name]. You used to say it differently.":
            hide youngynquiet
            show youngyntalkingg at right_char
            yn "...[player_name]."
            pause 0.3
            yn "You used to say it differently."
            hide youngyntalkingg
            show youngynquiet at right_char
            pause 0.5
            hide muiquiet
            show muitalking at left_char
            mui "..."
            pause 0.4
            mui "...How."
            hide muitalking
            show muiquiet at left_char
            pause 0.4
            thought "..."
            pause 0.3
            thought "Softer."
            pause 0.3
            thought "Like it was something you were careful with."
            pause 0.3
            thought "Like it was made of something that could break."
            pause 0.6

    hide youngynquiet
    show youngyntalkingg at right_char

    yn "Well... you never forgot before."

    hide youngyntalkingg
    show youngynquiet at right_char

    hide muiquiet
    show muitalking at left_char

    mui "..."

    hide muitalking
    show muiquiet at left_char

    pause 0.6

    thought "No answer. As always."
    pause 0.5

    hide youngynquiet
    show youngyntalkingg at right_char

    yn "You used to call me something."
    pause 0.4
    yn "...Sparrow."

    hide youngyntalkingg
    show youngynquiet at right_char

    hide muiquiet
    show muitalking at left_char

    mui "...Why would I call anyone that?"

    hide muitalking
    show muiquiet at left_char

    pause 0.8

    menu:
        "Because I moved like one. Small. Hard to catch.":
            hide youngynquiet
            show youngyntalkingg at right_char
            yn "Because I moved like one."
            pause 0.3
            yn "Small. Hard to catch."
            hide youngyntalkingg
            show youngynquiet at right_char
            pause 0.4
            hide muiquiet
            show muitalking at left_char
            mui "..."
            pause 0.3
            mui "That doesn't sound like something I'd say."
            hide muitalking
            show muiquiet at left_char
            thought "It was exactly something he'd say."
            pause 0.3
            thought "Once."
            pause 0.3
            thought "When he still noticed things like that."
            pause 0.6

        "Because you said sparrows always come back. Even when they shouldn't.":
            hide youngynquiet
            show youngyntalkingg at right_char
            yn "Because you said sparrows always come back."
            pause 0.3
            yn "Even when they shouldn't."
            hide youngyntalkingg
            show youngynquiet at right_char
            pause 0.5
            hide muiquiet
            show muitalking at left_char
            mui "..."
            pause 0.5
            mui "...I said that?"
            hide muitalking
            show muiquiet at left_char
            pause 0.4
            thought "..."
            pause 0.3
            thought "He's not denying it."
            pause 0.3
            thought "He's just... sitting with it."
            pause 0.3
            thought "Like it almost fits."
            pause 0.6

        "I don't know. You just started one day and never stopped.":
            hide youngynquiet
            show youngyntalkingg at right_char
            yn "I don't know."
            pause 0.3
            yn "You just started one day and never stopped."
            hide youngyntalkingg
            show youngynquiet at right_char
            pause 0.4
            hide muiquiet
            show muitalking at left_char
            mui "..."
            pause 0.4
            mui "That sounds inefficient."
            hide muitalking
            show muiquiet at left_char
            thought "..."
            pause 0.3
            thought "He used to say that about everything he didn't understand."
            pause 0.3
            thought "Inefficient."
            pause 0.3
            thought "Like feelings were a logistics problem."
            pause 0.3
            thought "Like love was something you could optimize."
            pause 0.6

        "It doesn't matter. You won't remember it anyway.":
            hide youngynquiet
            show youngyntalkingg at right_char
            yn "...It doesn't matter."
            pause 0.3
            yn "You won't remember it anyway."
            hide youngyntalkingg
            show youngynquiet at right_char
            pause 0.5
            hide muiquiet
            show muitalking at left_char
            mui "..."
            pause 0.5
            mui "...That was cruel."
            hide muitalking
            show muiquiet at left_char
            pause 0.4
            thought "..."
            pause 0.3
            thought "I know."
            pause 0.3
            thought "I said it anyway."
            pause 0.3
            thought "Because I'm tired."
            pause 0.3
            thought "Because it's true."
            pause 0.3
            thought "Because sometimes the truth is the cruelest thing you have."
            pause 0.6

    pause 0.5

    thought "Of course."
    pause 0.3
    thought "To him now—"
    pause 0.3
    thought "It probably is."
    pause 0.8

    demon2 "How cruel."
    pause 0.3
    demon2 "To stand before someone who once held your entire world."
    pause 0.4
    demon2 "...and be nothing to them."
    pause 0.5
    demon2 "Humans cling to bonds as if they are eternal."
    pause 0.4
    demon2 "But memory is the most fragile flesh."
    pause 0.4
    demon2 "It rots."
    pause 0.5
    demon2 "And eventually..."
    pause 0.4
    demon2 "...it forgets why it ever held on."
    pause 0.5

    menu:
        "...{i}(Don't move. Don't breathe. Don't let it in.){/i}":
            thought "..."
            pause 0.4
            thought "I hold very still."
            pause 0.3
            thought "The way you hold still when something is hunting you."
            pause 0.3
            thought "Don't move."
            pause 0.3
            thought "Don't breathe."
            pause 0.3
            thought "Don't let it find the thing it's looking for."
            pause 0.6

        "...{i}(Look at the trees. Not at him. Not at his face.){/i}":
            thought "I look at the trees."
            pause 0.3
            thought "The way the light doesn't reach the ground here."
            pause 0.3
            thought "The way the dark sits between the roots like it belongs there."
            pause 0.4
            thought "Anything."
            pause 0.3
            thought "Anything but his face."
            pause 0.3
            thought "Because if I look at his face I'll say something I can't take back."
            pause 0.6

        "...You're not saying anything I don't already know.":
            hide youngynquiet
            show youngyntalkingg at right_char
            yn "..."
            pause 0.3
            yn "You're not saying anything I don't already know."
            hide youngyntalkingg
            show youngynquiet at right_char
            pause 0.4
            demon2 "..."
            pause 0.3
            demon2 "Oh."
            pause 0.3
            demon2 "That's worse."
            pause 0.3
            demon2 "You already know."
            pause 0.3
            demon2 "And you're still here."
            pause 0.6

        "...{i}(Watch Muichiro. See if he flinches.){/i}":
            thought "I watch him instead."
            pause 0.3
            thought "His face."
            pause 0.3
            thought "Looking for something."
            pause 0.3
            thought "A flicker."
            pause 0.3
            thought "A crack."
            pause 0.3
            thought "Anything that says he heard it."
            pause 0.3
            thought "That it landed."
            pause 0.4
            thought "..."
            pause 0.3
            thought "Nothing."
            pause 0.3
            thought "Or maybe something."
            pause 0.3
            thought "I can't tell anymore."
            pause 0.6

    hide muiquiet
    show muitalking at left_char

    mui "Shut up."

    hide muitalking
    show muiquiet at left_char

    pause 0.4

    thought "He's angry."
    pause 0.3
    thought "That's new..."
    pause 0.3
    thought "Or maybe it isn't."
    pause 0.3
    thought "Maybe I just never saw it before."
    pause 0.6

    demon2 "Ah..."
    pause 0.3
    demon2 "So even mist can bleed..."
    pause 0.4
    demon2 "Tell me, Hashira..."
    pause 0.3
    demon2 "...how long will you run away?"
    pause 0.5

    with vpunch

    demon2 "Fall."
    pause 0.4
    demon2 "...together."
    pause 0.5

    with hpunch

    hide youngynquiet
    show youngyntalkingg at right_char

    yn "Muichiro—!"

    hide youngyntalkingg
    show youngynquiet at right_char

    hide muiquiet
    show muitalking at left_char

    mui "...Don't."
    pause 0.3
    mui "...call me like you used to."

    hide muitalking
    show muiquiet at left_char

    pause 0.6

    menu:
        "...Like I know you. Because I do.":
            hide youngynquiet
            show youngyntalkingg at right_char
            yn "...Like I know you."
            pause 0.3
            yn "Because I do."
            hide youngyntalkingg
            show youngynquiet at right_char
            pause 0.4
            hide muiquiet
            show muitalking at left_char
            mui "..."
            pause 0.3
            mui "...You don't."
            pause 0.3
            mui "Not anymore."
            hide muitalking
            show muiquiet at left_char
            thought "..."
            pause 0.3
            thought "He's right."
            pause 0.3
            thought "The person I knew is somewhere underneath this one."
            pause 0.3
            thought "And I don't know how deep."
            pause 0.6

        "...{i}(Say nothing. Let him have that.){/i}":
            thought "..."
            pause 0.4
            thought "He said don't."
            pause 0.3
            thought "So I don't."
            pause 0.3
            thought "Even though every part of me wants to say his name again."
            pause 0.3
            thought "Just to see if his eyes change."
            pause 0.3
            thought "Just to see if something comes back."
            pause 0.3
            thought "I give him the silence instead."
            pause 0.3
            thought "It's the only thing I have left that he hasn't forgotten."
            pause 0.6

        "...Muichiro.":
            hide youngynquiet
            show youngyntalkingg at right_char
            yn "...Muichiro."
            hide youngyntalkingg
            show youngynquiet at right_char
            pause 0.5
            hide muiquiet
            show muitalking at left_char
            mui "..."
            hide muitalking
            show muiquiet at left_char
            pause 0.4
            thought "He doesn't say anything."
            pause 0.3
            thought "But he doesn't look away either."
            pause 0.3
            thought "And for a moment—"
            pause 0.3
            thought "Just a moment—"
            pause 0.3
            thought "Something in his face goes very still."
            pause 0.3
            thought "The way things go still right before they remember."
            pause 0.6

        "...I'm sorry. I know you don't want me to.":
            hide youngynquiet
            show youngyntalkingg at right_char
            yn "...I'm sorry."
            pause 0.3
            yn "I know you don't want me to."
            hide youngyntalkingg
            show youngynquiet at right_char
            pause 0.5
            hide muiquiet
            show muitalking at left_char
            mui "..."
            pause 0.5
            mui "...Then why."
            hide muitalking
            show muiquiet at left_char
            pause 0.4
            thought "..."
            pause 0.3
            thought "Because I needed to hear it."
            pause 0.3
            thought "Even if you didn't."
            pause 0.3
            thought "Even if it costs me something."
            pause 0.3
            thought "Some things you say for yourself."
            pause 0.3
            thought "Not for the person listening."
            pause 0.6

    pause 0.5

    thought "...Too late."
    pause 0.4
    thought "For a moment—"
    pause 0.3
    thought "...his eyes changed."
    pause 0.4
    thought "Like we returned..."
    pause 0.3
    thought "...to that forest."
    pause 0.4
    thought "And I let it slip away again."
    pause 1.0

    scene black
    with Fade(0.3, 0.0, 0.8, color="#ffffff")

    pause 1.0

    jump mha_intro
