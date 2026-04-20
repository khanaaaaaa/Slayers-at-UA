transform bg_fit:
    xysize (config.screen_width, config.screen_height)
transform left_char:
    zoom 1.8
    xalign 0.0
    yalign 1.0
transform right_char:
    zoom 1.8
    xalign 1.0
    yalign 1.0
transform drift:
    linear 6.0 xoffset 10 yoffset -5
    linear 6.0 xoffset -10 yoffset 5
    repeat
define memory_fade = Fade(1.0, 0.5, 1.2)
define flash_white = Fade(0.05, 0.0, 0.3, color="#ffffff")
define hard_cut = Fade(0.0, 0.0, 0.0)
define slow_dissolve = Dissolve(1.2)
screen flash_overlay:
    add Solid("#ffffff") at truecenter