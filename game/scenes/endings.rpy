label ending_fade_out:

    scene black
    with water_cut

    stop sound fadeout 2.0

    thought "I stay."
    pause 0.5

    thought "The water is cold."
    thought "And then it isn't."
    thought "And then i can't feel anything."
    pause 0.5

    thought "That's okay. i think."
    thought "I'm tired of feeling things anyway."
    pause 0.6

    thought "I wonder if he'll notice when i'm gone."
    thought "I wonder if there'll be a moment where he looks up"
    thought "And something feels wrong"
    thought "And he doesn't know why."
    pause 0.6

    thought "Probably not."
    thought "That's the thing about being forgotten."
    thought "It doesn't announce itself."
    thought "It just stops."
    pause 0.8

    scene black
    with end_fade

    pause 1.5

    centered "{size=26}{color=#888888}Ending: She stayed.{/color}{/size}"
    pause 0.5
    centered "{size=20}{color=#555555}The forest forgot her name.{/color}{/size}"
    pause 0.5
    centered "{size=16}{color=#333344}She was the only one who knew where the good training spots were. This was a loss for everyone.{/color}{/size}"
    pause 1.2

    return


label ending_forgotten:

    scene bg rooftop at bg_fit
    with slow_dissolve

    play music "memory_theme.mp3" fadein 2.0
    pause 0.6

    show muiquiet at center_char
    with dissolve

    hide muiquiet
    show muitalking at center_char
    mui "..."
    mui "Sorry."
    mui "Do I know you?"
    hide muitalking
    show muiquiet at center_char

    pause 0.8

    thought "There it is."
    thought "The thing i was afraid of."
    thought "Casually, like it's nothing."
    pause 0.6

    yn "...Yes."
    pause 0.4

    hide muiquiet
    show muitalking at center_char
    mui "I don't think so."
    mui "I'm sorry."
    hide muitalking
    show muiquiet at center_char

    thought "He's not being cruel."
    thought "That's the worst part."
    pause 0.5

    thought "I can feel it. the edges of me going soft."
    thought "Like paper left in water."
    pause 0.5

    thought "I look at my hands."
    thought "I can see through them."
    pause 0.5

    thought "Okay, okay."
    thought "I knew this was possible."
    thought "I just thought i had more time."
    pause 0.6

    scene black
    with Fade(2.0, 1.0, 3.0)

    stop music fadeout 3.0

    pause 1.0

    centered "{size=26}{color=#888888}Ending: he forgot.{/color}{/size}"
    pause 0.5
    centered "{size=20}{color=#555555}And she went with it.{/color}{/size}"
    pause 0.5
    centered "{size=16}{color=#333344}He stood in the hallway for a while after. He didn't know why, so he blamed low blood sugar.{/color}{/size}"
    pause 1.2

    return


label ending_truth:

    scene bg office at bg_fit
    with soft_dissolve

    show aizawaquiet at center_char
    with dissolve

    pause 0.4



    aizawa "..."
    hide aizawaquiet
    show aizawatalking at center_char
    aizawa "Say that again."
    pause 0.4

    hide aizawatalking
    show yntalking at center_char

    yn "I said — I know this world."
    yn "I know all of you."
    yn "Because where I came from, you were fiction."
    yn "A story. That I read."
    pause 0.5

    hide yntalking
    show aizawaquiet at center_char

    aizawa "..."
    pause 0.5

    hide aizawa_quiet
    show aizawatalking at center_char

    aizawa "You know what happens."

    hide aizawatalking
    show aizawaquiet at center_char
    yn "...Yes."
    hide aizawaquiet
    show aizawatalking at center_char
    aizawa "To the students."
    hide aizawatalking
    show aizawaquiet at center_char
    yn "...Yes."
    hide aizawaquiet
    show aizawatalking at center_char
    aizawa "To me."
    pause 0.4

    hide aizawatalking
    show ynquiet at center_char
    yn "..."
    hide ynquiet
    show yntalking at center_char
    yn "...Yes."
    pause 0.6
    hide yntalking
    show aizawaquiet at center_char
    aizawa "..."
    hide aizawaquiet
    show aizawatalking at center_char
    aizawa "Then you understand why I can't let you stay."
    hide aizawatalking
    show aizawaquiet at center_char
    pause 0.5

    thought "I knew this was a possibility."
    thought "I knew it the moment i decided to say it."
    thought "Some truths are too heavy for the world they land in."
    pause 0.5

    hide aizawaquiet
    show yntalking at center_char

    yn "...I know."
    pause 0.4

    hide yntalking
    show aizawatalking at center_char

    aizawa "I'm sorry."
    hide aizawatalking
    show aizawaquiet at center_char
    pause 0.4

    thought "He means it. that's the thing about him."
    thought "He always means it."
    pause 0.5
    hide aizawaquiet

    scene black
    with guilt_fade

    thought "They found a way to send me back."
    thought "Or somewhere. i'm not sure it's the same place."
    thought "I'm not sure it matters."
    pause 0.5

    thought "I didn't get to say goodbye to him."
    thought "He wouldn't have remembered it anyway."
    thought "That doesn't make it better."
    pause 0.6

    scene black
    with end_fade

    pause 1.5

    centered "{size=26}{color=#888888}Ending: She told the truth.{/color}{/size}"
    pause 0.5
    centered "{size=20}{color=#555555}The world couldn't hold it.{/color}{/size}"
    pause 0.5
    centered "{size=16}{color=#333344}Nezu said 'fascinating' one more time on her way out. She did not find this comforting.{/color}{/size}"
    pause 1.2

    return
