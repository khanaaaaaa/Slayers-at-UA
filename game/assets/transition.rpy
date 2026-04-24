transform bg_fit:
    xysize (config.screen_width, config.screen_height)
transform left_char:
    zoom 1.8
    xalign 0.12
    yalign 1.0
transform right_char:
    zoom 1.8
    xalign 0.88
    yalign 1.0
transform center_char:
    zoom 1.8
    xalign 0.88
    yalign 1.0
transform left_char_ghost:
    zoom 1.8
    xalign 0.18
    yalign 1.0
    alpha 0.72
transform right_char_ghost:
    zoom 1.8
    xalign 0.82
    yalign 1.0
    alpha 0.72
transform drift:
    linear 7.0 xoffset 9 yoffset -5
    linear 7.0 xoffset -9 yoffset 5
    repeat
transform drift_slow:
    linear 12.0 xoffset 6 yoffset -3
    linear 12.0 xoffset -6 yoffset 3
    repeat

define memory_fade = Fade(1.2, 0.6, 1.5)
define slow_dissolve = Dissolve(1.4)
define soft_dissolve = Dissolve(0.7)
define hard_cut = Fade(0.0, 0.0, 0.0)
define flash_white = Fade(0.04, 0.0, 0.5, color="#ffffff")
define flash_blue = Fade(0.04, 0.0, 0.6, color="#c8e8ff")
define dream_fade = Fade(1.8, 1.2, 2.2, color="#080818")
define guilt_fade = Fade(1.0, 0.8, 1.8, color="#0a0a0a")
define water_cut = Fade(0.1, 0.0, 0.8, color="#1a3a5c")

screen vignette():
    add Solid("#00000055") at truecenter

transform memory_flash_anim:
    alpha 0.0
    linear 0.08 alpha 0.9
    linear 0.4 alpha 0.0

transform water_overlay_anim:
    alpha 0.0
    linear 0.2 alpha 0.35
    linear 1.2 alpha 0.0

screen memory_flash():
    add Solid("#ffffff") at memory_flash_anim

screen water_overlay():
    add Solid("#1a3a5c") at water_overlay_anim