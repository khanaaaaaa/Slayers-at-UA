label arrival_scene:

    scene bg office at bg_fit
    with slow_dissolve

    play music "nezu_theme.mp3" fadein 1.5

    show nezu at center_char
    with dissolve

    pause 0.4

    nezu "So."
    nezu "Two individuals with no registered quirks."
    nezu "No identification. No records of any kind."
    nezu "And swords."
    pause 0.4

    hide nezu
    show muichirotalking at center_char
    mui "The swords are ours."
    hide muichirotalking
    show nezu at center_char

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
            thought "Probably worse."

        "Somewhere you've never heard of.":
            yn "...Somewhere you've never heard of."
            nezu "I've heard of quite a lot of places."
            yn "Not this one."
            nezu "That's either very honest or very evasive."
            thought "Both. Definitely both."
            thought "I'm very good at both."

        "Somewhere that doesn't exist here.":
            yn "...Somewhere that doesn't exist here."
            nezu "Now that is interesting."
            nezu "Most people who don't want to answer say they don't remember."
            nezu "You said it doesn't exist."
            nezu "That's a very specific kind of answer."
            thought "He noticed. Of course he noticed."
            thought "He notices everything."
            thought "I hate that about him."
            thought "Respectfully."

        "Ask Muichiro.":
            hide nezu
            show muichiroquiet at center_char
            yn "...Ask him."
            hide muichiroquiet
            show muichirotalking at center_char
            mui "We were fighting a demon. Then we were here."
            mui "That's all I know."
            hide muichirotalking
            show nezu at center_char
            nezu "Concise. I appreciate that."
            thought "He gave the most accurate answer possible."
            thought "And somehow it sounds insane."

    nezu "You'll stay here for now. Under observation."
    nezu "Aizawa will supervise."
    pause 0.3
    hide nezu
    show aizawaquiet at center_char
    aizawa "..."
    hide aizawaquiet
    show aizawatalking at center_char
    aizawa "Lucky me."
    pause 0.4
    hide aizawatalking
    show nezu at center_char

    nezu "You'll attend classes. Integrate."
    nezu "And hopefully not destabilize anything."
    pause 0.3

    hide nezu
    show muichiroquiet at center_char

    thought "...Too late."
    pause 0.6

    menu:
        "We'll try.":
            yn "...We'll try."
            hide muichiroquiet
            show nezu at center_char
            nezu "That's all I ask."
            hide nezu 
            show aizawatalking at center_char
            aizawa "It's not. But it's a start."
            hide aizawatalking
            show aizawaquiet at center_char
            thought "I appreciate the participation trophy."

        "What does integrate mean exactly.":
            yn "...What does integrate mean exactly."
            hide muichiroquiet
            show nezu at center_char
            nezu "Attend classes."
            nezu "Don't use your swords on students."
            nezu "Try not to know things you shouldn't know."
            hide nezu
            show aizawaquiet at center_char
            thought "That last one."
            thought "He said it casually."
            thought "But he was looking at me when he said it."
            thought "He knows something. Or suspects something."
            thought "Either way I'm going to pretend I didn't notice."

        "What if we can't.":
            hide muichiroquiet
            show muichirotalking at center_char
            yn "...What if we can't."
            hide muichirotalking
            show nezu at center_char
            nezu "Then we'll deal with that when it happens."
            nezu "I find it's better not to borrow trouble."
            hide nezu
            show aizawatalking at center_char
            aizawa "You're already trouble. Both of you."
            hide aizawatalking
            show aizawaquiet at center_char
            thought "He said both of you."
            thought "Muichiro looks mildly offended."
            thought "Which is the most emotion I've seen from him today."

        "Say nothing.":
            hide muichiroquiet
            show aizawaquiet at center_char
            thought "I don't say anything."
            thought "Because I know exactly what's coming."
            thought "And I don't know if I can stop it."
            thought "Or if I should."
            thought "Or if stopping it would make things worse."
            thought "Probably worse."

    hide aizawaquiet
    scene black
    with soft_dissolve

    stop music fadeout 1.5
    pause 0.5

    thought "The classroom is on the third floor. Twenty seats."
    thought "Bakugo sits near the back. Izuku sits near the front."
    thought "I haven't been there yet. I shouldn't know that."
    thought "...Stop."
    pause 0.6

    scene bg classroom at bg_fit
    with slow_dissolve

    play music "class_1a.mp3" fadein 2.0

    show aizawatalking at center_char
    with dissolve

    aizawa "Two transfer students."
    aizawa "They'll be joining Class 1A temporarily."
    aizawa "Don't make it weird."
    pause 0.4
    hide aizawatalking
    show muichiroquiet at center_char
    with dissolve

    hide muichiroquiet
    show minatalking at center_char
    mina "Oh wow. Are those real swords?"
    hide minatalking
    show denki at center_char
    denki "That's so cool—"
    hide denki
    show iidatalking at center_char
    iida "Please refrain from bringing weapons onto school grounds without prior authorization—"
    pause 0.3
    thought "Iida has been talking for thirty seconds."
    thought "Muichiro has not blinked once."
    thought "I think Iida is kinda intimidated by that."
    pause 0.4
    hide iidatalking
    show bakugotalking at center_char

    bakugo "Tch. What are they even doing here."
    pause 0.3
    hide bakugotalking
    show bakugoquiet at center_char

    thought "There he is, exactly where I knew he'd be."
    thought "Exactly as loud as I knew he'd be."
    thought "...Don't let them see that you know them."
    pause 0.6

    yn "My name is [player_name]."
    pause 0.4

    hide bakugoquiet
    show muichirotalking at center_char
    mui "Muichiro Tokito."
    mui "Mist Hashira."
    mui "Former."
    hide muichirotalking
    show kirishimatalking at center_char

    kirishima "That's seriously manly!"
    pause 0.3

    hide kirishimatalking
    show muichirotalking at center_char
    mui "I don't know what that means."
    hide muichirotalking
    show muichiroquiet at center_char

    thought "He genuinely doesn't."
    thought "I watched him stare at a vending machine for forty seconds yesterday."
    thought "I don't know what he was thinking about."
    thought "I never know what he's thinking about."
    thought "He's so weird."
    pause 0.5

    hide muichiroquiet
    show dekutalking at center_char

    izuku "Your breathing form earlier... I've never seen anything like it."
    izuku "Is it a quirk? Or a technique?"
    pause 0.3
    hide dekutalking
    show dekuquiet at center_char


    menu:
        "It's a technique.":
            hide dekuquiet
            show muichirotalking at center_char
            mui "Technique. Quirks don't exist where we're from."
            hide muichirotalking
            show dekutalking at center_char
            izuku "Where you're from—"
            thought "Don't. Don't ask. Please don't ask."
            hide dekutalking
            show aizawatalking at center_char
            aizawa "That's enough. Sit down."
            hide aizawatalking
            show aizawaquiet at center_char
            thought "...Thank you."
            thought "I owe Aizawa one."

        "Something like a quirk.":
            yn "...Something like a quirk. But older. And it costs more."
            show dekutalking at center_char
            izuku "Costs more how?"
            hide dekutalking
            show dekuquiet at center_char
            thought "How do I explain that pain is a teacher."
            thought "That scars are a curriculum."
            thought "That you breathe until your lungs feel like they're tearing"
            thought "and then you breathe harder."
            yn "...It's hard to explain."
            hide dekuquiet
            show dekutalking at center_char
            izuku "I'd love to hear it sometime."
            hide dekutalking
            show aizawaquiet at center_char
            thought "He means it. He always means it."
            thought "He's going to write a twelve-page analysis."
            thought "I'm going to be in it."

        "Let Muichiro answer.":
            hide dekuquiet
            show muichiroquiet at center_char
            yn "...Ask him."
            hide muichiroquiet
            show muichirotalking at center_char
            mui "Total Concentration Breathing."
            mui "You push oxygen through your entire body."
            mui "It enhances speedand strength."
            mui "Anyone can learn it."
            mui "Most people don't survive the training."
            hide muichirotalking
            show denki at center_char
            denki "...Most people don't survive?"
            hide denki
            show muichirotalking at center_char
            mui "Correct."
            hide muichirotalking
            show aizawaquiet at center_char
            thought "He says it like it's a weather report."
            thought "Most people don't survive. Correct."
            thought "Denki looks like he's reconsidering his life choices."
            thought "Good."

        "Stay quiet.":
            hide dekuquiet
            show aizawaquiet at center_char
            thought "I don't answer."
            thought "Because the answer involves a world that shouldn't exist."
            thought "And a boy who was supposed to die in it."
            thought "And me. Standing in the middle of both."
            thought "That's a lot to explain before lunch."

    hide aizawaquiet

    stop music fadeout 2.0

    scene bg dorms_hallway at bg_fit
    with soft_dissolve

    pause 0.4

    show tsuyu at center_char
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
            thought "I'd prefer cruelty. Cruelty I can dismiss."

        "I read people well.":
            yn "...I read people well."
            tsuyu "Ribbit. That's not what that looked like."
            thought "She said ribbit."
            thought "And then immediately called me out."
            thought "I respect that absurdity."

        "Would you believe me if I told you.":
            yn "...Would you believe me if I told you?"
            tsuyu "Probably. I believe most things. Ribbit."
            thought "I almost tell her. Right there. In the hallway."
            thought "But I don't."
            thought "Because I've already changed too much."
            yn "...Maybe later."
            tsuyu "Okay. I'll be here."
            thought "She means it. She always means it."
            thought "That's either comforting or terrifying."
            thought "Both."

        "I don't know how to explain it.":
            yn "...I don't know how to explain it."
            tsuyu "That's okay. You don't have to."
            tsuyu "I just wanted you to know I noticed."
            thought "No pressure. Just — I noticed."
            thought "I don't know what to do with kindness that doesn't ask for anything."
            thought "It makes me want to sit down."

    hide tsuyu
    scene bg training_ground at bg_fit
    with soft_dissolve

    play sound "wind.wav" fadein 1.0
    pause 0.4

    show bakugotalking at center_char
    with dissolve

    bakugo "Hey."
    pause 0.3
    hide bakugotalking
    show bakugoquiet at center_char

    yn "..."
    pause 0.3

    hide bakugoquiet
    show bakugotalking at center_char

    bakugo "You knew Deku was going to trip."
    bakugo "You knew Half-and-Half's left side runs hot."
    bakugo "You knew Dunce Face was going to short-circuit."
    bakugo "You knew all of it before it happened."
    pause 0.4
    hide bakugotalking
    show bakugoquiet at center_char

    menu:
        "Say nothing.":
            yn "..."
            hide bakugoquiet
            show bakugotalking at center_char
            bakugo "I don't know what your deal is."
            bakugo "But I'm watching you."
            hide bakugotalking 
            show bakugoquiet at center_char
            thought "I know. You always watch."
            thought "You watch and you wait and you explode."
            thought "...Don't say that."
            thought "He would not take that well."

        "Okay.":
            yn "...Okay."
            hide bakugoquiet
            show bakugotalking at center_char
            bakugo "That's it? Just okay?"
            yn "What do you want me to say?"
            hide bakugotalking
            show bakugotalking at center_char
            bakugo "Something that makes sense."
            hide bakugotalking
            show bakugoquiet at center_char
            thought "I don't have that. I haven't had that in a long time."
            yn "...I'll let you know when I find it."
            hide bakugoquiet
            show bakugotalking at center_char
            bakugo "Tch."
            hide bakugotalking
            show bakugoquiet at center_char
            thought "He accepted that."
            thought "Somehow."

        "You're not wrong to be suspicious.":
            yn "...You're not wrong to be suspicious."
            hide bakugoquiet
            show bakugotalking at center_char
            bakugo "I know I'm not. So what is it."
            hide bakugotalking
            show bakugoquiet at center_char
            yn "...I can't tell you. Not yet."
            hide bakugoquiet
            show bakugotalking at center_char
            bakugo "Not yet. So there's a yet."
            hide bakugotalking
            show bakugoquiet at center_char
            thought "He caught that. Of course he caught that."
            thought "He catches everything."
            thought "It's annoying."

        "I could ask you the same thing.":
            yn "...I could ask you the same thing."
            hide bakugoquiet
            show bakugotalking at center_char
            bakugo "What."
            hide bakugotalking
            show bakugoquiet at center_char
            yn "You watch everyone. You catalogue weaknesses."
            yn "You're always three steps ahead."
            hide bakugoquiet
            show bakugotalking at center_char
            bakugo "That's called being prepared."
            hide bakugotalking
            show bakugoquiet at center_char
            yn "So is what I do."
            hide bakugoquiet
            show bakugotalking at center_char
            bakugo "Tch."
            hide bakugotalking
            show bakugoquiet at center_char
            thought "He walked away very aggressively."
            thought "The way you walk when you want someone to know you're thinking about them."
            thought "He would hate that I noticed that."

    hide bakugoquiet
    scene black
    with soft_dissolve

    thought "He's not wrong to watch me. I would watch me too."
    pause 0.6

    jump dorms_scene
