from kmk.modules.layers import Layers as _Layers
from controller import MenuController
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, make_key
from kmk.handlers.sequences import simple_key_sequence, send_string
from utlis import set_config, get_key


class Layers(_Layers):
    last_top_layer = 0

    def __init__(self, controller: MenuController = None):
        self.controller= controller
        super().__init__()

    def after_hid_send(self, keyboard: KMKKeyboard):
        if keyboard.active_layers[0] != self.last_top_layer and self.menu:
            self.last_top_layer = keyboard.active_layers[0]
            self.controller.setPage(self.last_top_layer)

        return super().after_hid_send(keyboard)


# MENU LAYERS CONFIG 



# Git Keybinds
GIT_AA = simple_key_sequence([send_string('git add .'), KC.MACRO_SLEEP_MS(100), KC.ENTER])
GIT_C = simple_key_sequence(
    [send_string('git commit -m ""'), KC.MACRO_SLEEP_MS(100), KC.LEFT]
)
GIT_P = simple_key_sequence([send_string("git push"), KC.MACRO_SLEEP_MS(100), KC.ENTER])


# CTRL Keybinds
CPY = simple_key_sequence(
    [
        KC.HOME,
        KC.LSFT(KC.END),
        KC.MACRO_SLEEP_MS(30),
        KC.LCTRL(KC.C),
    ]
)


PST = simple_key_sequence([KC.END, KC.ENTER,KC.LCTRL(KC.V)])
DEL_LN = simple_key_sequence([KC.HOME, KC.LSFT(KC.END), KC.DEL])

# Node 
CL_EXP_S = simple_key_sequence([send_string("cd client"), KC.MACRO_SLEEP_MS(50), KC.ENTER, send_string('npx expo start --web'), KC.MACRO_SLEEP_MS(50), KC.ENTER])