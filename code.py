print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D5, board.D6, board.D9)
keyboard.row_pins = (board.D10, board.D11, board.D12)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    # Numpad Layer
    # [
    #     KC.N7, KC.N8, KC.N9,
    #     KC.N4, KC.N5, KC.N6,
    #     KC.N1, KC.N2, KC.N3
    # ],
    # Arrow Key Layer
    [
        KC.HOME  , KC.UP  , KC.END,
        KC.LEFT  , KC.DOWN, KC.RIGHT,
        KC.PGDOWN, KC.NO, KC.PGUP,
    ],
    [   
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F,
        KC.G, KC.H, KC.I
    ]
]

if __name__ == '__main__':
    keyboard.go()
