label dorms_scene:
    scene bg dorms_hallway at bg_fit
    with slow_dissolve

    play sound "wind_soft.wav" fadein 1.5
    pause 0.8

    thought "They gave us rooms."
    pause 0.4
    thought "Side by side."
    pause 0.3
    thought "Like they knew we'd want to stay close."
    pause 0.5
    thought "..."
    pause 0.3
    thought "Did I ask for that?"
    pause 0.4
    thought "I don't remember asking."
    pause 0.8

    show muiquiet at center_char
    with dissolve
    pause 0.5
    hide muiquiet
    show muitalking at center_char

    mui "...This place is strange."

    hide muitalking
    show muiquiet at center_char

    yn "Yeah"
    pause 0.4

    hide muiquiet
    show muitalking at center_char

    mui "...Do you know who we are?"

    hide muitalking
    show muiquiet at center_char
    pause 0.5

    thought "Yes."
    pause 0.3
    thought "No."
    pause 0.3
    thought "I don't know."
    pause 0.5
    thought "Both answers feel true."
    pause 0.8

    yn "...I don't think so."
    pause 0.5

    hide muiquiet
    show muitalking at center_char
    
    mui "You hesitated."

    hide muitalking
    show muiquiet at center_char

    yn "..."
    pause 0.6

    hide muiquiet
    show muitalking at center_char

    mui "...You do that a lot."
    pause 0.3
    mui "Like you're deciding what to say."
    pause 0.3
    mui "Instead of just saying it."

    hide muitalking
    show muiquiet at center_char

    pause 0.6

    thought "He's right."
    pause 0.3
    thought "I do."
    pause 0.4
    thought "Because I know too much."
    pause 0.3
    thought "And I don't know how."
    pause 0.8

    yn "...Sorry."
    pause 0.5

    hide muiquiet
    show muitalking at center_char

    mui "Don't apologize."
    pause 0.3
    mui "It's just strange."
    pause 0.4
    mui "...You feel familiar."

    hide muitalking
    show muiquiet at center_char

    pause 0.8

    thought "...What."
    pause 0.5

    yn "...Familiar?"
    pause 0.4

    hide muiquiet
    show muitalking at center_char

    mui "..."
    pause 0.3
    mui "I don't know."
    pause 0.3
    mui "Like I've met you before."
    pause 0.3
    mui "But I haven't."
    pause 0.4
    mui "...Have I?"

    hide muitalking
    show muiquiet at center_char

    pause 0.8

    thought "Yes."
    pause 0.3
    thought "In the forest."
    pause 0.3
    thought "Every day for weeks."
    pause 0.4
    thought "You told me you'd remember my name."
    pause 0.4
    thought "You didn't."
    pause 0.5
    thought "But you're starting to."
    pause 0.8

    yn "...I don't think so."
    pause 0.6

    hide muiquiet
    show muitalking at center_char

    mui "...Right."
    pause 0.4
    mui "That makes sense."

    hide muitalking
    show muiquiet at center_char

    pause 0.5

    thought "It doesn't."
    pause 0.3
    thought "None of this makes sense."
    pause 0.5
    thought "But I can't tell him that."
    pause 0.4
    thought "Because I don't know what's real anymore."
    pause 1.0

    scene bg classroom at bg_fit
    with soft_dissolve

    play sound "city_ambience.wav" fadein 1.0
    pause 0.6

    thought "Training starts today."
    pause 0.3
    thought "Soneone's going to challenge him."
    pause 0.3
    thought "The loud one with the red hair."
    pause 0.4
    thought "He'll say something about being manly."
    pause 0.5
    thought "..."
    pause 0.5
    thought "Why do I know that."
    pause 0.8

    show muiquiet at left_char
    with dissolve

    kirishima "Hey! You're the transfer, right?"
    pause 0.3
    kirishima "That sword that you used earlier was seriously manly!"
    pause 0.4

    thought "...See."
    pause 0.5
    thought "I knew it."
    pause 0.3
    thought "I always know."
    pause 0.5
    thought "And I don't know why."
    pause 0.8

    hide muiquiet
    show muitalking at left_char

    mui "...I'm not interested in being manly."

    hide muitalking
    show muiquiet at left_char

    mui "...I'm not interested in being manly."

    hide muitalking
    show muiquiet at left_char

    izuku "Kaminari said your breathing technique looked like a sword style he'd never seen before."
    pause 0.3
    izuku "Is it a martial art? A quirk application?"
    pause 0.4

    yn "...It's a breathing form."
    pause 0.3
    yn "We were trained in it."
    pause 0.5

    izuku "Trained where?"
    pause 0.4

    thought "..."
    pause 0.3
    thougth "Good question."
    pause 0.4
    thought "I know the answer."
    pause 0.3
    thought "It feels like something I read."
    pause 0.5
    thought "..."
    pause 0.3
    thought "Read."
    pause 0.3
    thought "Where."
    pause 0.8

    yn "...Somewhere far from here."
    pause 0.6

    thought "That's not a lie"
    pause 0.3
    thought "It's just not the whole truth."
    pause 0.8

    scene bg office at bg_fit
    with soft_dissolve

    show aizawa at left_char
    with dissolve

    pausse 0.5

    aizawa "You knew Kaminari was going to short-circuit during training."
    pause 0.4
    aizawa "You moved before it happened."
    pause 0.5

    yn "...Instinct"
    pause 0.5

    aizawa "You also knew Todoroki's left side rns hot."
    pause 0.3
    aizawa "You adjusted your stance efore he activated it."
    pause 0.5

    yn "...I read people well."
    pause 0.5

    aizawa "..."
    pause 0.4
    aizawa "You're not from another country."
    pause 0.4
    aizawa "Are you?"
    pause 0.5

    thought "No."
    pause 0.3
    thought "I'm from another world."
    pause 0.3
    thought "This world."
    pause 0.4
    thought "But not this version of it."
    pause 0.5
    thought "..."
    pause 0.3
    thought "I don't know how to say that."
    pause 0.8

    yn "...I don't know where I'm from."
    pause 0.5

    aizawa "..."
    pause 0.4
    aizawa "That's the most honest thing you've said."
    pause 0.8

    hide aizawa

    scene black
    with soft_dissolve
    pause 0.8
    jump rooftop_scene

