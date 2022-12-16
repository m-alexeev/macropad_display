
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC 
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from layers import Layers

class Keyboard: 
  keyboard = None

  def __init__(self, keyboard: KMKKeyboard, row_pins, col_pins) -> None:
    self.keyboard = keyboard
    self.keyboard.col_pins = col_pins
    self.keyboard.row_pins = row_pins
    self.keyboard.diode_orientation = DiodeOrientation.COL2ROW

  def addModule(self, module: EncoderHandler | Layers ):
    self.keyboard.modules.append(module)
  
  def setDiodeOrientation(self, orientation: DiodeOrientation):
    self.keyboard.diode_orientation = orientation

    