label ending_fade_out:

    scene black
    with water_cut

    stop sound fadeout 2.0

    thought "i stay."
    pause 0.5

    thought "the water is cold."
    thought "and then it isn't."
    thought "and then i can't feel anything."
    pause 0.5

    thought "that's okay. i think."
    thought "i'm tired of feeling things anyway."
    pause 0.6

    thought "i wonder if he'll notice when i'm gone."
    thought "i wonder if there'll be a moment where he looks up"
    thought "and something feels wrong"
    thought "and he doesn't know why."
    pause 0.6

    thought "probably not."
    thought "that's the thing about being forgotten."
    thought "it doesn't announce itself."
    thought "it just stops."
    pause 0.8

    scene black
    with end_fade

    pause 1.5

    centered "{size=26}{color=#888888}ending: she stayed.{/color}{/size}"
    pause 0.5
    centered "{size=20}{color=#555555}the forest forgot her name.{/color}{/size}"
    pause 0.5
    centered "{size=16}{color=#333344}she was the only one who knew where the good training spots were. this was a loss for everyone.{/color}{/size}"
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

    thought "there it is."
    thought "the thing i was afraid of."
    thought "said out loud. casually. like it's nothing."
    pause 0.6

    yn "...Yes."
    pause 0.4

    hide muiquiet
    show muitalking at center_char
    mui "I don't think so."
    mui "I'm sorry."
    hide muitalking
    show muiquiet at center_char

    thought "he's not being cruel."
    thought "that's the worst part."
    thought "he's just telling the truth."
    pause 0.5

    thought "i can feel it. the edges of me going soft."
    thought "like paper left in water."
    pause 0.5

    thought "i look at my hands."
    thought "i can see through them."
    pause 0.5

    thought "okay. okay."
    thought "i knew this was possible."
    thought "i just thought i had more time."
    pause 0.6

    scene black
    with Fade(2.0, 1.0, 3.0)

    stop music fadeout 3.0

    pause 1.0

    centered "{size=26}{color=#888888}ending: he forgot.{/color}{/size}"
    pause 0.5
    centered "{size=20}{color=#555555}and she went with it.{/color}{/size}"
    pause 0.5
    centered "{size=16}{color=#333344}he stood in the hallway for a while after. he didn't know why. he blamed low blood sugar.{/color}{/size}"
    pause 1.2

    return


label ending_truth:

    scene bg office at bg_fit
    with soft_dissolve

    show aizawa at left_char
    with dissolve

    pause 0.4

    aizawa "..."
    aizawa "Say that again."
    pause 0.4

    yn "I said — I know this world."
    yn "I know all of you."
    yn "Because where I came from, you were fiction."
    yn "A story. That I read."
    pause 0.5

    aizawa "..."
    pause 0.5

    aizawa "You know what happens."
    yn "...Yes."
    aizawa "To the students."
    yn "...Yes."
    aizawa "To me."
    pause 0.4

    yn "..."
    yn "...Yes."
    pause 0.6

    aizawa "..."
    aizawa "Then you understand why I can't let you stay."
    pause 0.5

    thought "i knew this was a possibility."
    thought "i knew it the moment i decided to say it."
    thought "some truths are too heavy for the world they land in."
    pause 0.5

    yn "...I know."
    pause 0.4

    aizawa "I'm sorry."
    pause 0.4

    thought "he means it. that's the thing about him."
    thought "he always means it."
    pause 0.5

    scene black
    with guilt_fade

    thought "they found a way to send me back."
    thought "or somewhere. i'm not sure it's the same place."
    thought "i'm not sure it matters."
    pause 0.5

    thought "i didn't get to say goodbye to him."
    thought "he wouldn't have remembered it anyway."
    thought "that doesn't make it better."
    pause 0.6

    scene black
    with end_fade

    pause 1.5

    centered "{size=26}{color=#888888}ending: she told the truth.{/color}{/size}"
    pause 0.5
    centered "{size=20}{color=#555555}the world couldn't hold it.{/color}{/size}"
    pause 0.5
    centered "{size=16}{color=#333344}nezu said 'fascinating' one more time on her way out. she did not find this comforting.{/color}{/size}"
    pause 1.2

    return
