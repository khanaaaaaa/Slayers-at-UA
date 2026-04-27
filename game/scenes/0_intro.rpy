default route = "normal"

label game_intro:

    scene black
    with hard_cut

    pause 0.4

    centered "{size=30}{color=#7ecac3}Slayers at UA{/color}{/size}"
    pause 0.5

    centered "{size=22}{color=#aaaacc}Who are you in this situation?{/color}{/size}"
    pause 0.6

    menu:
        "The one who knows too much and says nothing.":
            $ route = "silent"
            centered "{size=20}{color=#7ecac3}Noted. You will suffer quietly and with dignity.{/color}{/size}"
            pause 0.7

        "The one who says too much at the wrong time.":
            $ route = "loud"
            centered "{size=20}{color=#7ecac3}Noted. You will cause several problems.{/color}{/size}"
            pause 0.7

        "The one who is just trying to get through the day.":
            $ route = "normal"
            centered "{size=20}{color=#7ecac3}Valid. Good luck.{/color}{/size}"
            pause 0.7

        "The one who read the manga and thinks they know everything.":
            $ route = "meta"
            centered "{size=20}{color=#7ecac3}Noted. You do know everything. It won't help.{/color}{/size}"
            pause 0.7

    scene black
    with hard_cut

    jump prologue_start
