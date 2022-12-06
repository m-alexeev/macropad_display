from kmk.modules.layers import Layers as _Layers
from menu import Menu
from kmk.kmk_keyboard import KMKKeyboard

class Layers(_Layers):
  last_top_layer = 0 

  def __init__(self, menu: Menu = None):
    self.menu = menu
    super().__init__()

  def after_hid_send(self, keyboard: KMKKeyboard):
    if keyboard.active_layers[0] != self.last_top_layer and self.menu:
      self.last_top_layer = keyboard.active_layers[0]
      self.menu.setPage(self.last_top_layer)

    return super().after_hid_send(keyboard)