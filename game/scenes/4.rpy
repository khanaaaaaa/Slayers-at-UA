label arrival_scene:

    scene bg office at bg_fit
    with slow_dissolve

    show nezu at center_char
    with dissolve

    pause 0.4

    nezu "So."
    nezu "Two individuals with no registered quirks."
    nezu "No identification. No records of any kind."
    nezu "And swords."
    pause 0.4

    show muiquiet at left_char
    with dissolve

    hide muiquiet
    show muitalking at left_char
    mui "The swords are ours."
    hide muitalking
    show muiquiet at left_char

    nezu "Yes, I gathered."
    nezu "What I haven't gathered is where you came from."
    pause 0.4

    menu:
        "We don't know.":
            yn "...We don't know."
            nezu "Fascinating. You say that with complete sincerity."
            thought "Because it's true."
            thought "I know where I came from. I just don't know how to say it."
            thought "And I don't know if saying it would make things better."
            thought "Or much, much worse."

        "Somewhere you've never heard of.":
            yn "...Somewhere you've never heard of."
            nezu "I've heard of quite a lot of places."
            yn "Not this one."
            nezu "That's either very honest or very evasive."
            thought "Both. Definitely both."

        "Somewhere that doesn't exist here.":
            yn "...Somewhere that doesn't exist here."
            nezu "Now that is interesting."
            nezu "Most people who don't want to answer say they don't remember."
            nezu "You said it doesn't exist."
            nezu "That's a very specific kind of answer."
            thought "He noticed. Of course he noticed. He notices everything."

        "Ask Muichiro.":
            yn "...Ask him."
            hide muiquiet
            show muitalking at left_char
            mui "We were fighting a demon. Then we were here."
            mui "That's all I know."
            hide muitalking
            show muiquiet at left_char
            nezu "Concise. I appreciate that."

    nezu "You'll stay here for now. Under observation."
    nezu "Aizawa will supervise."
    pause 0.3

    show aizawa at right_char
    with dissolve

    aizawa "..."
    aizawa "Lucky me."
    pause 0.4

    nezu "You'll attend classes. Integrate."
    nezu "And hopefully not destabilize anything."
    pause 0.3

    thought "...Too late."
    pause 0.6

    menu:
        "We'll try.":
            yn "...We'll try."
            nezu "That's all I ask."
            aizawa "It's not. But it's a start."

        "What does integrate mean exactly.":
            yn "...What does integrate mean exactly."
            nezu "Attend classes."
            nezu "Don't use your swords on students."
            nezu "Try not to know things you shouldn't know."
            thought "That last one."
            thought "He said it casually. But he was looking at me when he said it."

        "What if we can't.":
            yn "...What if we can't."
            nezu "Then we'll deal with that when it happens."
            nezu "I find it's better not to borrow trouble."
            aizawa "You're already trouble. Both of you."

        "Say nothing.":
            thought "I don't say anything."
            thought "Because I know exactly what's coming."
            thought "And I don't know if I can stop it. Or if I should."

    hide nezu
    hide aizawa

    scene black
    with soft_dissolve

    pause 0.5

    thought "The classroom is on the third floor. Twenty seats."
    thought "Bakugo sits near the back. Izuku sits near the front."
    thought "..."
    thought "I haven't been there yet. I shouldn't know that."
    thought "...Stop."
    pause 0.6

    scene bg classroom at bg_fit
    with slow_dissolve

    show aizawa at left_char
    with dissolve

    aizawa "Two transfer students."
    aizawa "They'll be joining Class 1A temporarily."
    aizawa "Don't make it weird."
    pause 0.4

    show muiquiet at right_char
    with dissolve

    mina "Oh wow. Are those real swords?"
    denki "That's so cool—"
    iida "Please refrain from bringing weapons onto school grounds without prior authorization—"
    bakugo "Tch. What are they even doing here."
    pause 0.3

    thought "There he is. Exactly where I knew he'd be."
    thought "Exactly as loud as I knew he'd be."
    thought "...Don't react. Don't let them see that you know them."
    pause 0.6

    yn "My name is [player_name]."
    pause 0.4

    hide muiquiet
    show muitalking at right_char
    mui "Muichiro Tokito."
    mui "Mist Hashira."
    mui "Former."
    hide muitalking
    show muiquiet at right_char

    kirishima "That's seriously manly!"
    pause 0.3

    hide muiquiet
    show muitalking at right_char
    mui "I don't know what that means."
    hide muitalking
    show muiquiet at right_char

    thought "He means it literally."
    thought "And somehow that's the funniest thing I've heard in weeks."
    thought "...I don't laugh. But I almost do."
    pause 0.6

    izuku "Your breathing form earlier — I've never seen anything like it."
    izuku "Is it a quirk? Or a technique?"
    pause 0.3

    menu:
        "It's a technique.":
            hide muiquiet
            show muitalking at right_char
            mui "Technique. Quirks don't exist where we're from."
            hide muitalking
            show muiquiet at right_char
            izuku "Where you're from—"
            thought "Don't. Don't ask. Please don't ask."
            aizawa "That's enough. Sit down."
            thought "...Thank you."

        "Something like a quirk.":
            yn "...Something like a quirk. But older. And it costs more."
            izuku "Costs more how?"
            thought "How do I explain that pain is a teacher."
            thought "That scars are a curriculum."
            yn "...It's hard to explain."
            izuku "I'd love to hear it sometime."
            thought "He means it. He always means it."

        "Let Muichiro answer.":
            yn "...Ask him."
            hide muiquiet
            show muitalking at right_char
            mui "Total Concentration Breathing."
            mui "You push oxygen through your entire body."
            mui "It enhances speed, strength, and perception."
            mui "Anyone can learn it."
            mui "Most people don't survive the training."
            hide muitalking
            show muiquiet at right_char
            denki "...Most people don't survive?"
            hide muiquiet
            show muitalking at right_char
            mui "Correct."
            hide muitalking
            show muiquiet at right_char
            thought "He says it like it's a weather report."
            thought "Most people don't survive. Correct."

        "Stay quiet.":
            thought "I don't answer."
            thought "Because the answer involves a world that shouldn't exist."
            thought "And a boy who was supposed to die in it."
            thought "And me. Standing in the middle of both."

    scene bg dorms_hallway at bg_fit
    with soft_dissolve

    pause 0.4

    show tsuyu at left_char
    with dissolve

    tsuyu "You knew Midoriya was going to trip on the stairs."
    tsuyu "You caught him before he fell."
    tsuyu "Before anyone else even saw it coming."
    pause 0.4

    menu:
        "Instinct.":
            yn "...Instinct."
            tsuyu "You do that a lot. The instinct thing."
            tsuyu "It doesn't sound like instinct."
            tsuyu "It sounds like you already know what's going to happen."
            thought "She's right. She's completely right."
            thought "Flat. Honest. Without cruelty."
            thought "Which somehow makes it worse."

        "I read people well.":
            yn "...I read people well."
            tsuyu "Ribbit. That's not what that looked like."
            thought "She's not going to let it go. She never lets things go."
            thought "I know that about her. I know too much about all of them."

        "Would you believe me if I told you.":
            yn "...Would you believe me if I told you?"
            tsuyu "Probably. I believe most things. Ribbit."
            thought "I almost tell her. Right there. In the hallway."
            thought "..."
            thought "But I don't."
            thought "Because I've already changed too much."
            yn "...Maybe later."
            tsuyu "Okay. I'll be here."
            thought "She means it. She always means it."

        "I don't know how to explain it.":
            yn "...I don't know how to explain it."
            tsuyu "That's okay. You don't have to."
            tsuyu "I just wanted you to know I noticed."
            thought "No pressure. Just — I noticed."
            thought "I don't know what to do with kindness that doesn't ask for anything."

    hide tsuyu

    scene bg training_ground at bg_fit
    with soft_dissolve

    play sound "wind.wav" fadein 1.0
    pause 0.4

    show bakugo at left_char
    with dissolve

    bakugo "Hey."
    pause 0.3

    yn "..."
    pause 0.3

    bakugo "You knew Deku was going to trip."
    bakugo "You knew Half-and-Half's left side runs hot."
    bakugo "You knew Dunce Face was going to short-circuit."
    bakugo "You knew all of it before it happened."
    pause 0.4

    menu:
        "Say nothing.":
            yn "..."
            bakugo "I don't know what your deal is."
            bakugo "But I'm watching you."
            thought "I know. You always watch."
            thought "You watch and you wait and you explode."
            thought "...Don't say that."

        "Okay.":
            yn "...Okay."
            bakugo "That's it? Just okay?"
            yn "What do you want me to say?"
            bakugo "Something that makes sense."
            thought "I don't have that. I haven't had that in a long time."
            yn "...I'll let you know when I find it."
            bakugo "Tch."

        "You're not wrong to be suspicious.":
            yn "...You're not wrong to be suspicious."
            bakugo "I know I'm not. So what is it."
            yn "...I can't tell you. Not yet."
            bakugo "Not yet. So there's a yet."
            thought "He caught that. Of course he caught that."
            thought "He catches everything."

        "I could ask you the same thing.":
            yn "...I could ask you the same thing."
            bakugo "What."
            yn "You watch everyone. You catalogue weaknesses."
            yn "You're always three steps ahead."
            bakugo "That's called being prepared."
            yn "So is what I do."
            bakugo "Tch."
            thought "He doesn't have an answer for that. Good."

    hide bakugo

    thought "He's not wrong to watch me. I would watch me too."
    pause 0.6

    scene black
    with soft_dissolve

    pause 0.6

    jump dorms_scene
