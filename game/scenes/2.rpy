label mission_scene:

    scene bg forest_night at bg_fit
    with slow_dissolve

    play sound "wind.wav" fadein 2.0
    pause 0.6

    thought "The forest remembers. It always does."
    thought "Even when people forget."
    thought "Even when promises turn into something unrecognizable."
    pause 0.5

    play sound "leaves_rustle.wav" fadein 1.0

    thought "We met here once."
    thought "Back when the nights felt shorter."
    thought "Back when he still laughed."
    pause 0.8

    with dissolve

    yn "Moon Breathing..."
    yn "...Third Form."
    yn "...Lunar Rings."

    with vpunch
    pause 0.3

    thought "Too clean. My body moved before I could even think."
    thought "...Just like before."
    pause 0.6

    show muiquiet at left_char
    with dissolve

    demon2 "Ara..."
    demon2 "What an unpleasant stillness."
    demon2 "The kind that follows someone who has too much blood on their hands."
    demon2 "I can sense it clearly now... A Hashira."
    demon2 "...and something distorted standing beside him."
    demon2 "Your scent is wrong. Not old... not new..."
    demon2 "...as if you slipped out of time and forgot how to return."
    pause 0.4

    thought "...Stop. Don't listen."
    pause 0.4

    demon2 "...Ah. That reaction..."
    demon2 "...regret?"
    pause 0.4

    menu:
        "...I don't have anything to say to you.":
            thought "I don't give it my face. I don't give it my voice."
            thought "I give it nothing."
            demon2 "Silence. How interesting."
            demon2 "The ones who go quiet are always the ones with the most to hide."

        "...You don't know what you're talking about.":
            yn "You don't know anything about me."
            demon2 "Oh. It speaks. And it's angry."
            demon2 "Good. Anger is honest."

        "...{i}(Look at Muichiro.){/i}":
            thought "He's not reacting. He never reacts to things like this."
            thought "That used to comfort me. Now I don't know what it means."
            demon2 "Ah. You looked at him. Instinct. Even now."

        "...It's not regret. It's something worse.":
            yn "It's not regret."
            demon2 "Oh? Then what is it."
            thought "I don't answer. Because I don't have a word for it."
            thought "Grief, maybe. But grief for something that hasn't finished happening yet."

    pause 0.4

    play sound "mist.wav" fadein 0.5

    hide muiquiet
    show muitalking at left_char
    mui "Mist Breathing..."
    mui "...Seventh Form."
    mui "...Obscuring Clouds."
    hide muitalking
    show muiquiet at left_char

    with hpunch
    pause 0.4

    thought "He moved without hesitation. He always does."
    thought "Even now. Even without the memories."
    thought "His body remembers what his mind won't."
    pause 0.6

    hide muiquiet
    show muitalking at left_char
    mui "You're still alive."
    hide muitalking
    show muiquiet at left_char

    thought "Not surprised."
    pause 0.3

    hide muiquiet
    show muitalking at left_char
    mui "You got slower."
    mui "Thought you would die eventually."
    mui "You were always slower to adapt."
    mui "...What was your name again?"
    hide muitalking
    show muiquiet at left_char

    thought "...Right. This is who he is now."
    pause 0.5

    menu:
        "...[player_name]. Same as it's always been.":
            yn "...[player_name]. Same as it's always been."
            hide muiquiet
            show muitalking at left_char
            mui "Right. You used to dislike it when I forgot."
            hide muitalking
            show muiquiet at left_char
            thought "Used to. I still do. I just stopped showing it."

        "...Does it matter to you?":
            thought "He asked. Like it's a small thing. Like it doesn't cost anything."
            yn "...Does it matter to you?"
            hide muiquiet
            show muitalking at left_char
            mui "Probably not. But I asked."
            hide muitalking
            show muiquiet at left_char
            yn "...[player_name]."
            thought "He asked. That's something. Even if he won't remember."

        "...[player_name]. You used to say it differently.":
            yn "...[player_name]. You used to say it differently."
            hide muiquiet
            show muitalking at left_char
            mui "...How."
            hide muitalking
            show muiquiet at left_char
            thought "Softer. Like it was something you were careful with."
            thought "Like it was made of something that could break."

    yn "Well... you never forgot before."

    hide muiquiet
    show muitalking at left_char
    mui "..."
    hide muitalking
    show muiquiet at left_char

    thought "No answer. As always."
    pause 0.4

    yn "You used to call me something."
    yn "...Sparrow."

    hide muiquiet
    show muitalking at left_char
    mui "...Why would I call anyone that?"
    hide muitalking
    show muiquiet at left_char

    pause 0.5

    menu:
        "Because I moved like one. Small. Hard to catch.":
            yn "Because I moved like one. Small. Hard to catch."
            hide muiquiet
            show muitalking at left_char
            mui "That doesn't sound like something I'd say."
            hide muitalking
            show muiquiet at left_char
            thought "It was exactly something he'd say. Once."
            thought "When he still noticed things like that."

        "Because you said sparrows always come back. Even when they shouldn't.":
            yn "Because you said sparrows always come back."
            yn "Even when they shouldn't."
            hide muiquiet
            show muitalking at left_char
            mui "...I said that?"
            hide muitalking
            show muiquiet at left_char
            thought "He's not denying it. He's just sitting with it."
            thought "Like it almost fits."

        "I don't know. You just started one day and never stopped.":
            yn "I don't know. You just started one day and never stopped."
            hide muiquiet
            show muitalking at left_char
            mui "That sounds inefficient."
            hide muitalking
            show muiquiet at left_char
            thought "He used to say that about everything he didn't understand."
            thought "Inefficient. Like feelings were a logistics problem."
            thought "Like love was something you could optimize."

        "It doesn't matter. You won't remember it anyway.":
            yn "...It doesn't matter. You won't remember it anyway."
            hide muiquiet
            show muitalking at left_char
            mui "...That was cruel."
            hide muitalking
            show muiquiet at left_char
            thought "I know. I said it anyway."
            thought "Because I'm tired. Because it's true."
            thought "Because sometimes the truth is the cruelest thing you have."

    thought "Of course. To him now — it probably is."
    pause 0.6

    demon2 "How cruel."
    demon2 "To stand before someone who once held your entire world."
    demon2 "...and be nothing to them."
    demon2 "Humans cling to bonds as if they are eternal."
    demon2 "But memory is the most fragile flesh."
    demon2 "It rots. And eventually..."
    demon2 "...it forgets why it ever held on."
    pause 0.4

    menu:
        "...{i}(Don't move. Don't breathe. Don't let it in.){/i}":
            thought "I hold very still."
            thought "The way you hold still when something is hunting you."
            thought "Don't move. Don't breathe."
            thought "Don't let it find the thing it's looking for."

        "...{i}(Look at the trees. Not at him. Not at his face.){/i}":
            thought "I look at the trees."
            thought "The way the dark sits between the roots like it belongs there."
            thought "Anything but his face."
            thought "Because if I look at his face I'll say something I can't take back."

        "...You're not saying anything I don't already know.":
            yn "You're not saying anything I don't already know."
            demon2 "Oh. That's worse."
            demon2 "You already know. And you're still here."

        "...{i}(Watch Muichiro. See if he flinches.){/i}":
            thought "I watch him instead. His face."
            thought "Looking for a flicker. A crack."
            thought "Anything that says he heard it. That it landed."
            thought "..."
            thought "Nothing. Or maybe something. I can't tell anymore."

    hide muiquiet
    show muitalking at left_char
    mui "Shut up."
    hide muitalking
    show muiquiet at left_char

    thought "He's angry. That's new..."
    thought "Or maybe it isn't. Maybe I just never saw it before."
    pause 0.5

    demon2 "Ah... So even mist can bleed..."
    demon2 "Tell me, Hashira..."
    demon2 "...how long will you run away?"
    pause 0.4

    with vpunch

    demon2 "Fall."
    demon2 "...together."
    pause 0.4

    with hpunch

    yn "Muichiro—!"

    hide muiquiet
    show muitalking at left_char
    mui "...Don't."
    mui "...call me like you used to."
    hide muitalking
    show muiquiet at left_char

    pause 0.5

    menu:
        "...Like I know you. Because I do.":
            yn "...Like I know you. Because I do."
            hide muiquiet
            show muitalking at left_char
            mui "...You don't. Not anymore."
            hide muitalking
            show muiquiet at left_char
            thought "He's right."
            thought "The person I knew is somewhere underneath this one."
            thought "And I don't know how deep."

        "...{i}(Say nothing. Let him have that.){/i}":
            thought "He said don't. So I don't."
            thought "Even though every part of me wants to say his name again."
            thought "Just to see if his eyes change."
            thought "I give him the silence instead."
            thought "It's the only thing I have left that he hasn't forgotten."

        "...Muichiro.":
            yn "...Muichiro."
            hide muiquiet
            show muitalking at left_char
            mui "..."
            hide muitalking
            show muiquiet at left_char
            thought "He doesn't say anything."
            thought "But he doesn't look away either."
            thought "And for a moment — just a moment —"
            thought "Something in his face goes very still."
            thought "The way things go still right before they remember."

        "...I'm sorry. I know you don't want me to.":
            yn "...I'm sorry. I know you don't want me to."
            hide muiquiet
            show muitalking at left_char
            mui "...Then why."
            hide muitalking
            show muiquiet at left_char
            thought "Because I needed to hear it. Even if you didn't."
            thought "Some things you say for yourself."
            thought "Not for the person listening."

    thought "...Too late."
    thought "For a moment — his eyes changed."
    thought "Like we returned... to that forest."
    thought "And I let it slip away again."
    pause 0.8

    scene black
    with Fade(0.3, 0.0, 0.8, color="#ffffff")

    pause 0.8

    jump mha_intro
