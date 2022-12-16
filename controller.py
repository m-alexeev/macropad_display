from menu import Menu
from display import Display

class MenuController: 
  def __init__(self, menu: Menu, display: Display) -> None:
    self.menu = menu
    self.display = display
  
  def setPage(self, page):
    # Grabs page data to display
    page_data = self.menu.getPageData(page)

    # Draw the page on the display
    self.display.draw(page_data)
