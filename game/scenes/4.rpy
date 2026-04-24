label arrival_scene:

    scene bg office at bg_fit
    with slow_dissolve

    show nezu at center_char
    with dissolve

    pause 0.5

    nezu "So."
    pause 0.3
    nezu "Two individuals with no registered quirks."
    pause 0.3
    nezu "No identification."
    pause 0.3
    nezu "No records of any kind."
    pause 0.4
    nezu "And swords."
    pause 0.5

    show muiquiet at left_char
    with dissolve

    hide muiquiet
    show muitalking at left_char

    mui "The swords are ours."

    hide muitalking
    show muiquiet at left_char

    nezu "Yes, I gathered."
    pause 0.4
    nezu "What I haven't gathered is where you came from."
    pause 0.5

    menu:
        "We don't know.":
            yn "...We don't know."
            pause 0.5
            nezu "..."
            pause 0.3
            nezu "Fascinating."
            pause 0.3
            nezu "You say that with complete sincerity."
            pause 0.4
            thought "Because it's true."
            pause 0.3
            thought "I know where I came from."
            pause 0.3
            thought "I just don't know how to say it."
            pause 0.4
            thought "And I don't know if saying it would make things better."
            pause 0.4
            thought "Or much, much worse."
            pause 0.6

        "Somewhere you've never heard of.":
            yn "...Somewhere you've never heard of."
            pause 0.4
            nezu "..."
            pause 0.3
            nezu "I've heard of quite a lot of places."
            pause 0.3
            yn "Not this one."
            pause 0.4
            nezu "..."
            pause 0.3
            nezu "That's either very honest or very evasive."
            pause 0.4
            thought "Both."
            pause 0.3
            thought "Definitely both."
            pause 0.6

        "Somewhere that doesn't exist here.":
            yn "...Somewhere that doesn't exist here."
            pause 0.5
            nezu "..."
            pause 0.4
            nezu "Now that is interesting."
            pause 0.3
            nezu "Most people who don't want to answer say they don't remember."
            pause 0.3
            nezu "You said it doesn't exist."
            pause 0.3
            nezu "That's a very specific kind of answer."
            pause 0.5
            thought "..."
            pause 0.3
            thought "He noticed."
            pause 0.3
            thought "Of course he noticed."
            pause 0.3
            thought "He notices everything."
            pause 0.6

        "Ask Muichiro.":
            yn "...Ask him."
            pause 0.4
            hide muiquiet
            show muitalking at left_char
            mui "..."
            pause 0.3
            mui "We were fighting a demon."
            pause 0.3
            mui "Then we were here."
            pause 0.3
            mui "That's all I know."
            hide muitalking
            show muiquiet at left_char
            pause 0.4
            nezu "..."
            pause 0.3
            nezu "Concise."
            pause 0.3
            nezu "I appreciate that."
            pause 0.6

    nezu "Well."
    pause 0.3
    nezu "You'll stay here for now."
    pause 0.3
    nezu "Under observation."
    pause 0.3
    nezu "Aizawa will supervise."
    pause 0.4

    show aizawa at right_char
    with dissolve

    aizawa "..."
    pause 0.3
    aizawa "Lucky me."
    pause 0.5

    nezu "You'll attend classes."
    pause 0.3
    nezu "Integrate."
    pause 0.3
    nezu "And hopefully not destabilize anything."
    pause 0.4

    thought "..."
    pause 0.3
    thought "Too late."
    pause 0.8

    menu:
        "We'll try.":
            yn "...We'll try."
            pause 0.4
            nezu "That's all I ask."
            pause 0.3
            aizawa "..."
            pause 0.3
            aizawa "It's not."
            pause 0.3
            aizawa "But it's a start."
            pause 0.6

        "What does integrate mean exactly.":
            yn "...What does integrate mean exactly."
            pause 0.4
            nezu "Attend classes."
            pause 0.3
            nezu "Don't use your swords on students."
            pause 0.3
            nezu "Try not to know things you shouldn't know."
            pause 0.4
            thought "..."
            pause 0.3
            thought "That last one."
            pause 0.3
            thought "He said it casually."
            pause 0.3
            thought "But he was looking at me when he said it."
            pause 0.6

        "What if we can't.":
            yn "...What if we can't."
            pause 0.5
            nezu "..."
            pause 0.4
            nezu "Then we'll deal with that when it happens."
            pause 0.3
            nezu "I find it's better not to borrow trouble."
            pause 0.4
            aizawa "..."
            pause 0.3
            aizawa "You're already trouble."
            pause 0.3
            aizawa "Both of you."
            pause 0.6

        "Say nothing.":
            thought "..."
            pause 0.3
            thought "I don't say anything."
            pause 0.3
            thought "Because I don't know what to say."
            pause 0.3
            thought "Because I know exactly what's coming."
            pause 0.3
            thought "And I don't know if I can stop it."
            pause 0.3
            thought "Or if I should."
            pause 0.6

    hide nezu
    hide aizawa

    scene black
    with soft_dissolve

    pause 0.6

    thought "The classroom is on the third floor."
    pause 0.3
    thought "Twenty seats."
    pause 0.3
    thought "Arranged in rows."
    pause 0.3
    thought "Bakugo sits near the back."
    pause 0.3
    thought "Izuku sits near the front."
    pause 0.4
    thought "..."
    pause 0.3
    thought "I haven't been there yet."
    pause 0.4
    thought "I shouldn't know that."
    pause 0.5
    thought "..."
    pause 0.3
    thought "Stop."
    pause 0.8

    scene bg classroom at bg_fit
    with slow_dissolve

    show aizawa at left_char
    with dissolve

    pause 0.5

    aizawa "Two transfer students."
    pause 0.4
    aizawa "They'll be joining Class 1A temporarily."
    pause 0.3
    aizawa "Don't make it weird."
    pause 0.5

    show muiquiet at right_char
    with dissolve

    pause 0.4

    mina "Oh wow."
    pause 0.3
    mina "Are those real swords?"
    pause 0.3

    denki "That's so cool—"
    pause 0.3

    iida "Please refrain from bringing weapons onto school grounds without prior authorization—"
    pause 0.3

    bakugo "Tch."
    pause 0.3
    bakugo "What are they even doing here."
    pause 0.4

    thought "..."
    pause 0.3
    thought "There he is."
    pause 0.3
    thought "Exactly where I knew he'd be."
    pause 0.4
    thought "Exactly as loud as I knew he'd be."
    pause 0.5
    thought "..."
    pause 0.3
    thought "Don't react."
    pause 0.3
    thought "Don't let them see that you know them."
    pause 0.8

    yn "My name is [player_name]."
    pause 0.5

    hide muiquiet
    show muitalking at right_char

    mui "Muichiro Tokito."
    pause 0.3
    mui "Mist Hashira."
    pause 0.3
    mui "Former."

    hide muitalking
    show muiquiet at right_char

    pause 0.5

    kirishima "That's seriously manly!"
    pause 0.3

    hide muiquiet
    show muitalking at right_char

    mui "..."
    pause 0.3
    mui "I don't know what that means."

    hide muitalking
    show muiquiet at right_char

    pause 0.4

    thought "He means it literally."
    pause 0.3
    thought "He has no idea what manly means in this context."
    pause 0.3
    thought "And somehow that's the funniest thing I've heard in weeks."
    pause 0.4
    thought "..."
    pause 0.3
    thought "I don't laugh."
    pause 0.3
    thought "But I almost do."
    pause 0.8

    izuku "Um—"
    pause 0.3
    izuku "Your breathing form earlier."
    pause 0.3
    izuku "When Aizawa-sensei had you demonstrate."
    pause 0.3
    izuku "I've never seen anything like it."
    pause 0.3
    izuku "Is it a quirk? Or a technique?"
    pause 0.4

    menu:
        "It's a technique.":
            hide muiquiet
            show muitalking at right_char
            mui "Technique."
            pause 0.3
            mui "Quirks don't exist where we're from."
            hide muitalking
            show muiquiet at right_char
            pause 0.4
            izuku "Where you're from—"
            pause 0.3
            thought "Don't."
            pause 0.3
            thought "Don't ask."
            pause 0.3
            thought "Please don't ask."
            pause 0.5
            aizawa "That's enough."
            pause 0.3
            aizawa "Sit down."
            pause 0.5
            thought "..."
            pause 0.3
            thought "Thank you."
            pause 0.6

        "Something like a quirk.":
            yn "...Something like a quirk."
            pause 0.3
            yn "But older."
            pause 0.3
            yn "And it costs more."
            pause 0.4
            izuku "Costs more how?"
            pause 0.4
            thought "..."
            pause 0.3
            thought "How do I explain breathing forms to someone who grew up with quirks."
            pause 0.3
            thought "How do I explain that the body can be trained past what it should be able to do."
            pause 0.3
            thought "That pain is a teacher."
            pause 0.3
            thought "That scars are a curriculum."
            pause 0.5
            yn "...It's hard to explain."
            pause 0.4
            izuku "I'd love to hear it sometime."
            pause 0.3
            thought "..."
            pause 0.3
            thought "He means it."
            pause 0.3
            thought "He always means it."
            pause 0.6

        "Let Muichiro answer.":
            yn "...Ask him."
            pause 0.4
            hide muiquiet
            show muitalking at right_char
            mui "..."
            pause 0.3
            mui "It's called Total Concentration Breathing."
            pause 0.3
            mui "You push oxygen through your entire body."
            pause 0.3
            mui "It enhances speed, strength, and perception."
            pause 0.3
            mui "Anyone can learn it."
            pause 0.3
            mui "Most people don't survive the training."
            hide muitalking
            show muiquiet at right_char
            pause 0.5
            denki "...Most people don't survive?"
            pause 0.3
            hide muiquiet
            show muitalking at right_char
            mui "Correct."
            hide muitalking
            show muiquiet at right_char
            pause 0.4
            thought "..."
            pause 0.3
            thought "He says it like it's a weather report."
            pause 0.3
            thought "Most people don't survive."
            pause 0.3
            thought "Correct."
            pause 0.6

        "Stay quiet.":
            thought "..."
            pause 0.3
            thought "I don't answer."
            pause 0.3
            thought "Because the answer is complicated."
            pause 0.3
            thought "Because the answer involves a world that shouldn't exist."
            pause 0.3
            thought "And a boy who was supposed to die in it."
            pause 0.3
            thought "And me."
            pause 0.3
            thought "Standing in the middle of both."
            pause 0.6

    scene bg dorms_hallway at bg_fit
    with soft_dissolve

    pause 0.5

    show tsuyu at left_char
    with dissolve

    tsuyu "You knew Midoriya was going to trip on the stairs."
    pause 0.4
    tsuyu "You caught him before he fell."
    pause 0.3
    tsuyu "Before anyone else even saw it coming."
    pause 0.5

    menu:
        "Instinct.":
            yn "...Instinct."
            pause 0.5
            tsuyu "..."
            pause 0.4
            tsuyu "You do that a lot."
            pause 0.3
            tsuyu "The instinct thing."
            pause 0.4
            tsuyu "It doesn't sound like instinct."
            pause 0.3
            tsuyu "It sounds like you already know what's going to happen."
            pause 0.5
            thought "..."
            pause 0.4
            thought "She's right."
            pause 0.3
            thought "She's completely right."
            pause 0.4
            thought "And she's saying it the way she says everything."
            pause 0.3
            thought "Flat. Honest. Without cruelty."
            pause 0.3
            thought "Which somehow makes it worse."
            pause 0.6

        "I read people well.":
            yn "...I read people well."
            pause 0.4
            tsuyu "..."
            pause 0.3
            tsuyu "Ribbit."
            pause 0.3
            tsuyu "That's not what that looked like."
            pause 0.4
            thought "..."
            pause 0.3
            thought "She's not going to let it go."
            pause 0.3
            thought "She never lets things go."
            pause 0.3
            thought "I know that about her."
            pause 0.3
            thought "I know too much about all of them."
            pause 0.6

        "Would you believe me if I told you.":
            yn "...Would you believe me if I told you?"
            pause 0.5
            tsuyu "..."
            pause 0.4
            tsuyu "Probably."
            pause 0.3
            tsuyu "I believe most things."
            pause 0.3
            tsuyu "Ribbit."
            pause 0.5
            thought "..."
            pause 0.3
            thought "I almost tell her."
            pause 0.4
            thought "Right there."
            pause 0.3
            thought "In the hallway."
            pause 0.4
            thought "I almost say all of it."
            pause 0.5
            thought "..."
            pause 0.3
            thought "But I don't."
            pause 0.4
            thought "Because I don't know what happens if I do."
            pause 0.4
            thought "And I've already changed too much."
            pause 0.6
            yn "...Maybe later."
            pause 0.5
            tsuyu "Okay."
            pause 0.3
            tsuyu "I'll be here."
            pause 0.5
            thought "..."
            pause 0.3
            thought "She means it."
            pause 0.3
            thought "She always means it."
            pause 0.6

        "I don't know how to explain it.":
            yn "...I don't know how to explain it."
            pause 0.4
            tsuyu "..."
            pause 0.3
            tsuyu "That's okay."
            pause 0.3
            tsuyu "You don't have to."
            pause 0.3
            tsuyu "I just wanted you to know I noticed."
            pause 0.5
            thought "..."
            pause 0.3
            thought "That's it."
            pause 0.3
            thought "No pressure."
            pause 0.3
            thought "Just — I noticed."
            pause 0.4
            thought "I don't know what to do with kindness that doesn't ask for anything."
            pause 0.6

    hide tsuyu

    scene bg training_ground at bg_fit
    with soft_dissolve

    play sound "wind.wav" fadein 1.0
    pause 0.5

    show bakugo at left_char
    with dissolve

    pause 0.4

    bakugo "Hey."
    pause 0.4

    yn "..."
    pause 0.3

    bakugo "You knew Deku was going to trip."
    pause 0.3
    bakugo "You knew Half-and-Half's left side runs hot."
    pause 0.3
    bakugo "You knew Dunce Face was going to short-circuit."
    pause 0.4
    bakugo "..."
    pause 0.3
    bakugo "You knew all of it before it happened."
    pause 0.5

    menu:
        "Say nothing.":
            yn "..."
            pause 0.5
            bakugo "..."
            pause 0.4
            bakugo "I don't know what your deal is."
            pause 0.3
            bakugo "But I'm watching you."
            pause 0.4
            thought "I know."
            pause 0.3
            thought "You always watch."
            pause 0.3
            thought "That's what you do."
            pause 0.4
            thought "You watch and you wait and you explode."
            pause 0.4
            thought "..."
            pause 0.3
            thought "Don't say that."
            pause 0.6

        "Okay.":
            yn "...Okay."
            pause 0.5
            bakugo "..."
            pause 0.4
            bakugo "That's it? Just okay?"
            pause 0.4
            yn "What do you want me to say?"
            pause 0.5
            bakugo "..."
            pause 0.4
            bakugo "Something that makes sense."
            pause 0.5
            thought "..."
            pause 0.3
            thought "I don't have that."
            pause 0.3
            thought "I haven't had that in a long time."
            pause 0.6
            yn "...I'll let you know when I find it."
            pause 0.6
            bakugo "..."
            pause 0.4
            bakugo "Tch."
            pause 0.5

        "You're not wrong to be suspicious.":
            yn "...You're not wrong to be suspicious."
            pause 0.5
            bakugo "..."
            pause 0.4
            bakugo "I know I'm not."
            pause 0.3
            bakugo "So what is it."
            pause 0.4
            yn "...I can't tell you."
            pause 0.3
            yn "Not yet."
            pause 0.4
            bakugo "..."
            pause 0.3
            bakugo "Not yet."
            pause 0.3
            bakugo "So there's a yet."
            pause 0.4
            thought "..."
            pause 0.3
            thought "He caught that."
            pause 0.3
            thought "Of course he caught that."
            pause 0.3
            thought "He catches everything."
            pause 0.6

        "I could ask you the same thing.":
            yn "...I could ask you the same thing."
            pause 0.5
            bakugo "..."
            pause 0.4
            bakugo "What."
            pause 0.3
            yn "You watch everyone."
            pause 0.3
            yn "You catalogue weaknesses."
            pause 0.3
            yn "You're always three steps ahead."
            pause 0.4
            bakugo "..."
            pause 0.4
            bakugo "That's called being prepared."
            pause 0.4
            yn "So is what I do."
            pause 0.5
            bakugo "..."
            pause 0.5
            bakugo "Tch."
            pause 0.4
            thought "..."
            pause 0.3
            thought "He doesn't have an answer for that."
            pause 0.3
            thought "Good."
            pause 0.6

    hide bakugo

    pause 0.6

    thought "..."
    pause 0.3
    thought "He's not wrong to watch me."
    pause 0.4
    thought "I would watch me too."
    pause 0.8

    scene black
    with soft_dissolve

    pause 0.8

    jump dorms_scene
