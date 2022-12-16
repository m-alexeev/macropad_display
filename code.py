print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from layers import Layers, GIT_C, GIT_P, CPY, PST, DEL_LN,GIT_AA, CL_EXP_S
from menu import Menu
from display import Display
from controller import MenuController
from utlis import create_image_arr

# Menu and Display Functionality
display = Display(board.D24, board.A3, board.D4)
menu = Menu(3, 3, [])
menuController = MenuController(menu=menu, display=display)

display.create_grid(3, 3)

# Keyboard Config
layers = Layers(controller=menuController)
encoder = EncoderHandler()
keyboard = KMKKeyboard()

img_arr = create_image_arr('./images/res.txt')

display.draw(img_arr)

keyboard.modules = [layers, encoder]

encoder.pins = (
    (board.A0, board.A1, board.A2, False),
)
# Keyboard Config 
keyboard.col_pins = (board.D5, board.D6, board.D9)
keyboard.row_pins = (board.D10, board.D11, board.D12)
keyboard.diode_orientation = DiodeOrientation.COL2ROW



_____ = KC.TRNS
xxxxx = KC.NO 

keyboard.keymap = [
    # Nump
    [
        GIT_AA,GIT_C, GIT_P,
        CPY, PST, CL_EXP_S,
        DEL_LN, KC.N2, KC.N3
    ],
    # Arrow Key Layer
    [
        KC.HOME  , KC.UP  , KC.END,
        KC.LEFT  , KC.DOWN, KC.RIGHT,
        KC.PGDOWN, KC.NO, KC.PGUP,
    ],
    # Numpad Layer
    [   
        GIT_C, KC.N8, KC.N9,
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



