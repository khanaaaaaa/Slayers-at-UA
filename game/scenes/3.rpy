label mha_intro:

    scene black
    with Fade(1.5, 0.5, 1.5)

    play sound "wind_low.wav" fadein 1.5

    thought "..Cold."
    pause 0.4
    thought "Not the cold of night training."
    pause 0.3
    thought "This is different."
    pause 0.8

    play sound "heartbeat.wav"
    pause 0.5

    thought "...My body hurts."
    pause 0.5
    thought "That means I'm alive."
    pause 0.4
    thought "...Again."
    pause 1.0

    scene black
    with flash_blue

    thought "—water—"
    pause 0.2
    thought "—cold, so cold—"
    pause 0.2
    thought "—can't breathe—"
    pause 0.2
    thought "—sinking—"
    pause 0.3
    thought "—did I jump—"
    pause 0.3
    thought "—or did I fall—"
    pause 0.5

    scene black
    with hard_cut

    thought "..."
    pause 0.4
    thought "I don't remember."
    pause 0.5
    thought "I never remember that part."
    pause 1.0

    scene bg street at bg_fit
    with slow_dissolve

    play sound "city_ambience.wav" fadein 1.5
    pause 0.6

    thought "Too bright."
    pause 0.3
    thought "The sky—"
    pause 0.4
    thought "...it's wrong."
    pause 0.5
    thought "No."
    pause 0.3
    thought "It's just different."
    pause 0.4
    thought "You've seen worse."
    pause 0.4
    thought "Haven't you?"
    pause 0.8
    thought "..."
    pause 0.5
    thought "I don't remember."
    pause 1.0

    show muiquiet at center_char
    with dissolve

    pause 0.4

    hide muiquiet
    show muitalking at center_char

    mui "...Tch."
    pause 0.4
    mui "So you're alive."

    hide muitalking
    show muiquiet at center_char

    pause 0.5

    menu:
        "Barely.":
            hide muiquiet
            show muitalking at center_char
            yn "...Barely."
            hide muitalking
            show muiquiet at center_char
            pause 0.4
            hide muiquiet
            show muitalking at center_char
            mui "..."
            pause 0.3
            mui "That's still alive."
            hide muitalking
            show muiquiet at center_char
            thought "He says it like it's a correction."
            pause 0.3
            thought "Like barely doesn't count as a qualifier."
            pause 0.6

        "Unfortunately.":
            yn "...Unfortunately."
            pause 0.4
            hide muiquiet
            show muitalking at center_char
            mui "..."
            pause 0.3
            mui "Don't say that."
            hide muitalking
            show muiquiet at center_char
            pause 0.4
            thought "..."
            pause 0.3
            thought "He said it fast."
            pause 0.3
            thought "Like it bothered him."
            pause 0.3
            thought "Like he didn't want it to."
            pause 0.6

        "Yeah.":
            yn "...Yeah."
            pause 0.4
            hide muiquiet
            show muitalking at center_char
            mui "..."
            pause 0.3
            mui "Good."
            hide muitalking
            show muiquiet at center_char
            thought "One word."
            pause 0.3
            thought "Good."
            pause 0.3
            thought "I don't know what to do with that."
            pause 0.6

    yn "...Where.."
    pause 0.3
    yn "Where is this?"
    pause 0.4

    thought "The sky is too bright."
    pause 0.3
    thought "It feels artificial."
    pause 0.4
    thought "Like something built to look like sky."
    pause 0.4
    thought "Rather than actual sky."
    pause 0.5
    thought "..."
    pause 0.3
    thought "Why do I know the difference."
    pause 0.8

    hide muiquiet
    show muitalking at center_char

    mui "I don't know."

    hide muitalking
    show muiquiet at center_char

    pause 0.5

    thought "That answer shouldn't scare me."
    pause 0.3
    thought "But it does."
    pause 0.4
    thought "Because he always knows."
    pause 0.3
    thought "He always has an answer."
    pause 0.4
    thought "Even if it's wrong."
    pause 0.4
    thought "Even if it's cold."
    pause 0.4
    thought "He always has something."
    pause 0.5
    thought "And right now he has nothing."
    pause 0.8

    show aizawa at left_char
    with dissolve

    pause 0.5
    aizawa "..You two are finally awake."
    pause 0.6

    menu:
        "How long were we out.":
            yn "..How long were we out?"
            pause 0.4
            aizawa "..."
            pause 0.3
            aizawa "Three hours."
            pause 0.3
            aizawa "Give or take."
            pause 0.4
            thought "Three hours."
            pause 0.3
            thought "That's nothing."
            pause 0.3
            thought "I've been out longer after worse."
            pause 0.3
            thought "..."
            pause 0.3
            thought "Have I?"
            pause 0.6

        "Where are we.":
            yn "..Where are we."
            pause 0.4
            aizawa "Safe."
            pause 0.3
            aizawa "For now."
            pause 0.3
            aizawa "That's all you need to know right now."
            pause 0.4
            thought "..."
            pause 0.3
            thought "He says it like a professional."
            pause 0.3
            thought "Measured."
            pause 0.3
            thought "Controlled."
            pause 0.3
            thought "Like he's done this before."
            pause 0.3
            thought "Talked to people who woke up somewhere wrong."
            pause 0.6

        "Say nothing.":
            thought "..."
            pause 0.4
            thought "I look at him."
            pause 0.3
            thought "Dark clothes."
            pause 0.3
            thought "Tired eyes."
            pause 0.3
            thought "The kind of tired that doesn't go away with sleep."
            pause 0.4
            thought "I know who he is."
            pause 0.3
            thought "I know his name."
            pause 0.3
            thought "I know his quirk."
            pause 0.3
            thought "I know his students."
            pause 0.4
            thought "..."
            pause 0.3
            thought "Don't say any of that."
            pause 0.6

    yn "..Who—"
    pause 0.3

    hide muiquiet
    show muitalking at center_char

    mui "..Not a demon."

    hide muitalking
    show muiquiet at center_char

    pause 0.6

    thought "...Oh no."
    pause 0.5

    yn "This isn't the South district."

    hide muiquiet
    show muitalking at center_char

    mui "No."
    pause 0.3
    mui "It's not anywhere I recognize."

    hide muitalking
    show muiquiet at center_char

    pause 0.5

    yn "Muichiro.. look around."

    hide muiquiet
    show muitalking at center_char

    mui "I am."
    pause 0.3
    mui "It's loud."
    pause 0.3
    mui "Pointlessly loud."

    hide muitalking
    show muiquiet at center_char

    pause 0.5

    yn "You're not even surprised?"

    hide muiquiet
    show muitalking at center_char

    mui "Surprise doesn't change anything."

    hide muitalking
    show muiquiet at center_char

    menu:
        "That's not true.":
            yn "That's not true."
            pause 0.4
            hide muiquiet
            show muitalking at center_char
            mui "..."
            pause 0.3
            mui "Maybe."
            hide muitalking
            show muiquiet at center_char
            thought "He doesn't argue."
            pause 0.3
            thought "He never argues when he's not sure."
            pause 0.3
            thought "That's new."
            pause 0.3
            thought "Or maybe it isn't."
            pause 0.6

        "You're right.":
            yn "...You're right."
            pause 0.4
            hide muiquiet
            show muitalking at center_char
            mui "..."
            pause 0.3
            mui "I usually am."
            hide muitalking
            show muiquiet at center_char
            thought "..."
            pause 0.3
            thought "There it is."
            pause 0.3
            thought "That flat certainty."
            pause 0.3
            thought "I missed it."
            pause 0.3
            thought "I didn't know I missed it until just now."
            pause 0.6

        "I don't know what I feel.":
            thought "..."
            pause 0.4
            thought "I don't know what I feel."
            pause 0.3
            thought "Scared."
            pause 0.3
            thought "Relieved."
            pause 0.3
            thought "Both."
            pause 0.3
            thought "Neither."
            pause 0.3
            thought "Something that doesn't have a name yet."
            pause 0.6

    aizawa "Aizawa. Pro Hero."
    pause 0.3
    aizawa "You collapsed in the middle of the street."
    pause 0.5

    yn "Hero..?"

    thought "That word."
    pause 0.3
    thought "I know that word."
    pause 0.4
    thought "But not from the Corps."
    pause 0.4
    thought "From somewhere else."
    pause 0.5
    thought "Somewhere with tall buildings."
    pause 0.3
    thought "And people who fly."
    pause 0.5
    thought "..."
    pause 0.3
    thought "Why do I know that."
    pause 0.8

    hide muiquiet
    show muitalking at center_char

    mui "That word doesn't exist where we're from."

    hide muitalking
    show muiquiet at center_char

    aizawa "That's becoming obvious."
    pause 0.5

    yn "We were fighting a demon."
    pause 0.3
    aizawa "...That again."
    pause 0.4

    hide muiquiet
    show muitalking at center_char

    mui "Upper Rank."
    pause 0.3
    mui "I am a Hashira."

    hide muitalking
    show muiquiet at center_char

    pause 0.8

    aizawa "Either this is the worst coordinated lie I've heard.."
    pause 0.4
    aizawa "Or reality itself is malfunctioning."
    pause 0.6

    menu:
        "It's not a lie.":
            yn "...It's not a lie."
            pause 0.4
            aizawa "..."
            pause 0.3
            aizawa "I know."
            pause 0.3
            aizawa "That's what concerns me."
            pause 0.6

        "We don't expect you to believe us.":
            yn "...We don't expect you to believe us."
            pause 0.4
            aizawa "..."
            pause 0.3
            aizawa "Smart."
            pause 0.3
            aizawa "Most people in your situation try to convince me."
            pause 0.3
            aizawa "You're not."
            pause 0.3
            aizawa "That's either very honest or very calculated."
            pause 0.4
            thought "..."
            pause 0.3
            thought "Both."
            pause 0.6

        "What would convince you.":
            yn "...What would convince you?"
            pause 0.4
            aizawa "..."
            pause 0.4
            aizawa "Nothing right now."
            pause 0.3
            aizawa "But keep talking."
            pause 0.6

    scene black
    with Fade(0.8, 0.3, 0.8)

    thought "We used to train under the same sky."
    pause 0.4
    thought "Same ground."
    pause 0.3
    thought "Same silence."
    pause 0.5
    thought "This.. isn't that sky."
    pause 1.0

    scene bg street at bg_fit
    with slow_dissolve

    show muiquiet at center_char
    with dissolve

    show aizawa at left_char
    with dissolve

    pause 0.4

    yn "Do you recognize anything?"

    hide muiquiet
    show muitalking at center_char

    mui "No."
    pause 0.3
    mui "But it feels.. wrong."

    hide muitalking
    show muiquiet at center_char

    thought "I don't like the sound of that."
    pause 0.8

    yn "You used to say every place had a 'breathing rhythm'."

    hide muiquiet
    show muitalking at center_char

    mui "..Did I?"

    hide muitalking
    show muiquiet at center_char

    yn "Yes."
    pause 0.3
    yn "You said you could hear it when you stopped talking."

    mui "..."
    pause 0.5

    hide muiquiet
    show muitalking at center_char

    mui "This place doesn't have one."

    hide muitalking
    show muiquiet at center_char

    pause 0.5

    thought "I don't like the sound of that either."
    pause 0.4
    thought "A place with no breathing rhythm."
    pause 0.3
    thought "He used to say those were the dangerous ones."
    pause 0.4
    thought "The ones that had already forgotten how to be alive."
    pause 0.8

    aizawa "You don't have anywhere to go."
    pause 0.3

    menu:
        "No.":
            yn "No."
            pause 0.4
            hide muiquiet
            show muitalking at center_char
            mui "No."
            hide muitalking
            show muiquiet at center_char
            pause 0.4

        "Not here.":
            yn "...Not here."
            pause 0.4
            aizawa "..."
            pause 0.3
            aizawa "Somewhere else then."
            pause 0.3
            yn "...Somewhere that doesn't exist anymore."
            pause 0.5
            thought "Or maybe it does."
            pause 0.3
            thought "I don't know."
            pause 0.3
            thought "I don't know if the KNY world still exists."
            pause 0.3
            thought "Or if I left it behind completely."
            pause 0.6

        "We had somewhere.":
            yn "...We had somewhere."
            pause 0.4
            hide muiquiet
            show muitalking at center_char
            mui "..."
            pause 0.3
            mui "Past tense."
            hide muitalking
            show muiquiet at center_char
            pause 0.4
            thought "He noticed."
            pause 0.3
            thought "He always notices the small things."
            pause 0.3
            thought "Even now."
            pause 0.6

    aizawa "Then you're coming with me."
    pause 0.4

    hide muiquiet
    show muitalking at center_char

    mui "We don't trust strangers."

    hide muitalking
    show muiquiet at center_char

    aizawa "Then don't."
    pause 0.3
    aizawa "But you won't survive here alone."
    pause 0.8

    menu:
        "He's right.":
            thought "He's right."
            pause 0.3
            thought "I know he's right."
            pause 0.3
            thought "I know exactly how dangerous this world is."
            pause 0.3
            thought "I know the villains."
            pause 0.3
            thought "I know the threats."
            pause 0.3
            thought "I know things that haven't happened yet."
            pause 0.4
            thought "And that terrifies me more than any of it."
            pause 0.6

        "Look at Muichiro.":
            thought "I look at him."
            pause 0.3
            thought "He's already looking at me."
            pause 0.4
            thought "Not asking."
            pause 0.3
            thought "Just waiting."
            pause 0.3
            thought "Like he always does."
            pause 0.3
            thought "Like the decision is mine."
            pause 0.3
            thought "It always was."
            pause 0.6

        "We don't have a choice.":
            thought "..."
            pause 0.3
            thought "We don't have a choice."
            pause 0.3
            thought "We never did."
            pause 0.3
            thought "Not really."
            pause 0.3
            thought "The river took that from us."
            pause 0.6

    hide muiquiet
    show muitalking at center_char

    mui "…Tch."

    hide muitalking
    show muiquiet at center_char

    yn "We'll go."
    pause 0.6

    scene bg ua_gate at bg_fit
    with slow_dissolve

    play sound "distant_city.wav" fadein 1.0
    pause 0.8

    thought "Everything feels too alive."
    pause 0.4
    thought "And somehow… empty."
    pause 0.6

    hide muiquiet
    show muitalking at center_char

    mui "…So this is the new world."

    hide muitalking
    show muiquiet at center_char

    menu:
        "Yeah. And we're stuck in it.":
            yn "Yeah."
            pause 0.3
            yn "And we're stuck in it."
            pause 0.5
            hide muiquiet
            show muitalking at center_char
            mui "..."
            pause 0.3
            mui "Stuck implies we want to leave."
            hide muitalking
            show muiquiet at center_char
            pause 0.4
            thought "..."
            pause 0.3
            thought "Do I want to leave."
            pause 0.3
            thought "I don't know."
            pause 0.3
            thought "I don't know what I'd go back to."
            pause 0.6

        "It's not so different.":
            yn "...It's not so different."
            pause 0.4
            hide muiquiet
            show muitalking at center_char
            mui "..."
            pause 0.3
            mui "It's completely different."
            hide muitalking
            show muiquiet at center_char
            pause 0.4
            yn "...The sky is still sky."
            pause 0.3
            yn "The ground is still ground."
            pause 0.4
            hide muiquiet
            show muitalking at center_char
            mui "..."
            pause 0.3
            mui "That's a very low bar."
            hide muitalking
            show muiquiet at center_char
            thought "..."
            pause 0.3
            thought "He's right."
            pause 0.3
            thought "It is."
            pause 0.6

        "I've been here before.":
            thought "..."
            pause 0.4
            thought "I almost say it."
            pause 0.3
            thought "I've been here before."
            pause 0.3
            thought "Not like this."
            pause 0.3
            thought "But I know this gate."
            pause 0.3
            thought "I know what's behind it."
            pause 0.3
            thought "I know the hallways."
            pause 0.3
            thought "The classrooms."
            pause 0.3
            thought "The names on the doors."
            pause 0.4
            thought "..."
            pause 0.3
            thought "I don't say it."
            pause 0.6

    scene black
    with Fade(0.8, 0.3, 0.8)

    scene bg office at bg_fit
    with slow_dissolve

    show nezu at center_char
    with dissolve

    pause 0.5
    nezu "Interesting."
    pause 0.3
    nezu "A fractured connection across worlds.. fascinating!"
    pause 0.5

    menu:
        "Don't analyze it like that.":
            yn "Don't analyze it like that."
            pause 0.4
            nezu "Oh?"
            pause 0.3
            nezu "How would you prefer I analyze it?"
            pause 0.4
            yn "...Like it happened to people."
            pause 0.3
            yn "Not like a phenomenon."
            pause 0.5
            nezu "..."
            pause 0.3
            nezu "Fair."
            pause 0.3
            nezu "My apologies."
            pause 0.6

        "What do you know about it.":
            yn "...What do you know about it."
            pause 0.4
            nezu "Very little."
            pause 0.3
            nezu "Which is precisely what makes it fascinating."
            pause 0.3
            nezu "I know a great deal about a great many things."
            pause 0.3
            nezu "Gaps in my knowledge are rare."
            pause 0.3
            nezu "And therefore interesting."
            pause 0.5
            thought "..."
            pause 0.3
            thought "He's not wrong."
            pause 0.3
            thought "He knows almost everything."
            pause 0.3
            thought "Almost."
            pause 0.6

        "Say nothing.":
            thought "..."
            pause 0.3
            thought "I let him talk."
            pause 0.3
            thought "He will anyway."
            pause 0.3
            thought "That's what he does."
            pause 0.3
            thought "Talks."
            pause 0.3
            thought "Observes."
            pause 0.3
            thought "Files things away."
            pause 0.3
            thought "I know that about him."
            pause 0.3
            thought "I know too much about all of them."
            pause 0.6

    show muiquiet at left_char
    with dissolve

    hide muiquiet
    show muitalking at left_char

    mui "I always liked animals."

    hide muitalking
    show muiquiet at left_char

    yn "You called them 'walking mysteries' when we were kids."

    hide muiquiet
    show muitalking at left_char

    mui "..That's accurate."

    hide muitalking
    show muiquiet at left_char

    nezu "Oh my!"
    pause 0.8

    scene bg classroom at bg_fit
    with slow_dissolve

    show aizawa at center_char
    with dissolve

    pause 0.5
    aizawa "Two transfer students."
    pause 0.6

    yn "My name is [player_name]."
    pause 0.4

    thought "Someone's going to ask about the sword."
    pause 0.3
    thought "And someone's going to ask if we're cosplayers."
    pause 0.4
    thought "..."
    pause 0.3
    thought "How do I know that."
    pause 0.6

    mina "Are you two like… cosplayers?"
    pause 0.3

    thought "...See."
    pause 0.5

    denki "That sword is REAL?!"
    pause 0.3

    show muiquiet at left_char
    with dissolve

    hide muiquiet
    show muitalking at left_char

    mui "It is."

    hide muitalking
    show muiquiet at left_char

    pause 0.5

    menu:
        "Watch their faces.":
            thought "I watch their faces."
            pause 0.3
            thought "Mina — delighted."
            pause 0.3
            thought "Denki — terrified and excited at the same time."
            pause 0.3
            thought "Iida — already composing a formal complaint."
            pause 0.3
            thought "Bakugo — suspicious."
            pause 0.3
            thought "Izuku — writing in his notebook."
            pause 0.4
            thought "..."
            pause 0.3
            thought "I know all of them."
            pause 0.3
            thought "Every single one."
            pause 0.3
            thought "And none of them know me."
            pause 0.6

        "Look at Muichiro.":
            thought "I look at him."
            pause 0.3
            thought "He's looking at the class."
            pause 0.3
            thought "Cataloguing."
            pause 0.3
            thought "The way he always does."
            pause 0.3
            thought "Threat assessment."
            pause 0.3
            thought "Old habit."
            pause 0.3
            thought "He doesn't know that's what he's doing."
            pause 0.3
            thought "But I do."
            pause 0.6

        "Look at the room.":
            thought "The classroom."
            pause 0.3
            thought "Third floor."
            pause 0.3
            thought "Twenty seats."
            pause 0.3
            thought "Exactly where I knew they'd be."
            pause 0.4
            thought "..."
            pause 0.3
            thought "I've never been here before."
            pause 0.3
            thought "I shouldn't know this."
            pause 0.3
            thought "I shouldn't know any of this."
            pause 0.6

    thought "This place."
    pause 0.3
    thought "I know this place."
    pause 0.4
    thought "Not from being here."
    pause 0.3
    thought "From somewhere else."
    pause 0.5
    thought "Like I've seen it before."
    pause 0.4
    thought "On a screen."
    pause 0.5
    thought "..."
    pause 0.3
    thought "What's a screen."
    pause 1.0

    scene black
    with Fade(1.0, 0.5, 1.5)

    jump arrival_scene
