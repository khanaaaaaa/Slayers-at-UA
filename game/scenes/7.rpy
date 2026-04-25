label anchor_scene:

    scene bg rooftop at bg_fit
    with slow_dissolve

    play music "memory_theme.mp3" fadein 2.5
    pause 0.6

    thought "I came back up here."
    thought "He's here again. He's always here."
    thought "Even when he doesn't know why."
    pause 0.6

    show muiquiet at center_char
    with dissolve

    hide muiquiet
    show muitalking at center_char
    mui "...You look different."
    hide muitalking
    show muiquiet at center_char

    yn "...Different how?"

    hide muiquiet
    show muitalking at center_char
    mui "More solid."
    mui "Before you looked like you were... disappearing."
    hide muitalking
    show muiquiet at center_char

    thought "I was. I think I still am. Just slower now."
    pause 0.5

    yn "...I remembered something."

    hide muiquiet
    show muitalking at center_char
    mui "...What?"
    hide muitalking
    show muiquiet at center_char

    yn "Where I'm from. What I did. How I got here."
    pause 0.4

    hide muiquiet
    show muitalking at center_char
    mui "..."
    mui "Tell me."
    hide muitalking
    show muiquiet at center_char

    thought "He says it like it's simple."
    thought "Like the answer won't change anything."
    thought "It will."
    pause 0.5

    yn "...I'm from here. This world."
    yn "But not this version of it."
    pause 0.3

    hide muiquiet
    show muitalking at center_char
    mui "...What does that mean?"
    hide muitalking
    show muiquiet at center_char

    yn "Where I came from... you were a story."
    yn "The world you came from. The demons. The Hashira."
    yn "I knew it before I was ever there."
    yn "Because someone wrote it. And I read it."
    pause 0.5

    hide muiquiet
    show muitalking at center_char
    mui "..."
    mui "So you knew. Everything."
    hide muitalking
    show muiquiet at center_char

    yn "...Yes."
    pause 0.4

    hide muiquiet
    show muitalking at center_char
    mui "...You knew what would happen to me."
    hide muitalking
    show muiquiet at center_char

    thought "Yes. I knew exactly."
    pause 0.5

    yn "...Yes."
    pause 0.4

    hide muiquiet
    show muitalking at center_char
    mui "..."
    mui "And you changed it."
    hide muitalking
    show muiquiet at center_char

    thought "It's not a question. He already knows."
    pause 0.4

    yn "...Yes."
    pause 0.4

    hide muiquiet
    show muitalking at center_char
    mui "..."
    mui "Why."
    hide muitalking
    show muiquiet at center_char

    pause 0.6

    menu:
        "Because I knew you. And I didn't want to watch it happen.":
            yn "Because I knew you."
            yn "And I didn't want to watch it happen."
            hide muiquiet
            show muitalking at center_char
            mui "..."
            mui "Even though it wasn't your story to change."
            hide muitalking
            show muiquiet at center_char
            thought "Yes. Even though."

        "Because I couldn't not.":
            yn "Because I couldn't not."
            hide muiquiet
            show muitalking at center_char
            mui "..."
            hide muitalking
            show muiquiet at center_char
            thought "He doesn't say anything."
            thought "Which is somehow the right answer."

        "I don't know. I just did.":
            yn "...I don't know. I just did."
            hide muiquiet
            show muitalking at center_char
            mui "..."
            mui "That's honest."
            hide muitalking
            show muiquiet at center_char
            thought "He says it like a fact. Not a compliment."

    pause 0.5

    yn "...There's something else."
    yn "Something I'm not saying."
    pause 0.4

    hide muiquiet
    show muitalking at center_char
    mui "I know."
    hide muitalking
    show muiquiet at center_char

    yn "..."
    pause 0.4

    yn "I did something. Before I came here."
    yn "In my world."
    yn "Something I can't take back."
    pause 0.4

    yn "My quirk. I lost control of it."
    yn "And I—"
    yn "..."
    yn "My parents."
    pause 0.6

    hide muiquiet
    show muitalking at center_char
    mui "..."
    hide muitalking
    show muiquiet at center_char

    thought "He's not saying anything."
    thought "He's just looking at me."
    thought "The way he looked at me in the forest."
    thought "Like he's trying to memorize me before I'm gone."
    pause 0.6

    yn "...I ran. I found a river."
    yn "And I—"
    yn "I don't know if I jumped. Or if I fell."
    yn "I've never known."
    pause 0.5

    hide muiquiet
    show muitalking at center_char
    mui "..."
    mui "Does it matter."
    hide muitalking
    show muiquiet at center_char

    thought "..."
    thought "I've been asking myself that for a long time."
    thought "And I still don't know."
    pause 0.5

    yn "...I don't know."
    pause 0.4

    hide muiquiet
    show muitalking at center_char
    mui "..."
    mui "You're still fading."
    hide muitalking
    show muiquiet at center_char

    thought "I know. Remembering helped. But it's not enough."
    thought "Someone else has to remember me too."
    thought "And he forgets. He always forgets."
    pause 0.5

    yn "...I know. It's okay."
    pause 0.3

    hide muiquiet
    show muitalking at center_char
    mui "It's not."
    hide muitalking
    show muiquiet at center_char

    yn "...You can't help it. Your memory—"
    pause 0.3

    hide muiquiet
    show muitalking at center_char
    mui "I know what my memory does."
    mui "..."
    mui "Tell me your name."
    hide muitalking
    show muiquiet at center_char

    yn "...You know my name."
    pause 0.3

    hide muiquiet
    show muitalking at center_char
    mui "Tell me anyway."
    hide muitalking
    show muiquiet at center_char

    yn "[player_name]."
    pause 0.5

    hide muiquiet
    show muitalking at center_char
    mui "[player_name]."
    mui "..."
    mui "I'll remember it."
    hide muitalking
    show muiquiet at center_char

    thought "He says that every time."
    thought "..."
    thought "But this time he's looking at me differently."
    thought "Like he's choosing it. Not just saying it."
    pause 0.6

    hide muiquiet
    show muitalking at center_char
    mui "You called me Sparrow."
    mui "In the forest."
    mui "I called you Sparrow."
    hide muitalking
    show muiquiet at center_char

    thought "..."
    thought "He remembered. On his own."
    thought "Without me telling him."
    pause 0.6

    yn "...You remembered."
    pause 0.4

    hide muiquiet
    show muitalking at center_char
    mui "Fragments. The same way you remember things."
    mui "Out of order. Wrong. But there."
    hide muitalking
    show muiquiet at center_char

    thought "We're the same."
    thought "Both fractured. Both out of order."
    thought "Both trying to hold onto something that keeps slipping."
    pause 0.6

    hide muiquiet
    show muitalking at center_char
    mui "...You're more solid now."
    hide muitalking
    show muiquiet at center_char

    thought "I am. I can feel it."
    thought "Like something settling. Like weight returning."
    thought "Like I exist again."
    pause 0.5

    yn "...Yeah. I think I am."
    pause 0.4

    hide muiquiet
    show muitalking at center_char
    mui "..."
    mui "Good."
    hide muitalking
    show muiquiet at center_char

    thought "That's all he says. Good."
    thought "One word. And somehow it's enough."
    pause 0.8

    scene black
    with Fade(1.0, 0.5, 1.5)

    jump epilogue_scene
