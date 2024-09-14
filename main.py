def on_button_pressed_a():
    doDemo(5)
input.on_button_pressed(Button.A, on_button_pressed_a)

def doDemo(num: number):
    global demo
    if 1 == num:
        music.play(music.builtin_playable_sound_effect(soundExpression.hello),
            music.PlaybackMode.IN_BACKGROUND)
        xgo.execution_action(xgo.action_enum.SQUAT)
    elif 2 == num:
        music.play(music.builtin_playable_sound_effect(soundExpression.slide),
            music.PlaybackMode.IN_BACKGROUND)
        xgo.execution_action(xgo.action_enum.STAND)
    elif 3 == num:
        music.play(music.builtin_playable_sound_effect(soundExpression.twinkle),
            music.PlaybackMode.IN_BACKGROUND)
        xgo.execution_action(xgo.action_enum.TWIRL_ROLL)
    elif 4 == num:
        music.play(music.builtin_playable_sound_effect(soundExpression.spring),
            music.PlaybackMode.IN_BACKGROUND)
        xgo.execution_action(xgo.action_enum.SUR_PLACE)
    elif 4 == num:
        music.play(music.builtin_playable_sound_effect(soundExpression.soaring),
            music.PlaybackMode.IN_BACKGROUND)
        xgo.execution_action(xgo.action_enum.TRIAXIAL_ROTATION)
    elif 5 == num:
        music.play(music.builtin_playable_sound_effect(soundExpression.yawn),
            music.PlaybackMode.IN_BACKGROUND)
        xgo.execution_action(xgo.action_enum.STRETCH_ONESELF)
    elif 6 == num:
        music.play(music.builtin_playable_sound_effect(soundExpression.mysterious),
            music.PlaybackMode.IN_BACKGROUND)
        xgo.execution_action(xgo.action_enum.REQUEST_FEEDING)
    elif 7 == num:
        music.play(music.builtin_playable_sound_effect(soundExpression.mysterious),
            music.PlaybackMode.IN_BACKGROUND)
        xgo.execution_action(xgo.action_enum.LOOKING_FOR_FOOD)
    else:
        music.play(music.builtin_playable_sound_effect(soundExpression.mysterious),
            music.PlaybackMode.IN_BACKGROUND)
        xgo.execution_action(xgo.action_enum.SIT_DOWN)
    demo += 1
    if demo >= MAXDEMOS:
        demo = 0

def on_sound_loud():
    doDemo(1)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_button_pressed_b():
    doDemo(MAXDEMOS)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    doDemo(1)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

MAXDEMOS = 0
demo = 0
demo = 0
input.set_sound_threshold(SoundThreshold.LOUD, 75)
MAXDEMOS = 10

def on_forever():
    pass
basic.forever(on_forever)
