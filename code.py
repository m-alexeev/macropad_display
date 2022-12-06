print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers as _Layers
from kmk.modules.encoder import EncoderHandler
from kmk.keys import make_key
from layers import Layers
from menu import Menu

menu = Menu(4)
layers = Layers()
encoder = EncoderHandler()
keyboard = KMKKeyboard()

keyboard.modules = [layers, encoder]

encoder.pins = (
    (board.A0, board.A1, board.A2, False),
)

keyboard.col_pins = (board.D5, board.D6, board.D9)
keyboard.row_pins = (board.D10, board.D11, board.D12)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    # Numpad Layer
    [
        KC.N7, KC.N8, KC.N9,
        KC.N4, KC.N5, KC.N6,
        KC.N1, KC.N2, KC.N3
    ],
    # Arrow Key Layer
    [
        KC.HOME  , KC.UP  , KC.END,
        KC.LEFT  , KC.DOWN, KC.RIGHT,
        KC.PGDOWN, KC.NO, KC.PGUP,
    ],
    # Test Layer 1
    [   
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F,
        KC.G, KC.H, KC.I
    ],
    # Test Layer 2
    [   
        KC.Z, KC.Y, KC.X,
        KC.W, KC.G, KC.H,
        KC.J, KC.U, KC.P
    ]
]

class EncoderLayer(): 
    def SetOther(self, layer, *args, **kwargs):
        print(*args, **kwargs)
        print(KC.TO(layer))
        # print(KC.TO(1))

    def SetLayer(self, layer, *args, **kwargs):
        return KC.TO(layer)

encoder_layer = EncoderLayer()


make_key(
    names=('MYKEY',),
    on_press=lambda *args: encoder_layer.SetOther(1),
)

make_key(
    names=('FUNC',),
    on_press=lambda *args: KC.TO(0),
)

encoder.map = [
    ((encoder_layer.SetLayer(1), encoder_layer.SetLayer(3), KC.MYKEY),),
    ((encoder_layer.SetLayer(2), encoder_layer.SetLayer(0), KC.FUNC),),
    ((encoder_layer.SetLayer(3), encoder_layer.SetLayer(1), KC.FUNC),),
    ((encoder_layer.SetLayer(0), encoder_layer.SetLayer(2), KC.FUNC),),
]
if __name__ == '__main__':
    keyboard.go()