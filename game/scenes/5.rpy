label dorms_scene:

    scene bg dorms_hallway at bg_fit
    with slow_dissolve

    play sound "wind_soft.wav" fadein 1.5
    pause 0.6

    thought "They gave us rooms... side by side."
    thought "Like they knew we'd want to stay close."
    thought "...Did I ask for that? I don't remember asking."
    thought "I'm going to choose to believe I asked."
    pause 0.6

    show muichiroquiet at center_char
    with dissolve

    hide muichiroquiet
    show muichirotalking at center_char
    mui "...This place is strange."
    hide muichirotalking

    yn "Yeah."
    pause 0.3

    show muichirotalking at center_char
    mui "...Do you know where we are?"
    hide muichirotalking
    show muichiroquiet at center_char

    thought "Yes. No. I don't know."
    thought "Both answers feel true."
    thought "That's been happening a lot lately."
    pause 0.5

    hide muichiroquiet

    yn "...I don't think so."
    pause 0.4

    show muichirotalking at center_char
    mui "You hesitated."
    hide muichirotalking
    show muichiroquiet at center_char

    yn "..."
    pause 0.4

    hide muichiroquiet
    show muichirotalking at center_char
    mui "...You do that a lot."
    mui "Like you're deciding what to say instead of just saying it."
    hide muichirotalking
    show muichiroquiet at center_char

    thought "He's right. Because I know too much."
    thought "And I don't know how."
    thought "And if I just said things I'd say something like"
    thought "'you're going to call me Sparrow in about six months'"
    thought "and that would be a lot."
    pause 0.6

    yn "...Sorry."
    pause 0.4

    hide muichiroquiet
    show muichirotalking at center_char
    mui "Don't apologize."
    mui "It's just strange."
    mui "...You feel familiar."
    hide muichirotalking
    show muichiroquiet at center_char

    if route == "meta":
        thought "Of course I do."
        thought "I've been reading about you for years."
        thought "This is deeply weird and I'm handling it terribly."
    elif route == "loud":
        thought "I almost said 'yeah we met in a forest for weeks.'"
        thought "I didn't."
        thought "Barely."
        thought "It was close."
    else:
        thought "...What."
        pause 0.4

    yn "...Familiar?"
    pause 0.3

    hide muichiroquiet
    show muichirotalking at center_char
    mui "..."
    mui "Like I've met you before. But I haven't."
    mui "...Have I?"
    hide muichirotalking
    show muichiroquiet at center_char

    thought "Yes, in the forest. Every day for weeks."
    thought "You told me you'd remember my name... you didn't."
    thought "But you're starting to."
    thought "Which is either progress or a coincidence."
    thought "I'm choosing to believe it's progress."
    pause 0.6

    yn "...I don't think so."
    pause 0.4

    hide muichiroquiet
    show muichirotalking at center_char
    mui "...Right. That makes sense."
    hide muichirotalking
    show muichiroquiet at center_char

    thought "It doesn't. None of this makes sense."
    thought "But I can't tell him that."
    thought "Because I don't know what's real anymore."
    thought "And also because it would take a very long time to explain."
    pause 0.8
    hide muichiroquiet

    scene bg classroom at bg_fit
    with soft_dissolve

    play sound "city_ambience.wav" fadein 1.0
    pause 0.5


    thought "Training starts today."
    thought "Someone's going to challenge him. The loud one with the red hair."
    thought "He'll say something about being manly."
    thought "...Why do I know that."
    pause 0.6

    show kirishimatalking at center_char
    with dissolve

    kirishima "Hey! You're the transfer, right?"
    kirishima "That sword form you used earlier was seriously manly!"
    pause 0.3

    hide kirishimatalking
    show kirishimaquiet with center_char

    thought "...See. I knew."
    thought "I always know. And I don't know why."
    thought "Well. I do know why."
    thought "But I'm not thinking about that right now."
    pause 0.5

    hide kirishimaquiet
    show muichirotalking at center_char
    mui "...I'm not interested in being manly."
    hide muichirotalking
    show dekutalking at center_char

    izuku "Kaminari said your breathing technique looked like a sword style he'd never seen before."
    izuku "Is it a martial art? A quirk application?"
    pause 0.3
    hide dekutalking
    show dekuquiet at center_char

    yn "...It's a breathing form. We were trained in it."
    pause 0.3
    hide dekuqiet
    show dekutalking at center_char

    izuku "Trained where?"
    pause 0.3

    hide dekutalking
    show dekuquiet at center_char

    thought "Good question."
    thought "I know the answer. But it feels like something I read."
    thought "...Read. Where."
    thought "On a screen."
    thought "What's a screen."
    thought "I keep doing that."
    pause 0.6

    yn "...Somewhere far from here."
    pause 0.4

    thought "That's not a lie. It's just not the whole truth."
    thought "I'm getting good at that."
    pause 0.6

    hide dekuquiet

    scene bg office at bg_fit
    with soft_dissolve

    show aizawaquiet at center_char
    with dissolve

    pause 0.4

    hide aizawaquiet
    show aizawatalking at center_char

    aizawa "You knew Kaminari was going to short-circuit during training."
    aizawa "You moved before it happened."
    pause 0.3

    hide aizawatalking

    yn "...Instinct."
    pause 0.3

    show aizawatalking at center_char

    aizawa "You also knew Todoroki's left side runs hot."
    aizawa "You adjusted your stance before he activated it."
    pause 0.3

    hide aizawatalking

    yn "...I read people well."
    pause 0.3

    show aizawaquiet at center_char

    aizawa "..."

    hide aizawaquiet
    show aizawatalking at center_char
    aizawa "You're not from another country. Are you."
    pause 0.4
    hide aizawatalking
    show aizawaquiet at center_char

    thought "No. I'm from another world."
    thought "This world. But not this version of it."
    thought "...I don't know how to say that."
    thought "I've been trying to figure out how to say that for days."
    pause 0.6

    hide aizawaquiet

    yn "...I don't know where I'm from."
    pause 0.4

    show aizawaquiet at center_char

    aizawa "..."

    hide aizawaquiet
    show aizawatalking at center_char

    aizawa "That's the most honest thing you've said."
    pause 0.4

    hide aizawatalking
    show aizawaquiet at center_char

    thought "He's not wrong."
    thought "Everything else has been technically true."
    thought "But that one I actually meant."
    pause 0.6

    hide aizawaquiet

    scene black
    with soft_dissolve

    pause 0.6

    jump rooftop_scene


