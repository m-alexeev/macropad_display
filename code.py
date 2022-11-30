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
    [   
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F,
        KC.G, KC.H, KC.I
    ]
]

if __name__ == '__main__':
    keyboard.go()
