class Menu: 
	current_page = 0
	num_pages = 0
	def __init__(self, num_pages) -> None:
		self.num_pages = num_pages

	def setPage(self, page: int) -> None:
		if (page >= 0 and page <= self.num_pages): 
			self.current_page = page
		print(self.current_page)