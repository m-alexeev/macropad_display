from menu import Menu
from graphics import Graphics

class MenuController: 
  index = 0
  def __init__(self, menu: Menu, graphics: Graphics) -> None:
    self.menu = menu
    self.graphics = graphics
  
  def setPage(self, page):
    # Grabs page data to display
    tiles = self.menu.getPageData(page)
    # Draw the page on the display
    self.graphics.draw_tiles(tiles)
    
