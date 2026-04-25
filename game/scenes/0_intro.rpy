centered "{size=22}{color=#555566}loading your problems...{/color}{/size}"
pause 0.7

centered "{size=22}{color=#555566}wow. that's... a lot.{/color}{/size}"
pause 0.9

centered "{size=22}{color=#555566}loading his memory issues...{/color}{/size}"
pause 0.8

centered "{size=22}{color=#555566}...oh he has none. great. awesome. love that for us.{/color}{/size}"
pause 1.0

centered "{size=22}{color=#555566}loading one (1) sword...{/color}{/size}"
pause 0.6

centered "{size=22}{color=#555566}loading zero (0) explanations...{/color}{/size}"
pause 0.8

centered "{size=22}{color=#555566}so we're just doing things now. no context. just vibes.{/color}{/size}"
pause 1.0

centered "{size=22}{color=#aa4444}warning: plot coherence critically low{/color}{/size}"
pause 0.9

centered "{size=22}{color=#555566}don't worry. i'm sure it'll fix itself. it never does, but like... optimism.{/color}{/size}"
pause 1.2


scene black
with hard_cut

pause 0.5


centered "{size=30}{color=#7ecac3}slayers at UA{/color}{/size}"
pause 0.4

centered "{size=20}{color=#444455}a visual novel about memory loss, bad decisions,{/color}{/size}"
pause 0.3

centered "{size=20}{color=#444455}and a crossover nobody approved but we're here anyway{/color}{/size}"
pause 0.6

centered "{size=26}{color=#aaaacc}Before we begin{/color}{/size}"
pause 0.6
centered "{size=22}{color=#666677}Who are you in this situation?{/color}{/size}"
pause 0.8

menu:
    "The one who knows too much and says nothing.":
        $ route = "silent"
        centered "{size=20}{color=#7ecac3}noted. you will suffer quietly and with dignity.{/color}{/size}"
            pause 0.8
            centered "{size=18}{color=#444455}(this is the most painful route. congratulations.){/color}{/size}"
            pause 1.0

    "The one who says too much at the wrong time.":
            $ route = "loud"
            centered "{size=20}{color=#7ecac3}noted. you will cause several problems.{/color}{/size}"
            pause 0.8
            centered "{size=18}{color=#444455}(some of them are funny. most of them are not.){/color}{/size}"
            pause 1.0

    "The one who is just trying to get through the day.":
            $ route = "normal"
            centered "{size=20}{color=#7ecac3}noted. relatable. valid. good luck.{/color}{/size}"
            pause 0.8
            centered "{size=18}{color=#444455}(you will not have good luck.){/color}{/size}"
            pause 1.0

    "The one who read the manga and thinks they know everything.":
            $ route = "meta"
            centered "{size=20}{color=#7ecac3}noted. you do know everything.{/color}{/size}"
            pause 0.8
            centered "{size=18}{color=#444455}(it won't help.){/color}{/size}"
            pause 1.0

scene black
    with hard_cut

    pause 0.5

    centered "{size=22}{color=#555566}one more thing.{/color}{/size}"
    pause 0.6
    centered "{size=20}{color=#444455}this game contains:{/color}{/size}"
    pause 0.4
    centered "{size=18}{color=#333344}memory loss (his){/color}{/size}"
    pause 0.3
    centered "{size=18}{color=#333344}memory loss (yours, eventually){/color}{/size}"
    pause 0.3
    centered "{size=18}{color=#333344}one (1) demon who is way too philosophical{/color}{/size}"
    pause 0.3
    centered "{size=18}{color=#333344}class 1A being normal about nothing{/color}{/size}"
    pause 0.3
    centered "{size=18}{color=#333344}a river{/color}{/size}"
    pause 0.3
    centered "{size=18}{color=#333344}feelings{/color}{/size}"
    pause 0.5
    centered "{size=16}{color=#2a2a33}(the feelings are the worst part){/color}{/size}"
    pause 1.2

    scene black
    with hard_cut

    pause 0.5

    centered "{size=20}{color=#7ecac3}okay. let's go.{/color}{/size}"
    pause 0.8

    jump prologue_start