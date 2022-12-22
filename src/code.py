print("Starting")

import gc



from board import D24, A3, D4, A0, A1, A2, D5, D6, D9, D10, D11, D12

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from layers import Layers, GIT_C, GIT_P, CPY, PST, DEL_LN,GIT_AA, CL_EXP_S, icon_layer
from menu import Menu
from display import Display
from controller import MenuController
from graphics import Graphics


PAD_SIZE = (3,3)

# Menu and Display Functionality
display = Display(D24, A3, D4)
menu = Menu(PAD_SIZE, icon_layer)
graphics = Graphics(display, PAD_SIZE, './images/icons.bmp', 40, 40)
menuController = MenuController(menu=menu, graphics=graphics)


# Initialize first layer
graphics.draw_tiles(icon_layer[0])

# Keyboard Config
layers = Layers(controller=menuController)
encoder = EncoderHandler()
keyboard = KMKKeyboard()


keyboard.modules = [layers, encoder]

encoder.pins = (
    (A0, A1, A2, False),
)
# Keyboard Config 
keyboard.col_pins = (D5, D6, D9)
keyboard.row_pins = (D10, D11, D12)
keyboard.diode_orientation = DiodeOrientation.COL2ROW



_____ = KC.TRNS
xxxxx = KC.NO 

keyboard.keymap = [
    # Custom
    [
        GIT_AA,GIT_C, GIT_P,
        CPY, PST, CL_EXP_S,
        DEL_LN, xxxxx, xxxxx
    ],
    # Arrow Key Layer
    [
        KC.HOME  , KC.UP  , KC.END,
        KC.LEFT  , KC.DOWN, KC.RIGHT,
        KC.PGDOWN, xxxxx, KC.PGUP,
    ],
    # Numpad Layer
    [   
        KC.N7, KC.N8, KC.N9,
        KC.N4, KC.N5, KC.N6,
        KC.N1, KC.N2, KC.N3
    ],
    # Password Layer
    [
        _____, _____, _____,
        _____, _____, _____,
        _____, _____, _____
    ]
]

encoder.map = [
    ((KC.TO(1), KC.TO(3), xxxxx),),
    ((KC.TO(2), KC.TO(0), _____),),
    ((KC.TO(3), KC.TO(1), _____),),
    ((KC.TO(0), KC.TO(2), _____),),
]

if __name__ == '__main__':
    keyboard.go()
