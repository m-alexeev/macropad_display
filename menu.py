from utils import read_txt_file

FILE_PATH = "./images/output"

class Menu: 
  layers = []
  rows = 0 
  cols = 0
  current_page = 0
  num_pages = 0
  
  def __init__(self, pad_size: tuple[int, int], layers) -> None:
    self.rows = pad_size[0]
    self.cols = pad_size[1]
    self.layers = layers

  def getPageData(self, page):
    if page >= 0 and page < len(self.layers):
      # return layer 
      return self.layers[page]