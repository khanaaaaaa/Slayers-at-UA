# img
image black_vortex = Solid("#000000")
image bg sky="sky.png"
image bg street="mhastreet.png"

# transition
define wipe = ImageDissolve("black", 0.5, 32)
define snap = vpunch
define cut = MoveTransition(0.4)
transform fall_into_hole:
    yalign 0.5
    zoom 1.0
    alpha 1.0

    linear 0.4 yoffset 600 alpha 0.0 zoom 0.7

# start

label start:
    scene black
    with fade
    "Mui... I really hate the color red..."
    crowyn "CAW! CAW!"
    crowyn "KASUGAI CROW REPORT! NEW MISSION - SOUTHERN DISTRICT!"
    menu:
        "Understood.":
            "You immediately move toward the location."
        "Am I assigned a partner?":
            crowyn "TOKITO MUICHIRO WILL ACCOMPANY YOU."
            "...A Hashira. This should be quick."
    # Mission Site
    scene bg forest_night with fade
    "Moon Breathing, 3rd form.. Lunar Rings."
    show demon1 at center
    pause 0.5
    show slash_effect at center
    with vpunch
    hide slash_effect
    hide demon1
    "...Too easy."
    demon2 "Ara~ How dissapointing."
    demon2 "And here I thought I'd find something entertaining..."
    show demon2 at center
    "You step back."
    "Moon Breathing, Eleventh Form~"
    demon2 "So reckless."
    mui "Mist breathing, Fifth for... Sea of Clouds and Haze."
    show slash_effect at center
    with vpunch
    hide slash_effect
    hide demon2
    "The air stills."
    "You exhale slowly."
    "...Tokito Muichiro"
    mui "I think I've seen you before."
    mui "What was your name again?"
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Y/N"
    yn "It's [player_name]."
    mui "Right."
    mui "You're slower than I remember."
    yn "And you haven't changed at all."
    mui "That's because I don't need to."
    play sound "teleport.wav"
    show demon2 at center:
        alpha 0.0
        linear 0.1 alpha 1.0
    show black_vortex
    with Dissolve(0.1)
    demon2 "Dd you really think this was over?"
    mui "...!"
    "The ground beneath you fractures."
    show mui at fall_into_hole
    with vpunch
    play sound "void.wav"
    scene white with Fade(0.1, 0.0, 0.3, color="#fff")
    scene bg street with fade
    #Aizawa
    "Aizawa Shota was doing his night patrol when he saw two kids lying on the cold floor"
    aizawa "I wonder if they're cosplaying or something."
    yn "Where am I? Didn't I die?"
    mui "Loud as ever"
    yn "Muichiro-san, I tho- I thought you died!"
    mui "I'm not that weak."
    aizawa "Okay kids, tell me what's going on"
    yn "Who's this old man?"
    aizawa "Old man?"
    yn "Who are you?"
    yn "I asked who are YOU?"
    aizawa "Calm down, I just have some questions."
    aizawa "Where did you come from?"
    mui "We were in a mission."
    aizawa "What is the mission that you're talking about?"
    yn "We were battling a demon."
    aizawa "What is the demon you're taliking about"
    yn "A demon is a super strong creature that eats human."
    mui "We were fighting an upper moon when we suddenly ended up here."
    mui "We are hashiras, basically the best at killing the demons."
    aizawa "Well we have something called quirks, basically powers that make us strong."
    aizawa "I'm a pro hero and I have never heard about any demons."
    mui "I think we somehow transported into another world."
    yn "But how could a demon do that."
    aizawa "So I'm guessing you don't have a place to stay?"
    aizawa "I teach at a school called UA."
    aizawa "You are classified as threats and since you have no one here for you"
    aizawa "It's easy to look after you"
    yn "Threats? How?"
    mui "About that.."
    aizawa "Your friend over here was attacking everyone he saw."
    mui "Let us go home, old man!"
    #slashes the door open
    "S-stop riht there!"
    mui "Who the he-"
    yn "Who are you?"
    "I-I'm Izuku Midoriya!"
    izuku "U-uhm..you're not allowed to g-go inside the-"
    mui "Shut up weakilng!"
    yn "Excuse him.. what year is it right now?"
    izuku "It's 2023?"
    mui "What are you talking about!"
    yn "It almost feels like we're in anther world"
    "YOU, I HEARD YOU WERE STRONG!"
    "COME FIGHT ME!"
    mui "Who's he talking to, daikon-chan?"
    yn "I think he's talking to you.."
    izuku "His name in Bakugo, and he's a bit competitive..."
    bakugo "COME BATTLE ME IN THE ARENA IF YOU AREN'T A SACREDY CAT!"
    mui "Bet."
    #shows his sword or something
    bakugo "WHAT'S THAT STUPID THING!"
    mui "My weapon."
    bakugo "YOU'RE REALLY GOING TO FIGHT ME WITH THAT?"
    #explosins or sum
    mui "Demon!"
    #pins him or sum shi
    "HAH?!??!"
    aizawa "Knock it off you two!"
    yn "Shut up, old man!"
    aizawa "Come to UA, I promise I'll help you find your way home."
    mui "Seems like we have no choice either."
    yn "Treat us well, old man."
    aizawa "The principal made that decision."
    aizawa "He wants to meet you two."
    #office
    nezu "Pleased to meet you, Muichiro Tokito and yn"
    yn "IS THAT A TALKING MOUSE?"
    nezu "Nice to meet you too!"
    #class
    show aizawa at center
    aizawa "Everyone, we'll be having two new transfer students!"
    yn "Hello everyone! My name is yn"
    mina "Are you cosplaying or something?"
    denki "What's that?"
    yn "My katana."



    #goes to



    return