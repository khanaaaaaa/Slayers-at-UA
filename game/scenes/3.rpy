label mha_intro:

    scene black
    with Fade(1.5, 0.5, 1.5)

    play sound "wind_low.wav" fadein 1.5

    thought "..Cold. Not the cold of night training."
    thought "This is different."
    pause 0.6

    play sound "heartbeat.wav"
    pause 0.4

    thought "...My body hurts. That means I'm alive."
    thought "...Again."
    pause 0.8

    scene black
    with flash_blue

    thought "Water—"
    thought "—Cold, so cold—"
    thought "—Can't breathe—"
    thought "—The river—"
    thought "—I don't remember falling—"
    thought "—And then nothing—"
    pause 0.4

    scene black
    with hard_cut

    thought "I don't remember. I never remember that part."
    pause 0.8

    scene bg street at bg_fit
    with slow_dissolve

    play music "city_unease.mp3" fadein 2.0
    play sound "city_ambience.wav" fadein 1.5
    pause 0.5

    thought "Too bright. The sky—"
    thought "...It's wrong."
    thought "No. It's just different."
    thought "You've seen worse. Haven't you?"
    thought "I don't remember."
    pause 0.8

    show muichiroquiet at center_char
    with dissolve

    hide muichiroquiet
    show muichirotalking at center_char
    mui "...Tch."
    mui "So you're alive."
    hide muichirotalking
    show muichiroquiet at center_char

    pause 0.4

    menu:
        "Barely.":
            yn "...Barely."
            hide muichiroquiet
            show muichirotalking at center_char
            mui "That's still alive."
            hide muichirotalking
            show muichiroquiet at center_char
            thought "He says it like it's a correction."
            thought "Like barely doesn't count as a qualifier."
            thought "It absolutely counts as a qualifier."

        "Unfortunately.":
            yn "...Unfortunately."
            hide muichiroquiet
            show muichirotalking at center_char
            mui "Don't say that."
            hide muichirotalking
            show muichiroquiet at center_char
            thought "He said it fast. Like it bothered him."
            thought "Like he didn't want it to."
            thought "Interesting."

        "Yeah.":
            yn "...Yeah."
            hide muichiroquiet
            show muichirotalking at center_char
            mui "Good."
            hide muichirotalking
            show muichiroquiet at center_char
            thought "One word. Good."
            thought "I've been through a dimensional rift and he said good."
            thought "Okay."

    yn "...Where.. Where is this?"
    pause 0.3

    thought "The sky is too bright. It feels artificial."
    thought "Like something built to look like sky rather than actual sky."
    thought "...Why do I know the difference."
    pause 0.6

    hide muichiroquiet
    show muichirotalking at center_char
    mui "I don't know."
    hide muichirotalking
    show muichiroquiet at center_char

    thought "That answer shouldn't scare me. But it does."
    thought "He always has something. And right now he has nothing."
    thought "We're so cooked."
    pause 0.6
    hide muichiroquiet

    show aizawatalking at center_char
    with dissolve

    aizawa "..You two are finally awake."
    pause 0.4

    menu:
        "How long were we out.":
            hide aizawatalking
            show aizawaquiet at center_char
            yn "..How long were we out?"
            hide aizawaquiet
            show aizawatalking at center_char
            aizawa "Three hours. Give or take."
            hide aizawatalking
            show aizawaquiet at center_char
            thought "Three hours. That's nothing."
            thought "I've been out longer after worse."
            thought "...Have I?"

        "Where are we.":
            hide aizawatalking
            show aizawaquiet at center_char
            yn "..Where are we."
            hide aizawaquiet
            show aizawatalking at center_char
            aizawa "Safe. For now."
            aizawa "That's all you need to know right now."
            hide aizawatalking
            show aizawaquiet at center_char
            thought "He says it like a professional."
            thought "Like he's done this before."
            thought "Talked to people who woke up somewhere wrong."
            thought "Which, honestly, probably."

        "Say nothing.":
            thought "I look at him. Dark clothes. Tired eyes."
            thought "The kind of tired that doesn't go away with sleep."
            thought "Something about him feels familiar in a way I can't explain."
            thought "...Don't stare."
            thought "That would be a weird thing to do."

    yn "..Who—"
    pause 0.3

    hide aizawaquiet
    show muichiroquiet at center_char
    with dissolve

    hide muichiroquiet
    show muichirotalking at center_char
    mui "..Not a demon."
    hide muichirotalking
    show muichiroquiet at center_char

    thought "...Oh no."
    pause 0.4

    yn "This isn't the South district."

    hide muichiroquiet
    show muichirotalking at center_char
    mui "No. It's not anywhere I recognize."
    hide muichirotalking
    show muichiroquiet at center_char

    yn "Muichiro.. look around."

    hide muichiroquiet
    show muichirotalking at center_char
    mui "I am. It's loud. Pointlessly loud."
    hide muichirotalking
    show muichiroquiet at center_char

    thought "He's not wrong."
    thought "There's a kid over there who just exploded something for fun."
    thought "Nobody reacted. This is just normal here."
    thought "This is fine. Everything is fine."
    pause 0.5

    yn "You're not even surprised?"

    hide muichiroquiet
    show muichirotalking at center_char
    mui "Surprise doesn't change anything."
    hide muichirotalking
    show muichiroquiet at center_char

    menu:
        "That's not true.":
            yn "That's not true."
            hide muichiroquiet
            show muichirotalking at center_char
            mui "...Maybe."
            hide muichirotalking
            show muichiroquiet at center_char
            thought "He doesn't argue when he's not sure."
            thought "Which is new. Or maybe it isn't."
            thought "I genuinely can't tell anymore."

        "You're right.":
            yn "...You're right."
            hide muichiroquiet
            show muichirotalking at center_char
            mui "I usually am."
            hide muichirotalking
            show muichiroquiet at center_char
            thought "There it is. That flat certainty."
            thought "I missed it. I didn't know I missed it until just now."
            thought "That's embarrassing."

        "I don't know what I feel.":
            thought "Scared. Relieved. Both. Neither."
            thought "Something that doesn't have a name yet."
            thought "Probably several somethings."

    hide muichiroquiet
    show aizawatalking at center_char
    aizawa "Aizawa. Pro Hero."
    aizawa "You collapsed in the middle of the street."
    hide aizawatalking
    show aizawaquiet at center_char
    pause 0.4

    yn "Hero..?"

    thought "That word."
    thought "I know it. I don't know how I know it."
    thought "But it fits here like it was always supposed to."
    thought "...Why do I know that."
    pause 0.6

    hide aizawaquiet
    show muichirotalking at center_char
    mui "That word doesn't exist where we're from."
    hide muichirotalking
    show aizawatalking at center_char

    aizawa "That's becoming obvious."
    hide aizawatalking
    show aizawaquiet at center_char
    pause 0.3

    yn "We were fighting a demon."
    hide aizawaquiet
    show aizawatalking at center_char
    aizawa "...That again."
    hide aizawatalking
    show aizawaquiet at center_char
    pause 0.3

    hide aizawaquiet
    show muichirotalking at center_char
    mui "Upper Rank. I am a Hashira."
    hide muichirotalking
    show muichiroquiet at center_char

    pause 0.6

    hide muichiroquiet
    show aizawatalking at center_char
    aizawa "Either this is the worst coordinated lie I've heard.."
    aizawa "Or reality itself is malfunctioning."
    hide aizawatalking
    show aizawaquiet at center_char
    pause 0.5

    menu:
        "It's not a lie.":
            yn "...It's not a lie."
            aizawa "I know. That's what concerns me."
            thought "Yeah. Me too."

        "We don't expect you to believe us.":
            yn "...We don't expect you to believe us."
            aizawa "Smart."
            aizawa "Most people in your situation try to convince me."
            aizawa "You're not."
            aizawa "That's either very honest or very calculated."
            thought "Both."
            thought "Mostly the first one though."

        "What would convince you.":
            yn "...What would convince you?"
            aizawa "Nothing right now."
            aizawa "But keep talking."
            thought "He said keep talking."
            thought "That's either a good sign or a trap."
            thought "Probably both."

    hide aizawaquiet
    stop music fadeout 2.0

    scene black
    with Fade(0.8, 0.3, 0.8)

    thought "We used to train under the same sky."
    thought "Same ground. Same silence."
    thought "This.. isn't that sky."
    pause 0.8

    scene bg street at bg_fit
    with slow_dissolve

    play music "city_unease.mp3" fadein 1.5

    show muichiroquiet at center_char
    with dissolve

    yn "Do you recognize anything?"

    hide muichiroquiet
    show muichirotalking at center_char
    mui "No. But it feels.. wrong."
    hide muichirotalking
    show muichiroquiet at center_char

    thought "I don't like the sound of that."
    pause 0.5

    yn "You used to say every place had a 'breathing rhythm'."

    hide muichiroquiet
    show muichirotalking at center_char
    mui "..Did I?"
    hide muichirotalking
    show muichiroquiet at center_char

    yn "Yes. You said you could hear it when you stopped talking."

    hide muichiroquiet
    show muichirotalking at center_char
    mui "This place doesn't have one."
    hide muichirotalking
    show muichiroquiet at center_char

    thought "A place with no breathing rhythm."
    thought "He used to say those were the dangerous ones."
    thought "The ones that had already forgotten how to be alive."
    thought "Cool. Great. We're in one of those."
    pause 0.6

    hide muichiroquiet
    show aizawatalking at center_char
    aizawa "You don't have anywhere to go."
    hide aizawatalking
    show aizawaquiet at center_char

    menu:
        "No.":
            yn "No."
            hide aizawaquiet
            show muichirotalking at center_char
            mui "No."
            hide muichirotalking
            show muichiroquiet at center_char
            thought "We said no at the same time."
            thought "That's either sweet or deeply sad."

        "Not here.":
            yn "...Not here."
            hide aizawaquiet
            show aizawatalking at center_char
            aizawa "Somewhere else then."
            hide aizawatalking
            show muichiroquiet at center_char
            yn "...Somewhere that doesn't exist anymore."
            thought "Or maybe it does. I don't know."
            thought "I don't know if I can go back."
            thought "I try not to think about that."

        "We had somewhere.":
            yn "...We had somewhere."
            hide aizawaquiet
            show muichirotalking at center_char
            mui "Past tense."
            hide muichirotalking
            show muichiroquiet at center_char
            thought "He noticed. He always notices the small things."
            thought "Even now. Even without the memories."
            thought "It's kind of annoying actually."

    hide muichiroquiet
    show aizawatalking at center_char
    aizawa "Then you're coming with me."
    hide aizawatalking
    show muichirotalking at center_char
    mui "We don't trust strangers."
    hide muichirotalking
    show aizawatalking at center_char

    aizawa "Then don't."
    aizawa "But you won't survive here alone."
    hide aizawatalking
    show aizawaquiet at center_char

    menu:
        "He's right.":
            thought "He's right."
            thought "Something in me already knows how dangerous this place is."
            thought "I don't know where that knowledge comes from."
            thought "And that terrifies me more than any of it."

        "Look at Muichiro.":
            thought "I look at him. He's already looking at me."
            thought "Not asking. Just waiting."
            thought "Like the decision is mine. It always was."
            thought "No pressure or anything."

        "We don't have a choice.":
            thought "We don't have a choice. We never did."
            thought "Not really. The river took that from us."
            thought "The river takes a lot of things."

    hide aizawaquiet
    show muichirotalking at center_char
    mui "…Tch."
    hide muichirotalking
    show muichiroquiet at center_char

    yn "We'll go."
    pause 0.5

    scene bg ua_gate at bg_fit
    with slow_dissolve

    stop music fadeout 1.5
    play music "ua_theme.mp3" fadein 2.0
    play sound "distant_city.wav" fadein 1.0
    pause 0.6

    thought "Everything feels too alive. And somehow… empty."
    pause 0.4

    hide muichiroquiet
    show muichirotalking at center_char
    mui "…So this is the new world."
    hide muichirotalking
    show muichiroquiet at center_char

    menu:
        "Yeah. And we're stuck in it.":
            yn "Yeah. And we're stuck in it."
            hide muichiroquiet
            show muichirotalking at center_char
            mui "Stuck implies we want to leave."
            hide muichirotalking
            show muichiroquiet at center_char
            thought "Do I want to leave."
            thought "I don't know what I'd go back to."
            thought "That's a question for later."
            thought "Much later."

        "It's not so different.":
            yn "...It's not so different."
            hide muichiroquiet
            show muichirotalking at center_char
            mui "It's completely different."
            hide muichirotalking
            show muichiroquiet at center_char
            yn "...The sky is still sky. The ground is still ground."
            hide muichiroquiet
            show muichirotalking at center_char
            mui "That's a very low bar."
            hide muichirotalking
            show muichiroquiet at center_char
            thought "He's right. It is."
            thought "I set a very low bar and he still cleared it."

        "I've been here before.":
            thought "I almost say it."
            thought "Something about this gate feels known."
            thought "Like I've seen it from a distance. Through glass, maybe."
            thought "I don't say any of that."
            thought "I don't know how to explain it even to myself."

    stop music fadeout 1.5
    hide muichiroquiet

    scene black
    with Fade(1.0, 0.5, 1.5)

    jump arrival_scene
