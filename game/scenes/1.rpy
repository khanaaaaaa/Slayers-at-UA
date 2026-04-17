label prologue_start:
    scene black with fade
    thought "...Red"
    thought "He used to say red was my color."
    thought "I guess people change."
    crownyn "CAW! CAW!"
    crownyn "KASUAI CROW REPORT! NEW MISSION - SOUTHERN DISTRICT!"

    menu:
        "Understood.":
            pass
        "...Is he coming?":
            crownyn "TOKITO MUICHIRO WILL ACCOMPANY YOU."
            thought "...Of course he is."
        jump mission_scene
