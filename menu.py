import displayio

class Cell: 
  pass



class Menu: 
  layers = []
  rows = 0 
  cols = 0
  current_page = 0
  num_pages = 0
  
  def __init__(self, width: int, height: int, layers) -> None:
    self.rows = height
    self.cols = width
    self.num_pages = len(layers)
    self.layers = layers