label rooftop_scene:

    scene bg rooftop at bg_fit
    with slow_dissolve

    play music "night_calm.mp3" fadein 2.0
    pause 0.6

    thought "I came up here without thinking."
    thought "Like my body knew where to go."
    thought "...He's already here."
    thought "Of course he is."
    pause 0.6

    show muichiroquiet at center_char
    with dissolve

    pause 0.4

    hide muichiroquiet
    show muichirotalking at center_char
    mui "...You came."
    hide muichirotalking
    show muichiroquiet at center_char

    yn "...Did you know I would?"
    pause 0.3

    hide muichiroquiet
    show muichirotalking at center_char
    mui "...I don't know. I just waited."
    hide muichirotalking
    show muichiroquiet at center_char

    thought "He waited... for me... without knowing why."
    thought "That's actually kind of a lot."
    thought "But I'm NOT going to say that out loud."
    pause 0.6

    yn "...Do you remember anything?"
    pause 0.3

    hide muichiroquiet
    show muichirotalking at center_char
    mui "No."
    hide muichirotalking
    show muichiroquiet at center_char

    yn "Not even us?"
    pause 0.4

    hide muichiroquiet
    show muichirotalking at center_char
    mui "Should I?"
    hide muichirotalking
    show muichiroquiet at center_char

    thought "Yes. You should remember the forest."
    thought "You should remember my name."
    thought "You should remember calling me Sparrow."
    thought "But you don't."
    thought "And I don't know if that's your fault. Or mine."
    thought "Probably mine."
    thought "Most things are."
    pause 0.8

    yn "...I don't know."
    pause 0.4

    hide muiquiet
    show muitalking at center_char
    mui "You're lying."
    hide muitalking
    show muiquiet at center_char

    yn "..."
    pause 0.4

    hide muiquiet
    show muitalking at center_char
    mui "You do that too. You lie. But not well."
    mui "...Why?"
    hide muitalking
    show muiquiet at center_char
    thoguht "Because I know things I shouldn't."
    thought "Because if I told you the truth you'd look at me like I'm a monster."
    thought "And I'm not ready for that."
    pause 0.6

    yn "...I don't know how to answer that."
    pause 0.4

    mui "..."
    hide muichiroquiet
    show muichirotalking at center_char
    mui "You're fading."
    hide muichirotalking
    show muichiroquiet at center_char

    hide muichiroquiet

    yn "...What?"
    pause 0.3

    show muitalking at center_char
    mui "Your hand. It's... translucent."
    hide muitalking
    show muiquiet at center_char

    thought "No. No no no. Not yet. I'm not ready."
    thought "I haven't even figured out the vending machine situation."
    pause 0.6

    hide muichiroquiet

    yn "...I'm fine."
    pause 0.3

    show muichirotalking at center_char
    mui "You're not."
    mui "...What's happening to you?"
    hide muichirotalking
    show muiciroquiet at center_char

    thought "I'm being forgotten."
    thought "If no one remembers me — I stop existing."
    thought "...How do I know that."
    thought "I just do. The same way I know everything."
    thought "Which is a terrible way to know things."
    pause 0.6

    yn "...I don't know."
    pause 0.4

    hide muichiroquiet
    show muichirotalking at center_char
    mui "...Then remember."
    hide muichirotalking
    show muichiroquiet at center_char

    yn "...What?"
    pause 0.3

    hide muichiroquiet
    show muichirotalking at center_char
    mui "Whatever you're forgetting."
    mui "Remember it. Before it's gone."
    hide muichirotalking
    show muichiroquiet at center_char

    thought "He's right... I have to remember."
    thought "Even if it hurts... even if I don't want to."
    thought "Even if what I remember is the reason I ended up in a river."
    pause 0.8

    scene black
    with Fade(1.0, 0.5, 1.5)

    jump memory_scene
