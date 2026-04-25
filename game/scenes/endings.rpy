## ════════════════════════════════════════════════════════════════
##  ENDINGS
##  Bad endings branch from choices in scenes 1-6.
##  ending_fade_out  — Y/N stays in the river. She fades.
##  ending_forgotten — Muichiro forgets her completely. She vanishes.
##  ending_truth     — Y/N tells everyone the truth. It breaks things.
## ════════════════════════════════════════════════════════════════


## ── BAD ENDING 1 ─────────────────────────────────────────────────
## Triggered from scene 6 memory_scene menu: "...stay."
## Y/N chooses to stay in the memory. She doesn't surface.
## She fades out of existence entirely.

label ending_fade_out:

    scene black
    with water_cut

    stop sound fadeout 2.0

    thought "..."
    thought "i stay."
    pause 0.5

    thought "the water is cold."
    thought "and then it isn't."
    thought "and then i can't feel anything."
    pause 0.5

    thought "..."
    thought "that's okay."
    thought "i think."
    thought "i'm tired of feeling things anyway."
    pause 0.6

    thought "i wonder if he'll notice."
    thought "when i'm gone."
    thought "i wonder if there'll be a moment where he looks up"
    thought "and something feels wrong"
    thought "and he doesn't know why."
    pause 0.6

    thought "probably not."
    thought "that's the thing about being forgotten."
    thought "it doesn't announce itself."
    thought "it just."
    thought "stops."
    pause 0.8

    scene black
    with end_fade

    pause 1.5

    centered "{size=28}{color=#888888}she stayed.{/color}{/size}"
    pause 0.5
    centered "{size=22}{color=#555555}and the forest forgot her name.{/color}{/size}"
    pause 1.0

    return


## ── BAD ENDING 2 ─────────────────────────────────────────────────
## Triggered if the player consistently pushes Muichiro away
## across scenes 5-7 (call this label from anchor_scene if needed).
## He forgets her. She vanishes mid-scene.

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

    thought "..."
    thought "There it is."
    thought "The thing I was afraid of."
    thought "Said out loud."
    thought "Casually."
    thought "Like it's nothing."
    pause 0.6

    yn "...Yes."
    pause 0.4

    hide muiquiet
    show muitalking at center_char
    mui "..."
    mui "I don't think so."
    mui "I'm sorry."
    hide muitalking
    show muiquiet at center_char

    thought "He's not being cruel."
    thought "That's the worst part."
    thought "He's just telling the truth."
    pause 0.6

    thought "I can feel it."
    thought "The edges of me."
    thought "Going soft."
    thought "Like paper left in water."
    pause 0.5

    thought "..."
    thought "I look at my hands."
    thought "I can see through them."
    pause 0.5

    thought "okay."
    thought "okay."
    thought "i knew this was possible."
    thought "i just thought—"
    thought "i thought i had more time."
    pause 0.6

    scene black
    with Fade(2.0, 1.0, 3.0)

    stop music fadeout 3.0

    pause 1.0

    centered "{size=28}{color=#888888}he forgot.{/color}{/size}"
    pause 0.5
    centered "{size=22}{color=#555555}and she went with it.{/color}{/size}"
    pause 1.0

    return


## ── BAD ENDING 3 ─────────────────────────────────────────────────
## Triggered if Y/N tells Aizawa everything in scene 3/4.
## The truth destabilizes the world. She's removed from it.

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
    pause 0.3

    yn "...Yes."
    pause 0.4

    aizawa "To the students."
    pause 0.3

    yn "...Yes."
    pause 0.4

    aizawa "To me."
    pause 0.4

    yn "..."
    pause 0.5

    yn "...Yes."
    pause 0.6

    aizawa "..."
    aizawa "Then you understand why I can't let you stay."
    pause 0.5

    thought "..."
    thought "I knew this was a possibility."
    thought "I knew it the moment I decided to say it."
    thought "Some truths are too heavy for the world they land in."
    pause 0.6

    yn "...I know."
    pause 0.4

    aizawa "I'm sorry."
    pause 0.4

    thought "He means it."
    thought "That's the thing about him."
    thought "He always means it."
    pause 0.5

    scene black
    with guilt_fade

    thought "They found a way to send me back."
    thought "Or somewhere."
    thought "I'm not sure it's the same place."
    thought "I'm not sure it matters."
    pause 0.6

    thought "I didn't get to say goodbye to him."
    thought "He wouldn't have remembered it anyway."
    thought "..."
    thought "That doesn't make it better."
    pause 0.6

    scene black
    with end_fade

    pause 1.5

    centered "{size=28}{color=#888888}she told the truth.{/color}{/size}"
    pause 0.5
    centered "{size=22}{color=#555555}the world couldn't hold it.{/color}{/size}"
    pause 1.0

    return
