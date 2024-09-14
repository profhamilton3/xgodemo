input.onButtonPressed(Button.A, function () {
    doDemo(5)
})
function doDemo (num: number) {
    if (1 == num) {
        music.play(music.builtinPlayableSoundEffect(soundExpression.hello), music.PlaybackMode.InBackground)
        xgo.execution_action(xgo.action_enum.Squat)
    } else if (2 == num) {
        music.play(music.builtinPlayableSoundEffect(soundExpression.slide), music.PlaybackMode.InBackground)
        xgo.execution_action(xgo.action_enum.Stand)
    } else if (3 == num) {
        music.play(music.builtinPlayableSoundEffect(soundExpression.twinkle), music.PlaybackMode.InBackground)
        xgo.execution_action(xgo.action_enum.Twirl_Roll)
    } else if (4 == num) {
        music.play(music.builtinPlayableSoundEffect(soundExpression.spring), music.PlaybackMode.InBackground)
        xgo.execution_action(xgo.action_enum.Sur_place)
    } else if (4 == num) {
        music.play(music.builtinPlayableSoundEffect(soundExpression.soaring), music.PlaybackMode.InBackground)
        xgo.execution_action(xgo.action_enum.Triaxial_rotation)
    } else if (5 == num) {
        music.play(music.builtinPlayableSoundEffect(soundExpression.yawn), music.PlaybackMode.InBackground)
        xgo.execution_action(xgo.action_enum.Stretch_oneself)
    } else if (6 == num) {
        music.play(music.builtinPlayableSoundEffect(soundExpression.mysterious), music.PlaybackMode.InBackground)
        xgo.execution_action(xgo.action_enum.Request_feeding)
    } else if (7 == num) {
        music.play(music.builtinPlayableSoundEffect(soundExpression.mysterious), music.PlaybackMode.InBackground)
        xgo.execution_action(xgo.action_enum.Looking_for_food)
    } else {
        music.play(music.builtinPlayableSoundEffect(soundExpression.mysterious), music.PlaybackMode.InBackground)
        xgo.execution_action(xgo.action_enum.Sit_down)
    }
    demo += 1
    if (demo >= MAXDEMOS) {
        demo = 0
    }
}
input.onSound(DetectedSound.Loud, function () {
    doDemo(1)
})
input.onButtonPressed(Button.B, function () {
    doDemo(MAXDEMOS)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    doDemo(1)
})
let MAXDEMOS = 0
let demo = 0
xgo.init_xgo_serial(SerialPin.P2, SerialPin.P1)
demo = 0
input.setSoundThreshold(SoundThreshold.Loud, 75)
MAXDEMOS = 10
basic.showLeds(`
    # # . # #
    . . # . .
    # . # . #
    . . . . .
    . # # # .
    `)