label rooftop_scene:
    scene bg rooftop at bg_fit
    with slow_dissolve

    play music "night_calm.mp3" fadein 2.0
    pause 0.8

    thought "I came up here without thinking."
    pause 0.4
    thought "Like my body knew where to go."
    pause 0.5
    thought "..."
    pause 0.3
    thought "He's already here."
    pause 0.8

    show muiquiet at center_char
    with dissolve

    pause 0.6
    hide muiquiet
    show muitalking at center_char

    mui "...You came."

    hide muitalking 
    show muiquiet at center_char
    mui "...You came ."

    hide muitalking
    show muiquiet at center_char

    yn "...Did you know I would?"
    pause 0.5

    hide muiquiet
    show muitalking at center_char

    mui "...I don't know."
    pause 0.3
    mui "I just waited."

    hide muitalking
    show muiquiet at center_char

    pause 0.8

    thought "He waited."
    pause 0.3
    thought "For me."
    pause 0.3
    thought "Without knowing why."
    pause 0.5
    thought "That's not nothing."
    pause 0.8

    yn "...Do you remember anything?"
    pause 0.5

    hide muiquiet
    show muitalking at center_char

    mui "No."

    hide muitalking
    show muiquiet at center_char

    yn "Not even us?"
    pause 0.5

    mui "..."
    pause 0.4

    hide muiquiet 
    show muitalking at center_char

    mui "Should I?"

    hide muitalking
    show muiquiet at center_char

    pause 0.8

    thought "Yes."
    pause 0.3
    thought "You should remember the forest."
    pause 0.3
    thought "You should remember my name."
    pause 0.3
    thought "You should remember calling me Sparrow."
    pause 0.5
    thought "But you don't."
    pause 0.4
    thought "And I don't know if that's your fault."
    pause 0.3
    thought "Or mine."
    pause 1.0

    yn "...I don't know."
    pause 0.6

    hide muiquiet
    show muitalking at center_char

    mui "You're lying."

    hide muitalking
    show muiquiet at center_char

    yn "..."
    pause 0.6

    hide muiquiet
    show muitalking at center_char

    mui "You do that too."
    pause 0.3
    mui "You lie."
    pause 0.3
    mui "But not well."
    pause 0.4
    mui "...Why?"

    hide muitalking
    show muiquiet at center_char

    pause 0.8

    thought "Because I don't know what's true."
    pause 0.4

    thought "Because I don't know what's true."
    pause 0.4
    thought "Because I remember things that haven't happened yet."
    pause 0.4
    thought "Because I know you."
    pause 0.3
    thought "And I shouldn't."
    pause 0.8

    yn "...I don't know how to answer that."
    pause 0.6

    hide muiquiet
    show muitalking at center_char

    mui "..."
    pause 0.4
    mui "You're fading."

    hide muitalking
    show muiquiet at center_char

    pause 0.8

    yn "...What?"
    pause 0.5

    hide muiquiet
    show muitalking at center_char

    mui "Your hand."
    pause 0.3
    mui "It's... translucent."

    hide muitalking
    show muiquiet at center_char

    pause 0.6

    thought "No."
    pause 0.4
    thought "No no no."
    pause 0.3
    thought "Not yet."
    pause 0.4
    thought "I'm not ready."
    pause 0.8

    yn "...I'm fine."
    pause 0.5

    hide muiquiet
    show muitalking at center_char

    mui "You're not."
    pause 0.3
    mui "...What's happening to you?"

    hide muitalking
    show muiquiet at center_char

    pause 0.8

    thought "I'm being forgotten."
    pause 0.4
    thought "If no one remembers me—"
    pause 0.3
    thought "I stop existing."
    pause 0.5
    thought "..."
    pause 0.3
    thought "How do I know that."
    pause 0.8

    yn "...I don't know."
    pause 0.6

    hide muiquiet
    show muitalking at center_char

    mui "...Then remember."

    hide muitalking
    show muiquiet at center_char

    yn "...What?"
    pause 0.5

    hide muiquiet
    show muitalking at center_char

    mui "Whatever you're forgetting."
    pause 0.3
    mui "Remember it."
    pause 0.4
    mui "Before it's gone."

    hide muitalking
    show muiquiet at center_char

    pause 1.0

    thought "..."
    pause 0.4
    thought "He's right."
    pause 0.3
    thought "I have to remember."
    pause 0.4
    thought "Even if it hurts."
    pause 0.5
    thought "Even if I don't want to."
    pause 0.8

    scene black
    with Fade(1.0, 0.5, 1.5)

    jump memory_scene