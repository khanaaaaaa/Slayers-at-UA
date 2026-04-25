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

    thought "—water—"
    thought "—cold, so cold—"
    thought "—can't breathe—"
    thought "—sinking—"
    thought "—did I jump—"
    thought "—or did I fall—"
    pause 0.4

    scene black
    with hard_cut

    thought "I don't remember. I never remember that part."
    pause 0.8

    scene bg street at bg_fit
    with slow_dissolve

    play sound "city_ambience.wav" fadein 1.5
    pause 0.5

    thought "Too bright. The sky—"
    thought "...it's wrong."
    thought "No. It's just different."
    thought "You've seen worse. Haven't you?"
    thought "I don't remember."
    pause 0.8

    show muiquiet at center_char
    with dissolve

    hide muiquiet
    show muitalking at center_char
    mui "...Tch."
    mui "So you're alive."
    hide muitalking
    show muiquiet at center_char

    pause 0.4

    menu:
        "Barely.":
            yn "...Barely."
            hide muiquiet
            show muitalking at center_char
            mui "That's still alive."
            hide muitalking
            show muiquiet at center_char
            thought "He says it like it's a correction."
            thought "Like barely doesn't count as a qualifier."
            thought "It absolutely counts as a qualifier."

        "Unfortunately.":
            yn "...Unfortunately."
            hide muiquiet
            show muitalking at center_char
            mui "Don't say that."
            hide muitalking
            show muiquiet at center_char
            thought "He said it fast. Like it bothered him."
            thought "Like he didn't want it to."
            thought "Interesting."

        "Yeah.":
            yn "...Yeah."
            hide muiquiet
            show muitalking at center_char
            mui "Good."
            hide muitalking
            show muiquiet at center_char
            thought "One word. Good."
            thought "I've been through a dimensional rift and he said good."
            thought "Okay."

    yn "...Where.. Where is this?"
    pause 0.3

    thought "The sky is too bright. It feels artificial."
    thought "Like something built to look like sky rather than actual sky."
    thought "...Why do I know the difference."
    pause 0.6

    hide muiquiet
    show muitalking at center_char
    mui "I don't know."
    hide muitalking
    show muiquiet at center_char

    thought "That answer shouldn't scare me. But it does."
    thought "He always has something. And right now he has nothing."
    thought "We're so cooked."
    pause 0.6

    show aizawa at left_char
    with dissolve

    aizawa "..You two are finally awake."
    pause 0.4

    menu:
        "How long were we out.":
            yn "..How long were we out?"
            aizawa "Three hours. Give or take."
            thought "Three hours. That's nothing."
            thought "I've been out longer after worse."
            thought "...Have I?"

        "Where are we.":
            yn "..Where are we."
            aizawa "Safe. For now."
            aizawa "That's all you need to know right now."
            thought "He says it like a professional."
            thought "Like he's done this before."
            thought "Talked to people who woke up somewhere wrong."
            thought "Which, honestly, probably."

        "Say nothing.":
            thought "I look at him. Dark clothes. Tired eyes."
            thought "The kind of tired that doesn't go away with sleep."
            thought "I know who he is. I know his name. I know his quirk."
            thought "I know his students."
            thought "...Don't say any of that."
            thought "That would be a weird thing to say."

    yn "..Who—"
    pause 0.3

    hide muiquiet
    show muitalking at center_char
    mui "..Not a demon."
    hide muitalking
    show muiquiet at center_char

    thought "...Oh no."
    pause 0.4

    yn "This isn't the South district."

    hide muiquiet
    show muitalking at center_char
    mui "No. It's not anywhere I recognize."
    hide muitalking
    show muiquiet at center_char

    yn "Muichiro.. look around."

    hide muiquiet
    show muitalking at center_char
    mui "I am. It's loud. Pointlessly loud."
    hide muitalking
    show muiquiet at center_char

    thought "He's not wrong."
    thought "There's a kid over there who just exploded something for fun."
    thought "Nobody reacted. This is just normal here."
    thought "This is fine. Everything is fine."
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
            hide muiquiet
            show muitalking at center_char
            mui "...Maybe."
            hide muitalking
            show muiquiet at center_char
            thought "He doesn't argue when he's not sure."
            thought "Which is new. Or maybe it isn't."
            thought "I genuinely can't tell anymore."

        "You're right.":
            yn "...You're right."
            hide muiquiet
            show muitalking at center_char
            mui "I usually am."
            hide muitalking
            show muiquiet at center_char
            thought "There it is. That flat certainty."
            thought "I missed it. I didn't know I missed it until just now."
            thought "That's embarrassing."

        "I don't know what I feel.":
            thought "Scared. Relieved. Both. Neither."
            thought "Something that doesn't have a name yet."
            thought "Probably several somethings."

    aizawa "Aizawa. Pro Hero."
    aizawa "You collapsed in the middle of the street."
    pause 0.4

    yn "Hero..?"

    thought "That word. I know that word."
    thought "But not from the Corps. From somewhere else."
    thought "Somewhere with tall buildings. And people who fly."
    thought "...Why do I know that."
    pause 0.6

    hide muiquiet
    show muitalking at center_char
    mui "That word doesn't exist where we're from."
    hide muitalking
    show muiquiet at center_char

    aizawa "That's becoming obvious."
    pause 0.3

    yn "We were fighting a demon."
    aizawa "...That again."
    pause 0.3

    hide muiquiet
    show muitalking at center_char
    mui "Upper Rank. I am a Hashira."
    hide muitalking
    show muiquiet at center_char

    pause 0.6

    aizawa "Either this is the worst coordinated lie I've heard.."
    aizawa "Or reality itself is malfunctioning."
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

    scene black
    with Fade(0.8, 0.3, 0.8)

    thought "We used to train under the same sky."
    thought "Same ground. Same silence."
    thought "This.. isn't that sky."
    pause 0.8

    scene bg street at bg_fit
    with slow_dissolve

    show muiquiet at center_char
    with dissolve

    show aizawa at left_char
    with dissolve

    yn "Do you recognize anything?"

    hide muiquiet
    show muitalking at center_char
    mui "No. But it feels.. wrong."
    hide muitalking
    show muiquiet at center_char

    thought "I don't like the sound of that."
    pause 0.5

    yn "You used to say every place had a 'breathing rhythm'."

    hide muiquiet
    show muitalking at center_char
    mui "..Did I?"
    hide muitalking
    show muiquiet at center_char

    yn "Yes. You said you could hear it when you stopped talking."

    hide muiquiet
    show muitalking at center_char
    mui "This place doesn't have one."
    hide muitalking
    show muiquiet at center_char

    thought "A place with no breathing rhythm."
    thought "He used to say those were the dangerous ones."
    thought "The ones that had already forgotten how to be alive."
    thought "Cool. Great. We're in one of those."
    pause 0.6

    aizawa "You don't have anywhere to go."
    pause 0.3

    menu:
        "No.":
            yn "No."
            hide muiquiet
            show muitalking at center_char
            mui "No."
            hide muitalking
            show muiquiet at center_char
            thought "We said no at the same time."
            thought "That's either sweet or deeply sad."

        "Not here.":
            yn "...Not here."
            aizawa "Somewhere else then."
            yn "...Somewhere that doesn't exist anymore."
            thought "Or maybe it does. I don't know."
            thought "I don't know if the KNY world still exists."
            thought "Or if I left it behind completely."
            thought "I try not to think about that."

        "We had somewhere.":
            yn "...We had somewhere."
            hide muiquiet
            show muitalking at center_char
            mui "Past tense."
            hide muitalking
            show muiquiet at center_char
            thought "He noticed. He always notices the small things."
            thought "Even now. Even without the memories."
            thought "It's kind of annoying actually."

    aizawa "Then you're coming with me."
    pause 0.3

    hide muiquiet
    show muitalking at center_char
    mui "We don't trust strangers."
    hide muitalking
    show muiquiet at center_char

    aizawa "Then don't."
    aizawa "But you won't survive here alone."
    pause 0.6

    menu:
        "He's right.":
            thought "He's right. I know he's right."
            thought "I know exactly how dangerous this world is."
            thought "I know the villains. I know the threats."
            thought "I know things that haven't happened yet."
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

    hide muiquiet
    show muitalking at center_char
    mui "…Tch."
    hide muitalking
    show muiquiet at center_char

    yn "We'll go."
    pause 0.5

    scene bg ua_gate at bg_fit
    with slow_dissolve

    play sound "distant_city.wav" fadein 1.0
    pause 0.6

    thought "Everything feels too alive. And somehow… empty."
    pause 0.4

    hide muiquiet
    show muitalking at center_char
    mui "…So this is the new world."
    hide muitalking
    show muiquiet at center_char

    menu:
        "Yeah. And we're stuck in it.":
            yn "Yeah. And we're stuck in it."
            hide muiquiet
            show muitalking at center_char
            mui "Stuck implies we want to leave."
            hide muitalking
            show muiquiet at center_char
            thought "Do I want to leave."
            thought "I don't know what I'd go back to."
            thought "That's a question for later."
            thought "Much later."

        "It's not so different.":
            yn "...It's not so different."
            hide muiquiet
            show muitalking at center_char
            mui "It's completely different."
            hide muitalking
            show muiquiet at center_char
            yn "...The sky is still sky. The ground is still ground."
            hide muiquiet
            show muitalking at center_char
            mui "That's a very low bar."
            hide muitalking
            show muiquiet at center_char
            thought "He's right. It is."
            thought "I set a very low bar and he still cleared it."

        "I've been here before.":
            thought "I almost say it."
            thought "I know this gate. I know what's behind it."
            thought "I know the hallways. The classrooms. The names on the doors."
            thought "I know which vending machine is broken on the second floor."
            thought "I don't say any of that."
            thought "That would be a lot to explain."

    scene black
    with Fade(0.8, 0.3, 0.8)

    scene bg office at bg_fit
    with slow_dissolve

    show nezu at center_char
    with dissolve

    nezu "Interesting."
    nezu "A fractured connection across worlds.. fascinating!"
    pause 0.4

    menu:
        "Don't analyze it like that.":
            yn "Don't analyze it like that."
            nezu "How would you prefer I analyze it?"
            yn "...Like it happened to people. Not like a phenomenon."
            nezu "Fair. My apologies."
            thought "He apologized."
            thought "A small animal apologized to me."
            thought "This world is something else."

        "What do you know about it.":
            yn "...What do you know about it."
            nezu "Very little. Which is precisely what makes it fascinating."
            nezu "Gaps in my knowledge are rare. And therefore interesting."
            thought "He knows almost everything. Almost."
            thought "I know what fills the gap."
            thought "I'm not going to tell him that."

        "Say nothing.":
            thought "I let him talk. He will anyway."
            thought "Talks. Observes. Files things away."
            thought "I know that about him."
            thought "I know too much about all of them."
            thought "It's exhausting."

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
    pause 0.3

    thought "He said oh my."
    thought "Like a small animal just did something delightful."
    thought "We told him we fell through a dimensional rift."
    thought "He said oh my."
    thought "I don't know what I expected."
    pause 0.6

    scene bg classroom at bg_fit
    with slow_dissolve

    show aizawa at center_char
    with dissolve

    aizawa "Two transfer students."
    pause 0.4

    yn "My name is [player_name]."
    pause 0.3

    thought "Someone's going to ask about the sword."
    thought "And someone's going to ask if we're cosplayers."
    thought "...How do I know that."
    pause 0.5

    mina "Are you two like… cosplayers?"
    pause 0.3

    thought "...See."
    pause 0.4

    denki "That sword is REAL?!"
    pause 0.3

    show muiquiet at left_char
    with dissolve

    hide muiquiet
    show muitalking at left_char
    mui "It is."
    hide muitalking
    show muiquiet at left_char

    pause 0.4

    menu:
        "Watch their faces.":
            thought "Mina — delighted."
            thought "Denki — terrified and excited at the same time."
            thought "Iida — already composing a formal complaint in his head."
            thought "Bakugo — suspicious."
            thought "Izuku — writing in his notebook. He's been writing since we walked in."
            thought "I know all of them. Every single one."
            thought "And none of them know me."
            thought "That's a weird feeling."

        "Look at Muichiro.":
            thought "He's looking at the class. Cataloguing."
            thought "Threat assessment. Old habit."
            thought "He doesn't know that's what he's doing."
            thought "But I do."
            thought "Twenty people. He's already ranked them."

        "Look at the room.":
            thought "Third floor. Twenty seats."
            thought "Exactly where I knew they'd be."
            thought "I've never been here before."
            thought "I shouldn't know any of this."
            thought "And yet."

    thought "I know this place. Not from being here."
    thought "From somewhere else. Like I've seen it before."
    thought "On a screen."
    thought "..."
    thought "What's a screen."
    pause 0.8

    scene black
    with Fade(1.0, 0.5, 1.5)

    jump arrival_scene
